from typing import Any, List, Optional

import pydicom


class PaletteColorLookupTableSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def PaletteColorLookupTableUID(self) -> Optional[str]:
        if "PaletteColorLookupTableUID" in self._dataset:
            return self._dataset.PaletteColorLookupTableUID
        return None

    @PaletteColorLookupTableUID.setter
    def PaletteColorLookupTableUID(self, value: Optional[str]):
        if value is None:
            if "PaletteColorLookupTableUID" in self._dataset:
                del self._dataset.PaletteColorLookupTableUID
        else:
            self._dataset.PaletteColorLookupTableUID = value

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
    def SegmentedRedPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "SegmentedRedPaletteColorLookupTableData" in self._dataset:
            return self._dataset.SegmentedRedPaletteColorLookupTableData
        return None

    @SegmentedRedPaletteColorLookupTableData.setter
    def SegmentedRedPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "SegmentedRedPaletteColorLookupTableData" in self._dataset:
                del self._dataset.SegmentedRedPaletteColorLookupTableData
        else:
            self._dataset.SegmentedRedPaletteColorLookupTableData = value

    @property
    def SegmentedGreenPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "SegmentedGreenPaletteColorLookupTableData" in self._dataset:
            return self._dataset.SegmentedGreenPaletteColorLookupTableData
        return None

    @SegmentedGreenPaletteColorLookupTableData.setter
    def SegmentedGreenPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "SegmentedGreenPaletteColorLookupTableData" in self._dataset:
                del self._dataset.SegmentedGreenPaletteColorLookupTableData
        else:
            self._dataset.SegmentedGreenPaletteColorLookupTableData = value

    @property
    def SegmentedBluePaletteColorLookupTableData(self) -> Optional[bytes]:
        if "SegmentedBluePaletteColorLookupTableData" in self._dataset:
            return self._dataset.SegmentedBluePaletteColorLookupTableData
        return None

    @SegmentedBluePaletteColorLookupTableData.setter
    def SegmentedBluePaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "SegmentedBluePaletteColorLookupTableData" in self._dataset:
                del self._dataset.SegmentedBluePaletteColorLookupTableData
        else:
            self._dataset.SegmentedBluePaletteColorLookupTableData = value
