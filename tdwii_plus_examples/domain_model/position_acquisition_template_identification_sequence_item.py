from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class PositionAcquisitionTemplateIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PositionAcquisitionTemplateCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PositionAcquisitionTemplateID(self) -> Optional[str]:
        if "PositionAcquisitionTemplateID" in self._dataset:
            return self._dataset.PositionAcquisitionTemplateID
        return None

    @PositionAcquisitionTemplateID.setter
    def PositionAcquisitionTemplateID(self, value: Optional[str]):
        if value is None:
            if "PositionAcquisitionTemplateID" in self._dataset:
                del self._dataset.PositionAcquisitionTemplateID
        else:
            self._dataset.PositionAcquisitionTemplateID = value

    @property
    def PositionAcquisitionTemplateName(self) -> Optional[str]:
        if "PositionAcquisitionTemplateName" in self._dataset:
            return self._dataset.PositionAcquisitionTemplateName
        return None

    @PositionAcquisitionTemplateName.setter
    def PositionAcquisitionTemplateName(self, value: Optional[str]):
        if value is None:
            if "PositionAcquisitionTemplateName" in self._dataset:
                del self._dataset.PositionAcquisitionTemplateName
        else:
            self._dataset.PositionAcquisitionTemplateName = value

    @property
    def PositionAcquisitionTemplateCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PositionAcquisitionTemplateCodeSequence" in self._dataset:
            if len(self._PositionAcquisitionTemplateCodeSequence) == len(
                self._dataset.PositionAcquisitionTemplateCodeSequence
            ):
                return self._PositionAcquisitionTemplateCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PositionAcquisitionTemplateCodeSequence]
        return None

    @PositionAcquisitionTemplateCodeSequence.setter
    def PositionAcquisitionTemplateCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PositionAcquisitionTemplateCodeSequence = []
            if "PositionAcquisitionTemplateCodeSequence" in self._dataset:
                del self._dataset.PositionAcquisitionTemplateCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PositionAcquisitionTemplateCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PositionAcquisitionTemplateCodeSequence = value
            if "PositionAcquisitionTemplateCodeSequence" not in self._dataset:
                self._dataset.PositionAcquisitionTemplateCodeSequence = pydicom.Sequence()
            self._dataset.PositionAcquisitionTemplateCodeSequence.clear()
            self._dataset.PositionAcquisitionTemplateCodeSequence.extend([item.to_dataset() for item in value])

    def add_PositionAcquisitionTemplateCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PositionAcquisitionTemplateCodeSequence.append(item)
        if "PositionAcquisitionTemplateCodeSequence" not in self._dataset:
            self._dataset.PositionAcquisitionTemplateCodeSequence = pydicom.Sequence()
        self._dataset.PositionAcquisitionTemplateCodeSequence.append(item.to_dataset())

    @property
    def PositionAcquisitionTemplateDescription(self) -> Optional[str]:
        if "PositionAcquisitionTemplateDescription" in self._dataset:
            return self._dataset.PositionAcquisitionTemplateDescription
        return None

    @PositionAcquisitionTemplateDescription.setter
    def PositionAcquisitionTemplateDescription(self, value: Optional[str]):
        if value is None:
            if "PositionAcquisitionTemplateDescription" in self._dataset:
                del self._dataset.PositionAcquisitionTemplateDescription
        else:
            self._dataset.PositionAcquisitionTemplateDescription = value
