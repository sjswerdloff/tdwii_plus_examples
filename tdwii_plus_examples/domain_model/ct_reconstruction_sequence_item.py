from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class CTReconstructionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReconstructionDiameter(self) -> Optional[Decimal]:
        if "ReconstructionDiameter" in self._dataset:
            return self._dataset.ReconstructionDiameter
        return None

    @ReconstructionDiameter.setter
    def ReconstructionDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "ReconstructionDiameter" in self._dataset:
                del self._dataset.ReconstructionDiameter
        else:
            self._dataset.ReconstructionDiameter = value

    @property
    def ConvolutionKernel(self) -> Optional[List[str]]:
        if "ConvolutionKernel" in self._dataset:
            return self._dataset.ConvolutionKernel
        return None

    @ConvolutionKernel.setter
    def ConvolutionKernel(self, value: Optional[List[str]]):
        if value is None:
            if "ConvolutionKernel" in self._dataset:
                del self._dataset.ConvolutionKernel
        else:
            self._dataset.ConvolutionKernel = value

    @property
    def ReconstructionAlgorithm(self) -> Optional[str]:
        if "ReconstructionAlgorithm" in self._dataset:
            return self._dataset.ReconstructionAlgorithm
        return None

    @ReconstructionAlgorithm.setter
    def ReconstructionAlgorithm(self, value: Optional[str]):
        if value is None:
            if "ReconstructionAlgorithm" in self._dataset:
                del self._dataset.ReconstructionAlgorithm
        else:
            self._dataset.ReconstructionAlgorithm = value

    @property
    def ConvolutionKernelGroup(self) -> Optional[str]:
        if "ConvolutionKernelGroup" in self._dataset:
            return self._dataset.ConvolutionKernelGroup
        return None

    @ConvolutionKernelGroup.setter
    def ConvolutionKernelGroup(self, value: Optional[str]):
        if value is None:
            if "ConvolutionKernelGroup" in self._dataset:
                del self._dataset.ConvolutionKernelGroup
        else:
            self._dataset.ConvolutionKernelGroup = value

    @property
    def ReconstructionFieldOfView(self) -> Optional[List[float]]:
        if "ReconstructionFieldOfView" in self._dataset:
            return self._dataset.ReconstructionFieldOfView
        return None

    @ReconstructionFieldOfView.setter
    def ReconstructionFieldOfView(self, value: Optional[List[float]]):
        if value is None:
            if "ReconstructionFieldOfView" in self._dataset:
                del self._dataset.ReconstructionFieldOfView
        else:
            self._dataset.ReconstructionFieldOfView = value

    @property
    def ReconstructionAngle(self) -> Optional[float]:
        if "ReconstructionAngle" in self._dataset:
            return self._dataset.ReconstructionAngle
        return None

    @ReconstructionAngle.setter
    def ReconstructionAngle(self, value: Optional[float]):
        if value is None:
            if "ReconstructionAngle" in self._dataset:
                del self._dataset.ReconstructionAngle
        else:
            self._dataset.ReconstructionAngle = value

    @property
    def ImageFilter(self) -> Optional[str]:
        if "ImageFilter" in self._dataset:
            return self._dataset.ImageFilter
        return None

    @ImageFilter.setter
    def ImageFilter(self, value: Optional[str]):
        if value is None:
            if "ImageFilter" in self._dataset:
                del self._dataset.ImageFilter
        else:
            self._dataset.ImageFilter = value

    @property
    def ReconstructionPixelSpacing(self) -> Optional[List[float]]:
        if "ReconstructionPixelSpacing" in self._dataset:
            return self._dataset.ReconstructionPixelSpacing
        return None

    @ReconstructionPixelSpacing.setter
    def ReconstructionPixelSpacing(self, value: Optional[List[float]]):
        if value is None:
            if "ReconstructionPixelSpacing" in self._dataset:
                del self._dataset.ReconstructionPixelSpacing
        else:
            self._dataset.ReconstructionPixelSpacing = value
