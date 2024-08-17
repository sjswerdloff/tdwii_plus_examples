from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .fixation_device_sequence_item import FixationDeviceSequenceItem
from .motion_synchronization_sequence_item import MotionSynchronizationSequenceItem
from .referenced_setup_image_sequence_item import ReferencedSetupImageSequenceItem
from .setup_device_sequence_item import SetupDeviceSequenceItem
from .shielding_device_sequence_item import ShieldingDeviceSequenceItem


class PatientSetupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._FixationDeviceSequence: List[FixationDeviceSequenceItem] = []
        self._ShieldingDeviceSequence: List[ShieldingDeviceSequenceItem] = []
        self._SetupDeviceSequence: List[SetupDeviceSequenceItem] = []
        self._ReferencedSetupImageSequence: List[ReferencedSetupImageSequenceItem] = []
        self._MotionSynchronizationSequence: List[MotionSynchronizationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PatientPosition(self) -> Optional[str]:
        if "PatientPosition" in self._dataset:
            return self._dataset.PatientPosition
        return None

    @PatientPosition.setter
    def PatientPosition(self, value: Optional[str]):
        if value is None:
            if "PatientPosition" in self._dataset:
                del self._dataset.PatientPosition
        else:
            self._dataset.PatientPosition = value

    @property
    def PatientSetupNumber(self) -> Optional[int]:
        if "PatientSetupNumber" in self._dataset:
            return self._dataset.PatientSetupNumber
        return None

    @PatientSetupNumber.setter
    def PatientSetupNumber(self, value: Optional[int]):
        if value is None:
            if "PatientSetupNumber" in self._dataset:
                del self._dataset.PatientSetupNumber
        else:
            self._dataset.PatientSetupNumber = value

    @property
    def PatientSetupLabel(self) -> Optional[str]:
        if "PatientSetupLabel" in self._dataset:
            return self._dataset.PatientSetupLabel
        return None

    @PatientSetupLabel.setter
    def PatientSetupLabel(self, value: Optional[str]):
        if value is None:
            if "PatientSetupLabel" in self._dataset:
                del self._dataset.PatientSetupLabel
        else:
            self._dataset.PatientSetupLabel = value

    @property
    def PatientAdditionalPosition(self) -> Optional[str]:
        if "PatientAdditionalPosition" in self._dataset:
            return self._dataset.PatientAdditionalPosition
        return None

    @PatientAdditionalPosition.setter
    def PatientAdditionalPosition(self, value: Optional[str]):
        if value is None:
            if "PatientAdditionalPosition" in self._dataset:
                del self._dataset.PatientAdditionalPosition
        else:
            self._dataset.PatientAdditionalPosition = value

    @property
    def FixationDeviceSequence(self) -> Optional[List[FixationDeviceSequenceItem]]:
        if "FixationDeviceSequence" in self._dataset:
            if len(self._FixationDeviceSequence) == len(self._dataset.FixationDeviceSequence):
                return self._FixationDeviceSequence
            else:
                return [FixationDeviceSequenceItem(x) for x in self._dataset.FixationDeviceSequence]
        return None

    @FixationDeviceSequence.setter
    def FixationDeviceSequence(self, value: Optional[List[FixationDeviceSequenceItem]]):
        if value is None:
            self._FixationDeviceSequence = []
            if "FixationDeviceSequence" in self._dataset:
                del self._dataset.FixationDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, FixationDeviceSequenceItem) for item in value):
            raise ValueError("FixationDeviceSequence must be a list of FixationDeviceSequenceItem objects")
        else:
            self._FixationDeviceSequence = value
            if "FixationDeviceSequence" not in self._dataset:
                self._dataset.FixationDeviceSequence = pydicom.Sequence()
            self._dataset.FixationDeviceSequence.clear()
            self._dataset.FixationDeviceSequence.extend([item.to_dataset() for item in value])

    def add_FixationDevice(self, item: FixationDeviceSequenceItem):
        if not isinstance(item, FixationDeviceSequenceItem):
            raise ValueError("Item must be an instance of FixationDeviceSequenceItem")
        self._FixationDeviceSequence.append(item)
        if "FixationDeviceSequence" not in self._dataset:
            self._dataset.FixationDeviceSequence = pydicom.Sequence()
        self._dataset.FixationDeviceSequence.append(item.to_dataset())

    @property
    def ShieldingDeviceSequence(self) -> Optional[List[ShieldingDeviceSequenceItem]]:
        if "ShieldingDeviceSequence" in self._dataset:
            if len(self._ShieldingDeviceSequence) == len(self._dataset.ShieldingDeviceSequence):
                return self._ShieldingDeviceSequence
            else:
                return [ShieldingDeviceSequenceItem(x) for x in self._dataset.ShieldingDeviceSequence]
        return None

    @ShieldingDeviceSequence.setter
    def ShieldingDeviceSequence(self, value: Optional[List[ShieldingDeviceSequenceItem]]):
        if value is None:
            self._ShieldingDeviceSequence = []
            if "ShieldingDeviceSequence" in self._dataset:
                del self._dataset.ShieldingDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ShieldingDeviceSequenceItem) for item in value):
            raise ValueError("ShieldingDeviceSequence must be a list of ShieldingDeviceSequenceItem objects")
        else:
            self._ShieldingDeviceSequence = value
            if "ShieldingDeviceSequence" not in self._dataset:
                self._dataset.ShieldingDeviceSequence = pydicom.Sequence()
            self._dataset.ShieldingDeviceSequence.clear()
            self._dataset.ShieldingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_ShieldingDevice(self, item: ShieldingDeviceSequenceItem):
        if not isinstance(item, ShieldingDeviceSequenceItem):
            raise ValueError("Item must be an instance of ShieldingDeviceSequenceItem")
        self._ShieldingDeviceSequence.append(item)
        if "ShieldingDeviceSequence" not in self._dataset:
            self._dataset.ShieldingDeviceSequence = pydicom.Sequence()
        self._dataset.ShieldingDeviceSequence.append(item.to_dataset())

    @property
    def SetupTechnique(self) -> Optional[str]:
        if "SetupTechnique" in self._dataset:
            return self._dataset.SetupTechnique
        return None

    @SetupTechnique.setter
    def SetupTechnique(self, value: Optional[str]):
        if value is None:
            if "SetupTechnique" in self._dataset:
                del self._dataset.SetupTechnique
        else:
            self._dataset.SetupTechnique = value

    @property
    def SetupTechniqueDescription(self) -> Optional[str]:
        if "SetupTechniqueDescription" in self._dataset:
            return self._dataset.SetupTechniqueDescription
        return None

    @SetupTechniqueDescription.setter
    def SetupTechniqueDescription(self, value: Optional[str]):
        if value is None:
            if "SetupTechniqueDescription" in self._dataset:
                del self._dataset.SetupTechniqueDescription
        else:
            self._dataset.SetupTechniqueDescription = value

    @property
    def SetupDeviceSequence(self) -> Optional[List[SetupDeviceSequenceItem]]:
        if "SetupDeviceSequence" in self._dataset:
            if len(self._SetupDeviceSequence) == len(self._dataset.SetupDeviceSequence):
                return self._SetupDeviceSequence
            else:
                return [SetupDeviceSequenceItem(x) for x in self._dataset.SetupDeviceSequence]
        return None

    @SetupDeviceSequence.setter
    def SetupDeviceSequence(self, value: Optional[List[SetupDeviceSequenceItem]]):
        if value is None:
            self._SetupDeviceSequence = []
            if "SetupDeviceSequence" in self._dataset:
                del self._dataset.SetupDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, SetupDeviceSequenceItem) for item in value):
            raise ValueError("SetupDeviceSequence must be a list of SetupDeviceSequenceItem objects")
        else:
            self._SetupDeviceSequence = value
            if "SetupDeviceSequence" not in self._dataset:
                self._dataset.SetupDeviceSequence = pydicom.Sequence()
            self._dataset.SetupDeviceSequence.clear()
            self._dataset.SetupDeviceSequence.extend([item.to_dataset() for item in value])

    def add_SetupDevice(self, item: SetupDeviceSequenceItem):
        if not isinstance(item, SetupDeviceSequenceItem):
            raise ValueError("Item must be an instance of SetupDeviceSequenceItem")
        self._SetupDeviceSequence.append(item)
        if "SetupDeviceSequence" not in self._dataset:
            self._dataset.SetupDeviceSequence = pydicom.Sequence()
        self._dataset.SetupDeviceSequence.append(item.to_dataset())

    @property
    def TableTopVerticalSetupDisplacement(self) -> Optional[Decimal]:
        if "TableTopVerticalSetupDisplacement" in self._dataset:
            return self._dataset.TableTopVerticalSetupDisplacement
        return None

    @TableTopVerticalSetupDisplacement.setter
    def TableTopVerticalSetupDisplacement(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopVerticalSetupDisplacement" in self._dataset:
                del self._dataset.TableTopVerticalSetupDisplacement
        else:
            self._dataset.TableTopVerticalSetupDisplacement = value

    @property
    def TableTopLongitudinalSetupDisplacement(self) -> Optional[Decimal]:
        if "TableTopLongitudinalSetupDisplacement" in self._dataset:
            return self._dataset.TableTopLongitudinalSetupDisplacement
        return None

    @TableTopLongitudinalSetupDisplacement.setter
    def TableTopLongitudinalSetupDisplacement(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLongitudinalSetupDisplacement" in self._dataset:
                del self._dataset.TableTopLongitudinalSetupDisplacement
        else:
            self._dataset.TableTopLongitudinalSetupDisplacement = value

    @property
    def TableTopLateralSetupDisplacement(self) -> Optional[Decimal]:
        if "TableTopLateralSetupDisplacement" in self._dataset:
            return self._dataset.TableTopLateralSetupDisplacement
        return None

    @TableTopLateralSetupDisplacement.setter
    def TableTopLateralSetupDisplacement(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLateralSetupDisplacement" in self._dataset:
                del self._dataset.TableTopLateralSetupDisplacement
        else:
            self._dataset.TableTopLateralSetupDisplacement = value

    @property
    def ReferencedSetupImageSequence(self) -> Optional[List[ReferencedSetupImageSequenceItem]]:
        if "ReferencedSetupImageSequence" in self._dataset:
            if len(self._ReferencedSetupImageSequence) == len(self._dataset.ReferencedSetupImageSequence):
                return self._ReferencedSetupImageSequence
            else:
                return [ReferencedSetupImageSequenceItem(x) for x in self._dataset.ReferencedSetupImageSequence]
        return None

    @ReferencedSetupImageSequence.setter
    def ReferencedSetupImageSequence(self, value: Optional[List[ReferencedSetupImageSequenceItem]]):
        if value is None:
            self._ReferencedSetupImageSequence = []
            if "ReferencedSetupImageSequence" in self._dataset:
                del self._dataset.ReferencedSetupImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSetupImageSequenceItem) for item in value):
            raise ValueError("ReferencedSetupImageSequence must be a list of ReferencedSetupImageSequenceItem objects")
        else:
            self._ReferencedSetupImageSequence = value
            if "ReferencedSetupImageSequence" not in self._dataset:
                self._dataset.ReferencedSetupImageSequence = pydicom.Sequence()
            self._dataset.ReferencedSetupImageSequence.clear()
            self._dataset.ReferencedSetupImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSetupImage(self, item: ReferencedSetupImageSequenceItem):
        if not isinstance(item, ReferencedSetupImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSetupImageSequenceItem")
        self._ReferencedSetupImageSequence.append(item)
        if "ReferencedSetupImageSequence" not in self._dataset:
            self._dataset.ReferencedSetupImageSequence = pydicom.Sequence()
        self._dataset.ReferencedSetupImageSequence.append(item.to_dataset())

    @property
    def MotionSynchronizationSequence(self) -> Optional[List[MotionSynchronizationSequenceItem]]:
        if "MotionSynchronizationSequence" in self._dataset:
            if len(self._MotionSynchronizationSequence) == len(self._dataset.MotionSynchronizationSequence):
                return self._MotionSynchronizationSequence
            else:
                return [MotionSynchronizationSequenceItem(x) for x in self._dataset.MotionSynchronizationSequence]
        return None

    @MotionSynchronizationSequence.setter
    def MotionSynchronizationSequence(self, value: Optional[List[MotionSynchronizationSequenceItem]]):
        if value is None:
            self._MotionSynchronizationSequence = []
            if "MotionSynchronizationSequence" in self._dataset:
                del self._dataset.MotionSynchronizationSequence
        elif not isinstance(value, list) or not all(isinstance(item, MotionSynchronizationSequenceItem) for item in value):
            raise ValueError("MotionSynchronizationSequence must be a list of MotionSynchronizationSequenceItem objects")
        else:
            self._MotionSynchronizationSequence = value
            if "MotionSynchronizationSequence" not in self._dataset:
                self._dataset.MotionSynchronizationSequence = pydicom.Sequence()
            self._dataset.MotionSynchronizationSequence.clear()
            self._dataset.MotionSynchronizationSequence.extend([item.to_dataset() for item in value])

    def add_MotionSynchronization(self, item: MotionSynchronizationSequenceItem):
        if not isinstance(item, MotionSynchronizationSequenceItem):
            raise ValueError("Item must be an instance of MotionSynchronizationSequenceItem")
        self._MotionSynchronizationSequence.append(item)
        if "MotionSynchronizationSequence" not in self._dataset:
            self._dataset.MotionSynchronizationSequence = pydicom.Sequence()
        self._dataset.MotionSynchronizationSequence.append(item.to_dataset())
