from typing import Any, List, Optional  # noqa

import pydicom


class CTAcquisitionTypeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AcquisitionType(self) -> Optional[str]:
        if "AcquisitionType" in self._dataset:
            return self._dataset.AcquisitionType
        return None

    @AcquisitionType.setter
    def AcquisitionType(self, value: Optional[str]):
        if value is None:
            if "AcquisitionType" in self._dataset:
                del self._dataset.AcquisitionType
        else:
            self._dataset.AcquisitionType = value

    @property
    def TubeAngle(self) -> Optional[float]:
        if "TubeAngle" in self._dataset:
            return self._dataset.TubeAngle
        return None

    @TubeAngle.setter
    def TubeAngle(self, value: Optional[float]):
        if value is None:
            if "TubeAngle" in self._dataset:
                del self._dataset.TubeAngle
        else:
            self._dataset.TubeAngle = value

    @property
    def ConstantVolumeFlag(self) -> Optional[str]:
        if "ConstantVolumeFlag" in self._dataset:
            return self._dataset.ConstantVolumeFlag
        return None

    @ConstantVolumeFlag.setter
    def ConstantVolumeFlag(self, value: Optional[str]):
        if value is None:
            if "ConstantVolumeFlag" in self._dataset:
                del self._dataset.ConstantVolumeFlag
        else:
            self._dataset.ConstantVolumeFlag = value

    @property
    def FluoroscopyFlag(self) -> Optional[str]:
        if "FluoroscopyFlag" in self._dataset:
            return self._dataset.FluoroscopyFlag
        return None

    @FluoroscopyFlag.setter
    def FluoroscopyFlag(self, value: Optional[str]):
        if value is None:
            if "FluoroscopyFlag" in self._dataset:
                del self._dataset.FluoroscopyFlag
        else:
            self._dataset.FluoroscopyFlag = value
