from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class FramePixelDataPropertiesSequenceItem:
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
    def ImagerPixelSpacing(self) -> Optional[List[Decimal]]:
        if "ImagerPixelSpacing" in self._dataset:
            return self._dataset.ImagerPixelSpacing
        return None

    @ImagerPixelSpacing.setter
    def ImagerPixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImagerPixelSpacing" in self._dataset:
                del self._dataset.ImagerPixelSpacing
        else:
            self._dataset.ImagerPixelSpacing = value

    @property
    def PixelDataAreaOriginRelativeToFOV(self) -> Optional[List[float]]:
        if "PixelDataAreaOriginRelativeToFOV" in self._dataset:
            return self._dataset.PixelDataAreaOriginRelativeToFOV
        return None

    @PixelDataAreaOriginRelativeToFOV.setter
    def PixelDataAreaOriginRelativeToFOV(self, value: Optional[List[float]]):
        if value is None:
            if "PixelDataAreaOriginRelativeToFOV" in self._dataset:
                del self._dataset.PixelDataAreaOriginRelativeToFOV
        else:
            self._dataset.PixelDataAreaOriginRelativeToFOV = value

    @property
    def PixelDataAreaRotationAngleRelativeToFOV(self) -> Optional[float]:
        if "PixelDataAreaRotationAngleRelativeToFOV" in self._dataset:
            return self._dataset.PixelDataAreaRotationAngleRelativeToFOV
        return None

    @PixelDataAreaRotationAngleRelativeToFOV.setter
    def PixelDataAreaRotationAngleRelativeToFOV(self, value: Optional[float]):
        if value is None:
            if "PixelDataAreaRotationAngleRelativeToFOV" in self._dataset:
                del self._dataset.PixelDataAreaRotationAngleRelativeToFOV
        else:
            self._dataset.PixelDataAreaRotationAngleRelativeToFOV = value

    @property
    def PixelIntensityRelationship(self) -> Optional[str]:
        if "PixelIntensityRelationship" in self._dataset:
            return self._dataset.PixelIntensityRelationship
        return None

    @PixelIntensityRelationship.setter
    def PixelIntensityRelationship(self, value: Optional[str]):
        if value is None:
            if "PixelIntensityRelationship" in self._dataset:
                del self._dataset.PixelIntensityRelationship
        else:
            self._dataset.PixelIntensityRelationship = value

    @property
    def PixelIntensityRelationshipSign(self) -> Optional[int]:
        if "PixelIntensityRelationshipSign" in self._dataset:
            return self._dataset.PixelIntensityRelationshipSign
        return None

    @PixelIntensityRelationshipSign.setter
    def PixelIntensityRelationshipSign(self, value: Optional[int]):
        if value is None:
            if "PixelIntensityRelationshipSign" in self._dataset:
                del self._dataset.PixelIntensityRelationshipSign
        else:
            self._dataset.PixelIntensityRelationshipSign = value

    @property
    def GeometricalProperties(self) -> Optional[str]:
        if "GeometricalProperties" in self._dataset:
            return self._dataset.GeometricalProperties
        return None

    @GeometricalProperties.setter
    def GeometricalProperties(self, value: Optional[str]):
        if value is None:
            if "GeometricalProperties" in self._dataset:
                del self._dataset.GeometricalProperties
        else:
            self._dataset.GeometricalProperties = value

    @property
    def GeometricMaximumDistortion(self) -> Optional[float]:
        if "GeometricMaximumDistortion" in self._dataset:
            return self._dataset.GeometricMaximumDistortion
        return None

    @GeometricMaximumDistortion.setter
    def GeometricMaximumDistortion(self, value: Optional[float]):
        if value is None:
            if "GeometricMaximumDistortion" in self._dataset:
                del self._dataset.GeometricMaximumDistortion
        else:
            self._dataset.GeometricMaximumDistortion = value

    @property
    def ImageProcessingApplied(self) -> Optional[List[str]]:
        if "ImageProcessingApplied" in self._dataset:
            return self._dataset.ImageProcessingApplied
        return None

    @ImageProcessingApplied.setter
    def ImageProcessingApplied(self, value: Optional[List[str]]):
        if value is None:
            if "ImageProcessingApplied" in self._dataset:
                del self._dataset.ImageProcessingApplied
        else:
            self._dataset.ImageProcessingApplied = value
