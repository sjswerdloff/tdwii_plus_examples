from typing import Any, List, Optional

import pydicom

from .ct_acquisition_details_sequence_item import CTAcquisitionDetailsSequenceItem
from .ct_exposure_sequence_item import CTExposureSequenceItem
from .ct_geometry_sequence_item import CTGeometrySequenceItem
from .ctx_ray_details_sequence_item import CTXRayDetailsSequenceItem
from .multienergy_ct_path_sequence_item import MultienergyCTPathSequenceItem
from .multienergy_ctx_ray_detector_sequence_item import (
    MultienergyCTXRayDetectorSequenceItem,
)
from .multienergy_ctx_ray_source_sequence_item import (
    MultienergyCTXRaySourceSequenceItem,
)


class MultienergyCTAcquisitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._CTAcquisitionDetailsSequence: List[CTAcquisitionDetailsSequenceItem] = []
        self._CTGeometrySequence: List[CTGeometrySequenceItem] = []
        self._CTExposureSequence: List[CTExposureSequenceItem] = []
        self._CTXRayDetailsSequence: List[CTXRayDetailsSequenceItem] = []
        self._MultienergyCTXRaySourceSequence: List[MultienergyCTXRaySourceSequenceItem] = []
        self._MultienergyCTXRayDetectorSequence: List[MultienergyCTXRayDetectorSequenceItem] = []
        self._MultienergyCTPathSequence: List[MultienergyCTPathSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CTAcquisitionDetailsSequence(self) -> Optional[List[CTAcquisitionDetailsSequenceItem]]:
        if "CTAcquisitionDetailsSequence" in self._dataset:
            if len(self._CTAcquisitionDetailsSequence) == len(self._dataset.CTAcquisitionDetailsSequence):
                return self._CTAcquisitionDetailsSequence
            else:
                return [CTAcquisitionDetailsSequenceItem(x) for x in self._dataset.CTAcquisitionDetailsSequence]
        return None

    @CTAcquisitionDetailsSequence.setter
    def CTAcquisitionDetailsSequence(self, value: Optional[List[CTAcquisitionDetailsSequenceItem]]):
        if value is None:
            self._CTAcquisitionDetailsSequence = []
            if "CTAcquisitionDetailsSequence" in self._dataset:
                del self._dataset.CTAcquisitionDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTAcquisitionDetailsSequenceItem) for item in value):
            raise ValueError(f"CTAcquisitionDetailsSequence must be a list of CTAcquisitionDetailsSequenceItem objects")
        else:
            self._CTAcquisitionDetailsSequence = value
            if "CTAcquisitionDetailsSequence" not in self._dataset:
                self._dataset.CTAcquisitionDetailsSequence = pydicom.Sequence()
            self._dataset.CTAcquisitionDetailsSequence.clear()
            self._dataset.CTAcquisitionDetailsSequence.extend([item.to_dataset() for item in value])

    def add_CTAcquisitionDetails(self, item: CTAcquisitionDetailsSequenceItem):
        if not isinstance(item, CTAcquisitionDetailsSequenceItem):
            raise ValueError(f"Item must be an instance of CTAcquisitionDetailsSequenceItem")
        self._CTAcquisitionDetailsSequence.append(item)
        if "CTAcquisitionDetailsSequence" not in self._dataset:
            self._dataset.CTAcquisitionDetailsSequence = pydicom.Sequence()
        self._dataset.CTAcquisitionDetailsSequence.append(item.to_dataset())

    @property
    def CTGeometrySequence(self) -> Optional[List[CTGeometrySequenceItem]]:
        if "CTGeometrySequence" in self._dataset:
            if len(self._CTGeometrySequence) == len(self._dataset.CTGeometrySequence):
                return self._CTGeometrySequence
            else:
                return [CTGeometrySequenceItem(x) for x in self._dataset.CTGeometrySequence]
        return None

    @CTGeometrySequence.setter
    def CTGeometrySequence(self, value: Optional[List[CTGeometrySequenceItem]]):
        if value is None:
            self._CTGeometrySequence = []
            if "CTGeometrySequence" in self._dataset:
                del self._dataset.CTGeometrySequence
        elif not isinstance(value, list) or not all(isinstance(item, CTGeometrySequenceItem) for item in value):
            raise ValueError(f"CTGeometrySequence must be a list of CTGeometrySequenceItem objects")
        else:
            self._CTGeometrySequence = value
            if "CTGeometrySequence" not in self._dataset:
                self._dataset.CTGeometrySequence = pydicom.Sequence()
            self._dataset.CTGeometrySequence.clear()
            self._dataset.CTGeometrySequence.extend([item.to_dataset() for item in value])

    def add_CTGeometry(self, item: CTGeometrySequenceItem):
        if not isinstance(item, CTGeometrySequenceItem):
            raise ValueError(f"Item must be an instance of CTGeometrySequenceItem")
        self._CTGeometrySequence.append(item)
        if "CTGeometrySequence" not in self._dataset:
            self._dataset.CTGeometrySequence = pydicom.Sequence()
        self._dataset.CTGeometrySequence.append(item.to_dataset())

    @property
    def CTExposureSequence(self) -> Optional[List[CTExposureSequenceItem]]:
        if "CTExposureSequence" in self._dataset:
            if len(self._CTExposureSequence) == len(self._dataset.CTExposureSequence):
                return self._CTExposureSequence
            else:
                return [CTExposureSequenceItem(x) for x in self._dataset.CTExposureSequence]
        return None

    @CTExposureSequence.setter
    def CTExposureSequence(self, value: Optional[List[CTExposureSequenceItem]]):
        if value is None:
            self._CTExposureSequence = []
            if "CTExposureSequence" in self._dataset:
                del self._dataset.CTExposureSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTExposureSequenceItem) for item in value):
            raise ValueError(f"CTExposureSequence must be a list of CTExposureSequenceItem objects")
        else:
            self._CTExposureSequence = value
            if "CTExposureSequence" not in self._dataset:
                self._dataset.CTExposureSequence = pydicom.Sequence()
            self._dataset.CTExposureSequence.clear()
            self._dataset.CTExposureSequence.extend([item.to_dataset() for item in value])

    def add_CTExposure(self, item: CTExposureSequenceItem):
        if not isinstance(item, CTExposureSequenceItem):
            raise ValueError(f"Item must be an instance of CTExposureSequenceItem")
        self._CTExposureSequence.append(item)
        if "CTExposureSequence" not in self._dataset:
            self._dataset.CTExposureSequence = pydicom.Sequence()
        self._dataset.CTExposureSequence.append(item.to_dataset())

    @property
    def CTXRayDetailsSequence(self) -> Optional[List[CTXRayDetailsSequenceItem]]:
        if "CTXRayDetailsSequence" in self._dataset:
            if len(self._CTXRayDetailsSequence) == len(self._dataset.CTXRayDetailsSequence):
                return self._CTXRayDetailsSequence
            else:
                return [CTXRayDetailsSequenceItem(x) for x in self._dataset.CTXRayDetailsSequence]
        return None

    @CTXRayDetailsSequence.setter
    def CTXRayDetailsSequence(self, value: Optional[List[CTXRayDetailsSequenceItem]]):
        if value is None:
            self._CTXRayDetailsSequence = []
            if "CTXRayDetailsSequence" in self._dataset:
                del self._dataset.CTXRayDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTXRayDetailsSequenceItem) for item in value):
            raise ValueError(f"CTXRayDetailsSequence must be a list of CTXRayDetailsSequenceItem objects")
        else:
            self._CTXRayDetailsSequence = value
            if "CTXRayDetailsSequence" not in self._dataset:
                self._dataset.CTXRayDetailsSequence = pydicom.Sequence()
            self._dataset.CTXRayDetailsSequence.clear()
            self._dataset.CTXRayDetailsSequence.extend([item.to_dataset() for item in value])

    def add_CTXRayDetails(self, item: CTXRayDetailsSequenceItem):
        if not isinstance(item, CTXRayDetailsSequenceItem):
            raise ValueError(f"Item must be an instance of CTXRayDetailsSequenceItem")
        self._CTXRayDetailsSequence.append(item)
        if "CTXRayDetailsSequence" not in self._dataset:
            self._dataset.CTXRayDetailsSequence = pydicom.Sequence()
        self._dataset.CTXRayDetailsSequence.append(item.to_dataset())

    @property
    def MultienergyCTXRaySourceSequence(self) -> Optional[List[MultienergyCTXRaySourceSequenceItem]]:
        if "MultienergyCTXRaySourceSequence" in self._dataset:
            if len(self._MultienergyCTXRaySourceSequence) == len(self._dataset.MultienergyCTXRaySourceSequence):
                return self._MultienergyCTXRaySourceSequence
            else:
                return [MultienergyCTXRaySourceSequenceItem(x) for x in self._dataset.MultienergyCTXRaySourceSequence]
        return None

    @MultienergyCTXRaySourceSequence.setter
    def MultienergyCTXRaySourceSequence(self, value: Optional[List[MultienergyCTXRaySourceSequenceItem]]):
        if value is None:
            self._MultienergyCTXRaySourceSequence = []
            if "MultienergyCTXRaySourceSequence" in self._dataset:
                del self._dataset.MultienergyCTXRaySourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, MultienergyCTXRaySourceSequenceItem) for item in value):
            raise ValueError(f"MultienergyCTXRaySourceSequence must be a list of MultienergyCTXRaySourceSequenceItem objects")
        else:
            self._MultienergyCTXRaySourceSequence = value
            if "MultienergyCTXRaySourceSequence" not in self._dataset:
                self._dataset.MultienergyCTXRaySourceSequence = pydicom.Sequence()
            self._dataset.MultienergyCTXRaySourceSequence.clear()
            self._dataset.MultienergyCTXRaySourceSequence.extend([item.to_dataset() for item in value])

    def add_MultienergyCTXRaySource(self, item: MultienergyCTXRaySourceSequenceItem):
        if not isinstance(item, MultienergyCTXRaySourceSequenceItem):
            raise ValueError(f"Item must be an instance of MultienergyCTXRaySourceSequenceItem")
        self._MultienergyCTXRaySourceSequence.append(item)
        if "MultienergyCTXRaySourceSequence" not in self._dataset:
            self._dataset.MultienergyCTXRaySourceSequence = pydicom.Sequence()
        self._dataset.MultienergyCTXRaySourceSequence.append(item.to_dataset())

    @property
    def MultienergyCTXRayDetectorSequence(self) -> Optional[List[MultienergyCTXRayDetectorSequenceItem]]:
        if "MultienergyCTXRayDetectorSequence" in self._dataset:
            if len(self._MultienergyCTXRayDetectorSequence) == len(self._dataset.MultienergyCTXRayDetectorSequence):
                return self._MultienergyCTXRayDetectorSequence
            else:
                return [MultienergyCTXRayDetectorSequenceItem(x) for x in self._dataset.MultienergyCTXRayDetectorSequence]
        return None

    @MultienergyCTXRayDetectorSequence.setter
    def MultienergyCTXRayDetectorSequence(self, value: Optional[List[MultienergyCTXRayDetectorSequenceItem]]):
        if value is None:
            self._MultienergyCTXRayDetectorSequence = []
            if "MultienergyCTXRayDetectorSequence" in self._dataset:
                del self._dataset.MultienergyCTXRayDetectorSequence
        elif not isinstance(value, list) or not all(isinstance(item, MultienergyCTXRayDetectorSequenceItem) for item in value):
            raise ValueError(
                f"MultienergyCTXRayDetectorSequence must be a list of MultienergyCTXRayDetectorSequenceItem objects"
            )
        else:
            self._MultienergyCTXRayDetectorSequence = value
            if "MultienergyCTXRayDetectorSequence" not in self._dataset:
                self._dataset.MultienergyCTXRayDetectorSequence = pydicom.Sequence()
            self._dataset.MultienergyCTXRayDetectorSequence.clear()
            self._dataset.MultienergyCTXRayDetectorSequence.extend([item.to_dataset() for item in value])

    def add_MultienergyCTXRayDetector(self, item: MultienergyCTXRayDetectorSequenceItem):
        if not isinstance(item, MultienergyCTXRayDetectorSequenceItem):
            raise ValueError(f"Item must be an instance of MultienergyCTXRayDetectorSequenceItem")
        self._MultienergyCTXRayDetectorSequence.append(item)
        if "MultienergyCTXRayDetectorSequence" not in self._dataset:
            self._dataset.MultienergyCTXRayDetectorSequence = pydicom.Sequence()
        self._dataset.MultienergyCTXRayDetectorSequence.append(item.to_dataset())

    @property
    def MultienergyCTPathSequence(self) -> Optional[List[MultienergyCTPathSequenceItem]]:
        if "MultienergyCTPathSequence" in self._dataset:
            if len(self._MultienergyCTPathSequence) == len(self._dataset.MultienergyCTPathSequence):
                return self._MultienergyCTPathSequence
            else:
                return [MultienergyCTPathSequenceItem(x) for x in self._dataset.MultienergyCTPathSequence]
        return None

    @MultienergyCTPathSequence.setter
    def MultienergyCTPathSequence(self, value: Optional[List[MultienergyCTPathSequenceItem]]):
        if value is None:
            self._MultienergyCTPathSequence = []
            if "MultienergyCTPathSequence" in self._dataset:
                del self._dataset.MultienergyCTPathSequence
        elif not isinstance(value, list) or not all(isinstance(item, MultienergyCTPathSequenceItem) for item in value):
            raise ValueError(f"MultienergyCTPathSequence must be a list of MultienergyCTPathSequenceItem objects")
        else:
            self._MultienergyCTPathSequence = value
            if "MultienergyCTPathSequence" not in self._dataset:
                self._dataset.MultienergyCTPathSequence = pydicom.Sequence()
            self._dataset.MultienergyCTPathSequence.clear()
            self._dataset.MultienergyCTPathSequence.extend([item.to_dataset() for item in value])

    def add_MultienergyCTPath(self, item: MultienergyCTPathSequenceItem):
        if not isinstance(item, MultienergyCTPathSequenceItem):
            raise ValueError(f"Item must be an instance of MultienergyCTPathSequenceItem")
        self._MultienergyCTPathSequence.append(item)
        if "MultienergyCTPathSequence" not in self._dataset:
            self._dataset.MultienergyCTPathSequence = pydicom.Sequence()
        self._dataset.MultienergyCTPathSequence.append(item.to_dataset())

    @property
    def MultienergyAcquisitionDescription(self) -> Optional[str]:
        if "MultienergyAcquisitionDescription" in self._dataset:
            return self._dataset.MultienergyAcquisitionDescription
        return None

    @MultienergyAcquisitionDescription.setter
    def MultienergyAcquisitionDescription(self, value: Optional[str]):
        if value is None:
            if "MultienergyAcquisitionDescription" in self._dataset:
                del self._dataset.MultienergyAcquisitionDescription
        else:
            self._dataset.MultienergyAcquisitionDescription = value
