from __future__ import annotations

from typing import List, Optional


class CodeSequenceItem:
    def __init__(self):
        self._CodeValue = None
        self._CodingSchemeDesignator = None
        self._CodingSchemeVersion = None
        self._CodeMeaning = None
        self._MappingResource = None
        self._ContextGroupVersion = None
        self._ContextGroupLocalVersion = None
        self._ContextGroupExtensionFlag = None
        self._ContextGroupExtensionCreatorUID = None
        self._ContextIdentifier = None
        self._ContextUID = None
        self._MappingResourceUID = None
        self._LongCodeValue = None
        self._URNCodeValue = None
        self._EquivalentCodeSequence: List[CodeSequenceItem] = []
        self._MappingResourceName = None

    @property
    def CodeValue(self):
        return self._CodeValue

    @CodeValue.setter
    def CodeValue(self, value):
        self._CodeValue = value

    @property
    def CodingSchemeDesignator(self):
        return self._CodingSchemeDesignator

    @CodingSchemeDesignator.setter
    def CodingSchemeDesignator(self, value):
        self._CodingSchemeDesignator = value

    @property
    def CodingSchemeVersion(self):
        return self._CodingSchemeVersion

    @CodingSchemeVersion.setter
    def CodingSchemeVersion(self, value):
        self._CodingSchemeVersion = value

    @property
    def CodeMeaning(self):
        return self._CodeMeaning

    @CodeMeaning.setter
    def CodeMeaning(self, value):
        self._CodeMeaning = value

    @property
    def MappingResource(self):
        return self._MappingResource

    @MappingResource.setter
    def MappingResource(self, value):
        self._MappingResource = value

    @property
    def ContextGroupVersion(self):
        return self._ContextGroupVersion

    @ContextGroupVersion.setter
    def ContextGroupVersion(self, value):
        self._ContextGroupVersion = value

    @property
    def ContextGroupLocalVersion(self):
        return self._ContextGroupLocalVersion

    @ContextGroupLocalVersion.setter
    def ContextGroupLocalVersion(self, value):
        self._ContextGroupLocalVersion = value

    @property
    def ContextGroupExtensionFlag(self):
        return self._ContextGroupExtensionFlag

    @ContextGroupExtensionFlag.setter
    def ContextGroupExtensionFlag(self, value):
        self._ContextGroupExtensionFlag = value

    @property
    def ContextGroupExtensionCreatorUID(self):
        return self._ContextGroupExtensionCreatorUID

    @ContextGroupExtensionCreatorUID.setter
    def ContextGroupExtensionCreatorUID(self, value):
        self._ContextGroupExtensionCreatorUID = value

    @property
    def ContextIdentifier(self):
        return self._ContextIdentifier

    @ContextIdentifier.setter
    def ContextIdentifier(self, value):
        self._ContextIdentifier = value

    @property
    def ContextUID(self):
        return self._ContextUID

    @ContextUID.setter
    def ContextUID(self, value):
        self._ContextUID = value

    @property
    def MappingResourceUID(self):
        return self._MappingResourceUID

    @MappingResourceUID.setter
    def MappingResourceUID(self, value):
        self._MappingResourceUID = value

    @property
    def LongCodeValue(self):
        return self._LongCodeValue

    @LongCodeValue.setter
    def LongCodeValue(self, value):
        self._LongCodeValue = value

    @property
    def URNCodeValue(self):
        return self._URNCodeValue

    @URNCodeValue.setter
    def URNCodeValue(self, value):
        self._URNCodeValue = value

    @property
    def EquivalentCodeSequence(self) -> List[CodeSequenceItem]:
        return self._EquivalentCodeSequence

    @EquivalentCodeSequence.setter
    def EquivalentCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EquivalentCodeSequence = []
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"EquivalentCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EquivalentCodeSequence = value

    def add_EquivalentCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._EquivalentCodeSequence.append(item)

    @property
    def MappingResourceName(self):
        return self._MappingResourceName

    @MappingResourceName.setter
    def MappingResourceName(self, value):
        self._MappingResourceName = value
