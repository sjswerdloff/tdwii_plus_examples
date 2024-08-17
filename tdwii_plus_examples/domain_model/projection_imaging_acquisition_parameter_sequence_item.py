from typing import Any, List, Optional  # noqa

import pydicom

from .imaging_aperture_sequence_item import ImagingApertureSequenceItem
from .imaging_device_location_matrix_sequence_item import (
    ImagingDeviceLocationMatrixSequenceItem,
)
from .imaging_device_location_parameter_sequence_item import (
    ImagingDeviceLocationParameterSequenceItem,
)


class ProjectionImagingAcquisitionParameterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ImagingDeviceLocationMatrixSequence: List[ImagingDeviceLocationMatrixSequenceItem] = []
        self._ImagingDeviceLocationParameterSequence: List[ImagingDeviceLocationParameterSequenceItem] = []
        self._ImagingApertureSequence: List[ImagingApertureSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImagingSourceLocationSpecificationType(self) -> Optional[str]:
        if "ImagingSourceLocationSpecificationType" in self._dataset:
            return self._dataset.ImagingSourceLocationSpecificationType
        return None

    @ImagingSourceLocationSpecificationType.setter
    def ImagingSourceLocationSpecificationType(self, value: Optional[str]):
        if value is None:
            if "ImagingSourceLocationSpecificationType" in self._dataset:
                del self._dataset.ImagingSourceLocationSpecificationType
        else:
            self._dataset.ImagingSourceLocationSpecificationType = value

    @property
    def ImagingDeviceLocationMatrixSequence(self) -> Optional[List[ImagingDeviceLocationMatrixSequenceItem]]:
        if "ImagingDeviceLocationMatrixSequence" in self._dataset:
            if len(self._ImagingDeviceLocationMatrixSequence) == len(self._dataset.ImagingDeviceLocationMatrixSequence):
                return self._ImagingDeviceLocationMatrixSequence
            else:
                return [ImagingDeviceLocationMatrixSequenceItem(x) for x in self._dataset.ImagingDeviceLocationMatrixSequence]
        return None

    @ImagingDeviceLocationMatrixSequence.setter
    def ImagingDeviceLocationMatrixSequence(self, value: Optional[List[ImagingDeviceLocationMatrixSequenceItem]]):
        if value is None:
            self._ImagingDeviceLocationMatrixSequence = []
            if "ImagingDeviceLocationMatrixSequence" in self._dataset:
                del self._dataset.ImagingDeviceLocationMatrixSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ImagingDeviceLocationMatrixSequenceItem) for item in value
        ):
            raise ValueError(
                "ImagingDeviceLocationMatrixSequence must be a list of ImagingDeviceLocationMatrixSequenceItem objects"
            )
        else:
            self._ImagingDeviceLocationMatrixSequence = value
            if "ImagingDeviceLocationMatrixSequence" not in self._dataset:
                self._dataset.ImagingDeviceLocationMatrixSequence = pydicom.Sequence()
            self._dataset.ImagingDeviceLocationMatrixSequence.clear()
            self._dataset.ImagingDeviceLocationMatrixSequence.extend([item.to_dataset() for item in value])

    def add_ImagingDeviceLocationMatrix(self, item: ImagingDeviceLocationMatrixSequenceItem):
        if not isinstance(item, ImagingDeviceLocationMatrixSequenceItem):
            raise ValueError("Item must be an instance of ImagingDeviceLocationMatrixSequenceItem")
        self._ImagingDeviceLocationMatrixSequence.append(item)
        if "ImagingDeviceLocationMatrixSequence" not in self._dataset:
            self._dataset.ImagingDeviceLocationMatrixSequence = pydicom.Sequence()
        self._dataset.ImagingDeviceLocationMatrixSequence.append(item.to_dataset())

    @property
    def ImagingDeviceLocationParameterSequence(self) -> Optional[List[ImagingDeviceLocationParameterSequenceItem]]:
        if "ImagingDeviceLocationParameterSequence" in self._dataset:
            if len(self._ImagingDeviceLocationParameterSequence) == len(self._dataset.ImagingDeviceLocationParameterSequence):
                return self._ImagingDeviceLocationParameterSequence
            else:
                return [
                    ImagingDeviceLocationParameterSequenceItem(x) for x in self._dataset.ImagingDeviceLocationParameterSequence
                ]
        return None

    @ImagingDeviceLocationParameterSequence.setter
    def ImagingDeviceLocationParameterSequence(self, value: Optional[List[ImagingDeviceLocationParameterSequenceItem]]):
        if value is None:
            self._ImagingDeviceLocationParameterSequence = []
            if "ImagingDeviceLocationParameterSequence" in self._dataset:
                del self._dataset.ImagingDeviceLocationParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ImagingDeviceLocationParameterSequenceItem) for item in value
        ):
            raise ValueError(
                "ImagingDeviceLocationParameterSequence must be a list of ImagingDeviceLocationParameterSequenceItem objects"
            )
        else:
            self._ImagingDeviceLocationParameterSequence = value
            if "ImagingDeviceLocationParameterSequence" not in self._dataset:
                self._dataset.ImagingDeviceLocationParameterSequence = pydicom.Sequence()
            self._dataset.ImagingDeviceLocationParameterSequence.clear()
            self._dataset.ImagingDeviceLocationParameterSequence.extend([item.to_dataset() for item in value])

    def add_ImagingDeviceLocationParameter(self, item: ImagingDeviceLocationParameterSequenceItem):
        if not isinstance(item, ImagingDeviceLocationParameterSequenceItem):
            raise ValueError("Item must be an instance of ImagingDeviceLocationParameterSequenceItem")
        self._ImagingDeviceLocationParameterSequence.append(item)
        if "ImagingDeviceLocationParameterSequence" not in self._dataset:
            self._dataset.ImagingDeviceLocationParameterSequence = pydicom.Sequence()
        self._dataset.ImagingDeviceLocationParameterSequence.append(item.to_dataset())

    @property
    def ImagingApertureSequence(self) -> Optional[List[ImagingApertureSequenceItem]]:
        if "ImagingApertureSequence" in self._dataset:
            if len(self._ImagingApertureSequence) == len(self._dataset.ImagingApertureSequence):
                return self._ImagingApertureSequence
            else:
                return [ImagingApertureSequenceItem(x) for x in self._dataset.ImagingApertureSequence]
        return None

    @ImagingApertureSequence.setter
    def ImagingApertureSequence(self, value: Optional[List[ImagingApertureSequenceItem]]):
        if value is None:
            self._ImagingApertureSequence = []
            if "ImagingApertureSequence" in self._dataset:
                del self._dataset.ImagingApertureSequence
        elif not isinstance(value, list) or not all(isinstance(item, ImagingApertureSequenceItem) for item in value):
            raise ValueError("ImagingApertureSequence must be a list of ImagingApertureSequenceItem objects")
        else:
            self._ImagingApertureSequence = value
            if "ImagingApertureSequence" not in self._dataset:
                self._dataset.ImagingApertureSequence = pydicom.Sequence()
            self._dataset.ImagingApertureSequence.clear()
            self._dataset.ImagingApertureSequence.extend([item.to_dataset() for item in value])

    def add_ImagingAperture(self, item: ImagingApertureSequenceItem):
        if not isinstance(item, ImagingApertureSequenceItem):
            raise ValueError("Item must be an instance of ImagingApertureSequenceItem")
        self._ImagingApertureSequence.append(item)
        if "ImagingApertureSequence" not in self._dataset:
            self._dataset.ImagingApertureSequence = pydicom.Sequence()
        self._dataset.ImagingApertureSequence.append(item.to_dataset())

    @property
    def ImagingApertureSpecificationType(self) -> Optional[str]:
        if "ImagingApertureSpecificationType" in self._dataset:
            return self._dataset.ImagingApertureSpecificationType
        return None

    @ImagingApertureSpecificationType.setter
    def ImagingApertureSpecificationType(self, value: Optional[str]):
        if value is None:
            if "ImagingApertureSpecificationType" in self._dataset:
                del self._dataset.ImagingApertureSpecificationType
        else:
            self._dataset.ImagingApertureSpecificationType = value

    @property
    def ImagingSourceToBeamModifierDefinitionPlaneDistance(self) -> Optional[float]:
        if "ImagingSourceToBeamModifierDefinitionPlaneDistance" in self._dataset:
            return self._dataset.ImagingSourceToBeamModifierDefinitionPlaneDistance
        return None

    @ImagingSourceToBeamModifierDefinitionPlaneDistance.setter
    def ImagingSourceToBeamModifierDefinitionPlaneDistance(self, value: Optional[float]):
        if value is None:
            if "ImagingSourceToBeamModifierDefinitionPlaneDistance" in self._dataset:
                del self._dataset.ImagingSourceToBeamModifierDefinitionPlaneDistance
        else:
            self._dataset.ImagingSourceToBeamModifierDefinitionPlaneDistance = value

    @property
    def ReferencedRadiationRTControlPointIndex(self) -> Optional[int]:
        if "ReferencedRadiationRTControlPointIndex" in self._dataset:
            return self._dataset.ReferencedRadiationRTControlPointIndex
        return None

    @ReferencedRadiationRTControlPointIndex.setter
    def ReferencedRadiationRTControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRadiationRTControlPointIndex" in self._dataset:
                del self._dataset.ReferencedRadiationRTControlPointIndex
        else:
            self._dataset.ReferencedRadiationRTControlPointIndex = value
