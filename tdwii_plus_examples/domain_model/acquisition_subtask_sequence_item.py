from typing import Any, List, Optional  # noqa

import pydicom

from .acquisition_initiation_sequence_item import AcquisitionInitiationSequenceItem
from .additional_rt_accessory_device_sequence_item import (
    AdditionalRTAccessoryDeviceSequenceItem,
)
from .code_sequence_item import CodeSequenceItem
from .ct_imaging_acquisition_parameter_sequence_item import (
    CTImagingAcquisitionParameterSequenceItem,
)
from .device_specific_acquisition_parameter_sequence_item import (
    DeviceSpecificAcquisitionParameterSequenceItem,
)
from .kv_imaging_generation_parameters_sequence_item import (
    KVImagingGenerationParametersSequenceItem,
)
from .mv_imaging_generation_parameters_sequence_item import (
    MVImagingGenerationParametersSequenceItem,
)
from .position_acquisition_template_identification_sequence_item import (
    PositionAcquisitionTemplateIdentificationSequenceItem,
)
from .projection_imaging_acquisition_parameter_sequence_item import (
    ProjectionImagingAcquisitionParameterSequenceItem,
)
from .referenced_baseline_parameters_rt_radiation_instance_sequence_item import (
    ReferencedBaselineParametersRTRadiationInstanceSequenceItem,
)
from .referenced_position_reference_instance_sequence_item import (
    ReferencedPositionReferenceInstanceSequenceItem,
)


class AcquisitionSubtaskSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SubtaskWorkitemCodeSequence: List[CodeSequenceItem] = []
        self._ReferencedBaselineParametersRTRadiationInstanceSequence: List[
            ReferencedBaselineParametersRTRadiationInstanceSequenceItem
        ] = []
        self._PositionAcquisitionTemplateIdentificationSequence: List[
            PositionAcquisitionTemplateIdentificationSequenceItem
        ] = []
        self._ProjectionImagingAcquisitionParameterSequence: List[ProjectionImagingAcquisitionParameterSequenceItem] = []
        self._CTImagingAcquisitionParameterSequence: List[CTImagingAcquisitionParameterSequenceItem] = []
        self._KVImagingGenerationParametersSequence: List[KVImagingGenerationParametersSequenceItem] = []
        self._MVImagingGenerationParametersSequence: List[MVImagingGenerationParametersSequenceItem] = []
        self._AdditionalRTAccessoryDeviceSequence: List[AdditionalRTAccessoryDeviceSequenceItem] = []
        self._DeviceSpecificAcquisitionParameterSequence: List[DeviceSpecificAcquisitionParameterSequenceItem] = []
        self._ReferencedPositionReferenceInstanceSequence: List[ReferencedPositionReferenceInstanceSequenceItem] = []
        self._AcquisitionInitiationSequence: List[AcquisitionInitiationSequenceItem] = []
        self._RTDeviceDistanceReferenceLocationCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SubtaskWorkitemCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SubtaskWorkitemCodeSequence" in self._dataset:
            if len(self._SubtaskWorkitemCodeSequence) == len(self._dataset.SubtaskWorkitemCodeSequence):
                return self._SubtaskWorkitemCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SubtaskWorkitemCodeSequence]
        return None

    @SubtaskWorkitemCodeSequence.setter
    def SubtaskWorkitemCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SubtaskWorkitemCodeSequence = []
            if "SubtaskWorkitemCodeSequence" in self._dataset:
                del self._dataset.SubtaskWorkitemCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SubtaskWorkitemCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SubtaskWorkitemCodeSequence = value
            if "SubtaskWorkitemCodeSequence" not in self._dataset:
                self._dataset.SubtaskWorkitemCodeSequence = pydicom.Sequence()
            self._dataset.SubtaskWorkitemCodeSequence.clear()
            self._dataset.SubtaskWorkitemCodeSequence.extend([item.to_dataset() for item in value])

    def add_SubtaskWorkitemCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SubtaskWorkitemCodeSequence.append(item)
        if "SubtaskWorkitemCodeSequence" not in self._dataset:
            self._dataset.SubtaskWorkitemCodeSequence = pydicom.Sequence()
        self._dataset.SubtaskWorkitemCodeSequence.append(item.to_dataset())

    @property
    def AcquisitionSubtaskIndex(self) -> Optional[int]:
        if "AcquisitionSubtaskIndex" in self._dataset:
            return self._dataset.AcquisitionSubtaskIndex
        return None

    @AcquisitionSubtaskIndex.setter
    def AcquisitionSubtaskIndex(self, value: Optional[int]):
        if value is None:
            if "AcquisitionSubtaskIndex" in self._dataset:
                del self._dataset.AcquisitionSubtaskIndex
        else:
            self._dataset.AcquisitionSubtaskIndex = value

    @property
    def ReferencedBaselineParametersRTRadiationInstanceSequence(
        self,
    ) -> Optional[List[ReferencedBaselineParametersRTRadiationInstanceSequenceItem]]:
        if "ReferencedBaselineParametersRTRadiationInstanceSequence" in self._dataset:
            if len(self._ReferencedBaselineParametersRTRadiationInstanceSequence) == len(
                self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence
            ):
                return self._ReferencedBaselineParametersRTRadiationInstanceSequence
            else:
                return [
                    ReferencedBaselineParametersRTRadiationInstanceSequenceItem(x)
                    for x in self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence
                ]
        return None

    @ReferencedBaselineParametersRTRadiationInstanceSequence.setter
    def ReferencedBaselineParametersRTRadiationInstanceSequence(
        self, value: Optional[List[ReferencedBaselineParametersRTRadiationInstanceSequenceItem]]
    ):
        if value is None:
            self._ReferencedBaselineParametersRTRadiationInstanceSequence = []
            if "ReferencedBaselineParametersRTRadiationInstanceSequence" in self._dataset:
                del self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedBaselineParametersRTRadiationInstanceSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedBaselineParametersRTRadiationInstanceSequence must be a list of"
                " ReferencedBaselineParametersRTRadiationInstanceSequenceItem objects"
            )
        else:
            self._ReferencedBaselineParametersRTRadiationInstanceSequence = value
            if "ReferencedBaselineParametersRTRadiationInstanceSequence" not in self._dataset:
                self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence.clear()
            self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBaselineParametersRTRadiationInstance(
        self, item: ReferencedBaselineParametersRTRadiationInstanceSequenceItem
    ):
        if not isinstance(item, ReferencedBaselineParametersRTRadiationInstanceSequenceItem):
            raise ValueError("Item must be an instance of ReferencedBaselineParametersRTRadiationInstanceSequenceItem")
        self._ReferencedBaselineParametersRTRadiationInstanceSequence.append(item)
        if "ReferencedBaselineParametersRTRadiationInstanceSequence" not in self._dataset:
            self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedBaselineParametersRTRadiationInstanceSequence.append(item.to_dataset())

    @property
    def PositionAcquisitionTemplateIdentificationSequence(
        self,
    ) -> Optional[List[PositionAcquisitionTemplateIdentificationSequenceItem]]:
        if "PositionAcquisitionTemplateIdentificationSequence" in self._dataset:
            if len(self._PositionAcquisitionTemplateIdentificationSequence) == len(
                self._dataset.PositionAcquisitionTemplateIdentificationSequence
            ):
                return self._PositionAcquisitionTemplateIdentificationSequence
            else:
                return [
                    PositionAcquisitionTemplateIdentificationSequenceItem(x)
                    for x in self._dataset.PositionAcquisitionTemplateIdentificationSequence
                ]
        return None

    @PositionAcquisitionTemplateIdentificationSequence.setter
    def PositionAcquisitionTemplateIdentificationSequence(
        self, value: Optional[List[PositionAcquisitionTemplateIdentificationSequenceItem]]
    ):
        if value is None:
            self._PositionAcquisitionTemplateIdentificationSequence = []
            if "PositionAcquisitionTemplateIdentificationSequence" in self._dataset:
                del self._dataset.PositionAcquisitionTemplateIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PositionAcquisitionTemplateIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "PositionAcquisitionTemplateIdentificationSequence must be a list of"
                " PositionAcquisitionTemplateIdentificationSequenceItem objects"
            )
        else:
            self._PositionAcquisitionTemplateIdentificationSequence = value
            if "PositionAcquisitionTemplateIdentificationSequence" not in self._dataset:
                self._dataset.PositionAcquisitionTemplateIdentificationSequence = pydicom.Sequence()
            self._dataset.PositionAcquisitionTemplateIdentificationSequence.clear()
            self._dataset.PositionAcquisitionTemplateIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_PositionAcquisitionTemplateIdentification(self, item: PositionAcquisitionTemplateIdentificationSequenceItem):
        if not isinstance(item, PositionAcquisitionTemplateIdentificationSequenceItem):
            raise ValueError("Item must be an instance of PositionAcquisitionTemplateIdentificationSequenceItem")
        self._PositionAcquisitionTemplateIdentificationSequence.append(item)
        if "PositionAcquisitionTemplateIdentificationSequence" not in self._dataset:
            self._dataset.PositionAcquisitionTemplateIdentificationSequence = pydicom.Sequence()
        self._dataset.PositionAcquisitionTemplateIdentificationSequence.append(item.to_dataset())

    @property
    def ProjectionImagingAcquisitionParameterSequence(
        self,
    ) -> Optional[List[ProjectionImagingAcquisitionParameterSequenceItem]]:
        if "ProjectionImagingAcquisitionParameterSequence" in self._dataset:
            if len(self._ProjectionImagingAcquisitionParameterSequence) == len(
                self._dataset.ProjectionImagingAcquisitionParameterSequence
            ):
                return self._ProjectionImagingAcquisitionParameterSequence
            else:
                return [
                    ProjectionImagingAcquisitionParameterSequenceItem(x)
                    for x in self._dataset.ProjectionImagingAcquisitionParameterSequence
                ]
        return None

    @ProjectionImagingAcquisitionParameterSequence.setter
    def ProjectionImagingAcquisitionParameterSequence(
        self, value: Optional[List[ProjectionImagingAcquisitionParameterSequenceItem]]
    ):
        if value is None:
            self._ProjectionImagingAcquisitionParameterSequence = []
            if "ProjectionImagingAcquisitionParameterSequence" in self._dataset:
                del self._dataset.ProjectionImagingAcquisitionParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ProjectionImagingAcquisitionParameterSequenceItem) for item in value
        ):
            raise ValueError(
                "ProjectionImagingAcquisitionParameterSequence must be a list of"
                " ProjectionImagingAcquisitionParameterSequenceItem objects"
            )
        else:
            self._ProjectionImagingAcquisitionParameterSequence = value
            if "ProjectionImagingAcquisitionParameterSequence" not in self._dataset:
                self._dataset.ProjectionImagingAcquisitionParameterSequence = pydicom.Sequence()
            self._dataset.ProjectionImagingAcquisitionParameterSequence.clear()
            self._dataset.ProjectionImagingAcquisitionParameterSequence.extend([item.to_dataset() for item in value])

    def add_ProjectionImagingAcquisitionParameter(self, item: ProjectionImagingAcquisitionParameterSequenceItem):
        if not isinstance(item, ProjectionImagingAcquisitionParameterSequenceItem):
            raise ValueError("Item must be an instance of ProjectionImagingAcquisitionParameterSequenceItem")
        self._ProjectionImagingAcquisitionParameterSequence.append(item)
        if "ProjectionImagingAcquisitionParameterSequence" not in self._dataset:
            self._dataset.ProjectionImagingAcquisitionParameterSequence = pydicom.Sequence()
        self._dataset.ProjectionImagingAcquisitionParameterSequence.append(item.to_dataset())

    @property
    def CTImagingAcquisitionParameterSequence(self) -> Optional[List[CTImagingAcquisitionParameterSequenceItem]]:
        if "CTImagingAcquisitionParameterSequence" in self._dataset:
            if len(self._CTImagingAcquisitionParameterSequence) == len(self._dataset.CTImagingAcquisitionParameterSequence):
                return self._CTImagingAcquisitionParameterSequence
            else:
                return [
                    CTImagingAcquisitionParameterSequenceItem(x) for x in self._dataset.CTImagingAcquisitionParameterSequence
                ]
        return None

    @CTImagingAcquisitionParameterSequence.setter
    def CTImagingAcquisitionParameterSequence(self, value: Optional[List[CTImagingAcquisitionParameterSequenceItem]]):
        if value is None:
            self._CTImagingAcquisitionParameterSequence = []
            if "CTImagingAcquisitionParameterSequence" in self._dataset:
                del self._dataset.CTImagingAcquisitionParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, CTImagingAcquisitionParameterSequenceItem) for item in value
        ):
            raise ValueError(
                "CTImagingAcquisitionParameterSequence must be a list of CTImagingAcquisitionParameterSequenceItem objects"
            )
        else:
            self._CTImagingAcquisitionParameterSequence = value
            if "CTImagingAcquisitionParameterSequence" not in self._dataset:
                self._dataset.CTImagingAcquisitionParameterSequence = pydicom.Sequence()
            self._dataset.CTImagingAcquisitionParameterSequence.clear()
            self._dataset.CTImagingAcquisitionParameterSequence.extend([item.to_dataset() for item in value])

    def add_CTImagingAcquisitionParameter(self, item: CTImagingAcquisitionParameterSequenceItem):
        if not isinstance(item, CTImagingAcquisitionParameterSequenceItem):
            raise ValueError("Item must be an instance of CTImagingAcquisitionParameterSequenceItem")
        self._CTImagingAcquisitionParameterSequence.append(item)
        if "CTImagingAcquisitionParameterSequence" not in self._dataset:
            self._dataset.CTImagingAcquisitionParameterSequence = pydicom.Sequence()
        self._dataset.CTImagingAcquisitionParameterSequence.append(item.to_dataset())

    @property
    def KVImagingGenerationParametersSequence(self) -> Optional[List[KVImagingGenerationParametersSequenceItem]]:
        if "KVImagingGenerationParametersSequence" in self._dataset:
            if len(self._KVImagingGenerationParametersSequence) == len(self._dataset.KVImagingGenerationParametersSequence):
                return self._KVImagingGenerationParametersSequence
            else:
                return [
                    KVImagingGenerationParametersSequenceItem(x) for x in self._dataset.KVImagingGenerationParametersSequence
                ]
        return None

    @KVImagingGenerationParametersSequence.setter
    def KVImagingGenerationParametersSequence(self, value: Optional[List[KVImagingGenerationParametersSequenceItem]]):
        if value is None:
            self._KVImagingGenerationParametersSequence = []
            if "KVImagingGenerationParametersSequence" in self._dataset:
                del self._dataset.KVImagingGenerationParametersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, KVImagingGenerationParametersSequenceItem) for item in value
        ):
            raise ValueError(
                "KVImagingGenerationParametersSequence must be a list of KVImagingGenerationParametersSequenceItem objects"
            )
        else:
            self._KVImagingGenerationParametersSequence = value
            if "KVImagingGenerationParametersSequence" not in self._dataset:
                self._dataset.KVImagingGenerationParametersSequence = pydicom.Sequence()
            self._dataset.KVImagingGenerationParametersSequence.clear()
            self._dataset.KVImagingGenerationParametersSequence.extend([item.to_dataset() for item in value])

    def add_KVImagingGenerationParameters(self, item: KVImagingGenerationParametersSequenceItem):
        if not isinstance(item, KVImagingGenerationParametersSequenceItem):
            raise ValueError("Item must be an instance of KVImagingGenerationParametersSequenceItem")
        self._KVImagingGenerationParametersSequence.append(item)
        if "KVImagingGenerationParametersSequence" not in self._dataset:
            self._dataset.KVImagingGenerationParametersSequence = pydicom.Sequence()
        self._dataset.KVImagingGenerationParametersSequence.append(item.to_dataset())

    @property
    def MVImagingGenerationParametersSequence(self) -> Optional[List[MVImagingGenerationParametersSequenceItem]]:
        if "MVImagingGenerationParametersSequence" in self._dataset:
            if len(self._MVImagingGenerationParametersSequence) == len(self._dataset.MVImagingGenerationParametersSequence):
                return self._MVImagingGenerationParametersSequence
            else:
                return [
                    MVImagingGenerationParametersSequenceItem(x) for x in self._dataset.MVImagingGenerationParametersSequence
                ]
        return None

    @MVImagingGenerationParametersSequence.setter
    def MVImagingGenerationParametersSequence(self, value: Optional[List[MVImagingGenerationParametersSequenceItem]]):
        if value is None:
            self._MVImagingGenerationParametersSequence = []
            if "MVImagingGenerationParametersSequence" in self._dataset:
                del self._dataset.MVImagingGenerationParametersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, MVImagingGenerationParametersSequenceItem) for item in value
        ):
            raise ValueError(
                "MVImagingGenerationParametersSequence must be a list of MVImagingGenerationParametersSequenceItem objects"
            )
        else:
            self._MVImagingGenerationParametersSequence = value
            if "MVImagingGenerationParametersSequence" not in self._dataset:
                self._dataset.MVImagingGenerationParametersSequence = pydicom.Sequence()
            self._dataset.MVImagingGenerationParametersSequence.clear()
            self._dataset.MVImagingGenerationParametersSequence.extend([item.to_dataset() for item in value])

    def add_MVImagingGenerationParameters(self, item: MVImagingGenerationParametersSequenceItem):
        if not isinstance(item, MVImagingGenerationParametersSequenceItem):
            raise ValueError("Item must be an instance of MVImagingGenerationParametersSequenceItem")
        self._MVImagingGenerationParametersSequence.append(item)
        if "MVImagingGenerationParametersSequence" not in self._dataset:
            self._dataset.MVImagingGenerationParametersSequence = pydicom.Sequence()
        self._dataset.MVImagingGenerationParametersSequence.append(item.to_dataset())

    @property
    def AcquisitionSignalType(self) -> Optional[str]:
        if "AcquisitionSignalType" in self._dataset:
            return self._dataset.AcquisitionSignalType
        return None

    @AcquisitionSignalType.setter
    def AcquisitionSignalType(self, value: Optional[str]):
        if value is None:
            if "AcquisitionSignalType" in self._dataset:
                del self._dataset.AcquisitionSignalType
        else:
            self._dataset.AcquisitionSignalType = value

    @property
    def AcquisitionMethod(self) -> Optional[str]:
        if "AcquisitionMethod" in self._dataset:
            return self._dataset.AcquisitionMethod
        return None

    @AcquisitionMethod.setter
    def AcquisitionMethod(self, value: Optional[str]):
        if value is None:
            if "AcquisitionMethod" in self._dataset:
                del self._dataset.AcquisitionMethod
        else:
            self._dataset.AcquisitionMethod = value

    @property
    def AdditionalRTAccessoryDeviceSequence(self) -> Optional[List[AdditionalRTAccessoryDeviceSequenceItem]]:
        if "AdditionalRTAccessoryDeviceSequence" in self._dataset:
            if len(self._AdditionalRTAccessoryDeviceSequence) == len(self._dataset.AdditionalRTAccessoryDeviceSequence):
                return self._AdditionalRTAccessoryDeviceSequence
            else:
                return [AdditionalRTAccessoryDeviceSequenceItem(x) for x in self._dataset.AdditionalRTAccessoryDeviceSequence]
        return None

    @AdditionalRTAccessoryDeviceSequence.setter
    def AdditionalRTAccessoryDeviceSequence(self, value: Optional[List[AdditionalRTAccessoryDeviceSequenceItem]]):
        if value is None:
            self._AdditionalRTAccessoryDeviceSequence = []
            if "AdditionalRTAccessoryDeviceSequence" in self._dataset:
                del self._dataset.AdditionalRTAccessoryDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, AdditionalRTAccessoryDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                "AdditionalRTAccessoryDeviceSequence must be a list of AdditionalRTAccessoryDeviceSequenceItem objects"
            )
        else:
            self._AdditionalRTAccessoryDeviceSequence = value
            if "AdditionalRTAccessoryDeviceSequence" not in self._dataset:
                self._dataset.AdditionalRTAccessoryDeviceSequence = pydicom.Sequence()
            self._dataset.AdditionalRTAccessoryDeviceSequence.clear()
            self._dataset.AdditionalRTAccessoryDeviceSequence.extend([item.to_dataset() for item in value])

    def add_AdditionalRTAccessoryDevice(self, item: AdditionalRTAccessoryDeviceSequenceItem):
        if not isinstance(item, AdditionalRTAccessoryDeviceSequenceItem):
            raise ValueError("Item must be an instance of AdditionalRTAccessoryDeviceSequenceItem")
        self._AdditionalRTAccessoryDeviceSequence.append(item)
        if "AdditionalRTAccessoryDeviceSequence" not in self._dataset:
            self._dataset.AdditionalRTAccessoryDeviceSequence = pydicom.Sequence()
        self._dataset.AdditionalRTAccessoryDeviceSequence.append(item.to_dataset())

    @property
    def DeviceSpecificAcquisitionParameterSequence(self) -> Optional[List[DeviceSpecificAcquisitionParameterSequenceItem]]:
        if "DeviceSpecificAcquisitionParameterSequence" in self._dataset:
            if len(self._DeviceSpecificAcquisitionParameterSequence) == len(
                self._dataset.DeviceSpecificAcquisitionParameterSequence
            ):
                return self._DeviceSpecificAcquisitionParameterSequence
            else:
                return [
                    DeviceSpecificAcquisitionParameterSequenceItem(x)
                    for x in self._dataset.DeviceSpecificAcquisitionParameterSequence
                ]
        return None

    @DeviceSpecificAcquisitionParameterSequence.setter
    def DeviceSpecificAcquisitionParameterSequence(
        self, value: Optional[List[DeviceSpecificAcquisitionParameterSequenceItem]]
    ):
        if value is None:
            self._DeviceSpecificAcquisitionParameterSequence = []
            if "DeviceSpecificAcquisitionParameterSequence" in self._dataset:
                del self._dataset.DeviceSpecificAcquisitionParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DeviceSpecificAcquisitionParameterSequenceItem) for item in value
        ):
            raise ValueError(
                "DeviceSpecificAcquisitionParameterSequence must be a list of DeviceSpecificAcquisitionParameterSequenceItem"
                " objects"
            )
        else:
            self._DeviceSpecificAcquisitionParameterSequence = value
            if "DeviceSpecificAcquisitionParameterSequence" not in self._dataset:
                self._dataset.DeviceSpecificAcquisitionParameterSequence = pydicom.Sequence()
            self._dataset.DeviceSpecificAcquisitionParameterSequence.clear()
            self._dataset.DeviceSpecificAcquisitionParameterSequence.extend([item.to_dataset() for item in value])

    def add_DeviceSpecificAcquisitionParameter(self, item: DeviceSpecificAcquisitionParameterSequenceItem):
        if not isinstance(item, DeviceSpecificAcquisitionParameterSequenceItem):
            raise ValueError("Item must be an instance of DeviceSpecificAcquisitionParameterSequenceItem")
        self._DeviceSpecificAcquisitionParameterSequence.append(item)
        if "DeviceSpecificAcquisitionParameterSequence" not in self._dataset:
            self._dataset.DeviceSpecificAcquisitionParameterSequence = pydicom.Sequence()
        self._dataset.DeviceSpecificAcquisitionParameterSequence.append(item.to_dataset())

    @property
    def ReferencedPositionReferenceInstanceSequence(self) -> Optional[List[ReferencedPositionReferenceInstanceSequenceItem]]:
        if "ReferencedPositionReferenceInstanceSequence" in self._dataset:
            if len(self._ReferencedPositionReferenceInstanceSequence) == len(
                self._dataset.ReferencedPositionReferenceInstanceSequence
            ):
                return self._ReferencedPositionReferenceInstanceSequence
            else:
                return [
                    ReferencedPositionReferenceInstanceSequenceItem(x)
                    for x in self._dataset.ReferencedPositionReferenceInstanceSequence
                ]
        return None

    @ReferencedPositionReferenceInstanceSequence.setter
    def ReferencedPositionReferenceInstanceSequence(
        self, value: Optional[List[ReferencedPositionReferenceInstanceSequenceItem]]
    ):
        if value is None:
            self._ReferencedPositionReferenceInstanceSequence = []
            if "ReferencedPositionReferenceInstanceSequence" in self._dataset:
                del self._dataset.ReferencedPositionReferenceInstanceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPositionReferenceInstanceSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedPositionReferenceInstanceSequence must be a list of ReferencedPositionReferenceInstanceSequenceItem"
                " objects"
            )
        else:
            self._ReferencedPositionReferenceInstanceSequence = value
            if "ReferencedPositionReferenceInstanceSequence" not in self._dataset:
                self._dataset.ReferencedPositionReferenceInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedPositionReferenceInstanceSequence.clear()
            self._dataset.ReferencedPositionReferenceInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPositionReferenceInstance(self, item: ReferencedPositionReferenceInstanceSequenceItem):
        if not isinstance(item, ReferencedPositionReferenceInstanceSequenceItem):
            raise ValueError("Item must be an instance of ReferencedPositionReferenceInstanceSequenceItem")
        self._ReferencedPositionReferenceInstanceSequence.append(item)
        if "ReferencedPositionReferenceInstanceSequence" not in self._dataset:
            self._dataset.ReferencedPositionReferenceInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedPositionReferenceInstanceSequence.append(item.to_dataset())

    @property
    def AcquisitionInitiationSequence(self) -> Optional[List[AcquisitionInitiationSequenceItem]]:
        if "AcquisitionInitiationSequence" in self._dataset:
            if len(self._AcquisitionInitiationSequence) == len(self._dataset.AcquisitionInitiationSequence):
                return self._AcquisitionInitiationSequence
            else:
                return [AcquisitionInitiationSequenceItem(x) for x in self._dataset.AcquisitionInitiationSequence]
        return None

    @AcquisitionInitiationSequence.setter
    def AcquisitionInitiationSequence(self, value: Optional[List[AcquisitionInitiationSequenceItem]]):
        if value is None:
            self._AcquisitionInitiationSequence = []
            if "AcquisitionInitiationSequence" in self._dataset:
                del self._dataset.AcquisitionInitiationSequence
        elif not isinstance(value, list) or not all(isinstance(item, AcquisitionInitiationSequenceItem) for item in value):
            raise ValueError("AcquisitionInitiationSequence must be a list of AcquisitionInitiationSequenceItem objects")
        else:
            self._AcquisitionInitiationSequence = value
            if "AcquisitionInitiationSequence" not in self._dataset:
                self._dataset.AcquisitionInitiationSequence = pydicom.Sequence()
            self._dataset.AcquisitionInitiationSequence.clear()
            self._dataset.AcquisitionInitiationSequence.extend([item.to_dataset() for item in value])

    def add_AcquisitionInitiation(self, item: AcquisitionInitiationSequenceItem):
        if not isinstance(item, AcquisitionInitiationSequenceItem):
            raise ValueError("Item must be an instance of AcquisitionInitiationSequenceItem")
        self._AcquisitionInitiationSequence.append(item)
        if "AcquisitionInitiationSequence" not in self._dataset:
            self._dataset.AcquisitionInitiationSequence = pydicom.Sequence()
        self._dataset.AcquisitionInitiationSequence.append(item.to_dataset())

    @property
    def ReferencedDeviceIndex(self) -> Optional[int]:
        if "ReferencedDeviceIndex" in self._dataset:
            return self._dataset.ReferencedDeviceIndex
        return None

    @ReferencedDeviceIndex.setter
    def ReferencedDeviceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedDeviceIndex" in self._dataset:
                del self._dataset.ReferencedDeviceIndex
        else:
            self._dataset.ReferencedDeviceIndex = value

    @property
    def RTDeviceDistanceReferenceLocationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTDeviceDistanceReferenceLocationCodeSequence" in self._dataset:
            if len(self._RTDeviceDistanceReferenceLocationCodeSequence) == len(
                self._dataset.RTDeviceDistanceReferenceLocationCodeSequence
            ):
                return self._RTDeviceDistanceReferenceLocationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTDeviceDistanceReferenceLocationCodeSequence]
        return None

    @RTDeviceDistanceReferenceLocationCodeSequence.setter
    def RTDeviceDistanceReferenceLocationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTDeviceDistanceReferenceLocationCodeSequence = []
            if "RTDeviceDistanceReferenceLocationCodeSequence" in self._dataset:
                del self._dataset.RTDeviceDistanceReferenceLocationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RTDeviceDistanceReferenceLocationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTDeviceDistanceReferenceLocationCodeSequence = value
            if "RTDeviceDistanceReferenceLocationCodeSequence" not in self._dataset:
                self._dataset.RTDeviceDistanceReferenceLocationCodeSequence = pydicom.Sequence()
            self._dataset.RTDeviceDistanceReferenceLocationCodeSequence.clear()
            self._dataset.RTDeviceDistanceReferenceLocationCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTDeviceDistanceReferenceLocationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RTDeviceDistanceReferenceLocationCodeSequence.append(item)
        if "RTDeviceDistanceReferenceLocationCodeSequence" not in self._dataset:
            self._dataset.RTDeviceDistanceReferenceLocationCodeSequence = pydicom.Sequence()
        self._dataset.RTDeviceDistanceReferenceLocationCodeSequence.append(item.to_dataset())

    @property
    def RTBeamModifierDefinitionDistance(self) -> Optional[float]:
        if "RTBeamModifierDefinitionDistance" in self._dataset:
            return self._dataset.RTBeamModifierDefinitionDistance
        return None

    @RTBeamModifierDefinitionDistance.setter
    def RTBeamModifierDefinitionDistance(self, value: Optional[float]):
        if value is None:
            if "RTBeamModifierDefinitionDistance" in self._dataset:
                del self._dataset.RTBeamModifierDefinitionDistance
        else:
            self._dataset.RTBeamModifierDefinitionDistance = value
