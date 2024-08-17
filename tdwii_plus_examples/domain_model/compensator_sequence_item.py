from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class CompensatorSequenceItem:
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
    def SourceToCompensatorTrayDistance(self) -> Optional[Decimal]:
        if "SourceToCompensatorTrayDistance" in self._dataset:
            return self._dataset.SourceToCompensatorTrayDistance
        return None

    @SourceToCompensatorTrayDistance.setter
    def SourceToCompensatorTrayDistance(self, value: Optional[Decimal]):
        if value is None:
            if "SourceToCompensatorTrayDistance" in self._dataset:
                del self._dataset.SourceToCompensatorTrayDistance
        else:
            self._dataset.SourceToCompensatorTrayDistance = value

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
    def CompensatorTransmissionData(self) -> Optional[List[Decimal]]:
        if "CompensatorTransmissionData" in self._dataset:
            return self._dataset.CompensatorTransmissionData
        return None

    @CompensatorTransmissionData.setter
    def CompensatorTransmissionData(self, value: Optional[List[Decimal]]):
        if value is None:
            if "CompensatorTransmissionData" in self._dataset:
                del self._dataset.CompensatorTransmissionData
        else:
            self._dataset.CompensatorTransmissionData = value

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
    def CompensatorType(self) -> Optional[str]:
        if "CompensatorType" in self._dataset:
            return self._dataset.CompensatorType
        return None

    @CompensatorType.setter
    def CompensatorType(self, value: Optional[str]):
        if value is None:
            if "CompensatorType" in self._dataset:
                del self._dataset.CompensatorType
        else:
            self._dataset.CompensatorType = value

    @property
    def CompensatorTrayID(self) -> Optional[str]:
        if "CompensatorTrayID" in self._dataset:
            return self._dataset.CompensatorTrayID
        return None

    @CompensatorTrayID.setter
    def CompensatorTrayID(self, value: Optional[str]):
        if value is None:
            if "CompensatorTrayID" in self._dataset:
                del self._dataset.CompensatorTrayID
        else:
            self._dataset.CompensatorTrayID = value

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
    def SourceToCompensatorDistance(self) -> Optional[List[Decimal]]:
        if "SourceToCompensatorDistance" in self._dataset:
            return self._dataset.SourceToCompensatorDistance
        return None

    @SourceToCompensatorDistance.setter
    def SourceToCompensatorDistance(self, value: Optional[List[Decimal]]):
        if value is None:
            if "SourceToCompensatorDistance" in self._dataset:
                del self._dataset.SourceToCompensatorDistance
        else:
            self._dataset.SourceToCompensatorDistance = value

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

    @property
    def TrayAccessoryCode(self) -> Optional[str]:
        if "TrayAccessoryCode" in self._dataset:
            return self._dataset.TrayAccessoryCode
        return None

    @TrayAccessoryCode.setter
    def TrayAccessoryCode(self, value: Optional[str]):
        if value is None:
            if "TrayAccessoryCode" in self._dataset:
                del self._dataset.TrayAccessoryCode
        else:
            self._dataset.TrayAccessoryCode = value
