from typing import Any, List, Optional

import pydicom


class BlendingLUT2SequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BlendingWeightConstant(self) -> Optional[float]:
        if "BlendingWeightConstant" in self._dataset:
            return self._dataset.BlendingWeightConstant
        return None

    @BlendingWeightConstant.setter
    def BlendingWeightConstant(self, value: Optional[float]):
        if value is None:
            if "BlendingWeightConstant" in self._dataset:
                del self._dataset.BlendingWeightConstant
        else:
            self._dataset.BlendingWeightConstant = value

    @property
    def BlendingLookupTableDescriptor(self) -> Optional[List[int]]:
        if "BlendingLookupTableDescriptor" in self._dataset:
            return self._dataset.BlendingLookupTableDescriptor
        return None

    @BlendingLookupTableDescriptor.setter
    def BlendingLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "BlendingLookupTableDescriptor" in self._dataset:
                del self._dataset.BlendingLookupTableDescriptor
        else:
            self._dataset.BlendingLookupTableDescriptor = value

    @property
    def BlendingLookupTableData(self) -> Optional[bytes]:
        if "BlendingLookupTableData" in self._dataset:
            return self._dataset.BlendingLookupTableData
        return None

    @BlendingLookupTableData.setter
    def BlendingLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "BlendingLookupTableData" in self._dataset:
                del self._dataset.BlendingLookupTableData
        else:
            self._dataset.BlendingLookupTableData = value

    @property
    def BlendingLUT2TransferFunction(self) -> Optional[str]:
        if "BlendingLUT2TransferFunction" in self._dataset:
            return self._dataset.BlendingLUT2TransferFunction
        return None

    @BlendingLUT2TransferFunction.setter
    def BlendingLUT2TransferFunction(self, value: Optional[str]):
        if value is None:
            if "BlendingLUT2TransferFunction" in self._dataset:
                del self._dataset.BlendingLUT2TransferFunction
        else:
            self._dataset.BlendingLUT2TransferFunction = value
