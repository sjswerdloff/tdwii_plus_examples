from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class CompensatorShapeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._CompensatorShapeFabricationCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MaterialID(self) -> Optional[str]:
        if "MaterialID" in self._dataset:
            return self._dataset.MaterialID
        return None

    @MaterialID.setter
    def MaterialID(self, value: Optional[str]):
        if value is None:
            if "MaterialID" in self._dataset:
                del self._dataset.MaterialID
        else:
            self._dataset.MaterialID = value

    @property
    def CompensatorDivergence(self) -> Optional[str]:
        if "CompensatorDivergence" in self._dataset:
            return self._dataset.CompensatorDivergence
        return None

    @CompensatorDivergence.setter
    def CompensatorDivergence(self, value: Optional[str]):
        if value is None:
            if "CompensatorDivergence" in self._dataset:
                del self._dataset.CompensatorDivergence
        else:
            self._dataset.CompensatorDivergence = value

    @property
    def CompensatorProximalThicknessMap(self) -> Optional[bytes]:
        if "CompensatorProximalThicknessMap" in self._dataset:
            return self._dataset.CompensatorProximalThicknessMap
        return None

    @CompensatorProximalThicknessMap.setter
    def CompensatorProximalThicknessMap(self, value: Optional[bytes]):
        if value is None:
            if "CompensatorProximalThicknessMap" in self._dataset:
                del self._dataset.CompensatorProximalThicknessMap
        else:
            self._dataset.CompensatorProximalThicknessMap = value

    @property
    def CompensatorDistalThicknessMap(self) -> Optional[bytes]:
        if "CompensatorDistalThicknessMap" in self._dataset:
            return self._dataset.CompensatorDistalThicknessMap
        return None

    @CompensatorDistalThicknessMap.setter
    def CompensatorDistalThicknessMap(self, value: Optional[bytes]):
        if value is None:
            if "CompensatorDistalThicknessMap" in self._dataset:
                del self._dataset.CompensatorDistalThicknessMap
        else:
            self._dataset.CompensatorDistalThicknessMap = value

    @property
    def CompensatorShapeFabricationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "CompensatorShapeFabricationCodeSequence" in self._dataset:
            if len(self._CompensatorShapeFabricationCodeSequence) == len(
                self._dataset.CompensatorShapeFabricationCodeSequence
            ):
                return self._CompensatorShapeFabricationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.CompensatorShapeFabricationCodeSequence]
        return None

    @CompensatorShapeFabricationCodeSequence.setter
    def CompensatorShapeFabricationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._CompensatorShapeFabricationCodeSequence = []
            if "CompensatorShapeFabricationCodeSequence" in self._dataset:
                del self._dataset.CompensatorShapeFabricationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("CompensatorShapeFabricationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._CompensatorShapeFabricationCodeSequence = value
            if "CompensatorShapeFabricationCodeSequence" not in self._dataset:
                self._dataset.CompensatorShapeFabricationCodeSequence = pydicom.Sequence()
            self._dataset.CompensatorShapeFabricationCodeSequence.clear()
            self._dataset.CompensatorShapeFabricationCodeSequence.extend([item.to_dataset() for item in value])

    def add_CompensatorShapeFabricationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._CompensatorShapeFabricationCodeSequence.append(item)
        if "CompensatorShapeFabricationCodeSequence" not in self._dataset:
            self._dataset.CompensatorShapeFabricationCodeSequence = pydicom.Sequence()
        self._dataset.CompensatorShapeFabricationCodeSequence.append(item.to_dataset())

    @property
    def RadiationBeamCompensatorMillingToolDiameter(self) -> Optional[float]:
        if "RadiationBeamCompensatorMillingToolDiameter" in self._dataset:
            return self._dataset.RadiationBeamCompensatorMillingToolDiameter
        return None

    @RadiationBeamCompensatorMillingToolDiameter.setter
    def RadiationBeamCompensatorMillingToolDiameter(self, value: Optional[float]):
        if value is None:
            if "RadiationBeamCompensatorMillingToolDiameter" in self._dataset:
                del self._dataset.RadiationBeamCompensatorMillingToolDiameter
        else:
            self._dataset.RadiationBeamCompensatorMillingToolDiameter = value
