from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .x_ray_filter_sequence_item import XRayFilterSequenceItem


class RTImageFramekVRadiationAcquisitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._XRayFilterSequence: List[XRayFilterSequenceItem] = []
        self._EnergyDerivationCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

    @property
    def AveragePulseWidth(self) -> Optional[Decimal]:
        if "AveragePulseWidth" in self._dataset:
            return self._dataset.AveragePulseWidth
        return None

    @AveragePulseWidth.setter
    def AveragePulseWidth(self, value: Optional[Decimal]):
        if value is None:
            if "AveragePulseWidth" in self._dataset:
                del self._dataset.AveragePulseWidth
        else:
            self._dataset.AveragePulseWidth = value

    @property
    def RadiationMode(self) -> Optional[str]:
        if "RadiationMode" in self._dataset:
            return self._dataset.RadiationMode
        return None

    @RadiationMode.setter
    def RadiationMode(self, value: Optional[str]):
        if value is None:
            if "RadiationMode" in self._dataset:
                del self._dataset.RadiationMode
        else:
            self._dataset.RadiationMode = value

    @property
    def ExposureTimeInuS(self) -> Optional[Decimal]:
        if "ExposureTimeInuS" in self._dataset:
            return self._dataset.ExposureTimeInuS
        return None

    @ExposureTimeInuS.setter
    def ExposureTimeInuS(self, value: Optional[Decimal]):
        if value is None:
            if "ExposureTimeInuS" in self._dataset:
                del self._dataset.ExposureTimeInuS
        else:
            self._dataset.ExposureTimeInuS = value

    @property
    def XRayTubeCurrentInuA(self) -> Optional[Decimal]:
        if "XRayTubeCurrentInuA" in self._dataset:
            return self._dataset.XRayTubeCurrentInuA
        return None

    @XRayTubeCurrentInuA.setter
    def XRayTubeCurrentInuA(self, value: Optional[Decimal]):
        if value is None:
            if "XRayTubeCurrentInuA" in self._dataset:
                del self._dataset.XRayTubeCurrentInuA
        else:
            self._dataset.XRayTubeCurrentInuA = value

    @property
    def XRayFilterSequence(self) -> Optional[List[XRayFilterSequenceItem]]:
        if "XRayFilterSequence" in self._dataset:
            if len(self._XRayFilterSequence) == len(self._dataset.XRayFilterSequence):
                return self._XRayFilterSequence
            else:
                return [XRayFilterSequenceItem(x) for x in self._dataset.XRayFilterSequence]
        return None

    @XRayFilterSequence.setter
    def XRayFilterSequence(self, value: Optional[List[XRayFilterSequenceItem]]):
        if value is None:
            self._XRayFilterSequence = []
            if "XRayFilterSequence" in self._dataset:
                del self._dataset.XRayFilterSequence
        elif not isinstance(value, list) or not all(isinstance(item, XRayFilterSequenceItem) for item in value):
            raise ValueError(f"XRayFilterSequence must be a list of XRayFilterSequenceItem objects")
        else:
            self._XRayFilterSequence = value
            if "XRayFilterSequence" not in self._dataset:
                self._dataset.XRayFilterSequence = pydicom.Sequence()
            self._dataset.XRayFilterSequence.clear()
            self._dataset.XRayFilterSequence.extend([item.to_dataset() for item in value])

    def add_XRayFilter(self, item: XRayFilterSequenceItem):
        if not isinstance(item, XRayFilterSequenceItem):
            raise ValueError(f"Item must be an instance of XRayFilterSequenceItem")
        self._XRayFilterSequence.append(item)
        if "XRayFilterSequence" not in self._dataset:
            self._dataset.XRayFilterSequence = pydicom.Sequence()
        self._dataset.XRayFilterSequence.append(item.to_dataset())

    @property
    def EnergyDerivationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "EnergyDerivationCodeSequence" in self._dataset:
            if len(self._EnergyDerivationCodeSequence) == len(self._dataset.EnergyDerivationCodeSequence):
                return self._EnergyDerivationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.EnergyDerivationCodeSequence]
        return None

    @EnergyDerivationCodeSequence.setter
    def EnergyDerivationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EnergyDerivationCodeSequence = []
            if "EnergyDerivationCodeSequence" in self._dataset:
                del self._dataset.EnergyDerivationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"EnergyDerivationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EnergyDerivationCodeSequence = value
            if "EnergyDerivationCodeSequence" not in self._dataset:
                self._dataset.EnergyDerivationCodeSequence = pydicom.Sequence()
            self._dataset.EnergyDerivationCodeSequence.clear()
            self._dataset.EnergyDerivationCodeSequence.extend([item.to_dataset() for item in value])

    def add_EnergyDerivationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._EnergyDerivationCodeSequence.append(item)
        if "EnergyDerivationCodeSequence" not in self._dataset:
            self._dataset.EnergyDerivationCodeSequence = pydicom.Sequence()
        self._dataset.EnergyDerivationCodeSequence.append(item.to_dataset())
