from typing import Any, List, Optional

import pydicom


class TrackSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

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
    def PointCoordinatesData(self) -> Optional[bytes]:
        if "PointCoordinatesData" in self._dataset:
            return self._dataset.PointCoordinatesData
        return None

    @PointCoordinatesData.setter
    def PointCoordinatesData(self, value: Optional[bytes]):
        if value is None:
            if "PointCoordinatesData" in self._dataset:
                del self._dataset.PointCoordinatesData
        else:
            self._dataset.PointCoordinatesData = value

    @property
    def RecommendedDisplayCIELabValueList(self) -> Optional[bytes]:
        if "RecommendedDisplayCIELabValueList" in self._dataset:
            return self._dataset.RecommendedDisplayCIELabValueList
        return None

    @RecommendedDisplayCIELabValueList.setter
    def RecommendedDisplayCIELabValueList(self, value: Optional[bytes]):
        if value is None:
            if "RecommendedDisplayCIELabValueList" in self._dataset:
                del self._dataset.RecommendedDisplayCIELabValueList
        else:
            self._dataset.RecommendedDisplayCIELabValueList = value
