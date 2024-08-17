from typing import Any, List, Optional  # noqa

import pydicom


class EnhancedPaletteColorLookupTableSequenceItem:
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
    def AlphaPaletteColorLookupTableDescriptor(self) -> Optional[List[int]]:
        if "AlphaPaletteColorLookupTableDescriptor" in self._dataset:
            return self._dataset.AlphaPaletteColorLookupTableDescriptor
        return None

    @AlphaPaletteColorLookupTableDescriptor.setter
    def AlphaPaletteColorLookupTableDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "AlphaPaletteColorLookupTableDescriptor" in self._dataset:
                del self._dataset.AlphaPaletteColorLookupTableDescriptor
        else:
            self._dataset.AlphaPaletteColorLookupTableDescriptor = value

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
    def AlphaPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "AlphaPaletteColorLookupTableData" in self._dataset:
            return self._dataset.AlphaPaletteColorLookupTableData
        return None

    @AlphaPaletteColorLookupTableData.setter
    def AlphaPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "AlphaPaletteColorLookupTableData" in self._dataset:
                del self._dataset.AlphaPaletteColorLookupTableData
        else:
            self._dataset.AlphaPaletteColorLookupTableData = value

    @property
    def DataPathID(self) -> Optional[str]:
        if "DataPathID" in self._dataset:
            return self._dataset.DataPathID
        return None

    @DataPathID.setter
    def DataPathID(self, value: Optional[str]):
        if value is None:
            if "DataPathID" in self._dataset:
                del self._dataset.DataPathID
        else:
            self._dataset.DataPathID = value

    @property
    def RGBLUTTransferFunction(self) -> Optional[str]:
        if "RGBLUTTransferFunction" in self._dataset:
            return self._dataset.RGBLUTTransferFunction
        return None

    @RGBLUTTransferFunction.setter
    def RGBLUTTransferFunction(self, value: Optional[str]):
        if value is None:
            if "RGBLUTTransferFunction" in self._dataset:
                del self._dataset.RGBLUTTransferFunction
        else:
            self._dataset.RGBLUTTransferFunction = value

    @property
    def AlphaLUTTransferFunction(self) -> Optional[str]:
        if "AlphaLUTTransferFunction" in self._dataset:
            return self._dataset.AlphaLUTTransferFunction
        return None

    @AlphaLUTTransferFunction.setter
    def AlphaLUTTransferFunction(self, value: Optional[str]):
        if value is None:
            if "AlphaLUTTransferFunction" in self._dataset:
                del self._dataset.AlphaLUTTransferFunction
        else:
            self._dataset.AlphaLUTTransferFunction = value
