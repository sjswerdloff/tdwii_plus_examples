from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .mydriatic_agent_sequence_item import MydriaticAgentSequenceItem
from .ophthalmic_axial_length_measurements_sequence_item import (
    OphthalmicAxialLengthMeasurementsSequenceItem,
)
from .optical_selected_ophthalmic_axial_length_sequence_item import (
    OpticalSelectedOphthalmicAxialLengthSequenceItem,
)
from .ultrasound_selected_ophthalmic_axial_length_sequence_item import (
    UltrasoundSelectedOphthalmicAxialLengthSequenceItem,
)


class OphthalmicAxialMeasurementsRightEyeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MydriaticAgentSequence: List[MydriaticAgentSequenceItem] = []
        self._LensStatusCodeSequence: List[CodeSequenceItem] = []
        self._VitreousStatusCodeSequence: List[CodeSequenceItem] = []
        self._OphthalmicAxialLengthMeasurementsSequence: List[OphthalmicAxialLengthMeasurementsSequenceItem] = []
        self._UltrasoundSelectedOphthalmicAxialLengthSequence: List[UltrasoundSelectedOphthalmicAxialLengthSequenceItem] = []
        self._OpticalSelectedOphthalmicAxialLengthSequence: List[OpticalSelectedOphthalmicAxialLengthSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PupilDilated(self) -> Optional[str]:
        if "PupilDilated" in self._dataset:
            return self._dataset.PupilDilated
        return None

    @PupilDilated.setter
    def PupilDilated(self, value: Optional[str]):
        if value is None:
            if "PupilDilated" in self._dataset:
                del self._dataset.PupilDilated
        else:
            self._dataset.PupilDilated = value

    @property
    def DegreeOfDilation(self) -> Optional[float]:
        if "DegreeOfDilation" in self._dataset:
            return self._dataset.DegreeOfDilation
        return None

    @DegreeOfDilation.setter
    def DegreeOfDilation(self, value: Optional[float]):
        if value is None:
            if "DegreeOfDilation" in self._dataset:
                del self._dataset.DegreeOfDilation
        else:
            self._dataset.DegreeOfDilation = value

    @property
    def MydriaticAgentSequence(self) -> Optional[List[MydriaticAgentSequenceItem]]:
        if "MydriaticAgentSequence" in self._dataset:
            if len(self._MydriaticAgentSequence) == len(self._dataset.MydriaticAgentSequence):
                return self._MydriaticAgentSequence
            else:
                return [MydriaticAgentSequenceItem(x) for x in self._dataset.MydriaticAgentSequence]
        return None

    @MydriaticAgentSequence.setter
    def MydriaticAgentSequence(self, value: Optional[List[MydriaticAgentSequenceItem]]):
        if value is None:
            self._MydriaticAgentSequence = []
            if "MydriaticAgentSequence" in self._dataset:
                del self._dataset.MydriaticAgentSequence
        elif not isinstance(value, list) or not all(isinstance(item, MydriaticAgentSequenceItem) for item in value):
            raise ValueError(f"MydriaticAgentSequence must be a list of MydriaticAgentSequenceItem objects")
        else:
            self._MydriaticAgentSequence = value
            if "MydriaticAgentSequence" not in self._dataset:
                self._dataset.MydriaticAgentSequence = pydicom.Sequence()
            self._dataset.MydriaticAgentSequence.clear()
            self._dataset.MydriaticAgentSequence.extend([item.to_dataset() for item in value])

    def add_MydriaticAgent(self, item: MydriaticAgentSequenceItem):
        if not isinstance(item, MydriaticAgentSequenceItem):
            raise ValueError(f"Item must be an instance of MydriaticAgentSequenceItem")
        self._MydriaticAgentSequence.append(item)
        if "MydriaticAgentSequence" not in self._dataset:
            self._dataset.MydriaticAgentSequence = pydicom.Sequence()
        self._dataset.MydriaticAgentSequence.append(item.to_dataset())

    @property
    def LensStatusCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "LensStatusCodeSequence" in self._dataset:
            if len(self._LensStatusCodeSequence) == len(self._dataset.LensStatusCodeSequence):
                return self._LensStatusCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.LensStatusCodeSequence]
        return None

    @LensStatusCodeSequence.setter
    def LensStatusCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._LensStatusCodeSequence = []
            if "LensStatusCodeSequence" in self._dataset:
                del self._dataset.LensStatusCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"LensStatusCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._LensStatusCodeSequence = value
            if "LensStatusCodeSequence" not in self._dataset:
                self._dataset.LensStatusCodeSequence = pydicom.Sequence()
            self._dataset.LensStatusCodeSequence.clear()
            self._dataset.LensStatusCodeSequence.extend([item.to_dataset() for item in value])

    def add_LensStatusCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._LensStatusCodeSequence.append(item)
        if "LensStatusCodeSequence" not in self._dataset:
            self._dataset.LensStatusCodeSequence = pydicom.Sequence()
        self._dataset.LensStatusCodeSequence.append(item.to_dataset())

    @property
    def VitreousStatusCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "VitreousStatusCodeSequence" in self._dataset:
            if len(self._VitreousStatusCodeSequence) == len(self._dataset.VitreousStatusCodeSequence):
                return self._VitreousStatusCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.VitreousStatusCodeSequence]
        return None

    @VitreousStatusCodeSequence.setter
    def VitreousStatusCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._VitreousStatusCodeSequence = []
            if "VitreousStatusCodeSequence" in self._dataset:
                del self._dataset.VitreousStatusCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"VitreousStatusCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._VitreousStatusCodeSequence = value
            if "VitreousStatusCodeSequence" not in self._dataset:
                self._dataset.VitreousStatusCodeSequence = pydicom.Sequence()
            self._dataset.VitreousStatusCodeSequence.clear()
            self._dataset.VitreousStatusCodeSequence.extend([item.to_dataset() for item in value])

    def add_VitreousStatusCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._VitreousStatusCodeSequence.append(item)
        if "VitreousStatusCodeSequence" not in self._dataset:
            self._dataset.VitreousStatusCodeSequence = pydicom.Sequence()
        self._dataset.VitreousStatusCodeSequence.append(item.to_dataset())

    @property
    def OphthalmicAxialLengthMeasurementsSequence(self) -> Optional[List[OphthalmicAxialLengthMeasurementsSequenceItem]]:
        if "OphthalmicAxialLengthMeasurementsSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthMeasurementsSequence) == len(
                self._dataset.OphthalmicAxialLengthMeasurementsSequence
            ):
                return self._OphthalmicAxialLengthMeasurementsSequence
            else:
                return [
                    OphthalmicAxialLengthMeasurementsSequenceItem(x)
                    for x in self._dataset.OphthalmicAxialLengthMeasurementsSequence
                ]
        return None

    @OphthalmicAxialLengthMeasurementsSequence.setter
    def OphthalmicAxialLengthMeasurementsSequence(self, value: Optional[List[OphthalmicAxialLengthMeasurementsSequenceItem]]):
        if value is None:
            self._OphthalmicAxialLengthMeasurementsSequence = []
            if "OphthalmicAxialLengthMeasurementsSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthMeasurementsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OphthalmicAxialLengthMeasurementsSequenceItem) for item in value
        ):
            raise ValueError(
                f"OphthalmicAxialLengthMeasurementsSequence must be a list of OphthalmicAxialLengthMeasurementsSequenceItem objects"
            )
        else:
            self._OphthalmicAxialLengthMeasurementsSequence = value
            if "OphthalmicAxialLengthMeasurementsSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthMeasurementsSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthMeasurementsSequence.clear()
            self._dataset.OphthalmicAxialLengthMeasurementsSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLengthMeasurements(self, item: OphthalmicAxialLengthMeasurementsSequenceItem):
        if not isinstance(item, OphthalmicAxialLengthMeasurementsSequenceItem):
            raise ValueError(f"Item must be an instance of OphthalmicAxialLengthMeasurementsSequenceItem")
        self._OphthalmicAxialLengthMeasurementsSequence.append(item)
        if "OphthalmicAxialLengthMeasurementsSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthMeasurementsSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthMeasurementsSequence.append(item.to_dataset())

    @property
    def LensStatusDescription(self) -> Optional[str]:
        if "LensStatusDescription" in self._dataset:
            return self._dataset.LensStatusDescription
        return None

    @LensStatusDescription.setter
    def LensStatusDescription(self, value: Optional[str]):
        if value is None:
            if "LensStatusDescription" in self._dataset:
                del self._dataset.LensStatusDescription
        else:
            self._dataset.LensStatusDescription = value

    @property
    def VitreousStatusDescription(self) -> Optional[str]:
        if "VitreousStatusDescription" in self._dataset:
            return self._dataset.VitreousStatusDescription
        return None

    @VitreousStatusDescription.setter
    def VitreousStatusDescription(self, value: Optional[str]):
        if value is None:
            if "VitreousStatusDescription" in self._dataset:
                del self._dataset.VitreousStatusDescription
        else:
            self._dataset.VitreousStatusDescription = value

    @property
    def UltrasoundSelectedOphthalmicAxialLengthSequence(
        self,
    ) -> Optional[List[UltrasoundSelectedOphthalmicAxialLengthSequenceItem]]:
        if "UltrasoundSelectedOphthalmicAxialLengthSequence" in self._dataset:
            if len(self._UltrasoundSelectedOphthalmicAxialLengthSequence) == len(
                self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence
            ):
                return self._UltrasoundSelectedOphthalmicAxialLengthSequence
            else:
                return [
                    UltrasoundSelectedOphthalmicAxialLengthSequenceItem(x)
                    for x in self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence
                ]
        return None

    @UltrasoundSelectedOphthalmicAxialLengthSequence.setter
    def UltrasoundSelectedOphthalmicAxialLengthSequence(
        self, value: Optional[List[UltrasoundSelectedOphthalmicAxialLengthSequenceItem]]
    ):
        if value is None:
            self._UltrasoundSelectedOphthalmicAxialLengthSequence = []
            if "UltrasoundSelectedOphthalmicAxialLengthSequence" in self._dataset:
                del self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, UltrasoundSelectedOphthalmicAxialLengthSequenceItem) for item in value
        ):
            raise ValueError(
                f"UltrasoundSelectedOphthalmicAxialLengthSequence must be a list of UltrasoundSelectedOphthalmicAxialLengthSequenceItem objects"
            )
        else:
            self._UltrasoundSelectedOphthalmicAxialLengthSequence = value
            if "UltrasoundSelectedOphthalmicAxialLengthSequence" not in self._dataset:
                self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence = pydicom.Sequence()
            self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence.clear()
            self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence.extend([item.to_dataset() for item in value])

    def add_UltrasoundSelectedOphthalmicAxialLength(self, item: UltrasoundSelectedOphthalmicAxialLengthSequenceItem):
        if not isinstance(item, UltrasoundSelectedOphthalmicAxialLengthSequenceItem):
            raise ValueError(f"Item must be an instance of UltrasoundSelectedOphthalmicAxialLengthSequenceItem")
        self._UltrasoundSelectedOphthalmicAxialLengthSequence.append(item)
        if "UltrasoundSelectedOphthalmicAxialLengthSequence" not in self._dataset:
            self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence = pydicom.Sequence()
        self._dataset.UltrasoundSelectedOphthalmicAxialLengthSequence.append(item.to_dataset())

    @property
    def OpticalSelectedOphthalmicAxialLengthSequence(self) -> Optional[List[OpticalSelectedOphthalmicAxialLengthSequenceItem]]:
        if "OpticalSelectedOphthalmicAxialLengthSequence" in self._dataset:
            if len(self._OpticalSelectedOphthalmicAxialLengthSequence) == len(
                self._dataset.OpticalSelectedOphthalmicAxialLengthSequence
            ):
                return self._OpticalSelectedOphthalmicAxialLengthSequence
            else:
                return [
                    OpticalSelectedOphthalmicAxialLengthSequenceItem(x)
                    for x in self._dataset.OpticalSelectedOphthalmicAxialLengthSequence
                ]
        return None

    @OpticalSelectedOphthalmicAxialLengthSequence.setter
    def OpticalSelectedOphthalmicAxialLengthSequence(
        self, value: Optional[List[OpticalSelectedOphthalmicAxialLengthSequenceItem]]
    ):
        if value is None:
            self._OpticalSelectedOphthalmicAxialLengthSequence = []
            if "OpticalSelectedOphthalmicAxialLengthSequence" in self._dataset:
                del self._dataset.OpticalSelectedOphthalmicAxialLengthSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OpticalSelectedOphthalmicAxialLengthSequenceItem) for item in value
        ):
            raise ValueError(
                f"OpticalSelectedOphthalmicAxialLengthSequence must be a list of OpticalSelectedOphthalmicAxialLengthSequenceItem objects"
            )
        else:
            self._OpticalSelectedOphthalmicAxialLengthSequence = value
            if "OpticalSelectedOphthalmicAxialLengthSequence" not in self._dataset:
                self._dataset.OpticalSelectedOphthalmicAxialLengthSequence = pydicom.Sequence()
            self._dataset.OpticalSelectedOphthalmicAxialLengthSequence.clear()
            self._dataset.OpticalSelectedOphthalmicAxialLengthSequence.extend([item.to_dataset() for item in value])

    def add_OpticalSelectedOphthalmicAxialLength(self, item: OpticalSelectedOphthalmicAxialLengthSequenceItem):
        if not isinstance(item, OpticalSelectedOphthalmicAxialLengthSequenceItem):
            raise ValueError(f"Item must be an instance of OpticalSelectedOphthalmicAxialLengthSequenceItem")
        self._OpticalSelectedOphthalmicAxialLengthSequence.append(item)
        if "OpticalSelectedOphthalmicAxialLengthSequence" not in self._dataset:
            self._dataset.OpticalSelectedOphthalmicAxialLengthSequence = pydicom.Sequence()
        self._dataset.OpticalSelectedOphthalmicAxialLengthSequence.append(item.to_dataset())
