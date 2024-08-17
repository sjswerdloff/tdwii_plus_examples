from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class TablePositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TableHorizontalRotationAngle(self) -> Optional[float]:
        if "TableHorizontalRotationAngle" in self._dataset:
            return self._dataset.TableHorizontalRotationAngle
        return None

    @TableHorizontalRotationAngle.setter
    def TableHorizontalRotationAngle(self, value: Optional[float]):
        if value is None:
            if "TableHorizontalRotationAngle" in self._dataset:
                del self._dataset.TableHorizontalRotationAngle
        else:
            self._dataset.TableHorizontalRotationAngle = value

    @property
    def TableHeadTiltAngle(self) -> Optional[float]:
        if "TableHeadTiltAngle" in self._dataset:
            return self._dataset.TableHeadTiltAngle
        return None

    @TableHeadTiltAngle.setter
    def TableHeadTiltAngle(self, value: Optional[float]):
        if value is None:
            if "TableHeadTiltAngle" in self._dataset:
                del self._dataset.TableHeadTiltAngle
        else:
            self._dataset.TableHeadTiltAngle = value

    @property
    def TableCradleTiltAngle(self) -> Optional[float]:
        if "TableCradleTiltAngle" in self._dataset:
            return self._dataset.TableCradleTiltAngle
        return None

    @TableCradleTiltAngle.setter
    def TableCradleTiltAngle(self, value: Optional[float]):
        if value is None:
            if "TableCradleTiltAngle" in self._dataset:
                del self._dataset.TableCradleTiltAngle
        else:
            self._dataset.TableCradleTiltAngle = value

    @property
    def TableTopVerticalPosition(self) -> Optional[Decimal]:
        if "TableTopVerticalPosition" in self._dataset:
            return self._dataset.TableTopVerticalPosition
        return None

    @TableTopVerticalPosition.setter
    def TableTopVerticalPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopVerticalPosition" in self._dataset:
                del self._dataset.TableTopVerticalPosition
        else:
            self._dataset.TableTopVerticalPosition = value

    @property
    def TableTopLongitudinalPosition(self) -> Optional[Decimal]:
        if "TableTopLongitudinalPosition" in self._dataset:
            return self._dataset.TableTopLongitudinalPosition
        return None

    @TableTopLongitudinalPosition.setter
    def TableTopLongitudinalPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLongitudinalPosition" in self._dataset:
                del self._dataset.TableTopLongitudinalPosition
        else:
            self._dataset.TableTopLongitudinalPosition = value

    @property
    def TableTopLateralPosition(self) -> Optional[Decimal]:
        if "TableTopLateralPosition" in self._dataset:
            return self._dataset.TableTopLateralPosition
        return None

    @TableTopLateralPosition.setter
    def TableTopLateralPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLateralPosition" in self._dataset:
                del self._dataset.TableTopLateralPosition
        else:
            self._dataset.TableTopLateralPosition = value
