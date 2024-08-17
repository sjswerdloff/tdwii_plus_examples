from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class IonRangeCompensatorSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

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
    def CompensatorNumber(self) -> Optional[int]:
        if "CompensatorNumber" in self._dataset:
            return self._dataset.CompensatorNumber
        return None

    @CompensatorNumber.setter
    def CompensatorNumber(self, value: Optional[int]):
        if value is None:
            if "CompensatorNumber" in self._dataset:
                del self._dataset.CompensatorNumber
        else:
            self._dataset.CompensatorNumber = value

    @property
    def CompensatorID(self) -> Optional[str]:
        if "CompensatorID" in self._dataset:
            return self._dataset.CompensatorID
        return None

    @CompensatorID.setter
    def CompensatorID(self, value: Optional[str]):
        if value is None:
            if "CompensatorID" in self._dataset:
                del self._dataset.CompensatorID
        else:
            self._dataset.CompensatorID = value

    @property
    def CompensatorRows(self) -> Optional[int]:
        if "CompensatorRows" in self._dataset:
            return self._dataset.CompensatorRows
        return None

    @CompensatorRows.setter
    def CompensatorRows(self, value: Optional[int]):
        if value is None:
            if "CompensatorRows" in self._dataset:
                del self._dataset.CompensatorRows
        else:
            self._dataset.CompensatorRows = value

    @property
    def CompensatorColumns(self) -> Optional[int]:
        if "CompensatorColumns" in self._dataset:
            return self._dataset.CompensatorColumns
        return None

    @CompensatorColumns.setter
    def CompensatorColumns(self, value: Optional[int]):
        if value is None:
            if "CompensatorColumns" in self._dataset:
                del self._dataset.CompensatorColumns
        else:
            self._dataset.CompensatorColumns = value

    @property
    def CompensatorPixelSpacing(self) -> Optional[List[Decimal]]:
        if "CompensatorPixelSpacing" in self._dataset:
            return self._dataset.CompensatorPixelSpacing
        return None

    @CompensatorPixelSpacing.setter
    def CompensatorPixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "CompensatorPixelSpacing" in self._dataset:
                del self._dataset.CompensatorPixelSpacing
        else:
            self._dataset.CompensatorPixelSpacing = value

    @property
    def CompensatorPosition(self) -> Optional[List[Decimal]]:
        if "CompensatorPosition" in self._dataset:
            return self._dataset.CompensatorPosition
        return None

    @CompensatorPosition.setter
    def CompensatorPosition(self, value: Optional[List[Decimal]]):
        if value is None:
            if "CompensatorPosition" in self._dataset:
                del self._dataset.CompensatorPosition
        else:
            self._dataset.CompensatorPosition = value

    @property
    def CompensatorThicknessData(self) -> Optional[List[Decimal]]:
        if "CompensatorThicknessData" in self._dataset:
            return self._dataset.CompensatorThicknessData
        return None

    @CompensatorThicknessData.setter
    def CompensatorThicknessData(self, value: Optional[List[Decimal]]):
        if value is None:
            if "CompensatorThicknessData" in self._dataset:
                del self._dataset.CompensatorThicknessData
        else:
            self._dataset.CompensatorThicknessData = value

    @property
    def AccessoryCode(self) -> Optional[str]:
        if "AccessoryCode" in self._dataset:
            return self._dataset.AccessoryCode
        return None

    @AccessoryCode.setter
    def AccessoryCode(self, value: Optional[str]):
        if value is None:
            if "AccessoryCode" in self._dataset:
                del self._dataset.AccessoryCode
        else:
            self._dataset.AccessoryCode = value

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
    def CompensatorMountingPosition(self) -> Optional[str]:
        if "CompensatorMountingPosition" in self._dataset:
            return self._dataset.CompensatorMountingPosition
        return None

    @CompensatorMountingPosition.setter
    def CompensatorMountingPosition(self, value: Optional[str]):
        if value is None:
            if "CompensatorMountingPosition" in self._dataset:
                del self._dataset.CompensatorMountingPosition
        else:
            self._dataset.CompensatorMountingPosition = value

    @property
    def IsocenterToCompensatorTrayDistance(self) -> Optional[float]:
        if "IsocenterToCompensatorTrayDistance" in self._dataset:
            return self._dataset.IsocenterToCompensatorTrayDistance
        return None

    @IsocenterToCompensatorTrayDistance.setter
    def IsocenterToCompensatorTrayDistance(self, value: Optional[float]):
        if value is None:
            if "IsocenterToCompensatorTrayDistance" in self._dataset:
                del self._dataset.IsocenterToCompensatorTrayDistance
        else:
            self._dataset.IsocenterToCompensatorTrayDistance = value

    @property
    def CompensatorColumnOffset(self) -> Optional[float]:
        if "CompensatorColumnOffset" in self._dataset:
            return self._dataset.CompensatorColumnOffset
        return None

    @CompensatorColumnOffset.setter
    def CompensatorColumnOffset(self, value: Optional[float]):
        if value is None:
            if "CompensatorColumnOffset" in self._dataset:
                del self._dataset.CompensatorColumnOffset
        else:
            self._dataset.CompensatorColumnOffset = value

    @property
    def IsocenterToCompensatorDistances(self) -> Optional[List[float]]:
        if "IsocenterToCompensatorDistances" in self._dataset:
            return self._dataset.IsocenterToCompensatorDistances
        return None

    @IsocenterToCompensatorDistances.setter
    def IsocenterToCompensatorDistances(self, value: Optional[List[float]]):
        if value is None:
            if "IsocenterToCompensatorDistances" in self._dataset:
                del self._dataset.IsocenterToCompensatorDistances
        else:
            self._dataset.IsocenterToCompensatorDistances = value

    @property
    def CompensatorRelativeStoppingPowerRatio(self) -> Optional[float]:
        if "CompensatorRelativeStoppingPowerRatio" in self._dataset:
            return self._dataset.CompensatorRelativeStoppingPowerRatio
        return None

    @CompensatorRelativeStoppingPowerRatio.setter
    def CompensatorRelativeStoppingPowerRatio(self, value: Optional[float]):
        if value is None:
            if "CompensatorRelativeStoppingPowerRatio" in self._dataset:
                del self._dataset.CompensatorRelativeStoppingPowerRatio
        else:
            self._dataset.CompensatorRelativeStoppingPowerRatio = value

    @property
    def CompensatorMillingToolDiameter(self) -> Optional[float]:
        if "CompensatorMillingToolDiameter" in self._dataset:
            return self._dataset.CompensatorMillingToolDiameter
        return None

    @CompensatorMillingToolDiameter.setter
    def CompensatorMillingToolDiameter(self, value: Optional[float]):
        if value is None:
            if "CompensatorMillingToolDiameter" in self._dataset:
                del self._dataset.CompensatorMillingToolDiameter
        else:
            self._dataset.CompensatorMillingToolDiameter = value

    @property
    def CompensatorDescription(self) -> Optional[str]:
        if "CompensatorDescription" in self._dataset:
            return self._dataset.CompensatorDescription
        return None

    @CompensatorDescription.setter
    def CompensatorDescription(self, value: Optional[str]):
        if value is None:
            if "CompensatorDescription" in self._dataset:
                del self._dataset.CompensatorDescription
        else:
            self._dataset.CompensatorDescription = value
