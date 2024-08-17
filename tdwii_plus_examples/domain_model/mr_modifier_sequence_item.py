from typing import Any, List, Optional

import pydicom


class MRModifierSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def InversionRecovery(self) -> Optional[str]:
        if "InversionRecovery" in self._dataset:
            return self._dataset.InversionRecovery
        return None

    @InversionRecovery.setter
    def InversionRecovery(self, value: Optional[str]):
        if value is None:
            if "InversionRecovery" in self._dataset:
                del self._dataset.InversionRecovery
        else:
            self._dataset.InversionRecovery = value

    @property
    def FlowCompensation(self) -> Optional[str]:
        if "FlowCompensation" in self._dataset:
            return self._dataset.FlowCompensation
        return None

    @FlowCompensation.setter
    def FlowCompensation(self, value: Optional[str]):
        if value is None:
            if "FlowCompensation" in self._dataset:
                del self._dataset.FlowCompensation
        else:
            self._dataset.FlowCompensation = value

    @property
    def Spoiling(self) -> Optional[str]:
        if "Spoiling" in self._dataset:
            return self._dataset.Spoiling
        return None

    @Spoiling.setter
    def Spoiling(self, value: Optional[str]):
        if value is None:
            if "Spoiling" in self._dataset:
                del self._dataset.Spoiling
        else:
            self._dataset.Spoiling = value

    @property
    def T2Preparation(self) -> Optional[str]:
        if "T2Preparation" in self._dataset:
            return self._dataset.T2Preparation
        return None

    @T2Preparation.setter
    def T2Preparation(self, value: Optional[str]):
        if value is None:
            if "T2Preparation" in self._dataset:
                del self._dataset.T2Preparation
        else:
            self._dataset.T2Preparation = value

    @property
    def SpectrallySelectedExcitation(self) -> Optional[str]:
        if "SpectrallySelectedExcitation" in self._dataset:
            return self._dataset.SpectrallySelectedExcitation
        return None

    @SpectrallySelectedExcitation.setter
    def SpectrallySelectedExcitation(self, value: Optional[str]):
        if value is None:
            if "SpectrallySelectedExcitation" in self._dataset:
                del self._dataset.SpectrallySelectedExcitation
        else:
            self._dataset.SpectrallySelectedExcitation = value

    @property
    def SpatialPresaturation(self) -> Optional[str]:
        if "SpatialPresaturation" in self._dataset:
            return self._dataset.SpatialPresaturation
        return None

    @SpatialPresaturation.setter
    def SpatialPresaturation(self, value: Optional[str]):
        if value is None:
            if "SpatialPresaturation" in self._dataset:
                del self._dataset.SpatialPresaturation
        else:
            self._dataset.SpatialPresaturation = value

    @property
    def PartialFourierDirection(self) -> Optional[str]:
        if "PartialFourierDirection" in self._dataset:
            return self._dataset.PartialFourierDirection
        return None

    @PartialFourierDirection.setter
    def PartialFourierDirection(self, value: Optional[str]):
        if value is None:
            if "PartialFourierDirection" in self._dataset:
                del self._dataset.PartialFourierDirection
        else:
            self._dataset.PartialFourierDirection = value

    @property
    def ParallelReductionFactorInPlane(self) -> Optional[float]:
        if "ParallelReductionFactorInPlane" in self._dataset:
            return self._dataset.ParallelReductionFactorInPlane
        return None

    @ParallelReductionFactorInPlane.setter
    def ParallelReductionFactorInPlane(self, value: Optional[float]):
        if value is None:
            if "ParallelReductionFactorInPlane" in self._dataset:
                del self._dataset.ParallelReductionFactorInPlane
        else:
            self._dataset.ParallelReductionFactorInPlane = value

    @property
    def ParallelAcquisition(self) -> Optional[str]:
        if "ParallelAcquisition" in self._dataset:
            return self._dataset.ParallelAcquisition
        return None

    @ParallelAcquisition.setter
    def ParallelAcquisition(self, value: Optional[str]):
        if value is None:
            if "ParallelAcquisition" in self._dataset:
                del self._dataset.ParallelAcquisition
        else:
            self._dataset.ParallelAcquisition = value

    @property
    def ParallelAcquisitionTechnique(self) -> Optional[str]:
        if "ParallelAcquisitionTechnique" in self._dataset:
            return self._dataset.ParallelAcquisitionTechnique
        return None

    @ParallelAcquisitionTechnique.setter
    def ParallelAcquisitionTechnique(self, value: Optional[str]):
        if value is None:
            if "ParallelAcquisitionTechnique" in self._dataset:
                del self._dataset.ParallelAcquisitionTechnique
        else:
            self._dataset.ParallelAcquisitionTechnique = value

    @property
    def InversionTimes(self) -> Optional[List[float]]:
        if "InversionTimes" in self._dataset:
            return self._dataset.InversionTimes
        return None

    @InversionTimes.setter
    def InversionTimes(self, value: Optional[List[float]]):
        if value is None:
            if "InversionTimes" in self._dataset:
                del self._dataset.InversionTimes
        else:
            self._dataset.InversionTimes = value

    @property
    def PartialFourier(self) -> Optional[str]:
        if "PartialFourier" in self._dataset:
            return self._dataset.PartialFourier
        return None

    @PartialFourier.setter
    def PartialFourier(self, value: Optional[str]):
        if value is None:
            if "PartialFourier" in self._dataset:
                del self._dataset.PartialFourier
        else:
            self._dataset.PartialFourier = value

    @property
    def ParallelReductionFactorOutOfPlane(self) -> Optional[float]:
        if "ParallelReductionFactorOutOfPlane" in self._dataset:
            return self._dataset.ParallelReductionFactorOutOfPlane
        return None

    @ParallelReductionFactorOutOfPlane.setter
    def ParallelReductionFactorOutOfPlane(self, value: Optional[float]):
        if value is None:
            if "ParallelReductionFactorOutOfPlane" in self._dataset:
                del self._dataset.ParallelReductionFactorOutOfPlane
        else:
            self._dataset.ParallelReductionFactorOutOfPlane = value

    @property
    def ParallelReductionFactorSecondInPlane(self) -> Optional[float]:
        if "ParallelReductionFactorSecondInPlane" in self._dataset:
            return self._dataset.ParallelReductionFactorSecondInPlane
        return None

    @ParallelReductionFactorSecondInPlane.setter
    def ParallelReductionFactorSecondInPlane(self, value: Optional[float]):
        if value is None:
            if "ParallelReductionFactorSecondInPlane" in self._dataset:
                del self._dataset.ParallelReductionFactorSecondInPlane
        else:
            self._dataset.ParallelReductionFactorSecondInPlane = value

    @property
    def FlowCompensationDirection(self) -> Optional[str]:
        if "FlowCompensationDirection" in self._dataset:
            return self._dataset.FlowCompensationDirection
        return None

    @FlowCompensationDirection.setter
    def FlowCompensationDirection(self, value: Optional[str]):
        if value is None:
            if "FlowCompensationDirection" in self._dataset:
                del self._dataset.FlowCompensationDirection
        else:
            self._dataset.FlowCompensationDirection = value
