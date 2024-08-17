from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .x_ray_filter_details_sequence_item import XRayFilterDetailsSequenceItem


class XAPlaneDetailsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._XRayFilterDetailsSequence: List[XRayFilterDetailsSequenceItem] = []

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
    def DistanceSourceToDetector(self) -> Optional[Decimal]:
        if "DistanceSourceToDetector" in self._dataset:
            return self._dataset.DistanceSourceToDetector
        return None

    @DistanceSourceToDetector.setter
    def DistanceSourceToDetector(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToDetector" in self._dataset:
                del self._dataset.DistanceSourceToDetector
        else:
            self._dataset.DistanceSourceToDetector = value

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
    def FocalSpots(self) -> Optional[List[Decimal]]:
        if "FocalSpots" in self._dataset:
            return self._dataset.FocalSpots
        return None

    @FocalSpots.setter
    def FocalSpots(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FocalSpots" in self._dataset:
                del self._dataset.FocalSpots
        else:
            self._dataset.FocalSpots = value

    @property
    def AcquisitionFieldOfViewLabel(self) -> Optional[str]:
        if "AcquisitionFieldOfViewLabel" in self._dataset:
            return self._dataset.AcquisitionFieldOfViewLabel
        return None

    @AcquisitionFieldOfViewLabel.setter
    def AcquisitionFieldOfViewLabel(self, value: Optional[str]):
        if value is None:
            if "AcquisitionFieldOfViewLabel" in self._dataset:
                del self._dataset.AcquisitionFieldOfViewLabel
        else:
            self._dataset.AcquisitionFieldOfViewLabel = value

    @property
    def XRayFilterDetailsSequence(self) -> Optional[List[XRayFilterDetailsSequenceItem]]:
        if "XRayFilterDetailsSequence" in self._dataset:
            if len(self._XRayFilterDetailsSequence) == len(self._dataset.XRayFilterDetailsSequence):
                return self._XRayFilterDetailsSequence
            else:
                return [XRayFilterDetailsSequenceItem(x) for x in self._dataset.XRayFilterDetailsSequence]
        return None

    @XRayFilterDetailsSequence.setter
    def XRayFilterDetailsSequence(self, value: Optional[List[XRayFilterDetailsSequenceItem]]):
        if value is None:
            self._XRayFilterDetailsSequence = []
            if "XRayFilterDetailsSequence" in self._dataset:
                del self._dataset.XRayFilterDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, XRayFilterDetailsSequenceItem) for item in value):
            raise ValueError("XRayFilterDetailsSequence must be a list of XRayFilterDetailsSequenceItem objects")
        else:
            self._XRayFilterDetailsSequence = value
            if "XRayFilterDetailsSequence" not in self._dataset:
                self._dataset.XRayFilterDetailsSequence = pydicom.Sequence()
            self._dataset.XRayFilterDetailsSequence.clear()
            self._dataset.XRayFilterDetailsSequence.extend([item.to_dataset() for item in value])

    def add_XRayFilterDetails(self, item: XRayFilterDetailsSequenceItem):
        if not isinstance(item, XRayFilterDetailsSequenceItem):
            raise ValueError("Item must be an instance of XRayFilterDetailsSequenceItem")
        self._XRayFilterDetailsSequence.append(item)
        if "XRayFilterDetailsSequence" not in self._dataset:
            self._dataset.XRayFilterDetailsSequence = pydicom.Sequence()
        self._dataset.XRayFilterDetailsSequence.append(item.to_dataset())

    @property
    def DetectorBinning(self) -> Optional[List[Decimal]]:
        if "DetectorBinning" in self._dataset:
            return self._dataset.DetectorBinning
        return None

    @DetectorBinning.setter
    def DetectorBinning(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorBinning" in self._dataset:
                del self._dataset.DetectorBinning
        else:
            self._dataset.DetectorBinning = value

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
    def PlaneIdentification(self) -> Optional[str]:
        if "PlaneIdentification" in self._dataset:
            return self._dataset.PlaneIdentification
        return None

    @PlaneIdentification.setter
    def PlaneIdentification(self, value: Optional[str]):
        if value is None:
            if "PlaneIdentification" in self._dataset:
                del self._dataset.PlaneIdentification
        else:
            self._dataset.PlaneIdentification = value

    @property
    def FieldOfViewDimensionsInFloat(self) -> Optional[List[float]]:
        if "FieldOfViewDimensionsInFloat" in self._dataset:
            return self._dataset.FieldOfViewDimensionsInFloat
        return None

    @FieldOfViewDimensionsInFloat.setter
    def FieldOfViewDimensionsInFloat(self, value: Optional[List[float]]):
        if value is None:
            if "FieldOfViewDimensionsInFloat" in self._dataset:
                del self._dataset.FieldOfViewDimensionsInFloat
        else:
            self._dataset.FieldOfViewDimensionsInFloat = value

    @property
    def PrimaryPositionerScanArc(self) -> Optional[float]:
        if "PrimaryPositionerScanArc" in self._dataset:
            return self._dataset.PrimaryPositionerScanArc
        return None

    @PrimaryPositionerScanArc.setter
    def PrimaryPositionerScanArc(self, value: Optional[float]):
        if value is None:
            if "PrimaryPositionerScanArc" in self._dataset:
                del self._dataset.PrimaryPositionerScanArc
        else:
            self._dataset.PrimaryPositionerScanArc = value

    @property
    def SecondaryPositionerScanArc(self) -> Optional[float]:
        if "SecondaryPositionerScanArc" in self._dataset:
            return self._dataset.SecondaryPositionerScanArc
        return None

    @SecondaryPositionerScanArc.setter
    def SecondaryPositionerScanArc(self, value: Optional[float]):
        if value is None:
            if "SecondaryPositionerScanArc" in self._dataset:
                del self._dataset.SecondaryPositionerScanArc
        else:
            self._dataset.SecondaryPositionerScanArc = value

    @property
    def PrimaryPositionerScanStartAngle(self) -> Optional[float]:
        if "PrimaryPositionerScanStartAngle" in self._dataset:
            return self._dataset.PrimaryPositionerScanStartAngle
        return None

    @PrimaryPositionerScanStartAngle.setter
    def PrimaryPositionerScanStartAngle(self, value: Optional[float]):
        if value is None:
            if "PrimaryPositionerScanStartAngle" in self._dataset:
                del self._dataset.PrimaryPositionerScanStartAngle
        else:
            self._dataset.PrimaryPositionerScanStartAngle = value

    @property
    def SecondaryPositionerScanStartAngle(self) -> Optional[float]:
        if "SecondaryPositionerScanStartAngle" in self._dataset:
            return self._dataset.SecondaryPositionerScanStartAngle
        return None

    @SecondaryPositionerScanStartAngle.setter
    def SecondaryPositionerScanStartAngle(self, value: Optional[float]):
        if value is None:
            if "SecondaryPositionerScanStartAngle" in self._dataset:
                del self._dataset.SecondaryPositionerScanStartAngle
        else:
            self._dataset.SecondaryPositionerScanStartAngle = value

    @property
    def PrimaryPositionerIncrement(self) -> Optional[float]:
        if "PrimaryPositionerIncrement" in self._dataset:
            return self._dataset.PrimaryPositionerIncrement
        return None

    @PrimaryPositionerIncrement.setter
    def PrimaryPositionerIncrement(self, value: Optional[float]):
        if value is None:
            if "PrimaryPositionerIncrement" in self._dataset:
                del self._dataset.PrimaryPositionerIncrement
        else:
            self._dataset.PrimaryPositionerIncrement = value

    @property
    def SecondaryPositionerIncrement(self) -> Optional[float]:
        if "SecondaryPositionerIncrement" in self._dataset:
            return self._dataset.SecondaryPositionerIncrement
        return None

    @SecondaryPositionerIncrement.setter
    def SecondaryPositionerIncrement(self, value: Optional[float]):
        if value is None:
            if "SecondaryPositionerIncrement" in self._dataset:
                del self._dataset.SecondaryPositionerIncrement
        else:
            self._dataset.SecondaryPositionerIncrement = value

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
    def BeamNumber(self) -> Optional[int]:
        if "BeamNumber" in self._dataset:
            return self._dataset.BeamNumber
        return None

    @BeamNumber.setter
    def BeamNumber(self, value: Optional[int]):
        if value is None:
            if "BeamNumber" in self._dataset:
                del self._dataset.BeamNumber
        else:
            self._dataset.BeamNumber = value
