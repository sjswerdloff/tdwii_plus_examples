from typing import Any, List, Optional

import pydicom


class DimensionIndexSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DimensionOrganizationUID(self) -> Optional[str]:
        if "DimensionOrganizationUID" in self._dataset:
            return self._dataset.DimensionOrganizationUID
        return None

    @DimensionOrganizationUID.setter
    def DimensionOrganizationUID(self, value: Optional[str]):
        if value is None:
            if "DimensionOrganizationUID" in self._dataset:
                del self._dataset.DimensionOrganizationUID
        else:
            self._dataset.DimensionOrganizationUID = value

    @property
    def DimensionIndexPointer(self) -> Optional[int]:
        if "DimensionIndexPointer" in self._dataset:
            return self._dataset.DimensionIndexPointer
        return None

    @DimensionIndexPointer.setter
    def DimensionIndexPointer(self, value: Optional[int]):
        if value is None:
            if "DimensionIndexPointer" in self._dataset:
                del self._dataset.DimensionIndexPointer
        else:
            self._dataset.DimensionIndexPointer = value

    @property
    def FunctionalGroupPointer(self) -> Optional[int]:
        if "FunctionalGroupPointer" in self._dataset:
            return self._dataset.FunctionalGroupPointer
        return None

    @FunctionalGroupPointer.setter
    def FunctionalGroupPointer(self, value: Optional[int]):
        if value is None:
            if "FunctionalGroupPointer" in self._dataset:
                del self._dataset.FunctionalGroupPointer
        else:
            self._dataset.FunctionalGroupPointer = value

    @property
    def DimensionIndexPrivateCreator(self) -> Optional[str]:
        if "DimensionIndexPrivateCreator" in self._dataset:
            return self._dataset.DimensionIndexPrivateCreator
        return None

    @DimensionIndexPrivateCreator.setter
    def DimensionIndexPrivateCreator(self, value: Optional[str]):
        if value is None:
            if "DimensionIndexPrivateCreator" in self._dataset:
                del self._dataset.DimensionIndexPrivateCreator
        else:
            self._dataset.DimensionIndexPrivateCreator = value

    @property
    def FunctionalGroupPrivateCreator(self) -> Optional[str]:
        if "FunctionalGroupPrivateCreator" in self._dataset:
            return self._dataset.FunctionalGroupPrivateCreator
        return None

    @FunctionalGroupPrivateCreator.setter
    def FunctionalGroupPrivateCreator(self, value: Optional[str]):
        if value is None:
            if "FunctionalGroupPrivateCreator" in self._dataset:
                del self._dataset.FunctionalGroupPrivateCreator
        else:
            self._dataset.FunctionalGroupPrivateCreator = value

    @property
    def DimensionDescriptionLabel(self) -> Optional[str]:
        if "DimensionDescriptionLabel" in self._dataset:
            return self._dataset.DimensionDescriptionLabel
        return None

    @DimensionDescriptionLabel.setter
    def DimensionDescriptionLabel(self, value: Optional[str]):
        if value is None:
            if "DimensionDescriptionLabel" in self._dataset:
                del self._dataset.DimensionDescriptionLabel
        else:
            self._dataset.DimensionDescriptionLabel = value
