from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class PETFrameAcquisitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DataCollectionDiameter(self) -> Optional[Decimal]:
        if "DataCollectionDiameter" in self._dataset:
            return self._dataset.DataCollectionDiameter
        return None

    @DataCollectionDiameter.setter
    def DataCollectionDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "DataCollectionDiameter" in self._dataset:
                del self._dataset.DataCollectionDiameter
        else:
            self._dataset.DataCollectionDiameter = value

    @property
    def GantryDetectorTilt(self) -> Optional[Decimal]:
        if "GantryDetectorTilt" in self._dataset:
            return self._dataset.GantryDetectorTilt
        return None

    @GantryDetectorTilt.setter
    def GantryDetectorTilt(self, value: Optional[Decimal]):
        if value is None:
            if "GantryDetectorTilt" in self._dataset:
                del self._dataset.GantryDetectorTilt
        else:
            self._dataset.GantryDetectorTilt = value

    @property
    def GantryDetectorSlew(self) -> Optional[Decimal]:
        if "GantryDetectorSlew" in self._dataset:
            return self._dataset.GantryDetectorSlew
        return None

    @GantryDetectorSlew.setter
    def GantryDetectorSlew(self, value: Optional[Decimal]):
        if value is None:
            if "GantryDetectorSlew" in self._dataset:
                del self._dataset.GantryDetectorSlew
        else:
            self._dataset.GantryDetectorSlew = value

    @property
    def TableHeight(self) -> Optional[Decimal]:
        if "TableHeight" in self._dataset:
            return self._dataset.TableHeight
        return None

    @TableHeight.setter
    def TableHeight(self, value: Optional[Decimal]):
        if value is None:
            if "TableHeight" in self._dataset:
                del self._dataset.TableHeight
        else:
            self._dataset.TableHeight = value
