""" RT Beams Delivery Instruction factory
"""

from copy import deepcopy
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from sys import argv
from time import mktime, strptime
from typing import List

import pydicom
from pydicom import DataElement, Dataset, uid
from pydicom.filereader import dcmread
from pydicom.filewriter import dcmwrite


def load_plan(path: Path) -> Dataset:
    """convenience function to load a dataset from the filename

    Args:
        path (Path): full or partial path to the rt plan

    Returns:
        Dataset: a pydicom Dataset containing the rt plan information
    """
    plan = dcmread(path, force=True)
    return plan


def load_treatment_records(treatment_record_paths: List[Path]) -> List[Dataset]:
    tx_rec_ds_list = [dcmread(x, force=True) for x in treatment_record_paths]
    return tx_rec_ds_list


def is_tx_record_for_plan(tx_rec_ds: Dataset, plan: Dataset) -> bool:
    try:
        is_ion_tx_rec = tx_rec_ds.SOPClassUID == uid.RTIonBeamsTreatmentRecordStorage
        if tx_rec_ds.ReferencedRTPlanSequence[0].ReferencedSOPInstanceUID != plan.SOPInstanceUID:
            return False
        else:
            if is_ion_tx_rec:
                if plan.SOPClassUID != uid.RTIonPlanStorage:
                    return False
                planned_beam_numbers = [x.BeamNumber for x in plan.IonBeamSequence]
                for tx_session in tx_rec_ds.TreatmentSessionIonBeamSequence:
                    referenced_beam_number = tx_session.ReferencedBeamNumber
                    if referenced_beam_number not in planned_beam_numbers:
                        return False
            else:
                if plan.SOPClassUID != uid.RTPlanStorage:
                    return False
                planned_beam_numbers = [x.BeamNumber for x in plan.BeamSequence]
                for tx_session in tx_rec_ds.TreatmentSessionBeamSequence:
                    referenced_beam_number = tx_session.ReferencedBeamNumber
                    if referenced_beam_number not in planned_beam_numbers:
                        return False
        return True
    except Exception as error:
        print(error)
        return False


def is_tx_record_for_bdi(tx_rec_ds: Dataset, bdi: Dataset) -> bool:
    try:
        is_ion_tx_rec = tx_rec_ds.SOPClassUID == uid.RTIonBeamsTreatmentRecordStorage
        bdi_current_fraction_list = [x.CurrentFractionNumber for x in bdi.BeamTaskSequence]
        if is_ion_tx_rec:
            for tx_session in tx_rec_ds.TreatmentSessionIonBeamSequence:
                current_fraction_number = tx_session.CurrentFractionNumber
                if current_fraction_number not in bdi_current_fraction_list:
                    return False
        else:
            for tx_session in tx_rec_ds.TreatmentSessionBeamSequence:
                current_fraction_number = tx_session.CurrentFractionNumber
                if current_fraction_number not in bdi_current_fraction_list:
                    return False
        return True
    except Exception as error:
        print(error)
        return False


def write_rtbdi(bdi: Dataset, filename: Path):
    if filename.is_dir():
        filename = filename.joinpath(f"RB_{str(bdi.SOPInstanceUID)}.dcm")
    _write_ds(bdi, filename)


def write_ups(ups: Dataset, filename: Path):
    if filename.is_dir():
        filename = filename.joinpath(f"UPS_{str(ups.SOPInstanceUID)}.dcm")
    _write_ds(ups, filename)


def _write_ds(ds: Dataset, filename: Path):
    ds.fix_meta_info()
    dcmwrite(filename, ds, write_like_original=False)


