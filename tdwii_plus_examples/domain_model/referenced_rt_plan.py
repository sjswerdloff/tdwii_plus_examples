from enum import Enum
from typing import List, Optional

from pydicom.dataset import Dataset


class PlanRelationship(Enum):
    PRIOR = "PRIOR"
    ALTERNATIVE = "ALTERNATIVE"
    PREDECESSOR = "PREDECESSOR"
    VERIFIED_PLAN = "VERIFIED_PLAN"
    CONCURRENT = "CONCURRENT"


class ReferencedRTPlanSequenceItem:
    def __init__(self, dataset: Optional[Dataset] = None):
        self._dataset = Dataset() if dataset is None else dataset
        if dataset is not None:
            self.validation_errors = self.validate()

    @property
    def referenced_sop_class_uid(self) -> Optional[str]:
        return self._dataset.get("ReferencedSOPClassUID")

    @referenced_sop_class_uid.setter
    def referenced_sop_class_uid(self, value: Optional[str]):
        if value is not None:
            self._dataset.ReferencedSOPClassUID = value

    @property
    def referenced_sop_instance_uid(self) -> Optional[str]:
        return self._dataset.get("ReferencedSOPInstanceUID")

    @referenced_sop_instance_uid.setter
    def referenced_sop_instance_uid(self, value: Optional[str]):
        if value is not None:
            self._dataset.ReferencedSOPInstanceUID = value

    @property
    def rt_plan_relationship(self) -> Optional[str]:
        return self._dataset.get("RTPlanRelationship")

    @rt_plan_relationship.setter
    def rt_plan_relationship(self, value: Optional[PlanRelationship]):
        if value is not None:
            self._dataset.RTPlanRelationship = value.value

    def validate(self) -> List[str]:
        errors = []

        # Check type 1 elements
        type1_elements = ["ReferencedSOPClassUID", "ReferencedSOPInstanceUID", "RTPlanRelationship"]
        for elem in type1_elements:
            if elem not in self._dataset or self._dataset[elem].value in (None, ""):
                errors.append(f"{elem} is a required element and must have a non-empty value")

        # Check enumerated values for RTPlanRelationship
        valid_relationships = [member.value for member in PlanRelationship]
        if "RTPlanRelationship" in self._dataset and self._dataset.RTPlanRelationship not in valid_relationships:
            errors.append(f"RTPlanRelationship should be one of {valid_relationships} unless you have a private definition")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset
