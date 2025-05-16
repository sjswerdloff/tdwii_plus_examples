from enum import Enum, unique

from pydicom import Sequence
from pydicom.dataset import Dataset
from pydicom.uid import UID


@unique
class ValueType(Enum):
    """
    Enumerates the allowed Content Item Value Type as defined in PS3.3 C.17.3.2.1

    """

    TEXT = "TEXT"
    NUM = "NUM"
    NUMERIC = "NUMERIC"  # not in Table C.17.3-7 !?
    CODE = "CODE"
    DATETIME = "DATETIME"
    DATE = "DATE"
    TIME = "TIME"
    UIDREF = "UIDREF"
    PNAME = "PNAME"
    COMPOSITE = "COMPOSITE"
    IMAGE = "IMAGE"
    WAVEFORM = "WAVEFORM"
    SCOORD = "SCOORD"
    SCOORD3D = "SCOORD3D"
    TCOORD = "TCOORD"
    CONTAINER = "CONTAINER"
    TABLE = "TABLE"


def create_measurement_unit_code_seq_item(value_unit: str = None) -> Dataset:
    """
    Return a DICOM Code Sequence Item for UCUM units of measurement.
    See PS3.16 7.2.2 Measurement Unit
    Only "no units" is supported so far.

    Args:
        value_unit (str): The unit of measurement. Only "no units" is supported.

    Returns:
        Dataset: DICOM code sequence item for 'no units'.

    Raises:
        ValueError: If value_unit is not supported.
    """
    if not value_unit or value_unit == "1" or value_unit == "no units":
        return create_code_seq_item("1", "UCUM", "no units")
    raise ValueError(f"Unsupported value_unit: {value_unit!r}")


def create_code_seq_item(value: str | int, designator: str, meaning: str) -> Dataset:
    """
    Create a DICOM Basic Code Sequence Item Dataset.
    See PS3.3 Table 8.8-1a. Basic Code Sequence Macro Attributes

    Args:
        value (str | int): The code value.
        designator (str): The coding scheme designator.
        meaning (str): The code meaning.

    Returns:
        Dataset: DICOM code sequence item.
    """
    code_seq_item = Dataset()
    code_seq_item.CodeValue = value
    code_seq_item.CodingSchemeDesignator = designator
    code_seq_item.CodeMeaning = meaning
    return code_seq_item


def create_content_item(value_type: ValueType, value: any, code_seq_item: Dataset, value_unit: str = None) -> Dataset:
    """
    Create a DICOM Content Item Dataset for use in Code Sequences of UPS.
    See PS3.3 Table 10-2. Content Item Macro Attributes
    See PS3.16 7.2.2 Measurement Unit

    Args:
        value_type (ValueType): The VT (ValueType.TEXT or ValueType.NUMERIC).
        value_unit (str): The unit of a value of type NUMERIC. Defaults to None.
        value (any): The value to store.
        code_seq_item (Dataset): The concept name code sequence item.

    Returns:
        Dataset: DICOM content item.
    """
    content_item = Dataset()
    content_item.ValueType = value_type.value
    if code_seq_item is not None:
        content_item.ConceptNameCodeSequence = Sequence([code_seq_item])
    if value_type == ValueType.TEXT:
        content_item.TextValue = str(value)
    elif value_type == ValueType.NUMERIC:
        content_item.MeasurementUnitsCodeSequence = Sequence([create_measurement_unit_code_seq_item()])
        content_item.NumericValue = value
    else:
        raise ValueError(f"Value Type {value_type} not supported")
    return content_item


def create_referenced_instances_and_access_item(
    retrieve_ae_title: str | UID,
    study_instance_uid: str | UID,
    series_instance_uid: str | UID,
    sop_class_uid: str | UID,
    sop_instance_uid: str | UID,
) -> Dataset:
    """
    Create a DICOM Referenced Instances and Access item Dataset.

    Args:
        retrieve_ae_title (str): AE Title for retrieval.
        study_instance_uid (str): Study Instance UID.
        series_instance_uid (str): Series Instance UID.
        sop_class_uid (str): SOP Class UID.
        sop_instance_uid (str): SOP Instance UID.

    Returns:
        Dataset: Referenced Instances and Access item.
    """

    ref_instance_seq_item = Dataset()

    ref_instance_seq_item.TypeOfInstances = "DICOM"
    ref_instance_seq_item.StudyInstanceUID = str(study_instance_uid)
    ref_instance_seq_item.SeriesInstanceUID = str(series_instance_uid)

    dicom_retrieval_seq_item = Dataset()
    dicom_retrieval_seq_item.RetrieveAETitle = retrieve_ae_title
    ref_instance_seq_item.DICOMRetrievalSequence = Sequence([dicom_retrieval_seq_item])

    ref_sop_seq_item = Dataset()
    ref_sop_seq_item.ReferencedSOPClassUID = str(sop_class_uid)
    ref_sop_seq_item.ReferencedSOPInstanceUID = str(sop_instance_uid)
    ref_instance_seq_item.ReferencedSOPSequence = Sequence([ref_sop_seq_item])

    return ref_instance_seq_item
