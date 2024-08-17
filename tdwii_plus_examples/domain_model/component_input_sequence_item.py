from typing import Any, List, Optional  # noqa

import pydicom


class ComponentInputSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BitsMappedToColorLookupTable(self) -> Optional[int]:
        if "BitsMappedToColorLookupTable" in self._dataset:
            return self._dataset.BitsMappedToColorLookupTable
        return None

    @BitsMappedToColorLookupTable.setter
    def BitsMappedToColorLookupTable(self, value: Optional[int]):
        if value is None:
            if "BitsMappedToColorLookupTable" in self._dataset:
                del self._dataset.BitsMappedToColorLookupTable
        else:
            self._dataset.BitsMappedToColorLookupTable = value

    @property
    def VolumetricPresentationInputIndex(self) -> Optional[int]:
        if "VolumetricPresentationInputIndex" in self._dataset:
            return self._dataset.VolumetricPresentationInputIndex
        return None

    @VolumetricPresentationInputIndex.setter
    def VolumetricPresentationInputIndex(self, value: Optional[int]):
        if value is None:
            if "VolumetricPresentationInputIndex" in self._dataset:
                del self._dataset.VolumetricPresentationInputIndex
        else:
            self._dataset.VolumetricPresentationInputIndex = value
