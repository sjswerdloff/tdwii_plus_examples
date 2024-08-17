from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .measurements_sequence_item import MeasurementsSequenceItem
from .track_sequence_item import TrackSequenceItem
from .track_set_statistics_sequence_item import TrackSetStatisticsSequenceItem
from .track_statistics_sequence_item import TrackStatisticsSequenceItem
from .tracking_algorithm_identification_sequence_item import (
    TrackingAlgorithmIdentificationSequenceItem,
)


class TrackSetSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TrackSequence: List[TrackSequenceItem] = []
        self._TrackingAlgorithmIdentificationSequence: List[TrackingAlgorithmIdentificationSequenceItem] = []
        self._TrackSetAnatomicalTypeCodeSequence: List[CodeSequenceItem] = []
        self._MeasurementsSequence: List[MeasurementsSequenceItem] = []
        self._TrackSetStatisticsSequence: List[TrackSetStatisticsSequenceItem] = []
        self._TrackStatisticsSequence: List[TrackStatisticsSequenceItem] = []
        self._DiffusionAcquisitionCodeSequence: List[CodeSequenceItem] = []
        self._DiffusionModelCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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

    @property
    def TrackSequence(self) -> Optional[List[TrackSequenceItem]]:
        if "TrackSequence" in self._dataset:
            if len(self._TrackSequence) == len(self._dataset.TrackSequence):
                return self._TrackSequence
            else:
                return [TrackSequenceItem(x) for x in self._dataset.TrackSequence]
        return None

    @TrackSequence.setter
    def TrackSequence(self, value: Optional[List[TrackSequenceItem]]):
        if value is None:
            self._TrackSequence = []
            if "TrackSequence" in self._dataset:
                del self._dataset.TrackSequence
        elif not isinstance(value, list) or not all(isinstance(item, TrackSequenceItem) for item in value):
            raise ValueError(f"TrackSequence must be a list of TrackSequenceItem objects")
        else:
            self._TrackSequence = value
            if "TrackSequence" not in self._dataset:
                self._dataset.TrackSequence = pydicom.Sequence()
            self._dataset.TrackSequence.clear()
            self._dataset.TrackSequence.extend([item.to_dataset() for item in value])

    def add_Track(self, item: TrackSequenceItem):
        if not isinstance(item, TrackSequenceItem):
            raise ValueError(f"Item must be an instance of TrackSequenceItem")
        self._TrackSequence.append(item)
        if "TrackSequence" not in self._dataset:
            self._dataset.TrackSequence = pydicom.Sequence()
        self._dataset.TrackSequence.append(item.to_dataset())

    @property
    def TrackingAlgorithmIdentificationSequence(self) -> Optional[List[TrackingAlgorithmIdentificationSequenceItem]]:
        if "TrackingAlgorithmIdentificationSequence" in self._dataset:
            if len(self._TrackingAlgorithmIdentificationSequence) == len(
                self._dataset.TrackingAlgorithmIdentificationSequence
            ):
                return self._TrackingAlgorithmIdentificationSequence
            else:
                return [
                    TrackingAlgorithmIdentificationSequenceItem(x)
                    for x in self._dataset.TrackingAlgorithmIdentificationSequence
                ]
        return None

    @TrackingAlgorithmIdentificationSequence.setter
    def TrackingAlgorithmIdentificationSequence(self, value: Optional[List[TrackingAlgorithmIdentificationSequenceItem]]):
        if value is None:
            self._TrackingAlgorithmIdentificationSequence = []
            if "TrackingAlgorithmIdentificationSequence" in self._dataset:
                del self._dataset.TrackingAlgorithmIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, TrackingAlgorithmIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"TrackingAlgorithmIdentificationSequence must be a list of TrackingAlgorithmIdentificationSequenceItem objects"
            )
        else:
            self._TrackingAlgorithmIdentificationSequence = value
            if "TrackingAlgorithmIdentificationSequence" not in self._dataset:
                self._dataset.TrackingAlgorithmIdentificationSequence = pydicom.Sequence()
            self._dataset.TrackingAlgorithmIdentificationSequence.clear()
            self._dataset.TrackingAlgorithmIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_TrackingAlgorithmIdentification(self, item: TrackingAlgorithmIdentificationSequenceItem):
        if not isinstance(item, TrackingAlgorithmIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of TrackingAlgorithmIdentificationSequenceItem")
        self._TrackingAlgorithmIdentificationSequence.append(item)
        if "TrackingAlgorithmIdentificationSequence" not in self._dataset:
            self._dataset.TrackingAlgorithmIdentificationSequence = pydicom.Sequence()
        self._dataset.TrackingAlgorithmIdentificationSequence.append(item.to_dataset())

    @property
    def TrackSetNumber(self) -> Optional[int]:
        if "TrackSetNumber" in self._dataset:
            return self._dataset.TrackSetNumber
        return None

    @TrackSetNumber.setter
    def TrackSetNumber(self, value: Optional[int]):
        if value is None:
            if "TrackSetNumber" in self._dataset:
                del self._dataset.TrackSetNumber
        else:
            self._dataset.TrackSetNumber = value

    @property
    def TrackSetLabel(self) -> Optional[str]:
        if "TrackSetLabel" in self._dataset:
            return self._dataset.TrackSetLabel
        return None

    @TrackSetLabel.setter
    def TrackSetLabel(self, value: Optional[str]):
        if value is None:
            if "TrackSetLabel" in self._dataset:
                del self._dataset.TrackSetLabel
        else:
            self._dataset.TrackSetLabel = value

    @property
    def TrackSetDescription(self) -> Optional[str]:
        if "TrackSetDescription" in self._dataset:
            return self._dataset.TrackSetDescription
        return None

    @TrackSetDescription.setter
    def TrackSetDescription(self, value: Optional[str]):
        if value is None:
            if "TrackSetDescription" in self._dataset:
                del self._dataset.TrackSetDescription
        else:
            self._dataset.TrackSetDescription = value

    @property
    def TrackSetAnatomicalTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "TrackSetAnatomicalTypeCodeSequence" in self._dataset:
            if len(self._TrackSetAnatomicalTypeCodeSequence) == len(self._dataset.TrackSetAnatomicalTypeCodeSequence):
                return self._TrackSetAnatomicalTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.TrackSetAnatomicalTypeCodeSequence]
        return None

    @TrackSetAnatomicalTypeCodeSequence.setter
    def TrackSetAnatomicalTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._TrackSetAnatomicalTypeCodeSequence = []
            if "TrackSetAnatomicalTypeCodeSequence" in self._dataset:
                del self._dataset.TrackSetAnatomicalTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"TrackSetAnatomicalTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TrackSetAnatomicalTypeCodeSequence = value
            if "TrackSetAnatomicalTypeCodeSequence" not in self._dataset:
                self._dataset.TrackSetAnatomicalTypeCodeSequence = pydicom.Sequence()
            self._dataset.TrackSetAnatomicalTypeCodeSequence.clear()
            self._dataset.TrackSetAnatomicalTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_TrackSetAnatomicalTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._TrackSetAnatomicalTypeCodeSequence.append(item)
        if "TrackSetAnatomicalTypeCodeSequence" not in self._dataset:
            self._dataset.TrackSetAnatomicalTypeCodeSequence = pydicom.Sequence()
        self._dataset.TrackSetAnatomicalTypeCodeSequence.append(item.to_dataset())

    @property
    def MeasurementsSequence(self) -> Optional[List[MeasurementsSequenceItem]]:
        if "MeasurementsSequence" in self._dataset:
            if len(self._MeasurementsSequence) == len(self._dataset.MeasurementsSequence):
                return self._MeasurementsSequence
            else:
                return [MeasurementsSequenceItem(x) for x in self._dataset.MeasurementsSequence]
        return None

    @MeasurementsSequence.setter
    def MeasurementsSequence(self, value: Optional[List[MeasurementsSequenceItem]]):
        if value is None:
            self._MeasurementsSequence = []
            if "MeasurementsSequence" in self._dataset:
                del self._dataset.MeasurementsSequence
        elif not isinstance(value, list) or not all(isinstance(item, MeasurementsSequenceItem) for item in value):
            raise ValueError(f"MeasurementsSequence must be a list of MeasurementsSequenceItem objects")
        else:
            self._MeasurementsSequence = value
            if "MeasurementsSequence" not in self._dataset:
                self._dataset.MeasurementsSequence = pydicom.Sequence()
            self._dataset.MeasurementsSequence.clear()
            self._dataset.MeasurementsSequence.extend([item.to_dataset() for item in value])

    def add_Measurements(self, item: MeasurementsSequenceItem):
        if not isinstance(item, MeasurementsSequenceItem):
            raise ValueError(f"Item must be an instance of MeasurementsSequenceItem")
        self._MeasurementsSequence.append(item)
        if "MeasurementsSequence" not in self._dataset:
            self._dataset.MeasurementsSequence = pydicom.Sequence()
        self._dataset.MeasurementsSequence.append(item.to_dataset())

    @property
    def TrackSetStatisticsSequence(self) -> Optional[List[TrackSetStatisticsSequenceItem]]:
        if "TrackSetStatisticsSequence" in self._dataset:
            if len(self._TrackSetStatisticsSequence) == len(self._dataset.TrackSetStatisticsSequence):
                return self._TrackSetStatisticsSequence
            else:
                return [TrackSetStatisticsSequenceItem(x) for x in self._dataset.TrackSetStatisticsSequence]
        return None

    @TrackSetStatisticsSequence.setter
    def TrackSetStatisticsSequence(self, value: Optional[List[TrackSetStatisticsSequenceItem]]):
        if value is None:
            self._TrackSetStatisticsSequence = []
            if "TrackSetStatisticsSequence" in self._dataset:
                del self._dataset.TrackSetStatisticsSequence
        elif not isinstance(value, list) or not all(isinstance(item, TrackSetStatisticsSequenceItem) for item in value):
            raise ValueError(f"TrackSetStatisticsSequence must be a list of TrackSetStatisticsSequenceItem objects")
        else:
            self._TrackSetStatisticsSequence = value
            if "TrackSetStatisticsSequence" not in self._dataset:
                self._dataset.TrackSetStatisticsSequence = pydicom.Sequence()
            self._dataset.TrackSetStatisticsSequence.clear()
            self._dataset.TrackSetStatisticsSequence.extend([item.to_dataset() for item in value])

    def add_TrackSetStatistics(self, item: TrackSetStatisticsSequenceItem):
        if not isinstance(item, TrackSetStatisticsSequenceItem):
            raise ValueError(f"Item must be an instance of TrackSetStatisticsSequenceItem")
        self._TrackSetStatisticsSequence.append(item)
        if "TrackSetStatisticsSequence" not in self._dataset:
            self._dataset.TrackSetStatisticsSequence = pydicom.Sequence()
        self._dataset.TrackSetStatisticsSequence.append(item.to_dataset())

    @property
    def TrackStatisticsSequence(self) -> Optional[List[TrackStatisticsSequenceItem]]:
        if "TrackStatisticsSequence" in self._dataset:
            if len(self._TrackStatisticsSequence) == len(self._dataset.TrackStatisticsSequence):
                return self._TrackStatisticsSequence
            else:
                return [TrackStatisticsSequenceItem(x) for x in self._dataset.TrackStatisticsSequence]
        return None

    @TrackStatisticsSequence.setter
    def TrackStatisticsSequence(self, value: Optional[List[TrackStatisticsSequenceItem]]):
        if value is None:
            self._TrackStatisticsSequence = []
            if "TrackStatisticsSequence" in self._dataset:
                del self._dataset.TrackStatisticsSequence
        elif not isinstance(value, list) or not all(isinstance(item, TrackStatisticsSequenceItem) for item in value):
            raise ValueError(f"TrackStatisticsSequence must be a list of TrackStatisticsSequenceItem objects")
        else:
            self._TrackStatisticsSequence = value
            if "TrackStatisticsSequence" not in self._dataset:
                self._dataset.TrackStatisticsSequence = pydicom.Sequence()
            self._dataset.TrackStatisticsSequence.clear()
            self._dataset.TrackStatisticsSequence.extend([item.to_dataset() for item in value])

    def add_TrackStatistics(self, item: TrackStatisticsSequenceItem):
        if not isinstance(item, TrackStatisticsSequenceItem):
            raise ValueError(f"Item must be an instance of TrackStatisticsSequenceItem")
        self._TrackStatisticsSequence.append(item)
        if "TrackStatisticsSequence" not in self._dataset:
            self._dataset.TrackStatisticsSequence = pydicom.Sequence()
        self._dataset.TrackStatisticsSequence.append(item.to_dataset())

    @property
    def DiffusionAcquisitionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DiffusionAcquisitionCodeSequence" in self._dataset:
            if len(self._DiffusionAcquisitionCodeSequence) == len(self._dataset.DiffusionAcquisitionCodeSequence):
                return self._DiffusionAcquisitionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DiffusionAcquisitionCodeSequence]
        return None

    @DiffusionAcquisitionCodeSequence.setter
    def DiffusionAcquisitionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DiffusionAcquisitionCodeSequence = []
            if "DiffusionAcquisitionCodeSequence" in self._dataset:
                del self._dataset.DiffusionAcquisitionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DiffusionAcquisitionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DiffusionAcquisitionCodeSequence = value
            if "DiffusionAcquisitionCodeSequence" not in self._dataset:
                self._dataset.DiffusionAcquisitionCodeSequence = pydicom.Sequence()
            self._dataset.DiffusionAcquisitionCodeSequence.clear()
            self._dataset.DiffusionAcquisitionCodeSequence.extend([item.to_dataset() for item in value])

    def add_DiffusionAcquisitionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DiffusionAcquisitionCodeSequence.append(item)
        if "DiffusionAcquisitionCodeSequence" not in self._dataset:
            self._dataset.DiffusionAcquisitionCodeSequence = pydicom.Sequence()
        self._dataset.DiffusionAcquisitionCodeSequence.append(item.to_dataset())

    @property
    def DiffusionModelCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DiffusionModelCodeSequence" in self._dataset:
            if len(self._DiffusionModelCodeSequence) == len(self._dataset.DiffusionModelCodeSequence):
                return self._DiffusionModelCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DiffusionModelCodeSequence]
        return None

    @DiffusionModelCodeSequence.setter
    def DiffusionModelCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DiffusionModelCodeSequence = []
            if "DiffusionModelCodeSequence" in self._dataset:
                del self._dataset.DiffusionModelCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DiffusionModelCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DiffusionModelCodeSequence = value
            if "DiffusionModelCodeSequence" not in self._dataset:
                self._dataset.DiffusionModelCodeSequence = pydicom.Sequence()
            self._dataset.DiffusionModelCodeSequence.clear()
            self._dataset.DiffusionModelCodeSequence.extend([item.to_dataset() for item in value])

    def add_DiffusionModelCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DiffusionModelCodeSequence.append(item)
        if "DiffusionModelCodeSequence" not in self._dataset:
            self._dataset.DiffusionModelCodeSequence = pydicom.Sequence()
        self._dataset.DiffusionModelCodeSequence.append(item.to_dataset())
