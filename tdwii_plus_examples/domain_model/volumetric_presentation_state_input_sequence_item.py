from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .voilut_sequence_item import VOILUTSequenceItem


class VolumetricPresentationStateInputSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._VOILUTSequence: List[VOILUTSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WindowCenter(self) -> Optional[List[Decimal]]:
        if "WindowCenter" in self._dataset:
            return self._dataset.WindowCenter
        return None

    @WindowCenter.setter
    def WindowCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowCenter" in self._dataset:
                del self._dataset.WindowCenter
        else:
            self._dataset.WindowCenter = value

    @property
    def WindowWidth(self) -> Optional[List[Decimal]]:
        if "WindowWidth" in self._dataset:
            return self._dataset.WindowWidth
        return None

    @WindowWidth.setter
    def WindowWidth(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowWidth" in self._dataset:
                del self._dataset.WindowWidth
        else:
            self._dataset.WindowWidth = value

    @property
    def WindowCenterWidthExplanation(self) -> Optional[List[str]]:
        if "WindowCenterWidthExplanation" in self._dataset:
            return self._dataset.WindowCenterWidthExplanation
        return None

    @WindowCenterWidthExplanation.setter
    def WindowCenterWidthExplanation(self, value: Optional[List[str]]):
        if value is None:
            if "WindowCenterWidthExplanation" in self._dataset:
                del self._dataset.WindowCenterWidthExplanation
        else:
            self._dataset.WindowCenterWidthExplanation = value

    @property
    def VOILUTFunction(self) -> Optional[str]:
        if "VOILUTFunction" in self._dataset:
            return self._dataset.VOILUTFunction
        return None

    @VOILUTFunction.setter
    def VOILUTFunction(self, value: Optional[str]):
        if value is None:
            if "VOILUTFunction" in self._dataset:
                del self._dataset.VOILUTFunction
        else:
            self._dataset.VOILUTFunction = value

    @property
    def VOILUTSequence(self) -> Optional[List[VOILUTSequenceItem]]:
        if "VOILUTSequence" in self._dataset:
            if len(self._VOILUTSequence) == len(self._dataset.VOILUTSequence):
                return self._VOILUTSequence
            else:
                return [VOILUTSequenceItem(x) for x in self._dataset.VOILUTSequence]
        return None

    @VOILUTSequence.setter
    def VOILUTSequence(self, value: Optional[List[VOILUTSequenceItem]]):
        if value is None:
            self._VOILUTSequence = []
            if "VOILUTSequence" in self._dataset:
                del self._dataset.VOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, VOILUTSequenceItem) for item in value):
            raise ValueError("VOILUTSequence must be a list of VOILUTSequenceItem objects")
        else:
            self._VOILUTSequence = value
            if "VOILUTSequence" not in self._dataset:
                self._dataset.VOILUTSequence = pydicom.Sequence()
            self._dataset.VOILUTSequence.clear()
            self._dataset.VOILUTSequence.extend([item.to_dataset() for item in value])

    def add_VOILUT(self, item: VOILUTSequenceItem):
        if not isinstance(item, VOILUTSequenceItem):
            raise ValueError("Item must be an instance of VOILUTSequenceItem")
        self._VOILUTSequence.append(item)
        if "VOILUTSequence" not in self._dataset:
            self._dataset.VOILUTSequence = pydicom.Sequence()
        self._dataset.VOILUTSequence.append(item.to_dataset())

    @property
    def InputSequencePositionIndex(self) -> Optional[int]:
        if "InputSequencePositionIndex" in self._dataset:
            return self._dataset.InputSequencePositionIndex
        return None

    @InputSequencePositionIndex.setter
    def InputSequencePositionIndex(self, value: Optional[int]):
        if value is None:
            if "InputSequencePositionIndex" in self._dataset:
                del self._dataset.InputSequencePositionIndex
        else:
            self._dataset.InputSequencePositionIndex = value

    @property
    def Crop(self) -> Optional[str]:
        if "Crop" in self._dataset:
            return self._dataset.Crop
        return None

    @Crop.setter
    def Crop(self, value: Optional[str]):
        if value is None:
            if "Crop" in self._dataset:
                del self._dataset.Crop
        else:
            self._dataset.Crop = value

    @property
    def CroppingSpecificationIndex(self) -> Optional[List[int]]:
        if "CroppingSpecificationIndex" in self._dataset:
            return self._dataset.CroppingSpecificationIndex
        return None

    @CroppingSpecificationIndex.setter
    def CroppingSpecificationIndex(self, value: Optional[List[int]]):
        if value is None:
            if "CroppingSpecificationIndex" in self._dataset:
                del self._dataset.CroppingSpecificationIndex
        else:
            self._dataset.CroppingSpecificationIndex = value

    @property
    def VolumetricPresentationInputNumber(self) -> Optional[int]:
        if "VolumetricPresentationInputNumber" in self._dataset:
            return self._dataset.VolumetricPresentationInputNumber
        return None

    @VolumetricPresentationInputNumber.setter
    def VolumetricPresentationInputNumber(self, value: Optional[int]):
        if value is None:
            if "VolumetricPresentationInputNumber" in self._dataset:
                del self._dataset.VolumetricPresentationInputNumber
        else:
            self._dataset.VolumetricPresentationInputNumber = value

    @property
    def VolumetricPresentationInputSetUID(self) -> Optional[str]:
        if "VolumetricPresentationInputSetUID" in self._dataset:
            return self._dataset.VolumetricPresentationInputSetUID
        return None

    @VolumetricPresentationInputSetUID.setter
    def VolumetricPresentationInputSetUID(self, value: Optional[str]):
        if value is None:
            if "VolumetricPresentationInputSetUID" in self._dataset:
                del self._dataset.VolumetricPresentationInputSetUID
        else:
            self._dataset.VolumetricPresentationInputSetUID = value

    @property
    def RenderingMethod(self) -> Optional[str]:
        if "RenderingMethod" in self._dataset:
            return self._dataset.RenderingMethod
        return None

    @RenderingMethod.setter
    def RenderingMethod(self, value: Optional[str]):
        if value is None:
            if "RenderingMethod" in self._dataset:
                del self._dataset.RenderingMethod
        else:
            self._dataset.RenderingMethod = value
