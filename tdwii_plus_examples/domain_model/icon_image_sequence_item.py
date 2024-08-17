from typing import Any, List, Optional  # noqa

import pydicom


class IconImageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SamplesPerPixel(self) -> Optional[int]:
        if "SamplesPerPixel" in self._dataset:
            return self._dataset.SamplesPerPixel
        return None

    @SamplesPerPixel.setter
    def SamplesPerPixel(self, value: Optional[int]):
        if value is None:
            if "SamplesPerPixel" in self._dataset:
                del self._dataset.SamplesPerPixel
        else:
            self._dataset.SamplesPerPixel = value

    @property
    def PhotometricInterpretation(self) -> Optional[str]:
        if "PhotometricInterpretation" in self._dataset:
            return self._dataset.PhotometricInterpretation
        return None

    @PhotometricInterpretation.setter
    def PhotometricInterpretation(self, value: Optional[str]):
        if value is None:
            if "PhotometricInterpretation" in self._dataset:
                del self._dataset.PhotometricInterpretation
        else:
            self._dataset.PhotometricInterpretation = value

    @property
    def PlanarConfiguration(self) -> Optional[int]:
        if "PlanarConfiguration" in self._dataset:
            return self._dataset.PlanarConfiguration
        return None

    @PlanarConfiguration.setter
    def PlanarConfiguration(self, value: Optional[int]):
        if value is None:
            if "PlanarConfiguration" in self._dataset:
                del self._dataset.PlanarConfiguration
        else:
            self._dataset.PlanarConfiguration = value

    @property
    def Rows(self) -> Optional[int]:
        if "Rows" in self._dataset:
            return self._dataset.Rows
        return None

    @Rows.setter
    def Rows(self, value: Optional[int]):
        if value is None:
            if "Rows" in self._dataset:
                del self._dataset.Rows
        else:
            self._dataset.Rows = value

    @property
    def Columns(self) -> Optional[int]:
        if "Columns" in self._dataset:
            return self._dataset.Columns
        return None

    @Columns.setter
    def Columns(self, value: Optional[int]):
        if value is None:
            if "Columns" in self._dataset:
                del self._dataset.Columns
        else:
            self._dataset.Columns = value

    @property
    def PixelAspectRatio(self) -> Optional[List[int]]:
        if "PixelAspectRatio" in self._dataset:
            return self._dataset.PixelAspectRatio
        return None

    @PixelAspectRatio.setter
    def PixelAspectRatio(self, value: Optional[List[int]]):
        if value is None:
            if "PixelAspectRatio" in self._dataset:
                del self._dataset.PixelAspectRatio
        else:
            self._dataset.PixelAspectRatio = value

    @property
    def BitsAllocated(self) -> Optional[int]:
        if "BitsAllocated" in self._dataset:
            return self._dataset.BitsAllocated
        return None

    @BitsAllocated.setter
    def BitsAllocated(self, value: Optional[int]):
        if value is None:
            if "BitsAllocated" in self._dataset:
                del self._dataset.BitsAllocated
        else:
            self._dataset.BitsAllocated = value

    @property
    def BitsStored(self) -> Optional[int]:
        if "BitsStored" in self._dataset:
            return self._dataset.BitsStored
        return None

    @BitsStored.setter
    def BitsStored(self, value: Optional[int]):
        if value is None:
            if "BitsStored" in self._dataset:
                del self._dataset.BitsStored
        else:
            self._dataset.BitsStored = value

    @property
    def HighBit(self) -> Optional[int]:
        if "HighBit" in self._dataset:
            return self._dataset.HighBit
        return None

    @HighBit.setter
    def HighBit(self, value: Optional[int]):
        if value is None:
            if "HighBit" in self._dataset:
                del self._dataset.HighBit
        else:
            self._dataset.HighBit = value

    @property
    def PixelRepresentation(self) -> Optional[int]:
        if "PixelRepresentation" in self._dataset:
            return self._dataset.PixelRepresentation
        return None

    @PixelRepresentation.setter
    def PixelRepresentation(self, value: Optional[int]):
        if value is None:
            if "PixelRepresentation" in self._dataset:
                del self._dataset.PixelRepresentation
        else:
            self._dataset.PixelRepresentation = value

    @property
    def SmallestImagePixelValue(self) -> Optional[int]:
        if "SmallestImagePixelValue" in self._dataset:
            return self._dataset.SmallestImagePixelValue
        return None

    @SmallestImagePixelValue.setter
    def SmallestImagePixelValue(self, value: Optional[int]):
        if value is None:
            if "SmallestImagePixelValue" in self._dataset:
                del self._dataset.SmallestImagePixelValue
        else:
            self._dataset.SmallestImagePixelValue = value

    @property
    def LargestImagePixelValue(self) -> Optional[int]:
        if "LargestImagePixelValue" in self._dataset:
            return self._dataset.LargestImagePixelValue
        return None

    @LargestImagePixelValue.setter
    def LargestImagePixelValue(self, value: Optional[int]):
        if value is None:
            if "LargestImagePixelValue" in self._dataset:
                del self._dataset.LargestImagePixelValue
        else:
            self._dataset.LargestImagePixelValue = value

    @property
    def RedPaletteColorLookupTableDescriptor(self) -> Optional[List[int]]:
        if "RedPaletteColorLookupTableDescriptor" in self._dataset:
            return self._dataset.RedPaletteColorLookupTableDescriptor
        return None

    @RedPaletteColorLookupTableDescriptor.setter
    def RedPaletteColorLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "RedPaletteColorLookupTableDescriptor" in self._dataset:
                del self._dataset.RedPaletteColorLookupTableDescriptor
        else:
            self._dataset.RedPaletteColorLookupTableDescriptor = value

    @property
    def GreenPaletteColorLookupTableDescriptor(self) -> Optional[List[int]]:
        if "GreenPaletteColorLookupTableDescriptor" in self._dataset:
            return self._dataset.GreenPaletteColorLookupTableDescriptor
        return None

    @GreenPaletteColorLookupTableDescriptor.setter
    def GreenPaletteColorLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "GreenPaletteColorLookupTableDescriptor" in self._dataset:
                del self._dataset.GreenPaletteColorLookupTableDescriptor
        else:
            self._dataset.GreenPaletteColorLookupTableDescriptor = value

    @property
    def BluePaletteColorLookupTableDescriptor(self) -> Optional[List[int]]:
        if "BluePaletteColorLookupTableDescriptor" in self._dataset:
            return self._dataset.BluePaletteColorLookupTableDescriptor
        return None

    @BluePaletteColorLookupTableDescriptor.setter
    def BluePaletteColorLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "BluePaletteColorLookupTableDescriptor" in self._dataset:
                del self._dataset.BluePaletteColorLookupTableDescriptor
        else:
            self._dataset.BluePaletteColorLookupTableDescriptor = value

    @property
    def RedPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "RedPaletteColorLookupTableData" in self._dataset:
            return self._dataset.RedPaletteColorLookupTableData
        return None

    @RedPaletteColorLookupTableData.setter
    def RedPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "RedPaletteColorLookupTableData" in self._dataset:
                del self._dataset.RedPaletteColorLookupTableData
        else:
            self._dataset.RedPaletteColorLookupTableData = value

    @property
    def GreenPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "GreenPaletteColorLookupTableData" in self._dataset:
            return self._dataset.GreenPaletteColorLookupTableData
        return None

    @GreenPaletteColorLookupTableData.setter
    def GreenPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "GreenPaletteColorLookupTableData" in self._dataset:
                del self._dataset.GreenPaletteColorLookupTableData
        else:
            self._dataset.GreenPaletteColorLookupTableData = value

    @property
    def BluePaletteColorLookupTableData(self) -> Optional[bytes]:
        if "BluePaletteColorLookupTableData" in self._dataset:
            return self._dataset.BluePaletteColorLookupTableData
        return None

    @BluePaletteColorLookupTableData.setter
    def BluePaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "BluePaletteColorLookupTableData" in self._dataset:
                del self._dataset.BluePaletteColorLookupTableData
        else:
            self._dataset.BluePaletteColorLookupTableData = value

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
    def PixelData(self) -> Optional[bytes]:
        if "PixelData" in self._dataset:
            return self._dataset.PixelData
        return None

    @PixelData.setter
    def PixelData(self, value: Optional[bytes]):
        if value is None:
            if "PixelData" in self._dataset:
                del self._dataset.PixelData
        else:
            self._dataset.PixelData = value
