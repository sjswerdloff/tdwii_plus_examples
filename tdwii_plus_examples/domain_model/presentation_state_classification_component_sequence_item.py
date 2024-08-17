from typing import Any, List, Optional  # noqa

import pydicom

from .component_input_sequence_item import ComponentInputSequenceItem


class PresentationStateClassificationComponentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ComponentInputSequence: List[ComponentInputSequenceItem] = []

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

    @property
    def SegmentedAlphaPaletteColorLookupTableData(self) -> Optional[bytes]:
        if "SegmentedAlphaPaletteColorLookupTableData" in self._dataset:
            return self._dataset.SegmentedAlphaPaletteColorLookupTableData
        return None

    @SegmentedAlphaPaletteColorLookupTableData.setter
    def SegmentedAlphaPaletteColorLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "SegmentedAlphaPaletteColorLookupTableData" in self._dataset:
                del self._dataset.SegmentedAlphaPaletteColorLookupTableData
        else:
            self._dataset.SegmentedAlphaPaletteColorLookupTableData = value

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

    @property
    def ComponentType(self) -> Optional[str]:
        if "ComponentType" in self._dataset:
            return self._dataset.ComponentType
        return None

    @ComponentType.setter
    def ComponentType(self, value: Optional[str]):
        if value is None:
            if "ComponentType" in self._dataset:
                del self._dataset.ComponentType
        else:
            self._dataset.ComponentType = value

    @property
    def ComponentInputSequence(self) -> Optional[List[ComponentInputSequenceItem]]:
        if "ComponentInputSequence" in self._dataset:
            if len(self._ComponentInputSequence) == len(self._dataset.ComponentInputSequence):
                return self._ComponentInputSequence
            else:
                return [ComponentInputSequenceItem(x) for x in self._dataset.ComponentInputSequence]
        return None

    @ComponentInputSequence.setter
    def ComponentInputSequence(self, value: Optional[List[ComponentInputSequenceItem]]):
        if value is None:
            self._ComponentInputSequence = []
            if "ComponentInputSequence" in self._dataset:
                del self._dataset.ComponentInputSequence
        elif not isinstance(value, list) or not all(isinstance(item, ComponentInputSequenceItem) for item in value):
            raise ValueError("ComponentInputSequence must be a list of ComponentInputSequenceItem objects")
        else:
            self._ComponentInputSequence = value
            if "ComponentInputSequence" not in self._dataset:
                self._dataset.ComponentInputSequence = pydicom.Sequence()
            self._dataset.ComponentInputSequence.clear()
            self._dataset.ComponentInputSequence.extend([item.to_dataset() for item in value])

    def add_ComponentInput(self, item: ComponentInputSequenceItem):
        if not isinstance(item, ComponentInputSequenceItem):
            raise ValueError("Item must be an instance of ComponentInputSequenceItem")
        self._ComponentInputSequence.append(item)
        if "ComponentInputSequence" not in self._dataset:
            self._dataset.ComponentInputSequence = pydicom.Sequence()
        self._dataset.ComponentInputSequence.append(item.to_dataset())

    @property
    def RGBATransferFunctionDescription(self) -> Optional[str]:
        if "RGBATransferFunctionDescription" in self._dataset:
            return self._dataset.RGBATransferFunctionDescription
        return None

    @RGBATransferFunctionDescription.setter
    def RGBATransferFunctionDescription(self, value: Optional[str]):
        if value is None:
            if "RGBATransferFunctionDescription" in self._dataset:
                del self._dataset.RGBATransferFunctionDescription
        else:
            self._dataset.RGBATransferFunctionDescription = value
