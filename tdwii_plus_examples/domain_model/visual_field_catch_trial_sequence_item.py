from typing import Any, List, Optional

import pydicom


class VisualFieldCatchTrialSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FalseNegativesEstimateFlag(self) -> Optional[str]:
        if "FalseNegativesEstimateFlag" in self._dataset:
            return self._dataset.FalseNegativesEstimateFlag
        return None

    @FalseNegativesEstimateFlag.setter
    def FalseNegativesEstimateFlag(self, value: Optional[str]):
        if value is None:
            if "FalseNegativesEstimateFlag" in self._dataset:
                del self._dataset.FalseNegativesEstimateFlag
        else:
            self._dataset.FalseNegativesEstimateFlag = value

    @property
    def FalseNegativesEstimate(self) -> Optional[float]:
        if "FalseNegativesEstimate" in self._dataset:
            return self._dataset.FalseNegativesEstimate
        return None

    @FalseNegativesEstimate.setter
    def FalseNegativesEstimate(self, value: Optional[float]):
        if value is None:
            if "FalseNegativesEstimate" in self._dataset:
                del self._dataset.FalseNegativesEstimate
        else:
            self._dataset.FalseNegativesEstimate = value

    @property
    def NegativeCatchTrialsQuantity(self) -> Optional[int]:
        if "NegativeCatchTrialsQuantity" in self._dataset:
            return self._dataset.NegativeCatchTrialsQuantity
        return None

    @NegativeCatchTrialsQuantity.setter
    def NegativeCatchTrialsQuantity(self, value: Optional[int]):
        if value is None:
            if "NegativeCatchTrialsQuantity" in self._dataset:
                del self._dataset.NegativeCatchTrialsQuantity
        else:
            self._dataset.NegativeCatchTrialsQuantity = value

    @property
    def FalseNegativesQuantity(self) -> Optional[int]:
        if "FalseNegativesQuantity" in self._dataset:
            return self._dataset.FalseNegativesQuantity
        return None

    @FalseNegativesQuantity.setter
    def FalseNegativesQuantity(self, value: Optional[int]):
        if value is None:
            if "FalseNegativesQuantity" in self._dataset:
                del self._dataset.FalseNegativesQuantity
        else:
            self._dataset.FalseNegativesQuantity = value

    @property
    def ExcessiveFalseNegativesDataFlag(self) -> Optional[str]:
        if "ExcessiveFalseNegativesDataFlag" in self._dataset:
            return self._dataset.ExcessiveFalseNegativesDataFlag
        return None

    @ExcessiveFalseNegativesDataFlag.setter
    def ExcessiveFalseNegativesDataFlag(self, value: Optional[str]):
        if value is None:
            if "ExcessiveFalseNegativesDataFlag" in self._dataset:
                del self._dataset.ExcessiveFalseNegativesDataFlag
        else:
            self._dataset.ExcessiveFalseNegativesDataFlag = value

    @property
    def ExcessiveFalseNegatives(self) -> Optional[str]:
        if "ExcessiveFalseNegatives" in self._dataset:
            return self._dataset.ExcessiveFalseNegatives
        return None

    @ExcessiveFalseNegatives.setter
    def ExcessiveFalseNegatives(self, value: Optional[str]):
        if value is None:
            if "ExcessiveFalseNegatives" in self._dataset:
                del self._dataset.ExcessiveFalseNegatives
        else:
            self._dataset.ExcessiveFalseNegatives = value

    @property
    def FalsePositivesEstimateFlag(self) -> Optional[str]:
        if "FalsePositivesEstimateFlag" in self._dataset:
            return self._dataset.FalsePositivesEstimateFlag
        return None

    @FalsePositivesEstimateFlag.setter
    def FalsePositivesEstimateFlag(self, value: Optional[str]):
        if value is None:
            if "FalsePositivesEstimateFlag" in self._dataset:
                del self._dataset.FalsePositivesEstimateFlag
        else:
            self._dataset.FalsePositivesEstimateFlag = value

    @property
    def FalsePositivesEstimate(self) -> Optional[float]:
        if "FalsePositivesEstimate" in self._dataset:
            return self._dataset.FalsePositivesEstimate
        return None

    @FalsePositivesEstimate.setter
    def FalsePositivesEstimate(self, value: Optional[float]):
        if value is None:
            if "FalsePositivesEstimate" in self._dataset:
                del self._dataset.FalsePositivesEstimate
        else:
            self._dataset.FalsePositivesEstimate = value

    @property
    def CatchTrialsDataFlag(self) -> Optional[str]:
        if "CatchTrialsDataFlag" in self._dataset:
            return self._dataset.CatchTrialsDataFlag
        return None

    @CatchTrialsDataFlag.setter
    def CatchTrialsDataFlag(self, value: Optional[str]):
        if value is None:
            if "CatchTrialsDataFlag" in self._dataset:
                del self._dataset.CatchTrialsDataFlag
        else:
            self._dataset.CatchTrialsDataFlag = value

    @property
    def PositiveCatchTrialsQuantity(self) -> Optional[int]:
        if "PositiveCatchTrialsQuantity" in self._dataset:
            return self._dataset.PositiveCatchTrialsQuantity
        return None

    @PositiveCatchTrialsQuantity.setter
    def PositiveCatchTrialsQuantity(self, value: Optional[int]):
        if value is None:
            if "PositiveCatchTrialsQuantity" in self._dataset:
                del self._dataset.PositiveCatchTrialsQuantity
        else:
            self._dataset.PositiveCatchTrialsQuantity = value

    @property
    def FalsePositivesQuantity(self) -> Optional[int]:
        if "FalsePositivesQuantity" in self._dataset:
            return self._dataset.FalsePositivesQuantity
        return None

    @FalsePositivesQuantity.setter
    def FalsePositivesQuantity(self, value: Optional[int]):
        if value is None:
            if "FalsePositivesQuantity" in self._dataset:
                del self._dataset.FalsePositivesQuantity
        else:
            self._dataset.FalsePositivesQuantity = value

    @property
    def ExcessiveFalsePositivesDataFlag(self) -> Optional[str]:
        if "ExcessiveFalsePositivesDataFlag" in self._dataset:
            return self._dataset.ExcessiveFalsePositivesDataFlag
        return None

    @ExcessiveFalsePositivesDataFlag.setter
    def ExcessiveFalsePositivesDataFlag(self, value: Optional[str]):
        if value is None:
            if "ExcessiveFalsePositivesDataFlag" in self._dataset:
                del self._dataset.ExcessiveFalsePositivesDataFlag
        else:
            self._dataset.ExcessiveFalsePositivesDataFlag = value

    @property
    def ExcessiveFalsePositives(self) -> Optional[str]:
        if "ExcessiveFalsePositives" in self._dataset:
            return self._dataset.ExcessiveFalsePositives
        return None

    @ExcessiveFalsePositives.setter
    def ExcessiveFalsePositives(self, value: Optional[str]):
        if value is None:
            if "ExcessiveFalsePositives" in self._dataset:
                del self._dataset.ExcessiveFalsePositives
        else:
            self._dataset.ExcessiveFalsePositives = value