def create_rtbdi_from_rtion_plan(
    plan: Dataset, fraction_number: int = 1, treatment_record_list: List[Dataset] = None, bdi_uid_prefix: str = None
) -> Dataset:
    """_summary_

    Args:
        plan (Dataset): _description_
        scheduled_datetime (datetime, optional): _description_. Defaults to datetime.now.
        fraction_number (int, optional): _description_. Defaults to 1.
        bdi_uid_prefix (str, optional): _description_. Defaults to None.

    Returns:
        Dataset: RT Beams Delivery Instruction
    """
    bdi_ds = pydicom.Dataset()
    for elem in plan:
        if elem.tag < 0x0020FFFF:
            bdi_ds[elem.tag] = deepcopy(elem)
    _delete_excess_plan_elements_from_bdi(bdi_ds)
    now_date = datetime.now().strftime("%Y%m%d")  # ,.date)
    now_time = datetime.now().strftime("%H%M")  # datetime.now().time,
    bdi_ds["SOPClassUID"] = DataElement("SOPClassUID", "UI", uid.RTBeamsDeliveryInstructionStorage)
    bdi_ds["SOPInstanceUID"] = DataElement("SOPInstanceUID", "UI", uid.generate_uid(bdi_uid_prefix))
    bdi_ds.InstanceCreationDate = now_date
    bdi_ds.InstanceCreationTime = now_time
    bdi_ds.SeriesDate = now_date
    bdi_ds.SeriesTime = now_time
    bdi_ds.Modality = "PLAN"
    bdi_ds.Manufacturer = "SJS Targeted Solutions"
    bdi_ds.ManufacturerModelName = "RTBDI Creator"
    bdi_ds.SoftwareVersions = "0.1"

    ref_plan_seq = Dataset()
    ref_plan_seq.ReferencedSOPClassUID = plan.SOPClassUID
    ref_plan_seq.ReferencedSOPInstanceUID = plan.SOPInstanceUID
    bdi_ds.ReferencedRTPlanSequence = pydicom.Sequence([ref_plan_seq])
    is_completion_session = treatment_record_list is not None and len(treatment_record_list) != 0
    list_of_beam_tasks = []
    list_of_omitted_beam_tasks = []
    if plan.SOPClassUID == uid.RTIonPlanStorage:
        list_of_beams = [x for x in plan.IonBeamSequence]
    else:
        list_of_beams = [x for x in plan.BeamSequence]
    for beam in list_of_beams:
        if is_completion_session:
            if _beam_already_treated_to_completion(beam.BeamNumber, treatment_record_list):
                omitted_beam_task_seq = Dataset()
                omitted_beam_task_seq.ReferencedBeamNumber = beam.BeamNumber
                omitted_beam_task_seq.ReasonForOmission = "ALREADY_TREATED"
                list_of_omitted_beam_tasks.append(omitted_beam_task_seq)
        else:
            beam_task_seq = Dataset()
            _populate_default_beam_task_elements(beam_task_seq)
            beam_task_seq.ReferencedBeamNumber = beam.BeamNumber
            beam_task_seq.CurrentFractionNumber = fraction_number
            beam_task_seq.BeamTaskType = "TREAT"
            treatment_delivery_type = "TREATMENT"
            if is_completion_session:
                if _beam_already_partially_treated(beam.BeamNumber, treatment_record_list):
                    treatment_delivery_type = "CONTINUATION"
            beam_task_seq.TreatmentDeliveryType = treatment_delivery_type
            list_of_beam_tasks.append(beam_task_seq)
    bdi_ds.BeamTaskSequence = pydicom.Sequence(list_of_beam_tasks)
    bdi_ds.OmittedBeamTaskSequence = pydicom.Sequence(list_of_omitted_beam_tasks)
    bdi_ds.is_implicit_VR = True
    bdi_ds.is_little_endian = True
    return bdi_ds


def _beam_already_treated_to_completion(beam_number: int, treatment_record_list: List[Dataset]) -> bool:
    for tx_record in treatment_record_list:
        if tx_record.SOPClassUID == uid.RTIonBeamsTreatmentRecordStorage:
            tx_session_list = [x for x in tx_record.TreatmentSessionIonBeamSequence]

        else:
            tx_session_list = [x for x in tx_record.TreatmentSessionBeamSequence]

        for tx_session in tx_session_list:
            if (tx_session.ReferencedBeamNumber == beam_number) and (tx_session.TreatmentTerminationStatus == "NORMAL"):
                return True

    return False


def _beam_already_partially_treated(beam_number: int, treatment_record_list: List[Dataset]) -> bool:
    for tx_record in treatment_record_list:
        if tx_record.SOPClassUID == uid.RTIonBeamsTreatmentRecordStorage:
            tx_session_list = [x for x in tx_record.TreatmentSessionIonBeamSequence]

        else:
            tx_session_list = [x for x in tx_record.TreatmentSessionBeamSequence]

        for tx_session in tx_session_list:
            if tx_session.ReferencedBeamNumber == beam_number:
                return True

    return False


