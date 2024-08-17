from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .palette_color_lookup_table_sequence_item import (
    PaletteColorLookupTableSequenceItem,
)


class OpticalPathSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._IlluminationTypeCodeSequence: List[CodeSequenceItem] = []
        self._LightPathFilterTypeStackCodeSequence: List[CodeSequenceItem] = []
        self._ImagePathFilterTypeStackCodeSequence: List[CodeSequenceItem] = []
        self._LensesCodeSequence: List[CodeSequenceItem] = []
        self._ChannelDescriptionCodeSequence: List[CodeSequenceItem] = []
        self._IlluminatorTypeCodeSequence: List[CodeSequenceItem] = []
        self._IlluminationColorCodeSequence: List[CodeSequenceItem] = []
        self._PaletteColorLookupTableSequence: List[PaletteColorLookupTableSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LightPathFilterPassThroughWavelength(self) -> Optional[int]:
        if "LightPathFilterPassThroughWavelength" in self._dataset:
            return self._dataset.LightPathFilterPassThroughWavelength
        return None

    @LightPathFilterPassThroughWavelength.setter
    def LightPathFilterPassThroughWavelength(self, value: Optional[int]):
        if value is None:
            if "LightPathFilterPassThroughWavelength" in self._dataset:
                del self._dataset.LightPathFilterPassThroughWavelength
        else:
            self._dataset.LightPathFilterPassThroughWavelength = value

    @property
    def LightPathFilterPassBand(self) -> Optional[List[int]]:
        if "LightPathFilterPassBand" in self._dataset:
            return self._dataset.LightPathFilterPassBand
        return None

    @LightPathFilterPassBand.setter
    def LightPathFilterPassBand(self, value: Optional[List[int]]):
        if value is None:
            if "LightPathFilterPassBand" in self._dataset:
                del self._dataset.LightPathFilterPassBand
        else:
            self._dataset.LightPathFilterPassBand = value

    @property
    def ImagePathFilterPassThroughWavelength(self) -> Optional[int]:
        if "ImagePathFilterPassThroughWavelength" in self._dataset:
            return self._dataset.ImagePathFilterPassThroughWavelength
        return None

    @ImagePathFilterPassThroughWavelength.setter
    def ImagePathFilterPassThroughWavelength(self, value: Optional[int]):
        if value is None:
            if "ImagePathFilterPassThroughWavelength" in self._dataset:
                del self._dataset.ImagePathFilterPassThroughWavelength
        else:
            self._dataset.ImagePathFilterPassThroughWavelength = value

    @property
    def ImagePathFilterPassBand(self) -> Optional[List[int]]:
        if "ImagePathFilterPassBand" in self._dataset:
            return self._dataset.ImagePathFilterPassBand
        return None

    @ImagePathFilterPassBand.setter
    def ImagePathFilterPassBand(self, value: Optional[List[int]]):
        if value is None:
            if "ImagePathFilterPassBand" in self._dataset:
                del self._dataset.ImagePathFilterPassBand
        else:
            self._dataset.ImagePathFilterPassBand = value

    @property
    def IlluminationTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "IlluminationTypeCodeSequence" in self._dataset:
            if len(self._IlluminationTypeCodeSequence) == len(self._dataset.IlluminationTypeCodeSequence):
                return self._IlluminationTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.IlluminationTypeCodeSequence]
        return None

    @IlluminationTypeCodeSequence.setter
    def IlluminationTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._IlluminationTypeCodeSequence = []
            if "IlluminationTypeCodeSequence" in self._dataset:
                del self._dataset.IlluminationTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"IlluminationTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._IlluminationTypeCodeSequence = value
            if "IlluminationTypeCodeSequence" not in self._dataset:
                self._dataset.IlluminationTypeCodeSequence = pydicom.Sequence()
            self._dataset.IlluminationTypeCodeSequence.clear()
            self._dataset.IlluminationTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_IlluminationTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._IlluminationTypeCodeSequence.append(item)
        if "IlluminationTypeCodeSequence" not in self._dataset:
            self._dataset.IlluminationTypeCodeSequence = pydicom.Sequence()
        self._dataset.IlluminationTypeCodeSequence.append(item.to_dataset())

    @property
    def LightPathFilterTypeStackCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "LightPathFilterTypeStackCodeSequence" in self._dataset:
            if len(self._LightPathFilterTypeStackCodeSequence) == len(self._dataset.LightPathFilterTypeStackCodeSequence):
                return self._LightPathFilterTypeStackCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.LightPathFilterTypeStackCodeSequence]
        return None

    @LightPathFilterTypeStackCodeSequence.setter
    def LightPathFilterTypeStackCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._LightPathFilterTypeStackCodeSequence = []
            if "LightPathFilterTypeStackCodeSequence" in self._dataset:
                del self._dataset.LightPathFilterTypeStackCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"LightPathFilterTypeStackCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._LightPathFilterTypeStackCodeSequence = value
            if "LightPathFilterTypeStackCodeSequence" not in self._dataset:
                self._dataset.LightPathFilterTypeStackCodeSequence = pydicom.Sequence()
            self._dataset.LightPathFilterTypeStackCodeSequence.clear()
            self._dataset.LightPathFilterTypeStackCodeSequence.extend([item.to_dataset() for item in value])

    def add_LightPathFilterTypeStackCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._LightPathFilterTypeStackCodeSequence.append(item)
        if "LightPathFilterTypeStackCodeSequence" not in self._dataset:
            self._dataset.LightPathFilterTypeStackCodeSequence = pydicom.Sequence()
        self._dataset.LightPathFilterTypeStackCodeSequence.append(item.to_dataset())

    @property
    def ImagePathFilterTypeStackCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ImagePathFilterTypeStackCodeSequence" in self._dataset:
            if len(self._ImagePathFilterTypeStackCodeSequence) == len(self._dataset.ImagePathFilterTypeStackCodeSequence):
                return self._ImagePathFilterTypeStackCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ImagePathFilterTypeStackCodeSequence]
        return None

    @ImagePathFilterTypeStackCodeSequence.setter
    def ImagePathFilterTypeStackCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ImagePathFilterTypeStackCodeSequence = []
            if "ImagePathFilterTypeStackCodeSequence" in self._dataset:
                del self._dataset.ImagePathFilterTypeStackCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ImagePathFilterTypeStackCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ImagePathFilterTypeStackCodeSequence = value
            if "ImagePathFilterTypeStackCodeSequence" not in self._dataset:
                self._dataset.ImagePathFilterTypeStackCodeSequence = pydicom.Sequence()
            self._dataset.ImagePathFilterTypeStackCodeSequence.clear()
            self._dataset.ImagePathFilterTypeStackCodeSequence.extend([item.to_dataset() for item in value])

    def add_ImagePathFilterTypeStackCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ImagePathFilterTypeStackCodeSequence.append(item)
        if "ImagePathFilterTypeStackCodeSequence" not in self._dataset:
            self._dataset.ImagePathFilterTypeStackCodeSequence = pydicom.Sequence()
        self._dataset.ImagePathFilterTypeStackCodeSequence.append(item.to_dataset())

    @property
    def LensesCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "LensesCodeSequence" in self._dataset:
            if len(self._LensesCodeSequence) == len(self._dataset.LensesCodeSequence):
                return self._LensesCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.LensesCodeSequence]
        return None

    @LensesCodeSequence.setter
    def LensesCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._LensesCodeSequence = []
            if "LensesCodeSequence" in self._dataset:
                del self._dataset.LensesCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"LensesCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._LensesCodeSequence = value
            if "LensesCodeSequence" not in self._dataset:
                self._dataset.LensesCodeSequence = pydicom.Sequence()
            self._dataset.LensesCodeSequence.clear()
            self._dataset.LensesCodeSequence.extend([item.to_dataset() for item in value])

    def add_LensesCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._LensesCodeSequence.append(item)
        if "LensesCodeSequence" not in self._dataset:
            self._dataset.LensesCodeSequence = pydicom.Sequence()
        self._dataset.LensesCodeSequence.append(item.to_dataset())

    @property
    def ChannelDescriptionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ChannelDescriptionCodeSequence" in self._dataset:
            if len(self._ChannelDescriptionCodeSequence) == len(self._dataset.ChannelDescriptionCodeSequence):
                return self._ChannelDescriptionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ChannelDescriptionCodeSequence]
        return None

    @ChannelDescriptionCodeSequence.setter
    def ChannelDescriptionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ChannelDescriptionCodeSequence = []
            if "ChannelDescriptionCodeSequence" in self._dataset:
                del self._dataset.ChannelDescriptionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ChannelDescriptionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ChannelDescriptionCodeSequence = value
            if "ChannelDescriptionCodeSequence" not in self._dataset:
                self._dataset.ChannelDescriptionCodeSequence = pydicom.Sequence()
            self._dataset.ChannelDescriptionCodeSequence.clear()
            self._dataset.ChannelDescriptionCodeSequence.extend([item.to_dataset() for item in value])

    def add_ChannelDescriptionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ChannelDescriptionCodeSequence.append(item)
        if "ChannelDescriptionCodeSequence" not in self._dataset:
            self._dataset.ChannelDescriptionCodeSequence = pydicom.Sequence()
        self._dataset.ChannelDescriptionCodeSequence.append(item.to_dataset())

    @property
    def IlluminationWaveLength(self) -> Optional[float]:
        if "IlluminationWaveLength" in self._dataset:
            return self._dataset.IlluminationWaveLength
        return None

    @IlluminationWaveLength.setter
    def IlluminationWaveLength(self, value: Optional[float]):
        if value is None:
            if "IlluminationWaveLength" in self._dataset:
                del self._dataset.IlluminationWaveLength
        else:
            self._dataset.IlluminationWaveLength = value

    @property
    def ICCProfile(self) -> Optional[bytes]:
        if "ICCProfile" in self._dataset:
            return self._dataset.ICCProfile
        return None

    @ICCProfile.setter
    def ICCProfile(self, value: Optional[bytes]):
        if value is None:
            if "ICCProfile" in self._dataset:
                del self._dataset.ICCProfile
        else:
            self._dataset.ICCProfile = value

    @property
    def ColorSpace(self) -> Optional[str]:
        if "ColorSpace" in self._dataset:
            return self._dataset.ColorSpace
        return None

    @ColorSpace.setter
    def ColorSpace(self, value: Optional[str]):
        if value is None:
            if "ColorSpace" in self._dataset:
                del self._dataset.ColorSpace
        else:
            self._dataset.ColorSpace = value

    @property
    def IlluminatorTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "IlluminatorTypeCodeSequence" in self._dataset:
            if len(self._IlluminatorTypeCodeSequence) == len(self._dataset.IlluminatorTypeCodeSequence):
                return self._IlluminatorTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.IlluminatorTypeCodeSequence]
        return None

    @IlluminatorTypeCodeSequence.setter
    def IlluminatorTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._IlluminatorTypeCodeSequence = []
            if "IlluminatorTypeCodeSequence" in self._dataset:
                del self._dataset.IlluminatorTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"IlluminatorTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._IlluminatorTypeCodeSequence = value
            if "IlluminatorTypeCodeSequence" not in self._dataset:
                self._dataset.IlluminatorTypeCodeSequence = pydicom.Sequence()
            self._dataset.IlluminatorTypeCodeSequence.clear()
            self._dataset.IlluminatorTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_IlluminatorTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._IlluminatorTypeCodeSequence.append(item)
        if "IlluminatorTypeCodeSequence" not in self._dataset:
            self._dataset.IlluminatorTypeCodeSequence = pydicom.Sequence()
        self._dataset.IlluminatorTypeCodeSequence.append(item.to_dataset())

    @property
    def OpticalPathIdentifier(self) -> Optional[str]:
        if "OpticalPathIdentifier" in self._dataset:
            return self._dataset.OpticalPathIdentifier
        return None

    @OpticalPathIdentifier.setter
    def OpticalPathIdentifier(self, value: Optional[str]):
        if value is None:
            if "OpticalPathIdentifier" in self._dataset:
                del self._dataset.OpticalPathIdentifier
        else:
            self._dataset.OpticalPathIdentifier = value

    @property
    def OpticalPathDescription(self) -> Optional[str]:
        if "OpticalPathDescription" in self._dataset:
            return self._dataset.OpticalPathDescription
        return None

    @OpticalPathDescription.setter
    def OpticalPathDescription(self, value: Optional[str]):
        if value is None:
            if "OpticalPathDescription" in self._dataset:
                del self._dataset.OpticalPathDescription
        else:
            self._dataset.OpticalPathDescription = value

    @property
    def IlluminationColorCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "IlluminationColorCodeSequence" in self._dataset:
            if len(self._IlluminationColorCodeSequence) == len(self._dataset.IlluminationColorCodeSequence):
                return self._IlluminationColorCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.IlluminationColorCodeSequence]
        return None

    @IlluminationColorCodeSequence.setter
    def IlluminationColorCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._IlluminationColorCodeSequence = []
            if "IlluminationColorCodeSequence" in self._dataset:
                del self._dataset.IlluminationColorCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"IlluminationColorCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._IlluminationColorCodeSequence = value
            if "IlluminationColorCodeSequence" not in self._dataset:
                self._dataset.IlluminationColorCodeSequence = pydicom.Sequence()
            self._dataset.IlluminationColorCodeSequence.clear()
            self._dataset.IlluminationColorCodeSequence.extend([item.to_dataset() for item in value])

    def add_IlluminationColorCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._IlluminationColorCodeSequence.append(item)
        if "IlluminationColorCodeSequence" not in self._dataset:
            self._dataset.IlluminationColorCodeSequence = pydicom.Sequence()
        self._dataset.IlluminationColorCodeSequence.append(item.to_dataset())

    @property
    def CondenserLensPower(self) -> Optional[Decimal]:
        if "CondenserLensPower" in self._dataset:
            return self._dataset.CondenserLensPower
        return None

    @CondenserLensPower.setter
    def CondenserLensPower(self, value: Optional[Decimal]):
        if value is None:
            if "CondenserLensPower" in self._dataset:
                del self._dataset.CondenserLensPower
        else:
            self._dataset.CondenserLensPower = value

    @property
    def ObjectiveLensPower(self) -> Optional[Decimal]:
        if "ObjectiveLensPower" in self._dataset:
            return self._dataset.ObjectiveLensPower
        return None

    @ObjectiveLensPower.setter
    def ObjectiveLensPower(self, value: Optional[Decimal]):
        if value is None:
            if "ObjectiveLensPower" in self._dataset:
                del self._dataset.ObjectiveLensPower
        else:
            self._dataset.ObjectiveLensPower = value

    @property
    def ObjectiveLensNumericalAperture(self) -> Optional[Decimal]:
        if "ObjectiveLensNumericalAperture" in self._dataset:
            return self._dataset.ObjectiveLensNumericalAperture
        return None

    @ObjectiveLensNumericalAperture.setter
    def ObjectiveLensNumericalAperture(self, value: Optional[Decimal]):
        if value is None:
            if "ObjectiveLensNumericalAperture" in self._dataset:
                del self._dataset.ObjectiveLensNumericalAperture
        else:
            self._dataset.ObjectiveLensNumericalAperture = value

    @property
    def PaletteColorLookupTableSequence(self) -> Optional[List[PaletteColorLookupTableSequenceItem]]:
        if "PaletteColorLookupTableSequence" in self._dataset:
            if len(self._PaletteColorLookupTableSequence) == len(self._dataset.PaletteColorLookupTableSequence):
                return self._PaletteColorLookupTableSequence
            else:
                return [PaletteColorLookupTableSequenceItem(x) for x in self._dataset.PaletteColorLookupTableSequence]
        return None

    @PaletteColorLookupTableSequence.setter
    def PaletteColorLookupTableSequence(self, value: Optional[List[PaletteColorLookupTableSequenceItem]]):
        if value is None:
            self._PaletteColorLookupTableSequence = []
            if "PaletteColorLookupTableSequence" in self._dataset:
                del self._dataset.PaletteColorLookupTableSequence
        elif not isinstance(value, list) or not all(isinstance(item, PaletteColorLookupTableSequenceItem) for item in value):
            raise ValueError(f"PaletteColorLookupTableSequence must be a list of PaletteColorLookupTableSequenceItem objects")
        else:
            self._PaletteColorLookupTableSequence = value
            if "PaletteColorLookupTableSequence" not in self._dataset:
                self._dataset.PaletteColorLookupTableSequence = pydicom.Sequence()
            self._dataset.PaletteColorLookupTableSequence.clear()
            self._dataset.PaletteColorLookupTableSequence.extend([item.to_dataset() for item in value])

    def add_PaletteColorLookupTable(self, item: PaletteColorLookupTableSequenceItem):
        if not isinstance(item, PaletteColorLookupTableSequenceItem):
            raise ValueError(f"Item must be an instance of PaletteColorLookupTableSequenceItem")
        self._PaletteColorLookupTableSequence.append(item)
        if "PaletteColorLookupTableSequence" not in self._dataset:
            self._dataset.PaletteColorLookupTableSequence = pydicom.Sequence()
        self._dataset.PaletteColorLookupTableSequence.append(item.to_dataset())
