from typing import Any, List, Optional

import pydicom


class MRImageFrameTypeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameType(self) -> Optional[List[str]]:
        if "FrameType" in self._dataset:
            return self._dataset.FrameType
        return None

    @FrameType.setter
    def FrameType(self, value: Optional[List[str]]):
        if value is None:
            if "FrameType" in self._dataset:
                del self._dataset.FrameType
        else:
            self._dataset.FrameType = value

    @property
    def PixelPresentation(self) -> Optional[str]:
        if "PixelPresentation" in self._dataset:
            return self._dataset.PixelPresentation
        return None

    @PixelPresentation.setter
    def PixelPresentation(self, value: Optional[str]):
        if value is None:
            if "PixelPresentation" in self._dataset:
                del self._dataset.PixelPresentation
        else:
            self._dataset.PixelPresentation = value

    @property
    def VolumetricProperties(self) -> Optional[str]:
        if "VolumetricProperties" in self._dataset:
            return self._dataset.VolumetricProperties
        return None

    @VolumetricProperties.setter
    def VolumetricProperties(self, value: Optional[str]):
        if value is None:
            if "VolumetricProperties" in self._dataset:
                del self._dataset.VolumetricProperties
        else:
            self._dataset.VolumetricProperties = value

    @property
    def VolumeBasedCalculationTechnique(self) -> Optional[str]:
        if "VolumeBasedCalculationTechnique" in self._dataset:
            return self._dataset.VolumeBasedCalculationTechnique
        return None

    @VolumeBasedCalculationTechnique.setter
    def VolumeBasedCalculationTechnique(self, value: Optional[str]):
        if value is None:
            if "VolumeBasedCalculationTechnique" in self._dataset:
                del self._dataset.VolumeBasedCalculationTechnique
        else:
            self._dataset.VolumeBasedCalculationTechnique = value

    @property
    def ComplexImageComponent(self) -> Optional[str]:
        if "ComplexImageComponent" in self._dataset:
            return self._dataset.ComplexImageComponent
        return None

    @ComplexImageComponent.setter
    def ComplexImageComponent(self, value: Optional[str]):
        if value is None:
            if "ComplexImageComponent" in self._dataset:
                del self._dataset.ComplexImageComponent
        else:
            self._dataset.ComplexImageComponent = value

    @property
    def AcquisitionContrast(self) -> Optional[str]:
        if "AcquisitionContrast" in self._dataset:
            return self._dataset.AcquisitionContrast
        return None

    @AcquisitionContrast.setter
    def AcquisitionContrast(self, value: Optional[str]):
        if value is None:
            if "AcquisitionContrast" in self._dataset:
                del self._dataset.AcquisitionContrast
        else:
            self._dataset.AcquisitionContrast = value

    @property
    def FunctionalSettlingPhaseFramesPresent(self) -> Optional[str]:
        if "FunctionalSettlingPhaseFramesPresent" in self._dataset:
            return self._dataset.FunctionalSettlingPhaseFramesPresent
        return None

    @FunctionalSettlingPhaseFramesPresent.setter
    def FunctionalSettlingPhaseFramesPresent(self, value: Optional[str]):
        if value is None:
            if "FunctionalSettlingPhaseFramesPresent" in self._dataset:
                del self._dataset.FunctionalSettlingPhaseFramesPresent
        else:
            self._dataset.FunctionalSettlingPhaseFramesPresent = value
