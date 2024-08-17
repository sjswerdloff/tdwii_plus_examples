from typing import Any, List, Optional  # noqa

import pydicom


class VisualFieldTestPointNormalsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AgeCorrectedSensitivityDeviationValue(self) -> Optional[float]:
        if "AgeCorrectedSensitivityDeviationValue" in self._dataset:
            return self._dataset.AgeCorrectedSensitivityDeviationValue
        return None

    @AgeCorrectedSensitivityDeviationValue.setter
    def AgeCorrectedSensitivityDeviationValue(self, value: Optional[float]):
        if value is None:
            if "AgeCorrectedSensitivityDeviationValue" in self._dataset:
                del self._dataset.AgeCorrectedSensitivityDeviationValue
        else:
            self._dataset.AgeCorrectedSensitivityDeviationValue = value

    @property
    def AgeCorrectedSensitivityDeviationProbabilityValue(self) -> Optional[float]:
        if "AgeCorrectedSensitivityDeviationProbabilityValue" in self._dataset:
            return self._dataset.AgeCorrectedSensitivityDeviationProbabilityValue
        return None

    @AgeCorrectedSensitivityDeviationProbabilityValue.setter
    def AgeCorrectedSensitivityDeviationProbabilityValue(self, value: Optional[float]):
        if value is None:
            if "AgeCorrectedSensitivityDeviationProbabilityValue" in self._dataset:
                del self._dataset.AgeCorrectedSensitivityDeviationProbabilityValue
        else:
            self._dataset.AgeCorrectedSensitivityDeviationProbabilityValue = value

    @property
    def GeneralizedDefectCorrectedSensitivityDeviationFlag(self) -> Optional[str]:
        if "GeneralizedDefectCorrectedSensitivityDeviationFlag" in self._dataset:
            return self._dataset.GeneralizedDefectCorrectedSensitivityDeviationFlag
        return None

    @GeneralizedDefectCorrectedSensitivityDeviationFlag.setter
    def GeneralizedDefectCorrectedSensitivityDeviationFlag(self, value: Optional[str]):
        if value is None:
            if "GeneralizedDefectCorrectedSensitivityDeviationFlag" in self._dataset:
                del self._dataset.GeneralizedDefectCorrectedSensitivityDeviationFlag
        else:
            self._dataset.GeneralizedDefectCorrectedSensitivityDeviationFlag = value

    @property
    def GeneralizedDefectCorrectedSensitivityDeviationValue(self) -> Optional[float]:
        if "GeneralizedDefectCorrectedSensitivityDeviationValue" in self._dataset:
            return self._dataset.GeneralizedDefectCorrectedSensitivityDeviationValue
        return None

    @GeneralizedDefectCorrectedSensitivityDeviationValue.setter
    def GeneralizedDefectCorrectedSensitivityDeviationValue(self, value: Optional[float]):
        if value is None:
            if "GeneralizedDefectCorrectedSensitivityDeviationValue" in self._dataset:
                del self._dataset.GeneralizedDefectCorrectedSensitivityDeviationValue
        else:
            self._dataset.GeneralizedDefectCorrectedSensitivityDeviationValue = value

    @property
    def GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue(self) -> Optional[float]:
        if "GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue" in self._dataset:
            return self._dataset.GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue
        return None

    @GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue.setter
    def GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue(self, value: Optional[float]):
        if value is None:
            if "GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue" in self._dataset:
                del self._dataset.GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue
        else:
            self._dataset.GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue = value
