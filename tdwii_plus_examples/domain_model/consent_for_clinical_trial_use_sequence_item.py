from typing import Any, List, Optional

import pydicom


class ConsentForClinicalTrialUseSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ClinicalTrialProtocolID(self) -> Optional[str]:
        if "ClinicalTrialProtocolID" in self._dataset:
            return self._dataset.ClinicalTrialProtocolID
        return None

    @ClinicalTrialProtocolID.setter
    def ClinicalTrialProtocolID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolID" in self._dataset:
                del self._dataset.ClinicalTrialProtocolID
        else:
            self._dataset.ClinicalTrialProtocolID = value

    @property
    def IssuerOfClinicalTrialProtocolID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialProtocolID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialProtocolID
        return None

    @IssuerOfClinicalTrialProtocolID.setter
    def IssuerOfClinicalTrialProtocolID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialProtocolID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialProtocolID
        else:
            self._dataset.IssuerOfClinicalTrialProtocolID = value

    @property
    def DistributionType(self) -> Optional[str]:
        if "DistributionType" in self._dataset:
            return self._dataset.DistributionType
        return None

    @DistributionType.setter
    def DistributionType(self, value: Optional[str]):
        if value is None:
            if "DistributionType" in self._dataset:
                del self._dataset.DistributionType
        else:
            self._dataset.DistributionType = value

    @property
    def ConsentForDistributionFlag(self) -> Optional[str]:
        if "ConsentForDistributionFlag" in self._dataset:
            return self._dataset.ConsentForDistributionFlag
        return None

    @ConsentForDistributionFlag.setter
    def ConsentForDistributionFlag(self, value: Optional[str]):
        if value is None:
            if "ConsentForDistributionFlag" in self._dataset:
                del self._dataset.ConsentForDistributionFlag
        else:
            self._dataset.ConsentForDistributionFlag = value