def _populate_default_beam_task_elements(beam_task: Dataset):
    beam_task.TableTopVerticalAdjustedPosition = 0
    beam_task.TableTopLongitudinalAdjustedPosition = 0
    beam_task.TableTopLateralAdjustedPosition = 0
    beam_task.PatientSupportAdjustedAngle = 0
    beam_task.TableTopEccentricAdjustedAngle = 0
    beam_task.TableTopPitchAdjustedAngle = 0
    beam_task.TableTopRollAdjustedAngle = 0
    beam_task.TableTopVerticalSetupDisplacement = 0
    beam_task.TableTopLongitudinalSetupDisplacement = 0
    beam_task.TableTopLateralSetupDisplacement = 0


def _delete_excess_plan_elements_from_bdi(bdi_ds: Dataset):
    excess_elements = ["PositionReferenceIndicator", "FrameOfReferenceUID"]
    for excess in excess_elements:
        if excess in bdi_ds:
            del bdi_ds[excess]


def _delete_excess_plan_elements_from_ups(ups_ds: Dataset):
    excess_elements = ["PositionReferenceIndicator", "FrameOfReferenceUID", "Modality"]
    for excess in excess_elements:
        if excess in ups_ds:
            del ups_ds[excess]


def create_ups_from_plan_and_bdi(
    plan: Dataset,
    bdi: Dataset,
    retrieve_ae_title: str,
    scheduled_datetime: datetime,
    treatment_records: List[Dataset],
    enable_photo_ref=True,
    enable_setup_image_ref=True,
) -> Dataset:
    """Build up the UPS

    Args:
        plan (Dataset): The RT Plan or RT Ion Plan that the UPS is based on
        bdi (Dataset): The RT Beams Delivery Instruction that the UPS is based on
        retrieve_ae_title (str): The AE Title of the OST (from which references will be retrieved)
        scheduled_datetime (datetime): The datetime to schedule the UPS for
        treatment_records (List):   list of datasets representing the treatment records previously delivered for the fraction
        enable_photo_ref (bool): whether to include a reference to a patient photo in the InputInformation Sequence
            if that is present in the plan
        enable_setup_image_ref: whether to include references to setup images (photos) in the InputInformationSequence
            if they are present in the plan

    """
    ups_ds = pydicom.Dataset()
    # enable_photo_ref = True;
    # enable_setup_image_ref = True;
    for elem in plan:
        if elem.tag < 0x0010FFFF:
            ups_ds[elem.tag] = deepcopy(elem)
    # _delete_excess_plan_elements_from_ups(ups_ds) # probably should rename the function
    ups_ds.SOPClassUID = "1.2.840.10008.5.1.4.34.6.1"  # UPS Push SOP Class
    ups_ds.SOPInstanceUID = uid.generate_uid()
    ups_ds.Manufacturer = "SJS Targeted Solutions"
    ups_ds.ManufacturerModelName = "RTBDI Creator"
    ups_ds.SoftwareVersions = "0.1"

    work_item = pydicom.Dataset()
    work_item.CodeValue = "121726"
    work_item.CodingSchemeDesignator = "DCM"
    work_item.CodeMeaning = "RT Treatment with Internal Verification"
    scheduled_work_item_code_sequence = pydicom.Sequence([work_item])
    ups_ds.ScheduledWorkitemCodeSequence = scheduled_work_item_code_sequence

    plan_reference_item = _create_referenced_instances_and_access_item(plan, retrieve_ae_title)
    bdi_reference_item = _create_referenced_instances_and_access_item(bdi, retrieve_ae_title)

    # because the Reference Patient Photo Sequence already contains Study and Series UID information... it isn't
    # necessary to load the patient photo to get that information.
    patient_photo_reference_items = []
    if enable_photo_ref and "ReferencedPatientPhotoSequence" in plan:
        for patient_photo_seq_item in plan.ReferencedPatientPhotoSequence:
            patient_photo_reference_item = _create_referenced_instances_and_access_item(
                patient_photo_seq_item, retrieve_ae_title
            )
            patient_photo_reference_items.append(patient_photo_reference_item)

    # Search for the Study and Series Instance UIDs for the Setup images in the Common Instance Reference module
    # If they are available, build up the reference for later inclusion in the InputInformationSequence
    # If not... don't attempt to include them.
    patient_setup_image_items = []
    if enable_setup_image_ref and "ReferencedSetupImageSequence" in plan.PatientSetupSequence[0]:
        for setup_image_seq_item in plan.PatientSetupSequence[0].ReferencedSetupImageSequence:
            ref_study_uid, ref_series_uid = _get_study_and_series_for_referenced_instance(
                plan, setup_image_seq_item.ReferencedSOPInstanceUID
            )
            if ref_study_uid is not None and ref_series_uid is not None:
                setup_image_reference_item = _create_referenced_instances_and_access_item(
                    setup_image_seq_item,
                    retrieve_ae_title,
                    study_instance_uid=ref_study_uid,
                    series_instance_uid=ref_series_uid,
                )
                patient_setup_image_items.append(setup_image_reference_item)

    treatment_record_reference_items = []
    for treatment_rec in treatment_records:
        treatment_rec_ref_item = _create_referenced_instances_and_access_item(treatment_rec, retrieve_ae_title)
        treatment_record_reference_items.append(treatment_rec_ref_item)

    list_of_reference_items = []
    list_of_reference_items.append(plan_reference_item)
    list_of_reference_items.append(bdi_reference_item)

    if len(patient_photo_reference_items) > 0:
        list_of_reference_items += patient_photo_reference_items

    if len(patient_setup_image_items) > 0:
        list_of_reference_items += patient_setup_image_items

    treatment_delivery_type = "TREATMENT"
    if len(treatment_record_reference_items) > 0:
        list_of_reference_items += treatment_record_reference_items
        treatment_delivery_type = "CONTINUATION"
    ups_ds.InputInformationSequence = pydicom.Sequence(list_of_reference_items)

    scheduled_station_name_code_sequence_item = _create_scheduled_station_name_code_sequence_item(plan)
    ups_ds.ScheduledStationNameCodeSequence = pydicom.Sequence([scheduled_station_name_code_sequence_item])
    ups_ds.InputReadinessState = "READY"
    ups_ds.ProcedureStepState = "SCHEDULED"
    ups_ds.ScheduledProcedureStepPriority = "MEDIUM"
    plan_label = "no plan label"
    plan_name = "no plan name"
    if "RTPlanLabel" in plan:
        plan_label = plan.RTPlanLabel
    if "RTPlanName" in plan:
        plan_name = plan.RTPlanName

    ups_ds.WorklistLabel = "Worklist label for " + plan_label
    ups_ds.ProcedureStepLabel = "Treatment Step for " + plan_name
    ups_ds.ScheduledProcedureStepStartDateTime = scheduled_datetime
    scheduled_processing_parameters_list = []
    treatment_delivery_concept = _create_code_seq_item("121740", "DCM", "Treatment Delivery Type")
    # maybe should be using treatment_delivery_type variable instead of "TREATMENT" hardcoded constant
    treatment_param_item = _create_ups_content_item("TEXT", treatment_delivery_type, treatment_delivery_concept)

    scheduled_processing_parameters_list.append(treatment_param_item)

    plan_label_concept = _create_code_seq_item("2018001", "99IHERO2018", "Plan Label")
    plan_label_value = "No Plan Label"
    if "RTPlanLabel" in plan:
        plan_label_value = plan.RTPlanLabel
    elif "RTPlanName" in plan:
        plan_label_value = plan.RTPlanName
    plan_label_item = _create_ups_content_item("TEXT", plan_label_value, plan_label_concept)

    scheduled_processing_parameters_list.append(plan_label_item)

    current_fraction_concept = _create_code_seq_item("2018002", "99IHERO2018", "Current Fraction Number")

    current_fraction_item = _create_ups_content_item(
        "NUMERIC", int(bdi.BeamTaskSequence[0].CurrentFractionNumber), current_fraction_concept
    )

    scheduled_processing_parameters_list.append(current_fraction_item)

    fractions_planned_concept = _create_code_seq_item("2018003", "99IHERO2018", "Number of Fractions Planned")
    fractions_planned_item = _create_ups_content_item(
        "NUMERIC", int(plan.FractionGroupSequence[0].NumberOfFractionsPlanned), fractions_planned_concept
    )
    scheduled_processing_parameters_list.append(fractions_planned_item)

    ups_ds.ScheduledProcessingParametersSequence = pydicom.Sequence(scheduled_processing_parameters_list)
    return ups_ds


