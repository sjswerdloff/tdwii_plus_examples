from typing import Any, List, Optional

import pydicom


class IsocenterReferenceSystemSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def XRaySourceIsocenterPrimaryAngle(self) -> Optional[float]:
        if "XRaySourceIsocenterPrimaryAngle" in self._dataset:
            return self._dataset.XRaySourceIsocenterPrimaryAngle
        return None

    @XRaySourceIsocenterPrimaryAngle.setter
    def XRaySourceIsocenterPrimaryAngle(self, value: Optional[float]):
        if value is None:
            if "XRaySourceIsocenterPrimaryAngle" in self._dataset:
                del self._dataset.XRaySourceIsocenterPrimaryAngle
        else:
            self._dataset.XRaySourceIsocenterPrimaryAngle = value

    @property
    def XRaySourceIsocenterSecondaryAngle(self) -> Optional[float]:
        if "XRaySourceIsocenterSecondaryAngle" in self._dataset:
            return self._dataset.XRaySourceIsocenterSecondaryAngle
        return None

    @XRaySourceIsocenterSecondaryAngle.setter
    def XRaySourceIsocenterSecondaryAngle(self, value: Optional[float]):
        if value is None:
            if "XRaySourceIsocenterSecondaryAngle" in self._dataset:
                del self._dataset.XRaySourceIsocenterSecondaryAngle
        else:
            self._dataset.XRaySourceIsocenterSecondaryAngle = value

    @property
    def BreastSupportIsocenterPrimaryAngle(self) -> Optional[float]:
        if "BreastSupportIsocenterPrimaryAngle" in self._dataset:
            return self._dataset.BreastSupportIsocenterPrimaryAngle
        return None

    @BreastSupportIsocenterPrimaryAngle.setter
    def BreastSupportIsocenterPrimaryAngle(self, value: Optional[float]):
        if value is None:
            if "BreastSupportIsocenterPrimaryAngle" in self._dataset:
                del self._dataset.BreastSupportIsocenterPrimaryAngle
        else:
            self._dataset.BreastSupportIsocenterPrimaryAngle = value

    @property
    def BreastSupportIsocenterSecondaryAngle(self) -> Optional[float]:
        if "BreastSupportIsocenterSecondaryAngle" in self._dataset:
            return self._dataset.BreastSupportIsocenterSecondaryAngle
        return None

    @BreastSupportIsocenterSecondaryAngle.setter
    def BreastSupportIsocenterSecondaryAngle(self, value: Optional[float]):
        if value is None:
            if "BreastSupportIsocenterSecondaryAngle" in self._dataset:
                del self._dataset.BreastSupportIsocenterSecondaryAngle
        else:
            self._dataset.BreastSupportIsocenterSecondaryAngle = value

    @property
    def BreastSupportXPositionToIsocenter(self) -> Optional[float]:
        if "BreastSupportXPositionToIsocenter" in self._dataset:
            return self._dataset.BreastSupportXPositionToIsocenter
        return None

    @BreastSupportXPositionToIsocenter.setter
    def BreastSupportXPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "BreastSupportXPositionToIsocenter" in self._dataset:
                del self._dataset.BreastSupportXPositionToIsocenter
        else:
            self._dataset.BreastSupportXPositionToIsocenter = value

    @property
    def BreastSupportYPositionToIsocenter(self) -> Optional[float]:
        if "BreastSupportYPositionToIsocenter" in self._dataset:
            return self._dataset.BreastSupportYPositionToIsocenter
        return None

    @BreastSupportYPositionToIsocenter.setter
    def BreastSupportYPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "BreastSupportYPositionToIsocenter" in self._dataset:
                del self._dataset.BreastSupportYPositionToIsocenter
        else:
            self._dataset.BreastSupportYPositionToIsocenter = value

    @property
    def BreastSupportZPositionToIsocenter(self) -> Optional[float]:
        if "BreastSupportZPositionToIsocenter" in self._dataset:
            return self._dataset.BreastSupportZPositionToIsocenter
        return None

    @BreastSupportZPositionToIsocenter.setter
    def BreastSupportZPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "BreastSupportZPositionToIsocenter" in self._dataset:
                del self._dataset.BreastSupportZPositionToIsocenter
        else:
            self._dataset.BreastSupportZPositionToIsocenter = value

    @property
    def DetectorIsocenterPrimaryAngle(self) -> Optional[float]:
        if "DetectorIsocenterPrimaryAngle" in self._dataset:
            return self._dataset.DetectorIsocenterPrimaryAngle
        return None

    @DetectorIsocenterPrimaryAngle.setter
    def DetectorIsocenterPrimaryAngle(self, value: Optional[float]):
        if value is None:
            if "DetectorIsocenterPrimaryAngle" in self._dataset:
                del self._dataset.DetectorIsocenterPrimaryAngle
        else:
            self._dataset.DetectorIsocenterPrimaryAngle = value

    @property
    def DetectorIsocenterSecondaryAngle(self) -> Optional[float]:
        if "DetectorIsocenterSecondaryAngle" in self._dataset:
            return self._dataset.DetectorIsocenterSecondaryAngle
        return None

    @DetectorIsocenterSecondaryAngle.setter
    def DetectorIsocenterSecondaryAngle(self, value: Optional[float]):
        if value is None:
            if "DetectorIsocenterSecondaryAngle" in self._dataset:
                del self._dataset.DetectorIsocenterSecondaryAngle
        else:
            self._dataset.DetectorIsocenterSecondaryAngle = value

    @property
    def DetectorXPositionToIsocenter(self) -> Optional[float]:
        if "DetectorXPositionToIsocenter" in self._dataset:
            return self._dataset.DetectorXPositionToIsocenter
        return None

    @DetectorXPositionToIsocenter.setter
    def DetectorXPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "DetectorXPositionToIsocenter" in self._dataset:
                del self._dataset.DetectorXPositionToIsocenter
        else:
            self._dataset.DetectorXPositionToIsocenter = value

    @property
    def DetectorYPositionToIsocenter(self) -> Optional[float]:
        if "DetectorYPositionToIsocenter" in self._dataset:
            return self._dataset.DetectorYPositionToIsocenter
        return None

    @DetectorYPositionToIsocenter.setter
    def DetectorYPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "DetectorYPositionToIsocenter" in self._dataset:
                del self._dataset.DetectorYPositionToIsocenter
        else:
            self._dataset.DetectorYPositionToIsocenter = value

    @property
    def DetectorZPositionToIsocenter(self) -> Optional[float]:
        if "DetectorZPositionToIsocenter" in self._dataset:
            return self._dataset.DetectorZPositionToIsocenter
        return None

    @DetectorZPositionToIsocenter.setter
    def DetectorZPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "DetectorZPositionToIsocenter" in self._dataset:
                del self._dataset.DetectorZPositionToIsocenter
        else:
            self._dataset.DetectorZPositionToIsocenter = value

    @property
    def DetectorActiveAreaTLHCPosition(self) -> Optional[List[float]]:
        if "DetectorActiveAreaTLHCPosition" in self._dataset:
            return self._dataset.DetectorActiveAreaTLHCPosition
        return None

    @DetectorActiveAreaTLHCPosition.setter
    def DetectorActiveAreaTLHCPosition(self, value: Optional[List[float]]):
        if value is None:
            if "DetectorActiveAreaTLHCPosition" in self._dataset:
                del self._dataset.DetectorActiveAreaTLHCPosition
        else:
            self._dataset.DetectorActiveAreaTLHCPosition = value

    @property
    def DetectorActiveAreaOrientation(self) -> Optional[List[float]]:
        if "DetectorActiveAreaOrientation" in self._dataset:
            return self._dataset.DetectorActiveAreaOrientation
        return None

    @DetectorActiveAreaOrientation.setter
    def DetectorActiveAreaOrientation(self, value: Optional[List[float]]):
        if value is None:
            if "DetectorActiveAreaOrientation" in self._dataset:
                del self._dataset.DetectorActiveAreaOrientation
        else:
            self._dataset.DetectorActiveAreaOrientation = value
