from typing import Any, List, Optional

import pydicom


class ReferencedSOPInstanceMACSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MACCalculationTransferSyntaxUID(self) -> Optional[str]:
        if "MACCalculationTransferSyntaxUID" in self._dataset:
            return self._dataset.MACCalculationTransferSyntaxUID
        return None

    @MACCalculationTransferSyntaxUID.setter
    def MACCalculationTransferSyntaxUID(self, value: Optional[str]):
        if value is None:
            if "MACCalculationTransferSyntaxUID" in self._dataset:
                del self._dataset.MACCalculationTransferSyntaxUID
        else:
            self._dataset.MACCalculationTransferSyntaxUID = value

    @property
    def MACAlgorithm(self) -> Optional[str]:
        if "MACAlgorithm" in self._dataset:
            return self._dataset.MACAlgorithm
        return None

    @MACAlgorithm.setter
    def MACAlgorithm(self, value: Optional[str]):
        if value is None:
            if "MACAlgorithm" in self._dataset:
                del self._dataset.MACAlgorithm
        else:
            self._dataset.MACAlgorithm = value

    @property
    def DataElementsSigned(self) -> Optional[List[int]]:
        if "DataElementsSigned" in self._dataset:
            return self._dataset.DataElementsSigned
        return None

    @DataElementsSigned.setter
    def DataElementsSigned(self, value: Optional[List[int]]):
        if value is None:
            if "DataElementsSigned" in self._dataset:
                del self._dataset.DataElementsSigned
        else:
            self._dataset.DataElementsSigned = value

    @property
    def MAC(self) -> Optional[bytes]:
        if "MAC" in self._dataset:
            return self._dataset.MAC
        return None

    @MAC.setter
    def MAC(self, value: Optional[bytes]):
        if value is None:
            if "MAC" in self._dataset:
                del self._dataset.MAC
        else:
            self._dataset.MAC = value