@lru_cache
def _measurement_units_code_seq_item_no_units() -> Dataset:
    return _create_code_seq_item("1", "UCUM", "no units")


def _create_code_seq_item(value: str | int, designator: str, meaning: str) -> Dataset:
    code_seq_item = Dataset()
    code_seq_item.CodeValue = value
    code_seq_item.CodingSchemeDesignator = designator
    code_seq_item.CodeMeaning = meaning
    return code_seq_item


def _create_ups_content_item(value_type: str, value: any, code_seq_item: Dataset) -> Dataset:
    content_item = Dataset()
    content_item.ValueType = value_type
    if code_seq_item is not None:
        content_item.ConceptNameCodeSequence = pydicom.Sequence([code_seq_item])
    if value_type == "TEXT":
        content_item.TextValue = str(value)
    elif value_type == "NUMERIC":
        content_item.MeasurementUnitsCodeSequence = pydicom.Sequence([_measurement_units_code_seq_item_no_units()])
        content_item.NumericValue = value
    else:
        raise ValueError(f"Value Type {value_type} not supported")
    return content_item


def _datetime_to_dicom_date(dt: datetime) -> str:
    dicom_date = dt.strftime("%Y%m%d")
    return dicom_date


def _datetime_to_dicom_time(dt: datetime) -> str:
    dicom_time = dt.strftime("%H%m.%s")
    return dicom_time


