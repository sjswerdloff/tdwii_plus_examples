from pydicom import dcmwrite
from pydicom.dataset import Dataset
from pydicom.uid import UID
from pynetdicom.sop_class import UnifiedProcedureStepPush


def generate_progress_update(
    sop_instance_uid: str | UID, transaction_uid: str | UID, progress: int, description: str = None
) -> Dataset:
    """Generates DICOM dataset to use as a Modification List for N-SET.

    Returns:
        A DICOM datasets.
    """

    modification_list = Dataset()
    modification_list.AffectedSOPInstanceUID = str(sop_instance_uid)
    modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
    modification_list.TransactionUID = str(transaction_uid)
    sequence_item = Dataset()
    sequence_item.ProcedureStepProgress = progress
    if description is not None:
        sequence_item.ProcedureStepProgressDescription = description
    modification_list.ProcedureStepProgressInformationSequence = [sequence_item]

    return modification_list


def save_modification_list(ds, output_file):
    """
    Save a DICOM modification list dataset to a file as a raw dataset (no meta info).
    """
    ds.is_little_endian = True
    ds.is_implicit_VR = True
    dcmwrite(output_file, ds, write_like_original=True)
