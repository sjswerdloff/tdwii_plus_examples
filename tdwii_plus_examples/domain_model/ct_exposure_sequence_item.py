from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class CTExposureSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._WaterEquivalentDiameterCalculationMethodCodeSequence: List[CodeSequenceItem] = []
        self._CTDIPhantomTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImageAndFluoroscopyAreaDoseProduct(self) -> Optional[Decimal]:
        if "ImageAndFluoroscopyAreaDoseProduct" in self._dataset:
            return self._dataset.ImageAndFluoroscopyAreaDoseProduct
        return None

    @ImageAndFluoroscopyAreaDoseProduct.setter
    def ImageAndFluoroscopyAreaDoseProduct(self, value: Optional[Decimal]):
        if value is None:
            if "ImageAndFluoroscopyAreaDoseProduct" in self._dataset:
                del self._dataset.ImageAndFluoroscopyAreaDoseProduct
        else:
            self._dataset.ImageAndFluoroscopyAreaDoseProduct = value

    @property
    def WaterEquivalentDiameter(self) -> Optional[float]:
        if "WaterEquivalentDiameter" in self._dataset:
            return self._dataset.WaterEquivalentDiameter
        return None

    @WaterEquivalentDiameter.setter
    def WaterEquivalentDiameter(self, value: Optional[float]):
        if value is None:
            if "WaterEquivalentDiameter" in self._dataset:
                del self._dataset.WaterEquivalentDiameter
        else:
            self._dataset.WaterEquivalentDiameter = value

    @property
    def WaterEquivalentDiameterCalculationMethodCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "WaterEquivalentDiameterCalculationMethodCodeSequence" in self._dataset:
            if len(self._WaterEquivalentDiameterCalculationMethodCodeSequence) == len(
                self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence
            ):
                return self._WaterEquivalentDiameterCalculationMethodCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence]
        return None

    @WaterEquivalentDiameterCalculationMethodCodeSequence.setter
    def WaterEquivalentDiameterCalculationMethodCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._WaterEquivalentDiameterCalculationMethodCodeSequence = []
            if "WaterEquivalentDiameterCalculationMethodCodeSequence" in self._dataset:
                del self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(
                f"WaterEquivalentDiameterCalculationMethodCodeSequence must be a list of CodeSequenceItem objects"
            )
        else:
            self._WaterEquivalentDiameterCalculationMethodCodeSequence = value
            if "WaterEquivalentDiameterCalculationMethodCodeSequence" not in self._dataset:
                self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence = pydicom.Sequence()
            self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence.clear()
            self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence.extend([item.to_dataset() for item in value])

    def add_WaterEquivalentDiameterCalculationMethodCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._WaterEquivalentDiameterCalculationMethodCodeSequence.append(item)
        if "WaterEquivalentDiameterCalculationMethodCodeSequence" not in self._dataset:
            self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence = pydicom.Sequence()
        self._dataset.WaterEquivalentDiameterCalculationMethodCodeSequence.append(item.to_dataset())

    @property
    def ExposureModulationType(self) -> Optional[List[str]]:
        if "ExposureModulationType" in self._dataset:
            return self._dataset.ExposureModulationType
        return None

    @ExposureModulationType.setter
    def ExposureModulationType(self, value: Optional[List[str]]):
        if value is None:
            if "ExposureModulationType" in self._dataset:
                del self._dataset.ExposureModulationType
        else:
            self._dataset.ExposureModulationType = value

    @property
    def ExposureTimeInms(self) -> Optional[float]:
        if "ExposureTimeInms" in self._dataset:
            return self._dataset.ExposureTimeInms
        return None

    @ExposureTimeInms.setter
    def ExposureTimeInms(self, value: Optional[float]):
        if value is None:
            if "ExposureTimeInms" in self._dataset:
                del self._dataset.ExposureTimeInms
        else:
            self._dataset.ExposureTimeInms = value

    @property
    def XRayTubeCurrentInmA(self) -> Optional[float]:
        if "XRayTubeCurrentInmA" in self._dataset:
            return self._dataset.XRayTubeCurrentInmA
        return None

    @XRayTubeCurrentInmA.setter
    def XRayTubeCurrentInmA(self, value: Optional[float]):
        if value is None:
            if "XRayTubeCurrentInmA" in self._dataset:
                del self._dataset.XRayTubeCurrentInmA
        else:
            self._dataset.XRayTubeCurrentInmA = value

    @property
    def ExposureInmAs(self) -> Optional[float]:
        if "ExposureInmAs" in self._dataset:
            return self._dataset.ExposureInmAs
        return None

    @ExposureInmAs.setter
    def ExposureInmAs(self, value: Optional[float]):
        if value is None:
            if "ExposureInmAs" in self._dataset:
                del self._dataset.ExposureInmAs
        else:
            self._dataset.ExposureInmAs = value

    @property
    def CTDIvol(self) -> Optional[float]:
        if "CTDIvol" in self._dataset:
            return self._dataset.CTDIvol
        return None

    @CTDIvol.setter
    def CTDIvol(self, value: Optional[float]):
        if value is None:
            if "CTDIvol" in self._dataset:
                del self._dataset.CTDIvol
        else:
            self._dataset.CTDIvol = value

    @property
    def CTDIPhantomTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "CTDIPhantomTypeCodeSequence" in self._dataset:
            if len(self._CTDIPhantomTypeCodeSequence) == len(self._dataset.CTDIPhantomTypeCodeSequence):
                return self._CTDIPhantomTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.CTDIPhantomTypeCodeSequence]
        return None

    @CTDIPhantomTypeCodeSequence.setter
    def CTDIPhantomTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._CTDIPhantomTypeCodeSequence = []
            if "CTDIPhantomTypeCodeSequence" in self._dataset:
                del self._dataset.CTDIPhantomTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"CTDIPhantomTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._CTDIPhantomTypeCodeSequence = value
            if "CTDIPhantomTypeCodeSequence" not in self._dataset:
                self._dataset.CTDIPhantomTypeCodeSequence = pydicom.Sequence()
            self._dataset.CTDIPhantomTypeCodeSequence.clear()
            self._dataset.CTDIPhantomTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_CTDIPhantomTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._CTDIPhantomTypeCodeSequence.append(item)
        if "CTDIPhantomTypeCodeSequence" not in self._dataset:
            self._dataset.CTDIPhantomTypeCodeSequence = pydicom.Sequence()
        self._dataset.CTDIPhantomTypeCodeSequence.append(item.to_dataset())

    @property
    def ReferencedXRaySourceIndex(self) -> Optional[List[int]]:
        if "ReferencedXRaySourceIndex" in self._dataset:
            return self._dataset.ReferencedXRaySourceIndex
        return None

    @ReferencedXRaySourceIndex.setter
    def ReferencedXRaySourceIndex(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedXRaySourceIndex" in self._dataset:
                del self._dataset.ReferencedXRaySourceIndex
        else:
            self._dataset.ReferencedXRaySourceIndex = value