def _create_referenced_instances_and_access_item(
    input_ds: Dataset, retrieve_ae_title: str, study_instance_uid: str = "", series_instance_uid: str = ""
) -> Dataset:
    ref_instance_seq_item = pydicom.Dataset()
    ref_instance_seq_item.TypeOfInstances = "DICOM"
    if "StudyInstanceUID" in input_ds:
        ref_instance_seq_item.StudyInstanceUID = input_ds.StudyInstanceUID
    elif len(study_instance_uid) > 0:
        ref_instance_seq_item.StudyInstanceUID = study_instance_uid
    else:
        raise KeyError("Missing Study Instance UID")

    if "SeriesInstanceUID" in input_ds:
        ref_instance_seq_item.SeriesInstanceUID = input_ds.SeriesInstanceUID
    elif len(series_instance_uid) > 0:
        ref_instance_seq_item.SeriesInstanceUID = series_instance_uid
    else:
        raise KeyError("Missing Series Instance UID")

    dicom_retrieval_seq_item = pydicom.Dataset()
    dicom_retrieval_seq_item.RetrieveAETitle = retrieve_ae_title
    ref_instance_seq_item.DICOMRetrievalSequence = pydicom.Sequence([dicom_retrieval_seq_item])

    ref_sop_seq_item = pydicom.Dataset()
    if "SOPClassUID" in input_ds:
        ref_sop_seq_item.ReferencedSOPClassUID = input_ds.SOPClassUID
        ref_sop_seq_item.ReferencedSOPInstanceUID = input_ds.SOPInstanceUID
    elif "ReferencedSOPSequence" in input_ds:  # a referenced Photo sequence was passed in, e.g. for Patient Photo
        ref_sop_seq_item.ReferencedSOPClassUID = input_ds.ReferencedSOPSequence[0].ReferencedSOPClassUID
        ref_sop_seq_item.ReferencedSOPInstanceUID = input_ds.ReferencedSOPSequence[0].ReferencedSOPInstanceUID
    elif "ReferencedSOPClassUID" in input_ds:  # a bare referenced SOP Sequence was passed in, e.g. for Setup images
        ref_sop_seq_item.ReferencedSOPClassUID = input_ds.ReferencedSOPClassUID
        ref_sop_seq_item.ReferencedSOPInstanceUID = input_ds.ReferencedSOPInstanceUID
    else:
        raise KeyError("Neither SOPClassUID, ReferencedSOPClassUID, nor ReferencedSOPSequence are present in input dataset")

    ref_instance_seq_item.ReferencedSOPSequence = pydicom.Sequence([ref_sop_seq_item])

    return ref_instance_seq_item


def _create_scheduled_station_name_code_sequence_item(plan: Dataset) -> Dataset:
    machine_name = ""
    if plan.SOPClassUID == uid.RTIonPlanStorage:
        while len(machine_name) == 0:
            for ion_beam in plan.IonBeamSequence:
                machine_name = ion_beam.TreatmentMachineName
    elif plan.SOPClassUID == uid.RTPlanStorage:
        while len(machine_name) == 0:
            for beam in plan.BeamSequence:
                machine_name = beam.TreatmentMachineName
    if len(machine_name) == 0:
        raise (ValueError("Treatment Machine Name not encoded in plan"))
    code_seq_item = Dataset()
    code_seq_item.CodingSchemeDesignator = "99IHERO2008"
    code_seq_item.CodeValue = machine_name
    code_seq_item.CodeMeaning = machine_name
    return code_seq_item


