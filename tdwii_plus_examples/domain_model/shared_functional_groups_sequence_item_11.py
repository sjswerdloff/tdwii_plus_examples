from typing import Any, List, Optional  # noqa

import pydicom

from .cardiac_synchronization_sequence_item import CardiacSynchronizationSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .intravascular_frame_content_sequence_item import (
    IntravascularFrameContentSequenceItem,
)
from .intravascular_oct_frame_content_sequence_item import (
    IntravascularOCTFrameContentSequenceItem,
)
from .intravascular_oct_frame_type_sequence_item import (
    IntravascularOCTFrameTypeSequenceItem,
)
from .pixel_intensity_relationship_lut_sequence_item import (
    PixelIntensityRelationshipLUTSequenceItem,
)
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem


class SharedFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._CardiacSynchronizationSequence: List[CardiacSynchronizationSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PixelMeasuresSequence: List[PixelMeasuresSequenceItem] = []
        self._FrameVOILUTSequence: List[FrameVOILUTSequenceItem] = []
        self._PixelIntensityRelationshipLUTSequence: List[PixelIntensityRelationshipLUTSequenceItem] = []
        self._IntravascularOCTFrameTypeSequence: List[IntravascularOCTFrameTypeSequenceItem] = []
        self._IntravascularFrameContentSequence: List[IntravascularFrameContentSequenceItem] = []
        self._IntravascularOCTFrameContentSequence: List[IntravascularOCTFrameContentSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DerivationImageSequence(self) -> Optional[List[DerivationImageSequenceItem]]:
        if "DerivationImageSequence" in self._dataset:
            if len(self._DerivationImageSequence) == len(self._dataset.DerivationImageSequence):
                return self._DerivationImageSequence
            else:
                return [DerivationImageSequenceItem(x) for x in self._dataset.DerivationImageSequence]
        return None

    @DerivationImageSequence.setter
    def DerivationImageSequence(self, value: Optional[List[DerivationImageSequenceItem]]):
        if value is None:
            self._DerivationImageSequence = []
            if "DerivationImageSequence" in self._dataset:
                del self._dataset.DerivationImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, DerivationImageSequenceItem) for item in value):
            raise ValueError("DerivationImageSequence must be a list of DerivationImageSequenceItem objects")
        else:
            self._DerivationImageSequence = value
            if "DerivationImageSequence" not in self._dataset:
                self._dataset.DerivationImageSequence = pydicom.Sequence()
            self._dataset.DerivationImageSequence.clear()
            self._dataset.DerivationImageSequence.extend([item.to_dataset() for item in value])

    def add_DerivationImage(self, item: DerivationImageSequenceItem):
        if not isinstance(item, DerivationImageSequenceItem):
            raise ValueError("Item must be an instance of DerivationImageSequenceItem")
        self._DerivationImageSequence.append(item)
        if "DerivationImageSequence" not in self._dataset:
            self._dataset.DerivationImageSequence = pydicom.Sequence()
        self._dataset.DerivationImageSequence.append(item.to_dataset())

    @property
    def CardiacSynchronizationSequence(self) -> Optional[List[CardiacSynchronizationSequenceItem]]:
        if "CardiacSynchronizationSequence" in self._dataset:
            if len(self._CardiacSynchronizationSequence) == len(self._dataset.CardiacSynchronizationSequence):
                return self._CardiacSynchronizationSequence
            else:
                return [CardiacSynchronizationSequenceItem(x) for x in self._dataset.CardiacSynchronizationSequence]
        return None

    @CardiacSynchronizationSequence.setter
    def CardiacSynchronizationSequence(self, value: Optional[List[CardiacSynchronizationSequenceItem]]):
        if value is None:
            self._CardiacSynchronizationSequence = []
            if "CardiacSynchronizationSequence" in self._dataset:
                del self._dataset.CardiacSynchronizationSequence
        elif not isinstance(value, list) or not all(isinstance(item, CardiacSynchronizationSequenceItem) for item in value):
            raise ValueError("CardiacSynchronizationSequence must be a list of CardiacSynchronizationSequenceItem objects")
        else:
            self._CardiacSynchronizationSequence = value
            if "CardiacSynchronizationSequence" not in self._dataset:
                self._dataset.CardiacSynchronizationSequence = pydicom.Sequence()
            self._dataset.CardiacSynchronizationSequence.clear()
            self._dataset.CardiacSynchronizationSequence.extend([item.to_dataset() for item in value])

    def add_CardiacSynchronization(self, item: CardiacSynchronizationSequenceItem):
        if not isinstance(item, CardiacSynchronizationSequenceItem):
            raise ValueError("Item must be an instance of CardiacSynchronizationSequenceItem")
        self._CardiacSynchronizationSequence.append(item)
        if "CardiacSynchronizationSequence" not in self._dataset:
            self._dataset.CardiacSynchronizationSequence = pydicom.Sequence()
        self._dataset.CardiacSynchronizationSequence.append(item.to_dataset())

    @property
    def FrameAnatomySequence(self) -> Optional[List[FrameAnatomySequenceItem]]:
        if "FrameAnatomySequence" in self._dataset:
            if len(self._FrameAnatomySequence) == len(self._dataset.FrameAnatomySequence):
                return self._FrameAnatomySequence
            else:
                return [FrameAnatomySequenceItem(x) for x in self._dataset.FrameAnatomySequence]
        return None

    @FrameAnatomySequence.setter
    def FrameAnatomySequence(self, value: Optional[List[FrameAnatomySequenceItem]]):
        if value is None:
            self._FrameAnatomySequence = []
            if "FrameAnatomySequence" in self._dataset:
                del self._dataset.FrameAnatomySequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameAnatomySequenceItem) for item in value):
            raise ValueError("FrameAnatomySequence must be a list of FrameAnatomySequenceItem objects")
        else:
            self._FrameAnatomySequence = value
            if "FrameAnatomySequence" not in self._dataset:
                self._dataset.FrameAnatomySequence = pydicom.Sequence()
            self._dataset.FrameAnatomySequence.clear()
            self._dataset.FrameAnatomySequence.extend([item.to_dataset() for item in value])

    def add_FrameAnatomy(self, item: FrameAnatomySequenceItem):
        if not isinstance(item, FrameAnatomySequenceItem):
            raise ValueError("Item must be an instance of FrameAnatomySequenceItem")
        self._FrameAnatomySequence.append(item)
        if "FrameAnatomySequence" not in self._dataset:
            self._dataset.FrameAnatomySequence = pydicom.Sequence()
        self._dataset.FrameAnatomySequence.append(item.to_dataset())

    @property
    def FrameContentSequence(self) -> Optional[List[FrameContentSequenceItem]]:
        if "FrameContentSequence" in self._dataset:
            if len(self._FrameContentSequence) == len(self._dataset.FrameContentSequence):
                return self._FrameContentSequence
            else:
                return [FrameContentSequenceItem(x) for x in self._dataset.FrameContentSequence]
        return None

    @FrameContentSequence.setter
    def FrameContentSequence(self, value: Optional[List[FrameContentSequenceItem]]):
        if value is None:
            self._FrameContentSequence = []
            if "FrameContentSequence" in self._dataset:
                del self._dataset.FrameContentSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameContentSequenceItem) for item in value):
            raise ValueError("FrameContentSequence must be a list of FrameContentSequenceItem objects")
        else:
            self._FrameContentSequence = value
            if "FrameContentSequence" not in self._dataset:
                self._dataset.FrameContentSequence = pydicom.Sequence()
            self._dataset.FrameContentSequence.clear()
            self._dataset.FrameContentSequence.extend([item.to_dataset() for item in value])

    def add_FrameContent(self, item: FrameContentSequenceItem):
        if not isinstance(item, FrameContentSequenceItem):
            raise ValueError("Item must be an instance of FrameContentSequenceItem")
        self._FrameContentSequence.append(item)
        if "FrameContentSequence" not in self._dataset:
            self._dataset.FrameContentSequence = pydicom.Sequence()
        self._dataset.FrameContentSequence.append(item.to_dataset())

    @property
    def PixelMeasuresSequence(self) -> Optional[List[PixelMeasuresSequenceItem]]:
        if "PixelMeasuresSequence" in self._dataset:
            if len(self._PixelMeasuresSequence) == len(self._dataset.PixelMeasuresSequence):
                return self._PixelMeasuresSequence
            else:
                return [PixelMeasuresSequenceItem(x) for x in self._dataset.PixelMeasuresSequence]
        return None

    @PixelMeasuresSequence.setter
    def PixelMeasuresSequence(self, value: Optional[List[PixelMeasuresSequenceItem]]):
        if value is None:
            self._PixelMeasuresSequence = []
            if "PixelMeasuresSequence" in self._dataset:
                del self._dataset.PixelMeasuresSequence
        elif not isinstance(value, list) or not all(isinstance(item, PixelMeasuresSequenceItem) for item in value):
            raise ValueError("PixelMeasuresSequence must be a list of PixelMeasuresSequenceItem objects")
        else:
            self._PixelMeasuresSequence = value
            if "PixelMeasuresSequence" not in self._dataset:
                self._dataset.PixelMeasuresSequence = pydicom.Sequence()
            self._dataset.PixelMeasuresSequence.clear()
            self._dataset.PixelMeasuresSequence.extend([item.to_dataset() for item in value])

    def add_PixelMeasures(self, item: PixelMeasuresSequenceItem):
        if not isinstance(item, PixelMeasuresSequenceItem):
            raise ValueError("Item must be an instance of PixelMeasuresSequenceItem")
        self._PixelMeasuresSequence.append(item)
        if "PixelMeasuresSequence" not in self._dataset:
            self._dataset.PixelMeasuresSequence = pydicom.Sequence()
        self._dataset.PixelMeasuresSequence.append(item.to_dataset())

    @property
    def FrameVOILUTSequence(self) -> Optional[List[FrameVOILUTSequenceItem]]:
        if "FrameVOILUTSequence" in self._dataset:
            if len(self._FrameVOILUTSequence) == len(self._dataset.FrameVOILUTSequence):
                return self._FrameVOILUTSequence
            else:
                return [FrameVOILUTSequenceItem(x) for x in self._dataset.FrameVOILUTSequence]
        return None

    @FrameVOILUTSequence.setter
    def FrameVOILUTSequence(self, value: Optional[List[FrameVOILUTSequenceItem]]):
        if value is None:
            self._FrameVOILUTSequence = []
            if "FrameVOILUTSequence" in self._dataset:
                del self._dataset.FrameVOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameVOILUTSequenceItem) for item in value):
            raise ValueError("FrameVOILUTSequence must be a list of FrameVOILUTSequenceItem objects")
        else:
            self._FrameVOILUTSequence = value
            if "FrameVOILUTSequence" not in self._dataset:
                self._dataset.FrameVOILUTSequence = pydicom.Sequence()
            self._dataset.FrameVOILUTSequence.clear()
            self._dataset.FrameVOILUTSequence.extend([item.to_dataset() for item in value])

    def add_FrameVOILUT(self, item: FrameVOILUTSequenceItem):
        if not isinstance(item, FrameVOILUTSequenceItem):
            raise ValueError("Item must be an instance of FrameVOILUTSequenceItem")
        self._FrameVOILUTSequence.append(item)
        if "FrameVOILUTSequence" not in self._dataset:
            self._dataset.FrameVOILUTSequence = pydicom.Sequence()
        self._dataset.FrameVOILUTSequence.append(item.to_dataset())

    @property
    def PixelIntensityRelationshipLUTSequence(self) -> Optional[List[PixelIntensityRelationshipLUTSequenceItem]]:
        if "PixelIntensityRelationshipLUTSequence" in self._dataset:
            if len(self._PixelIntensityRelationshipLUTSequence) == len(self._dataset.PixelIntensityRelationshipLUTSequence):
                return self._PixelIntensityRelationshipLUTSequence
            else:
                return [
                    PixelIntensityRelationshipLUTSequenceItem(x) for x in self._dataset.PixelIntensityRelationshipLUTSequence
                ]
        return None

    @PixelIntensityRelationshipLUTSequence.setter
    def PixelIntensityRelationshipLUTSequence(self, value: Optional[List[PixelIntensityRelationshipLUTSequenceItem]]):
        if value is None:
            self._PixelIntensityRelationshipLUTSequence = []
            if "PixelIntensityRelationshipLUTSequence" in self._dataset:
                del self._dataset.PixelIntensityRelationshipLUTSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PixelIntensityRelationshipLUTSequenceItem) for item in value
        ):
            raise ValueError(
                "PixelIntensityRelationshipLUTSequence must be a list of PixelIntensityRelationshipLUTSequenceItem objects"
            )
        else:
            self._PixelIntensityRelationshipLUTSequence = value
            if "PixelIntensityRelationshipLUTSequence" not in self._dataset:
                self._dataset.PixelIntensityRelationshipLUTSequence = pydicom.Sequence()
            self._dataset.PixelIntensityRelationshipLUTSequence.clear()
            self._dataset.PixelIntensityRelationshipLUTSequence.extend([item.to_dataset() for item in value])

    def add_PixelIntensityRelationshipLUT(self, item: PixelIntensityRelationshipLUTSequenceItem):
        if not isinstance(item, PixelIntensityRelationshipLUTSequenceItem):
            raise ValueError("Item must be an instance of PixelIntensityRelationshipLUTSequenceItem")
        self._PixelIntensityRelationshipLUTSequence.append(item)
        if "PixelIntensityRelationshipLUTSequence" not in self._dataset:
            self._dataset.PixelIntensityRelationshipLUTSequence = pydicom.Sequence()
        self._dataset.PixelIntensityRelationshipLUTSequence.append(item.to_dataset())

    @property
    def IntravascularOCTFrameTypeSequence(self) -> Optional[List[IntravascularOCTFrameTypeSequenceItem]]:
        if "IntravascularOCTFrameTypeSequence" in self._dataset:
            if len(self._IntravascularOCTFrameTypeSequence) == len(self._dataset.IntravascularOCTFrameTypeSequence):
                return self._IntravascularOCTFrameTypeSequence
            else:
                return [IntravascularOCTFrameTypeSequenceItem(x) for x in self._dataset.IntravascularOCTFrameTypeSequence]
        return None

    @IntravascularOCTFrameTypeSequence.setter
    def IntravascularOCTFrameTypeSequence(self, value: Optional[List[IntravascularOCTFrameTypeSequenceItem]]):
        if value is None:
            self._IntravascularOCTFrameTypeSequence = []
            if "IntravascularOCTFrameTypeSequence" in self._dataset:
                del self._dataset.IntravascularOCTFrameTypeSequence
        elif not isinstance(value, list) or not all(isinstance(item, IntravascularOCTFrameTypeSequenceItem) for item in value):
            raise ValueError(
                "IntravascularOCTFrameTypeSequence must be a list of IntravascularOCTFrameTypeSequenceItem objects"
            )
        else:
            self._IntravascularOCTFrameTypeSequence = value
            if "IntravascularOCTFrameTypeSequence" not in self._dataset:
                self._dataset.IntravascularOCTFrameTypeSequence = pydicom.Sequence()
            self._dataset.IntravascularOCTFrameTypeSequence.clear()
            self._dataset.IntravascularOCTFrameTypeSequence.extend([item.to_dataset() for item in value])

    def add_IntravascularOCTFrameType(self, item: IntravascularOCTFrameTypeSequenceItem):
        if not isinstance(item, IntravascularOCTFrameTypeSequenceItem):
            raise ValueError("Item must be an instance of IntravascularOCTFrameTypeSequenceItem")
        self._IntravascularOCTFrameTypeSequence.append(item)
        if "IntravascularOCTFrameTypeSequence" not in self._dataset:
            self._dataset.IntravascularOCTFrameTypeSequence = pydicom.Sequence()
        self._dataset.IntravascularOCTFrameTypeSequence.append(item.to_dataset())

    @property
    def IntravascularFrameContentSequence(self) -> Optional[List[IntravascularFrameContentSequenceItem]]:
        if "IntravascularFrameContentSequence" in self._dataset:
            if len(self._IntravascularFrameContentSequence) == len(self._dataset.IntravascularFrameContentSequence):
                return self._IntravascularFrameContentSequence
            else:
                return [IntravascularFrameContentSequenceItem(x) for x in self._dataset.IntravascularFrameContentSequence]
        return None

    @IntravascularFrameContentSequence.setter
    def IntravascularFrameContentSequence(self, value: Optional[List[IntravascularFrameContentSequenceItem]]):
        if value is None:
            self._IntravascularFrameContentSequence = []
            if "IntravascularFrameContentSequence" in self._dataset:
                del self._dataset.IntravascularFrameContentSequence
        elif not isinstance(value, list) or not all(isinstance(item, IntravascularFrameContentSequenceItem) for item in value):
            raise ValueError(
                "IntravascularFrameContentSequence must be a list of IntravascularFrameContentSequenceItem objects"
            )
        else:
            self._IntravascularFrameContentSequence = value
            if "IntravascularFrameContentSequence" not in self._dataset:
                self._dataset.IntravascularFrameContentSequence = pydicom.Sequence()
            self._dataset.IntravascularFrameContentSequence.clear()
            self._dataset.IntravascularFrameContentSequence.extend([item.to_dataset() for item in value])

    def add_IntravascularFrameContent(self, item: IntravascularFrameContentSequenceItem):
        if not isinstance(item, IntravascularFrameContentSequenceItem):
            raise ValueError("Item must be an instance of IntravascularFrameContentSequenceItem")
        self._IntravascularFrameContentSequence.append(item)
        if "IntravascularFrameContentSequence" not in self._dataset:
            self._dataset.IntravascularFrameContentSequence = pydicom.Sequence()
        self._dataset.IntravascularFrameContentSequence.append(item.to_dataset())

    @property
    def IntravascularOCTFrameContentSequence(self) -> Optional[List[IntravascularOCTFrameContentSequenceItem]]:
        if "IntravascularOCTFrameContentSequence" in self._dataset:
            if len(self._IntravascularOCTFrameContentSequence) == len(self._dataset.IntravascularOCTFrameContentSequence):
                return self._IntravascularOCTFrameContentSequence
            else:
                return [
                    IntravascularOCTFrameContentSequenceItem(x) for x in self._dataset.IntravascularOCTFrameContentSequence
                ]
        return None

    @IntravascularOCTFrameContentSequence.setter
    def IntravascularOCTFrameContentSequence(self, value: Optional[List[IntravascularOCTFrameContentSequenceItem]]):
        if value is None:
            self._IntravascularOCTFrameContentSequence = []
            if "IntravascularOCTFrameContentSequence" in self._dataset:
                del self._dataset.IntravascularOCTFrameContentSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, IntravascularOCTFrameContentSequenceItem) for item in value
        ):
            raise ValueError(
                "IntravascularOCTFrameContentSequence must be a list of IntravascularOCTFrameContentSequenceItem objects"
            )
        else:
            self._IntravascularOCTFrameContentSequence = value
            if "IntravascularOCTFrameContentSequence" not in self._dataset:
                self._dataset.IntravascularOCTFrameContentSequence = pydicom.Sequence()
            self._dataset.IntravascularOCTFrameContentSequence.clear()
            self._dataset.IntravascularOCTFrameContentSequence.extend([item.to_dataset() for item in value])

    def add_IntravascularOCTFrameContent(self, item: IntravascularOCTFrameContentSequenceItem):
        if not isinstance(item, IntravascularOCTFrameContentSequenceItem):
            raise ValueError("Item must be an instance of IntravascularOCTFrameContentSequenceItem")
        self._IntravascularOCTFrameContentSequence.append(item)
        if "IntravascularOCTFrameContentSequence" not in self._dataset:
            self._dataset.IntravascularOCTFrameContentSequence = pydicom.Sequence()
        self._dataset.IntravascularOCTFrameContentSequence.append(item.to_dataset())
