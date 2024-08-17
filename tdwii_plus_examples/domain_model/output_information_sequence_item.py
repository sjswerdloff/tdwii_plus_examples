from typing import Any, List, Optional

import pydicom

from .dicom_storage_sequence_item import DICOMStorageSequenceItem
from .stowrs_storage_sequence_item import STOWRSStorageSequenceItem
from .xds_storage_sequence_item import XDSStorageSequenceItem


class OutputInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DICOMStorageSequence: List[DICOMStorageSequenceItem] = []
        self._STOWRSStorageSequence: List[STOWRSStorageSequenceItem] = []
        self._XDSStorageSequence: List[XDSStorageSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPClassUID(self) -> Optional[str]:
        if "ReferencedSOPClassUID" in self._dataset:
            return self._dataset.ReferencedSOPClassUID
        return None

    @ReferencedSOPClassUID.setter
    def ReferencedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPClassUID" in self._dataset:
                del self._dataset.ReferencedSOPClassUID
        else:
            self._dataset.ReferencedSOPClassUID = value

    @property
    def DICOMStorageSequence(self) -> Optional[List[DICOMStorageSequenceItem]]:
        if "DICOMStorageSequence" in self._dataset:
            if len(self._DICOMStorageSequence) == len(self._dataset.DICOMStorageSequence):
                return self._DICOMStorageSequence
            else:
                return [DICOMStorageSequenceItem(x) for x in self._dataset.DICOMStorageSequence]
        return None

    @DICOMStorageSequence.setter
    def DICOMStorageSequence(self, value: Optional[List[DICOMStorageSequenceItem]]):
        if value is None:
            self._DICOMStorageSequence = []
            if "DICOMStorageSequence" in self._dataset:
                del self._dataset.DICOMStorageSequence
        elif not isinstance(value, list) or not all(isinstance(item, DICOMStorageSequenceItem) for item in value):
            raise ValueError(f"DICOMStorageSequence must be a list of DICOMStorageSequenceItem objects")
        else:
            self._DICOMStorageSequence = value
            if "DICOMStorageSequence" not in self._dataset:
                self._dataset.DICOMStorageSequence = pydicom.Sequence()
            self._dataset.DICOMStorageSequence.clear()
            self._dataset.DICOMStorageSequence.extend([item.to_dataset() for item in value])

    def add_DICOMStorage(self, item: DICOMStorageSequenceItem):
        if not isinstance(item, DICOMStorageSequenceItem):
            raise ValueError(f"Item must be an instance of DICOMStorageSequenceItem")
        self._DICOMStorageSequence.append(item)
        if "DICOMStorageSequence" not in self._dataset:
            self._dataset.DICOMStorageSequence = pydicom.Sequence()
        self._dataset.DICOMStorageSequence.append(item.to_dataset())

    @property
    def STOWRSStorageSequence(self) -> Optional[List[STOWRSStorageSequenceItem]]:
        if "STOWRSStorageSequence" in self._dataset:
            if len(self._STOWRSStorageSequence) == len(self._dataset.STOWRSStorageSequence):
                return self._STOWRSStorageSequence
            else:
                return [STOWRSStorageSequenceItem(x) for x in self._dataset.STOWRSStorageSequence]
        return None

    @STOWRSStorageSequence.setter
    def STOWRSStorageSequence(self, value: Optional[List[STOWRSStorageSequenceItem]]):
        if value is None:
            self._STOWRSStorageSequence = []
            if "STOWRSStorageSequence" in self._dataset:
                del self._dataset.STOWRSStorageSequence
        elif not isinstance(value, list) or not all(isinstance(item, STOWRSStorageSequenceItem) for item in value):
            raise ValueError(f"STOWRSStorageSequence must be a list of STOWRSStorageSequenceItem objects")
        else:
            self._STOWRSStorageSequence = value
            if "STOWRSStorageSequence" not in self._dataset:
                self._dataset.STOWRSStorageSequence = pydicom.Sequence()
            self._dataset.STOWRSStorageSequence.clear()
            self._dataset.STOWRSStorageSequence.extend([item.to_dataset() for item in value])

    def add_STOWRSStorage(self, item: STOWRSStorageSequenceItem):
        if not isinstance(item, STOWRSStorageSequenceItem):
            raise ValueError(f"Item must be an instance of STOWRSStorageSequenceItem")
        self._STOWRSStorageSequence.append(item)
        if "STOWRSStorageSequence" not in self._dataset:
            self._dataset.STOWRSStorageSequence = pydicom.Sequence()
        self._dataset.STOWRSStorageSequence.append(item.to_dataset())

    @property
    def XDSStorageSequence(self) -> Optional[List[XDSStorageSequenceItem]]:
        if "XDSStorageSequence" in self._dataset:
            if len(self._XDSStorageSequence) == len(self._dataset.XDSStorageSequence):
                return self._XDSStorageSequence
            else:
                return [XDSStorageSequenceItem(x) for x in self._dataset.XDSStorageSequence]
        return None

    @XDSStorageSequence.setter
    def XDSStorageSequence(self, value: Optional[List[XDSStorageSequenceItem]]):
        if value is None:
            self._XDSStorageSequence = []
            if "XDSStorageSequence" in self._dataset:
                del self._dataset.XDSStorageSequence
        elif not isinstance(value, list) or not all(isinstance(item, XDSStorageSequenceItem) for item in value):
            raise ValueError(f"XDSStorageSequence must be a list of XDSStorageSequenceItem objects")
        else:
            self._XDSStorageSequence = value
            if "XDSStorageSequence" not in self._dataset:
                self._dataset.XDSStorageSequence = pydicom.Sequence()
            self._dataset.XDSStorageSequence.clear()
            self._dataset.XDSStorageSequence.extend([item.to_dataset() for item in value])

    def add_XDSStorage(self, item: XDSStorageSequenceItem):
        if not isinstance(item, XDSStorageSequenceItem):
            raise ValueError(f"Item must be an instance of XDSStorageSequenceItem")
        self._XDSStorageSequence.append(item)
        if "XDSStorageSequence" not in self._dataset:
            self._dataset.XDSStorageSequence = pydicom.Sequence()
        self._dataset.XDSStorageSequence.append(item.to_dataset())
