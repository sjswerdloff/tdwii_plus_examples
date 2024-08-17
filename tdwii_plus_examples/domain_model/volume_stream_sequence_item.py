from typing import Any, List, Optional  # noqa

import pydicom

from .presentation_state_classification_component_sequence_item import (
    PresentationStateClassificationComponentSequenceItem,
)


class VolumeStreamSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PresentationStateClassificationComponentSequence: List[PresentationStateClassificationComponentSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VolumetricPresentationInputSetUID(self) -> Optional[str]:
        if "VolumetricPresentationInputSetUID" in self._dataset:
            return self._dataset.VolumetricPresentationInputSetUID
        return None

    @VolumetricPresentationInputSetUID.setter
    def VolumetricPresentationInputSetUID(self, value: Optional[str]):
        if value is None:
            if "VolumetricPresentationInputSetUID" in self._dataset:
                del self._dataset.VolumetricPresentationInputSetUID
        else:
            self._dataset.VolumetricPresentationInputSetUID = value

    @property
    def PresentationStateClassificationComponentSequence(
        self,
    ) -> Optional[List[PresentationStateClassificationComponentSequenceItem]]:
        if "PresentationStateClassificationComponentSequence" in self._dataset:
            if len(self._PresentationStateClassificationComponentSequence) == len(
                self._dataset.PresentationStateClassificationComponentSequence
            ):
                return self._PresentationStateClassificationComponentSequence
            else:
                return [
                    PresentationStateClassificationComponentSequenceItem(x)
                    for x in self._dataset.PresentationStateClassificationComponentSequence
                ]
        return None

    @PresentationStateClassificationComponentSequence.setter
    def PresentationStateClassificationComponentSequence(
        self, value: Optional[List[PresentationStateClassificationComponentSequenceItem]]
    ):
        if value is None:
            self._PresentationStateClassificationComponentSequence = []
            if "PresentationStateClassificationComponentSequence" in self._dataset:
                del self._dataset.PresentationStateClassificationComponentSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PresentationStateClassificationComponentSequenceItem) for item in value
        ):
            raise ValueError(
                "PresentationStateClassificationComponentSequence must be a list of"
                " PresentationStateClassificationComponentSequenceItem objects"
            )
        else:
            self._PresentationStateClassificationComponentSequence = value
            if "PresentationStateClassificationComponentSequence" not in self._dataset:
                self._dataset.PresentationStateClassificationComponentSequence = pydicom.Sequence()
            self._dataset.PresentationStateClassificationComponentSequence.clear()
            self._dataset.PresentationStateClassificationComponentSequence.extend([item.to_dataset() for item in value])

    def add_PresentationStateClassificationComponent(self, item: PresentationStateClassificationComponentSequenceItem):
        if not isinstance(item, PresentationStateClassificationComponentSequenceItem):
            raise ValueError("Item must be an instance of PresentationStateClassificationComponentSequenceItem")
        self._PresentationStateClassificationComponentSequence.append(item)
        if "PresentationStateClassificationComponentSequence" not in self._dataset:
            self._dataset.PresentationStateClassificationComponentSequence = pydicom.Sequence()
        self._dataset.PresentationStateClassificationComponentSequence.append(item.to_dataset())
