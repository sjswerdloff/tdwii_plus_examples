from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class ConstraintValueSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SelectorAEValue(self) -> Optional[List[str]]:
        if "SelectorAEValue" in self._dataset:
            return self._dataset.SelectorAEValue
        return None

    @SelectorAEValue.setter
    def SelectorAEValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorAEValue" in self._dataset:
                del self._dataset.SelectorAEValue
        else:
            self._dataset.SelectorAEValue = value

    @property
    def SelectorASValue(self) -> Optional[List[str]]:
        if "SelectorASValue" in self._dataset:
            return self._dataset.SelectorASValue
        return None

    @SelectorASValue.setter
    def SelectorASValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorASValue" in self._dataset:
                del self._dataset.SelectorASValue
        else:
            self._dataset.SelectorASValue = value

    @property
    def SelectorATValue(self) -> Optional[List[int]]:
        if "SelectorATValue" in self._dataset:
            return self._dataset.SelectorATValue
        return None

    @SelectorATValue.setter
    def SelectorATValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorATValue" in self._dataset:
                del self._dataset.SelectorATValue
        else:
            self._dataset.SelectorATValue = value

    @property
    def SelectorDAValue(self) -> Optional[List[str]]:
        if "SelectorDAValue" in self._dataset:
            return self._dataset.SelectorDAValue
        return None

    @SelectorDAValue.setter
    def SelectorDAValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorDAValue" in self._dataset:
                del self._dataset.SelectorDAValue
        else:
            self._dataset.SelectorDAValue = value

    @property
    def SelectorCSValue(self) -> Optional[List[str]]:
        if "SelectorCSValue" in self._dataset:
            return self._dataset.SelectorCSValue
        return None

    @SelectorCSValue.setter
    def SelectorCSValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorCSValue" in self._dataset:
                del self._dataset.SelectorCSValue
        else:
            self._dataset.SelectorCSValue = value

    @property
    def SelectorDTValue(self) -> Optional[List[str]]:
        if "SelectorDTValue" in self._dataset:
            return self._dataset.SelectorDTValue
        return None

    @SelectorDTValue.setter
    def SelectorDTValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorDTValue" in self._dataset:
                del self._dataset.SelectorDTValue
        else:
            self._dataset.SelectorDTValue = value

    @property
    def SelectorISValue(self) -> Optional[List[int]]:
        if "SelectorISValue" in self._dataset:
            return self._dataset.SelectorISValue
        return None

    @SelectorISValue.setter
    def SelectorISValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorISValue" in self._dataset:
                del self._dataset.SelectorISValue
        else:
            self._dataset.SelectorISValue = value

    @property
    def SelectorOBValue(self) -> Optional[bytes]:
        if "SelectorOBValue" in self._dataset:
            return self._dataset.SelectorOBValue
        return None

    @SelectorOBValue.setter
    def SelectorOBValue(self, value: Optional[bytes]):
        if value is None:
            if "SelectorOBValue" in self._dataset:
                del self._dataset.SelectorOBValue
        else:
            self._dataset.SelectorOBValue = value

    @property
    def SelectorLOValue(self) -> Optional[List[str]]:
        if "SelectorLOValue" in self._dataset:
            return self._dataset.SelectorLOValue
        return None

    @SelectorLOValue.setter
    def SelectorLOValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorLOValue" in self._dataset:
                del self._dataset.SelectorLOValue
        else:
            self._dataset.SelectorLOValue = value

    @property
    def SelectorOFValue(self) -> Optional[bytes]:
        if "SelectorOFValue" in self._dataset:
            return self._dataset.SelectorOFValue
        return None

    @SelectorOFValue.setter
    def SelectorOFValue(self, value: Optional[bytes]):
        if value is None:
            if "SelectorOFValue" in self._dataset:
                del self._dataset.SelectorOFValue
        else:
            self._dataset.SelectorOFValue = value

    @property
    def SelectorLTValue(self) -> Optional[str]:
        if "SelectorLTValue" in self._dataset:
            return self._dataset.SelectorLTValue
        return None

    @SelectorLTValue.setter
    def SelectorLTValue(self, value: Optional[str]):
        if value is None:
            if "SelectorLTValue" in self._dataset:
                del self._dataset.SelectorLTValue
        else:
            self._dataset.SelectorLTValue = value

    @property
    def SelectorOWValue(self) -> Optional[bytes]:
        if "SelectorOWValue" in self._dataset:
            return self._dataset.SelectorOWValue
        return None

    @SelectorOWValue.setter
    def SelectorOWValue(self, value: Optional[bytes]):
        if value is None:
            if "SelectorOWValue" in self._dataset:
                del self._dataset.SelectorOWValue
        else:
            self._dataset.SelectorOWValue = value

    @property
    def SelectorPNValue(self) -> Optional[List[str]]:
        if "SelectorPNValue" in self._dataset:
            return self._dataset.SelectorPNValue
        return None

    @SelectorPNValue.setter
    def SelectorPNValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorPNValue" in self._dataset:
                del self._dataset.SelectorPNValue
        else:
            self._dataset.SelectorPNValue = value

    @property
    def SelectorTMValue(self) -> Optional[List[str]]:
        if "SelectorTMValue" in self._dataset:
            return self._dataset.SelectorTMValue
        return None

    @SelectorTMValue.setter
    def SelectorTMValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorTMValue" in self._dataset:
                del self._dataset.SelectorTMValue
        else:
            self._dataset.SelectorTMValue = value

    @property
    def SelectorSHValue(self) -> Optional[List[str]]:
        if "SelectorSHValue" in self._dataset:
            return self._dataset.SelectorSHValue
        return None

    @SelectorSHValue.setter
    def SelectorSHValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorSHValue" in self._dataset:
                del self._dataset.SelectorSHValue
        else:
            self._dataset.SelectorSHValue = value

    @property
    def SelectorUNValue(self) -> Optional[bytes]:
        if "SelectorUNValue" in self._dataset:
            return self._dataset.SelectorUNValue
        return None

    @SelectorUNValue.setter
    def SelectorUNValue(self, value: Optional[bytes]):
        if value is None:
            if "SelectorUNValue" in self._dataset:
                del self._dataset.SelectorUNValue
        else:
            self._dataset.SelectorUNValue = value

    @property
    def SelectorSTValue(self) -> Optional[str]:
        if "SelectorSTValue" in self._dataset:
            return self._dataset.SelectorSTValue
        return None

    @SelectorSTValue.setter
    def SelectorSTValue(self, value: Optional[str]):
        if value is None:
            if "SelectorSTValue" in self._dataset:
                del self._dataset.SelectorSTValue
        else:
            self._dataset.SelectorSTValue = value

    @property
    def SelectorUCValue(self) -> Optional[List[str]]:
        if "SelectorUCValue" in self._dataset:
            return self._dataset.SelectorUCValue
        return None

    @SelectorUCValue.setter
    def SelectorUCValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorUCValue" in self._dataset:
                del self._dataset.SelectorUCValue
        else:
            self._dataset.SelectorUCValue = value

    @property
    def SelectorUTValue(self) -> Optional[str]:
        if "SelectorUTValue" in self._dataset:
            return self._dataset.SelectorUTValue
        return None

    @SelectorUTValue.setter
    def SelectorUTValue(self, value: Optional[str]):
        if value is None:
            if "SelectorUTValue" in self._dataset:
                del self._dataset.SelectorUTValue
        else:
            self._dataset.SelectorUTValue = value

    @property
    def SelectorURValue(self) -> Optional[str]:
        if "SelectorURValue" in self._dataset:
            return self._dataset.SelectorURValue
        return None

    @SelectorURValue.setter
    def SelectorURValue(self, value: Optional[str]):
        if value is None:
            if "SelectorURValue" in self._dataset:
                del self._dataset.SelectorURValue
        else:
            self._dataset.SelectorURValue = value

    @property
    def SelectorDSValue(self) -> Optional[List[Decimal]]:
        if "SelectorDSValue" in self._dataset:
            return self._dataset.SelectorDSValue
        return None

    @SelectorDSValue.setter
    def SelectorDSValue(self, value: Optional[List[Decimal]]):
        if value is None:
            if "SelectorDSValue" in self._dataset:
                del self._dataset.SelectorDSValue
        else:
            self._dataset.SelectorDSValue = value

    @property
    def SelectorODValue(self) -> Optional[bytes]:
        if "SelectorODValue" in self._dataset:
            return self._dataset.SelectorODValue
        return None

    @SelectorODValue.setter
    def SelectorODValue(self, value: Optional[bytes]):
        if value is None:
            if "SelectorODValue" in self._dataset:
                del self._dataset.SelectorODValue
        else:
            self._dataset.SelectorODValue = value

    @property
    def SelectorFDValue(self) -> Optional[List[float]]:
        if "SelectorFDValue" in self._dataset:
            return self._dataset.SelectorFDValue
        return None

    @SelectorFDValue.setter
    def SelectorFDValue(self, value: Optional[List[float]]):
        if value is None:
            if "SelectorFDValue" in self._dataset:
                del self._dataset.SelectorFDValue
        else:
            self._dataset.SelectorFDValue = value

    @property
    def SelectorOLValue(self) -> Optional[bytes]:
        if "SelectorOLValue" in self._dataset:
            return self._dataset.SelectorOLValue
        return None

    @SelectorOLValue.setter
    def SelectorOLValue(self, value: Optional[bytes]):
        if value is None:
            if "SelectorOLValue" in self._dataset:
                del self._dataset.SelectorOLValue
        else:
            self._dataset.SelectorOLValue = value

    @property
    def SelectorFLValue(self) -> Optional[List[float]]:
        if "SelectorFLValue" in self._dataset:
            return self._dataset.SelectorFLValue
        return None

    @SelectorFLValue.setter
    def SelectorFLValue(self, value: Optional[List[float]]):
        if value is None:
            if "SelectorFLValue" in self._dataset:
                del self._dataset.SelectorFLValue
        else:
            self._dataset.SelectorFLValue = value

    @property
    def SelectorULValue(self) -> Optional[List[int]]:
        if "SelectorULValue" in self._dataset:
            return self._dataset.SelectorULValue
        return None

    @SelectorULValue.setter
    def SelectorULValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorULValue" in self._dataset:
                del self._dataset.SelectorULValue
        else:
            self._dataset.SelectorULValue = value

    @property
    def SelectorUSValue(self) -> Optional[List[int]]:
        if "SelectorUSValue" in self._dataset:
            return self._dataset.SelectorUSValue
        return None

    @SelectorUSValue.setter
    def SelectorUSValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorUSValue" in self._dataset:
                del self._dataset.SelectorUSValue
        else:
            self._dataset.SelectorUSValue = value

    @property
    def SelectorSLValue(self) -> Optional[List[int]]:
        if "SelectorSLValue" in self._dataset:
            return self._dataset.SelectorSLValue
        return None

    @SelectorSLValue.setter
    def SelectorSLValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSLValue" in self._dataset:
                del self._dataset.SelectorSLValue
        else:
            self._dataset.SelectorSLValue = value

    @property
    def SelectorSSValue(self) -> Optional[List[int]]:
        if "SelectorSSValue" in self._dataset:
            return self._dataset.SelectorSSValue
        return None

    @SelectorSSValue.setter
    def SelectorSSValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSSValue" in self._dataset:
                del self._dataset.SelectorSSValue
        else:
            self._dataset.SelectorSSValue = value

    @property
    def SelectorUIValue(self) -> Optional[List[str]]:
        if "SelectorUIValue" in self._dataset:
            return self._dataset.SelectorUIValue
        return None

    @SelectorUIValue.setter
    def SelectorUIValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorUIValue" in self._dataset:
                del self._dataset.SelectorUIValue
        else:
            self._dataset.SelectorUIValue = value

    @property
    def SelectorCodeSequenceValue(self) -> Optional[list]:
        if "SelectorCodeSequenceValue" in self._dataset:
            return self._dataset.SelectorCodeSequenceValue
        return None

    @SelectorCodeSequenceValue.setter
    def SelectorCodeSequenceValue(self, value: Optional[list]):
        if value is None:
            if "SelectorCodeSequenceValue" in self._dataset:
                del self._dataset.SelectorCodeSequenceValue
        else:
            self._dataset.SelectorCodeSequenceValue = value

    @property
    def SelectorOVValue(self) -> Optional[bytes]:
        if "SelectorOVValue" in self._dataset:
            return self._dataset.SelectorOVValue
        return None

    @SelectorOVValue.setter
    def SelectorOVValue(self, value: Optional[bytes]):
        if value is None:
            if "SelectorOVValue" in self._dataset:
                del self._dataset.SelectorOVValue
        else:
            self._dataset.SelectorOVValue = value

    @property
    def SelectorSVValue(self) -> Optional[List[int]]:
        if "SelectorSVValue" in self._dataset:
            return self._dataset.SelectorSVValue
        return None

    @SelectorSVValue.setter
    def SelectorSVValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSVValue" in self._dataset:
                del self._dataset.SelectorSVValue
        else:
            self._dataset.SelectorSVValue = value

    @property
    def SelectorUVValue(self) -> Optional[List[int]]:
        if "SelectorUVValue" in self._dataset:
            return self._dataset.SelectorUVValue
        return None

    @SelectorUVValue.setter
    def SelectorUVValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorUVValue" in self._dataset:
                del self._dataset.SelectorUVValue
        else:
            self._dataset.SelectorUVValue = value
