from typing import Any, List, Optional  # noqa

import pydicom


class MACParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MACIDNumber(self) -> Optional[int]:
        if "MACIDNumber" in self._dataset:
            return self._dataset.MACIDNumber
        return None

    @MACIDNumber.setter
    def MACIDNumber(self, value: Optional[int]):
        if value is None:
            if "MACIDNumber" in self._dataset:
                del self._dataset.MACIDNumber
        else:
            self._dataset.MACIDNumber = value

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
