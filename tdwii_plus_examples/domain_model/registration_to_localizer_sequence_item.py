from typing import Any, List, Optional  # noqa

import pydicom


class RegistrationToLocalizerSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RegisteredLocalizerUnits(self) -> Optional[str]:
        if "RegisteredLocalizerUnits" in self._dataset:
            return self._dataset.RegisteredLocalizerUnits
        return None

    @RegisteredLocalizerUnits.setter
    def RegisteredLocalizerUnits(self, value: Optional[str]):
        if value is None:
            if "RegisteredLocalizerUnits" in self._dataset:
                del self._dataset.RegisteredLocalizerUnits
        else:
            self._dataset.RegisteredLocalizerUnits = value

    @property
    def RegisteredLocalizerTopLeftHandCorner(self) -> Optional[List[float]]:
        if "RegisteredLocalizerTopLeftHandCorner" in self._dataset:
            return self._dataset.RegisteredLocalizerTopLeftHandCorner
        return None

    @RegisteredLocalizerTopLeftHandCorner.setter
    def RegisteredLocalizerTopLeftHandCorner(self, value: Optional[List[float]]):
        if value is None:
            if "RegisteredLocalizerTopLeftHandCorner" in self._dataset:
                del self._dataset.RegisteredLocalizerTopLeftHandCorner
        else:
            self._dataset.RegisteredLocalizerTopLeftHandCorner = value

    @property
    def RegisteredLocalizerBottomRightHandCorner(self) -> Optional[List[float]]:
        if "RegisteredLocalizerBottomRightHandCorner" in self._dataset:
            return self._dataset.RegisteredLocalizerBottomRightHandCorner
        return None

    @RegisteredLocalizerBottomRightHandCorner.setter
    def RegisteredLocalizerBottomRightHandCorner(self, value: Optional[List[float]]):
        if value is None:
            if "RegisteredLocalizerBottomRightHandCorner" in self._dataset:
                del self._dataset.RegisteredLocalizerBottomRightHandCorner
        else:
            self._dataset.RegisteredLocalizerBottomRightHandCorner = value
