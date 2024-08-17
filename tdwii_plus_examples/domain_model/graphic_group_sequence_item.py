from typing import Any, List, Optional  # noqa

import pydicom


class GraphicGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def GraphicGroupLabel(self) -> Optional[str]:
        if "GraphicGroupLabel" in self._dataset:
            return self._dataset.GraphicGroupLabel
        return None

    @GraphicGroupLabel.setter
    def GraphicGroupLabel(self, value: Optional[str]):
        if value is None:
            if "GraphicGroupLabel" in self._dataset:
                del self._dataset.GraphicGroupLabel
        else:
            self._dataset.GraphicGroupLabel = value

    @property
    def GraphicGroupDescription(self) -> Optional[str]:
        if "GraphicGroupDescription" in self._dataset:
            return self._dataset.GraphicGroupDescription
        return None

    @GraphicGroupDescription.setter
    def GraphicGroupDescription(self, value: Optional[str]):
        if value is None:
            if "GraphicGroupDescription" in self._dataset:
                del self._dataset.GraphicGroupDescription
        else:
            self._dataset.GraphicGroupDescription = value

    @property
    def GraphicGroupID(self) -> Optional[int]:
        if "GraphicGroupID" in self._dataset:
            return self._dataset.GraphicGroupID
        return None

    @GraphicGroupID.setter
    def GraphicGroupID(self, value: Optional[int]):
        if value is None:
            if "GraphicGroupID" in self._dataset:
                del self._dataset.GraphicGroupID
        else:
            self._dataset.GraphicGroupID = value
