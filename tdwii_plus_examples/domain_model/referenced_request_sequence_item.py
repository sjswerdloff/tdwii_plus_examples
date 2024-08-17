from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .issuer_of_accession_number_sequence_item import (
    IssuerOfAccessionNumberSequenceItem,
)
from .order_filler_identifier_sequence_item import OrderFillerIdentifierSequenceItem
from .order_placer_identifier_sequence_item import OrderPlacerIdentifierSequenceItem
from .referenced_study_sequence_item import ReferencedStudySequenceItem


class ReferencedRequestSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._IssuerOfAccessionNumberSequence: List[IssuerOfAccessionNumberSequenceItem] = []
        self._ReferencedStudySequence: List[ReferencedStudySequenceItem] = []
        self._RequestedProcedureCodeSequence: List[CodeSequenceItem] = []
        self._OrderPlacerIdentifierSequence: List[OrderPlacerIdentifierSequenceItem] = []
        self._OrderFillerIdentifierSequence: List[OrderFillerIdentifierSequenceItem] = []
        self._ReasonForRequestedProcedureCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AccessionNumber(self) -> Optional[str]:
        if "AccessionNumber" in self._dataset:
            return self._dataset.AccessionNumber
        return None

    @AccessionNumber.setter
    def AccessionNumber(self, value: Optional[str]):
        if value is None:
            if "AccessionNumber" in self._dataset:
                del self._dataset.AccessionNumber
        else:
            self._dataset.AccessionNumber = value

    @property
    def IssuerOfAccessionNumberSequence(self) -> Optional[List[IssuerOfAccessionNumberSequenceItem]]:
        if "IssuerOfAccessionNumberSequence" in self._dataset:
            if len(self._IssuerOfAccessionNumberSequence) == len(self._dataset.IssuerOfAccessionNumberSequence):
                return self._IssuerOfAccessionNumberSequence
            else:
                return [IssuerOfAccessionNumberSequenceItem(x) for x in self._dataset.IssuerOfAccessionNumberSequence]
        return None

    @IssuerOfAccessionNumberSequence.setter
    def IssuerOfAccessionNumberSequence(self, value: Optional[List[IssuerOfAccessionNumberSequenceItem]]):
        if value is None:
            self._IssuerOfAccessionNumberSequence = []
            if "IssuerOfAccessionNumberSequence" in self._dataset:
                del self._dataset.IssuerOfAccessionNumberSequence
        elif not isinstance(value, list) or not all(isinstance(item, IssuerOfAccessionNumberSequenceItem) for item in value):
            raise ValueError(f"IssuerOfAccessionNumberSequence must be a list of IssuerOfAccessionNumberSequenceItem objects")
        else:
            self._IssuerOfAccessionNumberSequence = value
            if "IssuerOfAccessionNumberSequence" not in self._dataset:
                self._dataset.IssuerOfAccessionNumberSequence = pydicom.Sequence()
            self._dataset.IssuerOfAccessionNumberSequence.clear()
            self._dataset.IssuerOfAccessionNumberSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfAccessionNumber(self, item: IssuerOfAccessionNumberSequenceItem):
        if not isinstance(item, IssuerOfAccessionNumberSequenceItem):
            raise ValueError(f"Item must be an instance of IssuerOfAccessionNumberSequenceItem")
        self._IssuerOfAccessionNumberSequence.append(item)
        if "IssuerOfAccessionNumberSequence" not in self._dataset:
            self._dataset.IssuerOfAccessionNumberSequence = pydicom.Sequence()
        self._dataset.IssuerOfAccessionNumberSequence.append(item.to_dataset())

    @property
    def ReferencedStudySequence(self) -> Optional[List[ReferencedStudySequenceItem]]:
        if "ReferencedStudySequence" in self._dataset:
            if len(self._ReferencedStudySequence) == len(self._dataset.ReferencedStudySequence):
                return self._ReferencedStudySequence
            else:
                return [ReferencedStudySequenceItem(x) for x in self._dataset.ReferencedStudySequence]
        return None

    @ReferencedStudySequence.setter
    def ReferencedStudySequence(self, value: Optional[List[ReferencedStudySequenceItem]]):
        if value is None:
            self._ReferencedStudySequence = []
            if "ReferencedStudySequence" in self._dataset:
                del self._dataset.ReferencedStudySequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedStudySequenceItem) for item in value):
            raise ValueError(f"ReferencedStudySequence must be a list of ReferencedStudySequenceItem objects")
        else:
            self._ReferencedStudySequence = value
            if "ReferencedStudySequence" not in self._dataset:
                self._dataset.ReferencedStudySequence = pydicom.Sequence()
            self._dataset.ReferencedStudySequence.clear()
            self._dataset.ReferencedStudySequence.extend([item.to_dataset() for item in value])

    def add_ReferencedStudy(self, item: ReferencedStudySequenceItem):
        if not isinstance(item, ReferencedStudySequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedStudySequenceItem")
        self._ReferencedStudySequence.append(item)
        if "ReferencedStudySequence" not in self._dataset:
            self._dataset.ReferencedStudySequence = pydicom.Sequence()
        self._dataset.ReferencedStudySequence.append(item.to_dataset())

    @property
    def StudyInstanceUID(self) -> Optional[str]:
        if "StudyInstanceUID" in self._dataset:
            return self._dataset.StudyInstanceUID
        return None

    @StudyInstanceUID.setter
    def StudyInstanceUID(self, value: Optional[str]):
        if value is None:
            if "StudyInstanceUID" in self._dataset:
                del self._dataset.StudyInstanceUID
        else:
            self._dataset.StudyInstanceUID = value

    @property
    def RequestedProcedureDescription(self) -> Optional[str]:
        if "RequestedProcedureDescription" in self._dataset:
            return self._dataset.RequestedProcedureDescription
        return None

    @RequestedProcedureDescription.setter
    def RequestedProcedureDescription(self, value: Optional[str]):
        if value is None:
            if "RequestedProcedureDescription" in self._dataset:
                del self._dataset.RequestedProcedureDescription
        else:
            self._dataset.RequestedProcedureDescription = value

    @property
    def RequestedProcedureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RequestedProcedureCodeSequence" in self._dataset:
            if len(self._RequestedProcedureCodeSequence) == len(self._dataset.RequestedProcedureCodeSequence):
                return self._RequestedProcedureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RequestedProcedureCodeSequence]
        return None

    @RequestedProcedureCodeSequence.setter
    def RequestedProcedureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RequestedProcedureCodeSequence = []
            if "RequestedProcedureCodeSequence" in self._dataset:
                del self._dataset.RequestedProcedureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"RequestedProcedureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RequestedProcedureCodeSequence = value
            if "RequestedProcedureCodeSequence" not in self._dataset:
                self._dataset.RequestedProcedureCodeSequence = pydicom.Sequence()
            self._dataset.RequestedProcedureCodeSequence.clear()
            self._dataset.RequestedProcedureCodeSequence.extend([item.to_dataset() for item in value])

    def add_RequestedProcedureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RequestedProcedureCodeSequence.append(item)
        if "RequestedProcedureCodeSequence" not in self._dataset:
            self._dataset.RequestedProcedureCodeSequence = pydicom.Sequence()
        self._dataset.RequestedProcedureCodeSequence.append(item.to_dataset())

    @property
    def OrderPlacerIdentifierSequence(self) -> Optional[List[OrderPlacerIdentifierSequenceItem]]:
        if "OrderPlacerIdentifierSequence" in self._dataset:
            if len(self._OrderPlacerIdentifierSequence) == len(self._dataset.OrderPlacerIdentifierSequence):
                return self._OrderPlacerIdentifierSequence
            else:
                return [OrderPlacerIdentifierSequenceItem(x) for x in self._dataset.OrderPlacerIdentifierSequence]
        return None

    @OrderPlacerIdentifierSequence.setter
    def OrderPlacerIdentifierSequence(self, value: Optional[List[OrderPlacerIdentifierSequenceItem]]):
        if value is None:
            self._OrderPlacerIdentifierSequence = []
            if "OrderPlacerIdentifierSequence" in self._dataset:
                del self._dataset.OrderPlacerIdentifierSequence
        elif not isinstance(value, list) or not all(isinstance(item, OrderPlacerIdentifierSequenceItem) for item in value):
            raise ValueError(f"OrderPlacerIdentifierSequence must be a list of OrderPlacerIdentifierSequenceItem objects")
        else:
            self._OrderPlacerIdentifierSequence = value
            if "OrderPlacerIdentifierSequence" not in self._dataset:
                self._dataset.OrderPlacerIdentifierSequence = pydicom.Sequence()
            self._dataset.OrderPlacerIdentifierSequence.clear()
            self._dataset.OrderPlacerIdentifierSequence.extend([item.to_dataset() for item in value])

    def add_OrderPlacerIdentifier(self, item: OrderPlacerIdentifierSequenceItem):
        if not isinstance(item, OrderPlacerIdentifierSequenceItem):
            raise ValueError(f"Item must be an instance of OrderPlacerIdentifierSequenceItem")
        self._OrderPlacerIdentifierSequence.append(item)
        if "OrderPlacerIdentifierSequence" not in self._dataset:
            self._dataset.OrderPlacerIdentifierSequence = pydicom.Sequence()
        self._dataset.OrderPlacerIdentifierSequence.append(item.to_dataset())

    @property
    def OrderFillerIdentifierSequence(self) -> Optional[List[OrderFillerIdentifierSequenceItem]]:
        if "OrderFillerIdentifierSequence" in self._dataset:
            if len(self._OrderFillerIdentifierSequence) == len(self._dataset.OrderFillerIdentifierSequence):
                return self._OrderFillerIdentifierSequence
            else:
                return [OrderFillerIdentifierSequenceItem(x) for x in self._dataset.OrderFillerIdentifierSequence]
        return None

    @OrderFillerIdentifierSequence.setter
    def OrderFillerIdentifierSequence(self, value: Optional[List[OrderFillerIdentifierSequenceItem]]):
        if value is None:
            self._OrderFillerIdentifierSequence = []
            if "OrderFillerIdentifierSequence" in self._dataset:
                del self._dataset.OrderFillerIdentifierSequence
        elif not isinstance(value, list) or not all(isinstance(item, OrderFillerIdentifierSequenceItem) for item in value):
            raise ValueError(f"OrderFillerIdentifierSequence must be a list of OrderFillerIdentifierSequenceItem objects")
        else:
            self._OrderFillerIdentifierSequence = value
            if "OrderFillerIdentifierSequence" not in self._dataset:
                self._dataset.OrderFillerIdentifierSequence = pydicom.Sequence()
            self._dataset.OrderFillerIdentifierSequence.clear()
            self._dataset.OrderFillerIdentifierSequence.extend([item.to_dataset() for item in value])

    def add_OrderFillerIdentifier(self, item: OrderFillerIdentifierSequenceItem):
        if not isinstance(item, OrderFillerIdentifierSequenceItem):
            raise ValueError(f"Item must be an instance of OrderFillerIdentifierSequenceItem")
        self._OrderFillerIdentifierSequence.append(item)
        if "OrderFillerIdentifierSequence" not in self._dataset:
            self._dataset.OrderFillerIdentifierSequence = pydicom.Sequence()
        self._dataset.OrderFillerIdentifierSequence.append(item.to_dataset())

    @property
    def RequestedProcedureID(self) -> Optional[str]:
        if "RequestedProcedureID" in self._dataset:
            return self._dataset.RequestedProcedureID
        return None

    @RequestedProcedureID.setter
    def RequestedProcedureID(self, value: Optional[str]):
        if value is None:
            if "RequestedProcedureID" in self._dataset:
                del self._dataset.RequestedProcedureID
        else:
            self._dataset.RequestedProcedureID = value

    @property
    def ReasonForTheRequestedProcedure(self) -> Optional[str]:
        if "ReasonForTheRequestedProcedure" in self._dataset:
            return self._dataset.ReasonForTheRequestedProcedure
        return None

    @ReasonForTheRequestedProcedure.setter
    def ReasonForTheRequestedProcedure(self, value: Optional[str]):
        if value is None:
            if "ReasonForTheRequestedProcedure" in self._dataset:
                del self._dataset.ReasonForTheRequestedProcedure
        else:
            self._dataset.ReasonForTheRequestedProcedure = value

    @property
    def ReasonForRequestedProcedureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReasonForRequestedProcedureCodeSequence" in self._dataset:
            if len(self._ReasonForRequestedProcedureCodeSequence) == len(
                self._dataset.ReasonForRequestedProcedureCodeSequence
            ):
                return self._ReasonForRequestedProcedureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReasonForRequestedProcedureCodeSequence]
        return None

    @ReasonForRequestedProcedureCodeSequence.setter
    def ReasonForRequestedProcedureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReasonForRequestedProcedureCodeSequence = []
            if "ReasonForRequestedProcedureCodeSequence" in self._dataset:
                del self._dataset.ReasonForRequestedProcedureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ReasonForRequestedProcedureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReasonForRequestedProcedureCodeSequence = value
            if "ReasonForRequestedProcedureCodeSequence" not in self._dataset:
                self._dataset.ReasonForRequestedProcedureCodeSequence = pydicom.Sequence()
            self._dataset.ReasonForRequestedProcedureCodeSequence.clear()
            self._dataset.ReasonForRequestedProcedureCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReasonForRequestedProcedureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ReasonForRequestedProcedureCodeSequence.append(item)
        if "ReasonForRequestedProcedureCodeSequence" not in self._dataset:
            self._dataset.ReasonForRequestedProcedureCodeSequence = pydicom.Sequence()
        self._dataset.ReasonForRequestedProcedureCodeSequence.append(item.to_dataset())

    @property
    def PlacerOrderNumberImagingServiceRequest(self) -> Optional[str]:
        if "PlacerOrderNumberImagingServiceRequest" in self._dataset:
            return self._dataset.PlacerOrderNumberImagingServiceRequest
        return None

    @PlacerOrderNumberImagingServiceRequest.setter
    def PlacerOrderNumberImagingServiceRequest(self, value: Optional[str]):
        if value is None:
            if "PlacerOrderNumberImagingServiceRequest" in self._dataset:
                del self._dataset.PlacerOrderNumberImagingServiceRequest
        else:
            self._dataset.PlacerOrderNumberImagingServiceRequest = value

    @property
    def FillerOrderNumberImagingServiceRequest(self) -> Optional[str]:
        if "FillerOrderNumberImagingServiceRequest" in self._dataset:
            return self._dataset.FillerOrderNumberImagingServiceRequest
        return None

    @FillerOrderNumberImagingServiceRequest.setter
    def FillerOrderNumberImagingServiceRequest(self, value: Optional[str]):
        if value is None:
            if "FillerOrderNumberImagingServiceRequest" in self._dataset:
                del self._dataset.FillerOrderNumberImagingServiceRequest
        else:
            self._dataset.FillerOrderNumberImagingServiceRequest = value
