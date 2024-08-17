from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class DoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value

    @property
    def DoseReferenceNumber(self) -> Optional[int]:
        if "DoseReferenceNumber" in self._dataset:
            return self._dataset.DoseReferenceNumber
        return None

    @DoseReferenceNumber.setter
    def DoseReferenceNumber(self, value: Optional[int]):
        if value is None:
            if "DoseReferenceNumber" in self._dataset:
                del self._dataset.DoseReferenceNumber
        else:
            self._dataset.DoseReferenceNumber = value

    @property
    def DoseReferenceUID(self) -> Optional[str]:
        if "DoseReferenceUID" in self._dataset:
            return self._dataset.DoseReferenceUID
        return None

    @DoseReferenceUID.setter
    def DoseReferenceUID(self, value: Optional[str]):
        if value is None:
            if "DoseReferenceUID" in self._dataset:
                del self._dataset.DoseReferenceUID
        else:
            self._dataset.DoseReferenceUID = value

    @property
    def DoseReferenceStructureType(self) -> Optional[str]:
        if "DoseReferenceStructureType" in self._dataset:
            return self._dataset.DoseReferenceStructureType
        return None

    @DoseReferenceStructureType.setter
    def DoseReferenceStructureType(self, value: Optional[str]):
        if value is None:
            if "DoseReferenceStructureType" in self._dataset:
                del self._dataset.DoseReferenceStructureType
        else:
            self._dataset.DoseReferenceStructureType = value

    @property
    def DoseReferenceDescription(self) -> Optional[str]:
        if "DoseReferenceDescription" in self._dataset:
            return self._dataset.DoseReferenceDescription
        return None

    @DoseReferenceDescription.setter
    def DoseReferenceDescription(self, value: Optional[str]):
        if value is None:
            if "DoseReferenceDescription" in self._dataset:
                del self._dataset.DoseReferenceDescription
        else:
            self._dataset.DoseReferenceDescription = value

    @property
    def DoseReferencePointCoordinates(self) -> Optional[List[Decimal]]:
        if "DoseReferencePointCoordinates" in self._dataset:
            return self._dataset.DoseReferencePointCoordinates
        return None

    @DoseReferencePointCoordinates.setter
    def DoseReferencePointCoordinates(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DoseReferencePointCoordinates" in self._dataset:
                del self._dataset.DoseReferencePointCoordinates
        else:
            self._dataset.DoseReferencePointCoordinates = value

    @property
    def NominalPriorDose(self) -> Optional[Decimal]:
        if "NominalPriorDose" in self._dataset:
            return self._dataset.NominalPriorDose
        return None

    @NominalPriorDose.setter
    def NominalPriorDose(self, value: Optional[Decimal]):
        if value is None:
            if "NominalPriorDose" in self._dataset:
                del self._dataset.NominalPriorDose
        else:
            self._dataset.NominalPriorDose = value

    @property
    def DoseReferenceType(self) -> Optional[str]:
        if "DoseReferenceType" in self._dataset:
            return self._dataset.DoseReferenceType
        return None

    @DoseReferenceType.setter
    def DoseReferenceType(self, value: Optional[str]):
        if value is None:
            if "DoseReferenceType" in self._dataset:
                del self._dataset.DoseReferenceType
        else:
            self._dataset.DoseReferenceType = value

    @property
    def ConstraintWeight(self) -> Optional[Decimal]:
        if "ConstraintWeight" in self._dataset:
            return self._dataset.ConstraintWeight
        return None

    @ConstraintWeight.setter
    def ConstraintWeight(self, value: Optional[Decimal]):
        if value is None:
            if "ConstraintWeight" in self._dataset:
                del self._dataset.ConstraintWeight
        else:
            self._dataset.ConstraintWeight = value

    @property
    def DeliveryWarningDose(self) -> Optional[Decimal]:
        if "DeliveryWarningDose" in self._dataset:
            return self._dataset.DeliveryWarningDose
        return None

    @DeliveryWarningDose.setter
    def DeliveryWarningDose(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveryWarningDose" in self._dataset:
                del self._dataset.DeliveryWarningDose
        else:
            self._dataset.DeliveryWarningDose = value

    @property
    def DeliveryMaximumDose(self) -> Optional[Decimal]:
        if "DeliveryMaximumDose" in self._dataset:
            return self._dataset.DeliveryMaximumDose
        return None

    @DeliveryMaximumDose.setter
    def DeliveryMaximumDose(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveryMaximumDose" in self._dataset:
                del self._dataset.DeliveryMaximumDose
        else:
            self._dataset.DeliveryMaximumDose = value

    @property
    def TargetMinimumDose(self) -> Optional[Decimal]:
        if "TargetMinimumDose" in self._dataset:
            return self._dataset.TargetMinimumDose
        return None

    @TargetMinimumDose.setter
    def TargetMinimumDose(self, value: Optional[Decimal]):
        if value is None:
            if "TargetMinimumDose" in self._dataset:
                del self._dataset.TargetMinimumDose
        else:
            self._dataset.TargetMinimumDose = value

    @property
    def TargetPrescriptionDose(self) -> Optional[Decimal]:
        if "TargetPrescriptionDose" in self._dataset:
            return self._dataset.TargetPrescriptionDose
        return None

    @TargetPrescriptionDose.setter
    def TargetPrescriptionDose(self, value: Optional[Decimal]):
        if value is None:
            if "TargetPrescriptionDose" in self._dataset:
                del self._dataset.TargetPrescriptionDose
        else:
            self._dataset.TargetPrescriptionDose = value

    @property
    def TargetMaximumDose(self) -> Optional[Decimal]:
        if "TargetMaximumDose" in self._dataset:
            return self._dataset.TargetMaximumDose
        return None

    @TargetMaximumDose.setter
    def TargetMaximumDose(self, value: Optional[Decimal]):
        if value is None:
            if "TargetMaximumDose" in self._dataset:
                del self._dataset.TargetMaximumDose
        else:
            self._dataset.TargetMaximumDose = value

    @property
    def TargetUnderdoseVolumeFraction(self) -> Optional[Decimal]:
        if "TargetUnderdoseVolumeFraction" in self._dataset:
            return self._dataset.TargetUnderdoseVolumeFraction
        return None

    @TargetUnderdoseVolumeFraction.setter
    def TargetUnderdoseVolumeFraction(self, value: Optional[Decimal]):
        if value is None:
            if "TargetUnderdoseVolumeFraction" in self._dataset:
                del self._dataset.TargetUnderdoseVolumeFraction
        else:
            self._dataset.TargetUnderdoseVolumeFraction = value

    @property
    def OrganAtRiskFullVolumeDose(self) -> Optional[Decimal]:
        if "OrganAtRiskFullVolumeDose" in self._dataset:
            return self._dataset.OrganAtRiskFullVolumeDose
        return None

    @OrganAtRiskFullVolumeDose.setter
    def OrganAtRiskFullVolumeDose(self, value: Optional[Decimal]):
        if value is None:
            if "OrganAtRiskFullVolumeDose" in self._dataset:
                del self._dataset.OrganAtRiskFullVolumeDose
        else:
            self._dataset.OrganAtRiskFullVolumeDose = value

    @property
    def OrganAtRiskLimitDose(self) -> Optional[Decimal]:
        if "OrganAtRiskLimitDose" in self._dataset:
            return self._dataset.OrganAtRiskLimitDose
        return None

    @OrganAtRiskLimitDose.setter
    def OrganAtRiskLimitDose(self, value: Optional[Decimal]):
        if value is None:
            if "OrganAtRiskLimitDose" in self._dataset:
                del self._dataset.OrganAtRiskLimitDose
        else:
            self._dataset.OrganAtRiskLimitDose = value

    @property
    def OrganAtRiskMaximumDose(self) -> Optional[Decimal]:
        if "OrganAtRiskMaximumDose" in self._dataset:
            return self._dataset.OrganAtRiskMaximumDose
        return None

    @OrganAtRiskMaximumDose.setter
    def OrganAtRiskMaximumDose(self, value: Optional[Decimal]):
        if value is None:
            if "OrganAtRiskMaximumDose" in self._dataset:
                del self._dataset.OrganAtRiskMaximumDose
        else:
            self._dataset.OrganAtRiskMaximumDose = value

    @property
    def OrganAtRiskOverdoseVolumeFraction(self) -> Optional[Decimal]:
        if "OrganAtRiskOverdoseVolumeFraction" in self._dataset:
            return self._dataset.OrganAtRiskOverdoseVolumeFraction
        return None

    @OrganAtRiskOverdoseVolumeFraction.setter
    def OrganAtRiskOverdoseVolumeFraction(self, value: Optional[Decimal]):
        if value is None:
            if "OrganAtRiskOverdoseVolumeFraction" in self._dataset:
                del self._dataset.OrganAtRiskOverdoseVolumeFraction
        else:
            self._dataset.OrganAtRiskOverdoseVolumeFraction = value

    @property
    def DoseValuePurpose(self) -> Optional[List[str]]:
        if "DoseValuePurpose" in self._dataset:
            return self._dataset.DoseValuePurpose
        return None

    @DoseValuePurpose.setter
    def DoseValuePurpose(self, value: Optional[List[str]]):
        if value is None:
            if "DoseValuePurpose" in self._dataset:
                del self._dataset.DoseValuePurpose
        else:
            self._dataset.DoseValuePurpose = value

    @property
    def DoseValueInterpretation(self) -> Optional[str]:
        if "DoseValueInterpretation" in self._dataset:
            return self._dataset.DoseValueInterpretation
        return None

    @DoseValueInterpretation.setter
    def DoseValueInterpretation(self, value: Optional[str]):
        if value is None:
            if "DoseValueInterpretation" in self._dataset:
                del self._dataset.DoseValueInterpretation
        else:
            self._dataset.DoseValueInterpretation = value
