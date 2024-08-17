from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class PlannedVerificationImageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTImagePlane(self) -> Optional[str]:
        if "RTImagePlane" in self._dataset:
            return self._dataset.RTImagePlane
        return None

    @RTImagePlane.setter
    def RTImagePlane(self, value: Optional[str]):
        if value is None:
            if "RTImagePlane" in self._dataset:
                del self._dataset.RTImagePlane
        else:
            self._dataset.RTImagePlane = value

    @property
    def XRayImageReceptorAngle(self) -> Optional[Decimal]:
        if "XRayImageReceptorAngle" in self._dataset:
            return self._dataset.XRayImageReceptorAngle
        return None

    @XRayImageReceptorAngle.setter
    def XRayImageReceptorAngle(self, value: Optional[Decimal]):
        if value is None:
            if "XRayImageReceptorAngle" in self._dataset:
                del self._dataset.XRayImageReceptorAngle
        else:
            self._dataset.XRayImageReceptorAngle = value

    @property
    def RTImageOrientation(self) -> Optional[List[Decimal]]:
        if "RTImageOrientation" in self._dataset:
            return self._dataset.RTImageOrientation
        return None

    @RTImageOrientation.setter
    def RTImageOrientation(self, value: Optional[List[Decimal]]):
        if value is None:
            if "RTImageOrientation" in self._dataset:
                del self._dataset.RTImageOrientation
        else:
            self._dataset.RTImageOrientation = value

    @property
    def RTImagePosition(self) -> Optional[List[Decimal]]:
        if "RTImagePosition" in self._dataset:
            return self._dataset.RTImagePosition
        return None

    @RTImagePosition.setter
    def RTImagePosition(self, value: Optional[List[Decimal]]):
        if value is None:
            if "RTImagePosition" in self._dataset:
                del self._dataset.RTImagePosition
        else:
            self._dataset.RTImagePosition = value

    @property
    def RTImageSID(self) -> Optional[Decimal]:
        if "RTImageSID" in self._dataset:
            return self._dataset.RTImageSID
        return None

    @RTImageSID.setter
    def RTImageSID(self, value: Optional[Decimal]):
        if value is None:
            if "RTImageSID" in self._dataset:
                del self._dataset.RTImageSID
        else:
            self._dataset.RTImageSID = value

    @property
    def MetersetExposure(self) -> Optional[Decimal]:
        if "MetersetExposure" in self._dataset:
            return self._dataset.MetersetExposure
        return None

    @MetersetExposure.setter
    def MetersetExposure(self, value: Optional[Decimal]):
        if value is None:
            if "MetersetExposure" in self._dataset:
                del self._dataset.MetersetExposure
        else:
            self._dataset.MetersetExposure = value

    @property
    def ImagingDeviceSpecificAcquisitionParameters(self) -> Optional[List[str]]:
        if "ImagingDeviceSpecificAcquisitionParameters" in self._dataset:
            return self._dataset.ImagingDeviceSpecificAcquisitionParameters
        return None

    @ImagingDeviceSpecificAcquisitionParameters.setter
    def ImagingDeviceSpecificAcquisitionParameters(self, value: Optional[List[str]]):
        if value is None:
            if "ImagingDeviceSpecificAcquisitionParameters" in self._dataset:
                del self._dataset.ImagingDeviceSpecificAcquisitionParameters
        else:
            self._dataset.ImagingDeviceSpecificAcquisitionParameters = value

    @property
    def ReferencedReferenceImageNumber(self) -> Optional[int]:
        if "ReferencedReferenceImageNumber" in self._dataset:
            return self._dataset.ReferencedReferenceImageNumber
        return None

    @ReferencedReferenceImageNumber.setter
    def ReferencedReferenceImageNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedReferenceImageNumber" in self._dataset:
                del self._dataset.ReferencedReferenceImageNumber
        else:
            self._dataset.ReferencedReferenceImageNumber = value

    @property
    def StartCumulativeMetersetWeight(self) -> Optional[Decimal]:
        if "StartCumulativeMetersetWeight" in self._dataset:
            return self._dataset.StartCumulativeMetersetWeight
        return None

    @StartCumulativeMetersetWeight.setter
    def StartCumulativeMetersetWeight(self, value: Optional[Decimal]):
        if value is None:
            if "StartCumulativeMetersetWeight" in self._dataset:
                del self._dataset.StartCumulativeMetersetWeight
        else:
            self._dataset.StartCumulativeMetersetWeight = value

    @property
    def EndCumulativeMetersetWeight(self) -> Optional[Decimal]:
        if "EndCumulativeMetersetWeight" in self._dataset:
            return self._dataset.EndCumulativeMetersetWeight
        return None

    @EndCumulativeMetersetWeight.setter
    def EndCumulativeMetersetWeight(self, value: Optional[Decimal]):
        if value is None:
            if "EndCumulativeMetersetWeight" in self._dataset:
                del self._dataset.EndCumulativeMetersetWeight
        else:
            self._dataset.EndCumulativeMetersetWeight = value
