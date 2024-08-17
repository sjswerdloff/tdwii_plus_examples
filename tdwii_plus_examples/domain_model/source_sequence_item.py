from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class SourceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SourceSerialNumber(self) -> Optional[str]:
        if "SourceSerialNumber" in self._dataset:
            return self._dataset.SourceSerialNumber
        return None

    @SourceSerialNumber.setter
    def SourceSerialNumber(self, value: Optional[str]):
        if value is None:
            if "SourceSerialNumber" in self._dataset:
                del self._dataset.SourceSerialNumber
        else:
            self._dataset.SourceSerialNumber = value

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
    def SourceNumber(self) -> Optional[int]:
        if "SourceNumber" in self._dataset:
            return self._dataset.SourceNumber
        return None

    @SourceNumber.setter
    def SourceNumber(self, value: Optional[int]):
        if value is None:
            if "SourceNumber" in self._dataset:
                del self._dataset.SourceNumber
        else:
            self._dataset.SourceNumber = value

    @property
    def SourceType(self) -> Optional[str]:
        if "SourceType" in self._dataset:
            return self._dataset.SourceType
        return None

    @SourceType.setter
    def SourceType(self, value: Optional[str]):
        if value is None:
            if "SourceType" in self._dataset:
                del self._dataset.SourceType
        else:
            self._dataset.SourceType = value

    @property
    def SourceManufacturer(self) -> Optional[str]:
        if "SourceManufacturer" in self._dataset:
            return self._dataset.SourceManufacturer
        return None

    @SourceManufacturer.setter
    def SourceManufacturer(self, value: Optional[str]):
        if value is None:
            if "SourceManufacturer" in self._dataset:
                del self._dataset.SourceManufacturer
        else:
            self._dataset.SourceManufacturer = value

    @property
    def ActiveSourceDiameter(self) -> Optional[Decimal]:
        if "ActiveSourceDiameter" in self._dataset:
            return self._dataset.ActiveSourceDiameter
        return None

    @ActiveSourceDiameter.setter
    def ActiveSourceDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "ActiveSourceDiameter" in self._dataset:
                del self._dataset.ActiveSourceDiameter
        else:
            self._dataset.ActiveSourceDiameter = value

    @property
    def ActiveSourceLength(self) -> Optional[Decimal]:
        if "ActiveSourceLength" in self._dataset:
            return self._dataset.ActiveSourceLength
        return None

    @ActiveSourceLength.setter
    def ActiveSourceLength(self, value: Optional[Decimal]):
        if value is None:
            if "ActiveSourceLength" in self._dataset:
                del self._dataset.ActiveSourceLength
        else:
            self._dataset.ActiveSourceLength = value

    @property
    def SourceModelID(self) -> Optional[str]:
        if "SourceModelID" in self._dataset:
            return self._dataset.SourceModelID
        return None

    @SourceModelID.setter
    def SourceModelID(self, value: Optional[str]):
        if value is None:
            if "SourceModelID" in self._dataset:
                del self._dataset.SourceModelID
        else:
            self._dataset.SourceModelID = value

    @property
    def SourceDescription(self) -> Optional[str]:
        if "SourceDescription" in self._dataset:
            return self._dataset.SourceDescription
        return None

    @SourceDescription.setter
    def SourceDescription(self, value: Optional[str]):
        if value is None:
            if "SourceDescription" in self._dataset:
                del self._dataset.SourceDescription
        else:
            self._dataset.SourceDescription = value

    @property
    def SourceEncapsulationNominalThickness(self) -> Optional[Decimal]:
        if "SourceEncapsulationNominalThickness" in self._dataset:
            return self._dataset.SourceEncapsulationNominalThickness
        return None

    @SourceEncapsulationNominalThickness.setter
    def SourceEncapsulationNominalThickness(self, value: Optional[Decimal]):
        if value is None:
            if "SourceEncapsulationNominalThickness" in self._dataset:
                del self._dataset.SourceEncapsulationNominalThickness
        else:
            self._dataset.SourceEncapsulationNominalThickness = value

    @property
    def SourceEncapsulationNominalTransmission(self) -> Optional[Decimal]:
        if "SourceEncapsulationNominalTransmission" in self._dataset:
            return self._dataset.SourceEncapsulationNominalTransmission
        return None

    @SourceEncapsulationNominalTransmission.setter
    def SourceEncapsulationNominalTransmission(self, value: Optional[Decimal]):
        if value is None:
            if "SourceEncapsulationNominalTransmission" in self._dataset:
                del self._dataset.SourceEncapsulationNominalTransmission
        else:
            self._dataset.SourceEncapsulationNominalTransmission = value

    @property
    def SourceIsotopeName(self) -> Optional[str]:
        if "SourceIsotopeName" in self._dataset:
            return self._dataset.SourceIsotopeName
        return None

    @SourceIsotopeName.setter
    def SourceIsotopeName(self, value: Optional[str]):
        if value is None:
            if "SourceIsotopeName" in self._dataset:
                del self._dataset.SourceIsotopeName
        else:
            self._dataset.SourceIsotopeName = value

    @property
    def SourceIsotopeHalfLife(self) -> Optional[Decimal]:
        if "SourceIsotopeHalfLife" in self._dataset:
            return self._dataset.SourceIsotopeHalfLife
        return None

    @SourceIsotopeHalfLife.setter
    def SourceIsotopeHalfLife(self, value: Optional[Decimal]):
        if value is None:
            if "SourceIsotopeHalfLife" in self._dataset:
                del self._dataset.SourceIsotopeHalfLife
        else:
            self._dataset.SourceIsotopeHalfLife = value

    @property
    def SourceStrengthUnits(self) -> Optional[str]:
        if "SourceStrengthUnits" in self._dataset:
            return self._dataset.SourceStrengthUnits
        return None

    @SourceStrengthUnits.setter
    def SourceStrengthUnits(self, value: Optional[str]):
        if value is None:
            if "SourceStrengthUnits" in self._dataset:
                del self._dataset.SourceStrengthUnits
        else:
            self._dataset.SourceStrengthUnits = value

    @property
    def ReferenceAirKermaRate(self) -> Optional[Decimal]:
        if "ReferenceAirKermaRate" in self._dataset:
            return self._dataset.ReferenceAirKermaRate
        return None

    @ReferenceAirKermaRate.setter
    def ReferenceAirKermaRate(self, value: Optional[Decimal]):
        if value is None:
            if "ReferenceAirKermaRate" in self._dataset:
                del self._dataset.ReferenceAirKermaRate
        else:
            self._dataset.ReferenceAirKermaRate = value

    @property
    def SourceStrength(self) -> Optional[Decimal]:
        if "SourceStrength" in self._dataset:
            return self._dataset.SourceStrength
        return None

    @SourceStrength.setter
    def SourceStrength(self, value: Optional[Decimal]):
        if value is None:
            if "SourceStrength" in self._dataset:
                del self._dataset.SourceStrength
        else:
            self._dataset.SourceStrength = value

    @property
    def SourceStrengthReferenceDate(self) -> Optional[str]:
        if "SourceStrengthReferenceDate" in self._dataset:
            return self._dataset.SourceStrengthReferenceDate
        return None

    @SourceStrengthReferenceDate.setter
    def SourceStrengthReferenceDate(self, value: Optional[str]):
        if value is None:
            if "SourceStrengthReferenceDate" in self._dataset:
                del self._dataset.SourceStrengthReferenceDate
        else:
            self._dataset.SourceStrengthReferenceDate = value

    @property
    def SourceStrengthReferenceTime(self) -> Optional[str]:
        if "SourceStrengthReferenceTime" in self._dataset:
            return self._dataset.SourceStrengthReferenceTime
        return None

    @SourceStrengthReferenceTime.setter
    def SourceStrengthReferenceTime(self, value: Optional[str]):
        if value is None:
            if "SourceStrengthReferenceTime" in self._dataset:
                del self._dataset.SourceStrengthReferenceTime
        else:
            self._dataset.SourceStrengthReferenceTime = value
