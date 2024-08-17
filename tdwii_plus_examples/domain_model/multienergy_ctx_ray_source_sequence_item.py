from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class MultienergyCTXRaySourceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def GeneratorPower(self) -> Optional[int]:
        if "GeneratorPower" in self._dataset:
            return self._dataset.GeneratorPower
        return None

    @GeneratorPower.setter
    def GeneratorPower(self, value: Optional[int]):
        if value is None:
            if "GeneratorPower" in self._dataset:
                del self._dataset.GeneratorPower
        else:
            self._dataset.GeneratorPower = value

    @property
    def XRaySourceIndex(self) -> Optional[int]:
        if "XRaySourceIndex" in self._dataset:
            return self._dataset.XRaySourceIndex
        return None

    @XRaySourceIndex.setter
    def XRaySourceIndex(self, value: Optional[int]):
        if value is None:
            if "XRaySourceIndex" in self._dataset:
                del self._dataset.XRaySourceIndex
        else:
            self._dataset.XRaySourceIndex = value

    @property
    def XRaySourceID(self) -> Optional[str]:
        if "XRaySourceID" in self._dataset:
            return self._dataset.XRaySourceID
        return None

    @XRaySourceID.setter
    def XRaySourceID(self, value: Optional[str]):
        if value is None:
            if "XRaySourceID" in self._dataset:
                del self._dataset.XRaySourceID
        else:
            self._dataset.XRaySourceID = value

    @property
    def MultienergySourceTechnique(self) -> Optional[str]:
        if "MultienergySourceTechnique" in self._dataset:
            return self._dataset.MultienergySourceTechnique
        return None

    @MultienergySourceTechnique.setter
    def MultienergySourceTechnique(self, value: Optional[str]):
        if value is None:
            if "MultienergySourceTechnique" in self._dataset:
                del self._dataset.MultienergySourceTechnique
        else:
            self._dataset.MultienergySourceTechnique = value

    @property
    def SourceStartDateTime(self) -> Optional[str]:
        if "SourceStartDateTime" in self._dataset:
            return self._dataset.SourceStartDateTime
        return None

    @SourceStartDateTime.setter
    def SourceStartDateTime(self, value: Optional[str]):
        if value is None:
            if "SourceStartDateTime" in self._dataset:
                del self._dataset.SourceStartDateTime
        else:
            self._dataset.SourceStartDateTime = value

    @property
    def SourceEndDateTime(self) -> Optional[str]:
        if "SourceEndDateTime" in self._dataset:
            return self._dataset.SourceEndDateTime
        return None

    @SourceEndDateTime.setter
    def SourceEndDateTime(self, value: Optional[str]):
        if value is None:
            if "SourceEndDateTime" in self._dataset:
                del self._dataset.SourceEndDateTime
        else:
            self._dataset.SourceEndDateTime = value

    @property
    def SwitchingPhaseNumber(self) -> Optional[int]:
        if "SwitchingPhaseNumber" in self._dataset:
            return self._dataset.SwitchingPhaseNumber
        return None

    @SwitchingPhaseNumber.setter
    def SwitchingPhaseNumber(self, value: Optional[int]):
        if value is None:
            if "SwitchingPhaseNumber" in self._dataset:
                del self._dataset.SwitchingPhaseNumber
        else:
            self._dataset.SwitchingPhaseNumber = value

    @property
    def SwitchingPhaseNominalDuration(self) -> Optional[Decimal]:
        if "SwitchingPhaseNominalDuration" in self._dataset:
            return self._dataset.SwitchingPhaseNominalDuration
        return None

    @SwitchingPhaseNominalDuration.setter
    def SwitchingPhaseNominalDuration(self, value: Optional[Decimal]):
        if value is None:
            if "SwitchingPhaseNominalDuration" in self._dataset:
                del self._dataset.SwitchingPhaseNominalDuration
        else:
            self._dataset.SwitchingPhaseNominalDuration = value

    @property
    def SwitchingPhaseTransitionDuration(self) -> Optional[Decimal]:
        if "SwitchingPhaseTransitionDuration" in self._dataset:
            return self._dataset.SwitchingPhaseTransitionDuration
        return None

    @SwitchingPhaseTransitionDuration.setter
    def SwitchingPhaseTransitionDuration(self, value: Optional[Decimal]):
        if value is None:
            if "SwitchingPhaseTransitionDuration" in self._dataset:
                del self._dataset.SwitchingPhaseTransitionDuration
        else:
            self._dataset.SwitchingPhaseTransitionDuration = value
