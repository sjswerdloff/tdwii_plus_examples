from typing import Any, List, Optional

import pydicom

from .referenced_texture_sequence_item import ReferencedTextureSequenceItem


class UVMappingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedTextureSequence: List[ReferencedTextureSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSurfaceNumber(self) -> Optional[int]:
        if "ReferencedSurfaceNumber" in self._dataset:
            return self._dataset.ReferencedSurfaceNumber
        return None

    @ReferencedSurfaceNumber.setter
    def ReferencedSurfaceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedSurfaceNumber" in self._dataset:
                del self._dataset.ReferencedSurfaceNumber
        else:
            self._dataset.ReferencedSurfaceNumber = value

    @property
    def TextureLabel(self) -> Optional[str]:
        if "TextureLabel" in self._dataset:
            return self._dataset.TextureLabel
        return None

    @TextureLabel.setter
    def TextureLabel(self, value: Optional[str]):
        if value is None:
            if "TextureLabel" in self._dataset:
                del self._dataset.TextureLabel
        else:
            self._dataset.TextureLabel = value

    @property
    def UValueData(self) -> Optional[bytes]:
        if "UValueData" in self._dataset:
            return self._dataset.UValueData
        return None

    @UValueData.setter
    def UValueData(self, value: Optional[bytes]):
        if value is None:
            if "UValueData" in self._dataset:
                del self._dataset.UValueData
        else:
            self._dataset.UValueData = value

    @property
    def VValueData(self) -> Optional[bytes]:
        if "VValueData" in self._dataset:
            return self._dataset.VValueData
        return None

    @VValueData.setter
    def VValueData(self, value: Optional[bytes]):
        if value is None:
            if "VValueData" in self._dataset:
                del self._dataset.VValueData
        else:
            self._dataset.VValueData = value

    @property
    def ReferencedTextureSequence(self) -> Optional[List[ReferencedTextureSequenceItem]]:
        if "ReferencedTextureSequence" in self._dataset:
            if len(self._ReferencedTextureSequence) == len(self._dataset.ReferencedTextureSequence):
                return self._ReferencedTextureSequence
            else:
                return [ReferencedTextureSequenceItem(x) for x in self._dataset.ReferencedTextureSequence]
        return None

    @ReferencedTextureSequence.setter
    def ReferencedTextureSequence(self, value: Optional[List[ReferencedTextureSequenceItem]]):
        if value is None:
            self._ReferencedTextureSequence = []
            if "ReferencedTextureSequence" in self._dataset:
                del self._dataset.ReferencedTextureSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedTextureSequenceItem) for item in value):
            raise ValueError(f"ReferencedTextureSequence must be a list of ReferencedTextureSequenceItem objects")
        else:
            self._ReferencedTextureSequence = value
            if "ReferencedTextureSequence" not in self._dataset:
                self._dataset.ReferencedTextureSequence = pydicom.Sequence()
            self._dataset.ReferencedTextureSequence.clear()
            self._dataset.ReferencedTextureSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedTexture(self, item: ReferencedTextureSequenceItem):
        if not isinstance(item, ReferencedTextureSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedTextureSequenceItem")
        self._ReferencedTextureSequence.append(item)
        if "ReferencedTextureSequence" not in self._dataset:
            self._dataset.ReferencedTextureSequence = pydicom.Sequence()
        self._dataset.ReferencedTextureSequence.append(item.to_dataset())