def _get_study_and_series_for_referenced_instance(plan: Dataset, instance_uid: str) -> tuple[str, str]:
    """Searches Common Instance Reference Module for matching instance_uid

    Args:
        plan (Dataset): The plan containing the instance reference, e.g. setup images/photos, DRRs
        instance_uid (str): The string representation of the SOP Instance UID whose Study and Series UID are desired

    Returns:
        tuple[str, str]: Study UID and Series UID as a tuple, with individual entries set to None if not found
    """
    study_series_tuple = (None, None)
    series_uid = None
    study_uid = None
    if "ReferencedSeriesSequence" in plan:
        for series_seq_item in plan.ReferencedSeriesSequence:
            for ref_instance_seq_item in series_seq_item:
                if str(ref_instance_seq_item.ReferencedSOPInstanceUID) == instance_uid:
                    series_uid = str(series_seq_item.SeriesInstanceUID)
                    break
                #
            #
        #
    if series_uid is not None:
        study_uid = plan.StudyInstanceUID
    else:
        # it's not in the same study as the plan.
        if "StudiesContainingOtherReferencedInstancesSequence" in plan:
            for study_seq_item in plan.StudiesContainingOtherReferencedInstancesSequence:
                for series_seq_item in plan.ReferencedSeriesSequence:
                    for ref_instance_seq_item in series_seq_item:
                        if str(ref_instance_seq_item.ReferencedSOPInstanceUID) == instance_uid:
                            series_uid = str(series_seq_item.SeriesInstanceUID)
                            study_uid = str(study_seq_item.StudyInstanceUID)
                            break
                        #
                    #
                #
            #
    study_series_tuple = (study_uid, series_uid)

    return study_series_tuple


def main(args):
    """test harness for rtbdi factory

    Args:
        args (_type_): command line arguments passed in
    """
    filename = args[1]
    plan = load_plan(Path(filename))
    tx_record_list = []
    fraction_number = 1
    scheduled_time = datetime.now()
    retrieve_ae_title = "TDWII_MOVE_SCP"
    if len(args) > 2:
        fraction_number = int(args[2])
    if len(args) > 3:
        retrieve_ae_title = args[3]
    if len(args) > 4:
        scheduled_time = datetime.fromtimestamp(mktime(strptime(argv[4], "%Y%m%d%H%M")))
    if len(args) > 5:
        treatment_record_paths = args[5:]
        tx_record_list = load_treatment_records(treatment_record_paths)

    bdi = create_rtbdi_from_rtion_plan(plan, fraction_number=fraction_number, treatment_record_list=tx_record_list)
    write_rtbdi(bdi, Path.cwd())
    ups = create_ups_from_plan_and_bdi(plan, bdi, retrieve_ae_title, scheduled_time, tx_record_list)
    write_ups(ups, Path.cwd())


def gen_one_session(plan: Dataset, fraction_number: int, scheduled_date_time: datetime, retrieve_ae_title: str):
    """wrapper to simplify generation of an entire course worth of sessions by invoking this
    multiple times with incrementing fraction number and schedule datetime

    Args:
        plan (Dataset): _description_
        fraction_number (int): _description_
        scheduled_date_time (datetime): _description_
        retrieve_ae_title (str): _description_
    """
    tx_record_list = []
    scheduled_time = scheduled_date_time
    bdi = create_rtbdi_from_rtion_plan(plan, fraction_number, treatment_record_list=tx_record_list)
    write_rtbdi(bdi, Path.cwd())
    ups = create_ups_from_plan_and_bdi(plan, bdi, retrieve_ae_title, scheduled_time, tx_record_list)
    write_ups(ups, Path.cwd())


if __name__ == "__main__":
    if len(argv) < 2:
        print(
            'Usage: python {argv[0]} plan_file <fraction number> <retrieve_ae_title> <ScheduleDateTime "YYYYmmddHHMM"> '
            "<treatment_record1 treatment_record2 ...>"
        )
        print(
            "Defaults to fraction_number=1, retrieve_ae_title=TDWII_MOVE_SCP,"
            " scheduled_date_time=now, no interruptions/continuations"
        )
    else:
        print(" ".join(argv[1:]))
    main(argv)
