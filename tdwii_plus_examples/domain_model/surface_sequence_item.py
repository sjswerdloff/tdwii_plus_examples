from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .surface_mesh_primitives_sequence_item import SurfaceMeshPrimitivesSequenceItem
from .surface_points_normals_sequence_item import SurfacePointsNormalsSequenceItem
from .surface_points_sequence_item import SurfacePointsSequenceItem
from .surface_processing_algorithm_identification_sequence_item import (
    SurfaceProcessingAlgorithmIdentificationSequenceItem,
)


class SurfaceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SegmentedPropertyCategoryCodeSequence: List[CodeSequenceItem] = []
        self._SegmentedPropertyTypeCodeSequence: List[CodeSequenceItem] = []
        self._SurfacePointsSequence: List[SurfacePointsSequenceItem] = []
        self._SurfacePointsNormalsSequence: List[SurfacePointsNormalsSequenceItem] = []
        self._SurfaceMeshPrimitivesSequence: List[SurfaceMeshPrimitivesSequenceItem] = []
        self._SurfaceProcessingAlgorithmIdentificationSequence: List[SurfaceProcessingAlgorithmIdentificationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SegmentedPropertyCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentedPropertyCategoryCodeSequence" in self._dataset:
            if len(self._SegmentedPropertyCategoryCodeSequence) == len(self._dataset.SegmentedPropertyCategoryCodeSequence):
                return self._SegmentedPropertyCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentedPropertyCategoryCodeSequence]
        return None

    @SegmentedPropertyCategoryCodeSequence.setter
    def SegmentedPropertyCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentedPropertyCategoryCodeSequence = []
            if "SegmentedPropertyCategoryCodeSequence" in self._dataset:
                del self._dataset.SegmentedPropertyCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SegmentedPropertyCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyCategoryCodeSequence = value
            if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyCategoryCodeSequence.clear()
            self._dataset.SegmentedPropertyCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyCategoryCodeSequence.append(item)
        if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyCategoryCodeSequence.append(item.to_dataset())

    @property
    def RecommendedDisplayGrayscaleValue(self) -> Optional[int]:
        if "RecommendedDisplayGrayscaleValue" in self._dataset:
            return self._dataset.RecommendedDisplayGrayscaleValue
        return None

    @RecommendedDisplayGrayscaleValue.setter
    def RecommendedDisplayGrayscaleValue(self, value: Optional[int]):
        if value is None:
            if "RecommendedDisplayGrayscaleValue" in self._dataset:
                del self._dataset.RecommendedDisplayGrayscaleValue
        else:
            self._dataset.RecommendedDisplayGrayscaleValue = value

    @property
    def RecommendedDisplayCIELabValue(self) -> Optional[List[int]]:
        if "RecommendedDisplayCIELabValue" in self._dataset:
            return self._dataset.RecommendedDisplayCIELabValue
        return None

    @RecommendedDisplayCIELabValue.setter
    def RecommendedDisplayCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "RecommendedDisplayCIELabValue" in self._dataset:
                del self._dataset.RecommendedDisplayCIELabValue
        else:
            self._dataset.RecommendedDisplayCIELabValue = value

    @property
    def SegmentedPropertyTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentedPropertyTypeCodeSequence" in self._dataset:
            if len(self._SegmentedPropertyTypeCodeSequence) == len(self._dataset.SegmentedPropertyTypeCodeSequence):
                return self._SegmentedPropertyTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentedPropertyTypeCodeSequence]
        return None

    @SegmentedPropertyTypeCodeSequence.setter
    def SegmentedPropertyTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentedPropertyTypeCodeSequence = []
            if "SegmentedPropertyTypeCodeSequence" in self._dataset:
                del self._dataset.SegmentedPropertyTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SegmentedPropertyTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyTypeCodeSequence = value
            if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyTypeCodeSequence.clear()
            self._dataset.SegmentedPropertyTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyTypeCodeSequence.append(item)
        if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyTypeCodeSequence.append(item.to_dataset())

    @property
    def SurfaceNumber(self) -> Optional[int]:
        if "SurfaceNumber" in self._dataset:
            return self._dataset.SurfaceNumber
        return None

    @SurfaceNumber.setter
    def SurfaceNumber(self, value: Optional[int]):
        if value is None:
            if "SurfaceNumber" in self._dataset:
                del self._dataset.SurfaceNumber
        else:
            self._dataset.SurfaceNumber = value

    @property
    def SurfaceComments(self) -> Optional[str]:
        if "SurfaceComments" in self._dataset:
            return self._dataset.SurfaceComments
        return None

    @SurfaceComments.setter
    def SurfaceComments(self, value: Optional[str]):
        if value is None:
            if "SurfaceComments" in self._dataset:
                del self._dataset.SurfaceComments
        else:
            self._dataset.SurfaceComments = value

    @property
    def SurfaceProcessing(self) -> Optional[str]:
        if "SurfaceProcessing" in self._dataset:
            return self._dataset.SurfaceProcessing
        return None

    @SurfaceProcessing.setter
    def SurfaceProcessing(self, value: Optional[str]):
        if value is None:
            if "SurfaceProcessing" in self._dataset:
                del self._dataset.SurfaceProcessing
        else:
            self._dataset.SurfaceProcessing = value

    @property
    def SurfaceProcessingRatio(self) -> Optional[float]:
        if "SurfaceProcessingRatio" in self._dataset:
            return self._dataset.SurfaceProcessingRatio
        return None

    @SurfaceProcessingRatio.setter
    def SurfaceProcessingRatio(self, value: Optional[float]):
        if value is None:
            if "SurfaceProcessingRatio" in self._dataset:
                del self._dataset.SurfaceProcessingRatio
        else:
            self._dataset.SurfaceProcessingRatio = value

    @property
    def SurfaceProcessingDescription(self) -> Optional[str]:
        if "SurfaceProcessingDescription" in self._dataset:
            return self._dataset.SurfaceProcessingDescription
        return None

    @SurfaceProcessingDescription.setter
    def SurfaceProcessingDescription(self, value: Optional[str]):
        if value is None:
            if "SurfaceProcessingDescription" in self._dataset:
                del self._dataset.SurfaceProcessingDescription
        else:
            self._dataset.SurfaceProcessingDescription = value

    @property
    def RecommendedPresentationOpacity(self) -> Optional[float]:
        if "RecommendedPresentationOpacity" in self._dataset:
            return self._dataset.RecommendedPresentationOpacity
        return None

    @RecommendedPresentationOpacity.setter
    def RecommendedPresentationOpacity(self, value: Optional[float]):
        if value is None:
            if "RecommendedPresentationOpacity" in self._dataset:
                del self._dataset.RecommendedPresentationOpacity
        else:
            self._dataset.RecommendedPresentationOpacity = value

    @property
    def RecommendedPresentationType(self) -> Optional[str]:
        if "RecommendedPresentationType" in self._dataset:
            return self._dataset.RecommendedPresentationType
        return None

    @RecommendedPresentationType.setter
    def RecommendedPresentationType(self, value: Optional[str]):
        if value is None:
            if "RecommendedPresentationType" in self._dataset:
                del self._dataset.RecommendedPresentationType
        else:
            self._dataset.RecommendedPresentationType = value

    @property
    def FiniteVolume(self) -> Optional[str]:
        if "FiniteVolume" in self._dataset:
            return self._dataset.FiniteVolume
        return None

    @FiniteVolume.setter
    def FiniteVolume(self, value: Optional[str]):
        if value is None:
            if "FiniteVolume" in self._dataset:
                del self._dataset.FiniteVolume
        else:
            self._dataset.FiniteVolume = value

    @property
    def Manifold(self) -> Optional[str]:
        if "Manifold" in self._dataset:
            return self._dataset.Manifold
        return None

    @Manifold.setter
    def Manifold(self, value: Optional[str]):
        if value is None:
            if "Manifold" in self._dataset:
                del self._dataset.Manifold
        else:
            self._dataset.Manifold = value

    @property
    def SurfacePointsSequence(self) -> Optional[List[SurfacePointsSequenceItem]]:
        if "SurfacePointsSequence" in self._dataset:
            if len(self._SurfacePointsSequence) == len(self._dataset.SurfacePointsSequence):
                return self._SurfacePointsSequence
            else:
                return [SurfacePointsSequenceItem(x) for x in self._dataset.SurfacePointsSequence]
        return None

    @SurfacePointsSequence.setter
    def SurfacePointsSequence(self, value: Optional[List[SurfacePointsSequenceItem]]):
        if value is None:
            self._SurfacePointsSequence = []
            if "SurfacePointsSequence" in self._dataset:
                del self._dataset.SurfacePointsSequence
        elif not isinstance(value, list) or not all(isinstance(item, SurfacePointsSequenceItem) for item in value):
            raise ValueError("SurfacePointsSequence must be a list of SurfacePointsSequenceItem objects")
        else:
            self._SurfacePointsSequence = value
            if "SurfacePointsSequence" not in self._dataset:
                self._dataset.SurfacePointsSequence = pydicom.Sequence()
            self._dataset.SurfacePointsSequence.clear()
            self._dataset.SurfacePointsSequence.extend([item.to_dataset() for item in value])

    def add_SurfacePoints(self, item: SurfacePointsSequenceItem):
        if not isinstance(item, SurfacePointsSequenceItem):
            raise ValueError("Item must be an instance of SurfacePointsSequenceItem")
        self._SurfacePointsSequence.append(item)
        if "SurfacePointsSequence" not in self._dataset:
            self._dataset.SurfacePointsSequence = pydicom.Sequence()
        self._dataset.SurfacePointsSequence.append(item.to_dataset())

    @property
    def SurfacePointsNormalsSequence(self) -> Optional[List[SurfacePointsNormalsSequenceItem]]:
        if "SurfacePointsNormalsSequence" in self._dataset:
            if len(self._SurfacePointsNormalsSequence) == len(self._dataset.SurfacePointsNormalsSequence):
                return self._SurfacePointsNormalsSequence
            else:
                return [SurfacePointsNormalsSequenceItem(x) for x in self._dataset.SurfacePointsNormalsSequence]
        return None

    @SurfacePointsNormalsSequence.setter
    def SurfacePointsNormalsSequence(self, value: Optional[List[SurfacePointsNormalsSequenceItem]]):
        if value is None:
            self._SurfacePointsNormalsSequence = []
            if "SurfacePointsNormalsSequence" in self._dataset:
                del self._dataset.SurfacePointsNormalsSequence
        elif not isinstance(value, list) or not all(isinstance(item, SurfacePointsNormalsSequenceItem) for item in value):
            raise ValueError("SurfacePointsNormalsSequence must be a list of SurfacePointsNormalsSequenceItem objects")
        else:
            self._SurfacePointsNormalsSequence = value
            if "SurfacePointsNormalsSequence" not in self._dataset:
                self._dataset.SurfacePointsNormalsSequence = pydicom.Sequence()
            self._dataset.SurfacePointsNormalsSequence.clear()
            self._dataset.SurfacePointsNormalsSequence.extend([item.to_dataset() for item in value])

    def add_SurfacePointsNormals(self, item: SurfacePointsNormalsSequenceItem):
        if not isinstance(item, SurfacePointsNormalsSequenceItem):
            raise ValueError("Item must be an instance of SurfacePointsNormalsSequenceItem")
        self._SurfacePointsNormalsSequence.append(item)
        if "SurfacePointsNormalsSequence" not in self._dataset:
            self._dataset.SurfacePointsNormalsSequence = pydicom.Sequence()
        self._dataset.SurfacePointsNormalsSequence.append(item.to_dataset())

    @property
    def SurfaceMeshPrimitivesSequence(self) -> Optional[List[SurfaceMeshPrimitivesSequenceItem]]:
        if "SurfaceMeshPrimitivesSequence" in self._dataset:
            if len(self._SurfaceMeshPrimitivesSequence) == len(self._dataset.SurfaceMeshPrimitivesSequence):
                return self._SurfaceMeshPrimitivesSequence
            else:
                return [SurfaceMeshPrimitivesSequenceItem(x) for x in self._dataset.SurfaceMeshPrimitivesSequence]
        return None

    @SurfaceMeshPrimitivesSequence.setter
    def SurfaceMeshPrimitivesSequence(self, value: Optional[List[SurfaceMeshPrimitivesSequenceItem]]):
        if value is None:
            self._SurfaceMeshPrimitivesSequence = []
            if "SurfaceMeshPrimitivesSequence" in self._dataset:
                del self._dataset.SurfaceMeshPrimitivesSequence
        elif not isinstance(value, list) or not all(isinstance(item, SurfaceMeshPrimitivesSequenceItem) for item in value):
            raise ValueError("SurfaceMeshPrimitivesSequence must be a list of SurfaceMeshPrimitivesSequenceItem objects")
        else:
            self._SurfaceMeshPrimitivesSequence = value
            if "SurfaceMeshPrimitivesSequence" not in self._dataset:
                self._dataset.SurfaceMeshPrimitivesSequence = pydicom.Sequence()
            self._dataset.SurfaceMeshPrimitivesSequence.clear()
            self._dataset.SurfaceMeshPrimitivesSequence.extend([item.to_dataset() for item in value])

    def add_SurfaceMeshPrimitives(self, item: SurfaceMeshPrimitivesSequenceItem):
        if not isinstance(item, SurfaceMeshPrimitivesSequenceItem):
            raise ValueError("Item must be an instance of SurfaceMeshPrimitivesSequenceItem")
        self._SurfaceMeshPrimitivesSequence.append(item)
        if "SurfaceMeshPrimitivesSequence" not in self._dataset:
            self._dataset.SurfaceMeshPrimitivesSequence = pydicom.Sequence()
        self._dataset.SurfaceMeshPrimitivesSequence.append(item.to_dataset())

    @property
    def SurfaceProcessingAlgorithmIdentificationSequence(
        self,
    ) -> Optional[List[SurfaceProcessingAlgorithmIdentificationSequenceItem]]:
        if "SurfaceProcessingAlgorithmIdentificationSequence" in self._dataset:
            if len(self._SurfaceProcessingAlgorithmIdentificationSequence) == len(
                self._dataset.SurfaceProcessingAlgorithmIdentificationSequence
            ):
                return self._SurfaceProcessingAlgorithmIdentificationSequence
            else:
                return [
                    SurfaceProcessingAlgorithmIdentificationSequenceItem(x)
                    for x in self._dataset.SurfaceProcessingAlgorithmIdentificationSequence
                ]
        return None

    @SurfaceProcessingAlgorithmIdentificationSequence.setter
    def SurfaceProcessingAlgorithmIdentificationSequence(
        self, value: Optional[List[SurfaceProcessingAlgorithmIdentificationSequenceItem]]
    ):
        if value is None:
            self._SurfaceProcessingAlgorithmIdentificationSequence = []
            if "SurfaceProcessingAlgorithmIdentificationSequence" in self._dataset:
                del self._dataset.SurfaceProcessingAlgorithmIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SurfaceProcessingAlgorithmIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "SurfaceProcessingAlgorithmIdentificationSequence must be a list of"
                " SurfaceProcessingAlgorithmIdentificationSequenceItem objects"
            )
        else:
            self._SurfaceProcessingAlgorithmIdentificationSequence = value
            if "SurfaceProcessingAlgorithmIdentificationSequence" not in self._dataset:
                self._dataset.SurfaceProcessingAlgorithmIdentificationSequence = pydicom.Sequence()
            self._dataset.SurfaceProcessingAlgorithmIdentificationSequence.clear()
            self._dataset.SurfaceProcessingAlgorithmIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_SurfaceProcessingAlgorithmIdentification(self, item: SurfaceProcessingAlgorithmIdentificationSequenceItem):
        if not isinstance(item, SurfaceProcessingAlgorithmIdentificationSequenceItem):
            raise ValueError("Item must be an instance of SurfaceProcessingAlgorithmIdentificationSequenceItem")
        self._SurfaceProcessingAlgorithmIdentificationSequence.append(item)
        if "SurfaceProcessingAlgorithmIdentificationSequence" not in self._dataset:
            self._dataset.SurfaceProcessingAlgorithmIdentificationSequence = pydicom.Sequence()
        self._dataset.SurfaceProcessingAlgorithmIdentificationSequence.append(item.to_dataset())

    @property
    def RecommendedPointRadius(self) -> Optional[float]:
        if "RecommendedPointRadius" in self._dataset:
            return self._dataset.RecommendedPointRadius
        return None

    @RecommendedPointRadius.setter
    def RecommendedPointRadius(self, value: Optional[float]):
        if value is None:
            if "RecommendedPointRadius" in self._dataset:
                del self._dataset.RecommendedPointRadius
        else:
            self._dataset.RecommendedPointRadius = value

    @property
    def RecommendedLineThickness(self) -> Optional[float]:
        if "RecommendedLineThickness" in self._dataset:
            return self._dataset.RecommendedLineThickness
        return None

    @RecommendedLineThickness.setter
    def RecommendedLineThickness(self, value: Optional[float]):
        if value is None:
            if "RecommendedLineThickness" in self._dataset:
                del self._dataset.RecommendedLineThickness
        else:
            self._dataset.RecommendedLineThickness = value
