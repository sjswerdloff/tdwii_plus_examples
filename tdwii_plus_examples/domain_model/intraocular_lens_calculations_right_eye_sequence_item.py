from typing import Any, List, Optional

import pydicom

from .anterior_chamber_depth_sequence_item import AnteriorChamberDepthSequenceItem
from .calculation_comment_sequence_item import CalculationCommentSequenceItem
from .code_sequence_item import CodeSequenceItem
from .cornea_measurements_sequence_item import CorneaMeasurementsSequenceItem
from .corneal_size_sequence_item import CornealSizeSequenceItem
from .flat_keratometric_axis_sequence_item import FlatKeratometricAxisSequenceItem
from .iol_power_sequence_item import IOLPowerSequenceItem
from .lens_constant_sequence_item import LensConstantSequenceItem
from .lens_thickness_sequence_item import LensThicknessSequenceItem
from .ophthalmic_axial_length_sequence_item import OphthalmicAxialLengthSequenceItem
from .refractive_state_sequence_item import RefractiveStateSequenceItem
from .steep_keratometric_axis_sequence_item import SteepKeratometricAxisSequenceItem
from .surgically_induced_astigmatism_sequence_item import (
    SurgicallyInducedAstigmatismSequenceItem,
)
from .toric_iol_power_for_exact_emmetropia_sequence_item import (
    ToricIOLPowerForExactEmmetropiaSequenceItem,
)
from .toric_iol_power_for_exact_target_refraction_sequence_item import (
    ToricIOLPowerForExactTargetRefractionSequenceItem,
)


class IntraocularLensCalculationsRightEyeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RefractiveStateSequence: List[RefractiveStateSequenceItem] = []
        self._OphthalmicAxialLengthSequence: List[OphthalmicAxialLengthSequenceItem] = []
        self._IOLFormulaCodeSequence: List[CodeSequenceItem] = []
        self._RefractiveSurgeryTypeCodeSequence: List[CodeSequenceItem] = []
        self._SurgicallyInducedAstigmatismSequence: List[SurgicallyInducedAstigmatismSequenceItem] = []
        self._ToricIOLPowerForExactEmmetropiaSequence: List[ToricIOLPowerForExactEmmetropiaSequenceItem] = []
        self._ToricIOLPowerForExactTargetRefractionSequence: List[ToricIOLPowerForExactTargetRefractionSequenceItem] = []
        self._IOLPowerSequence: List[IOLPowerSequenceItem] = []
        self._LensConstantSequence: List[LensConstantSequenceItem] = []
        self._KeratometryMeasurementTypeCodeSequence: List[CodeSequenceItem] = []
        self._RefractiveErrorBeforeRefractiveSurgeryCodeSequence: List[CodeSequenceItem] = []
        self._LensThicknessSequence: List[LensThicknessSequenceItem] = []
        self._AnteriorChamberDepthSequence: List[AnteriorChamberDepthSequenceItem] = []
        self._CalculationCommentSequence: List[CalculationCommentSequenceItem] = []
        self._CornealSizeSequence: List[CornealSizeSequenceItem] = []
        self._SteepKeratometricAxisSequence: List[SteepKeratometricAxisSequenceItem] = []
        self._FlatKeratometricAxisSequence: List[FlatKeratometricAxisSequenceItem] = []
        self._CorneaMeasurementsSequence: List[CorneaMeasurementsSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RefractiveStateSequence(self) -> Optional[List[RefractiveStateSequenceItem]]:
        if "RefractiveStateSequence" in self._dataset:
            if len(self._RefractiveStateSequence) == len(self._dataset.RefractiveStateSequence):
                return self._RefractiveStateSequence
            else:
                return [RefractiveStateSequenceItem(x) for x in self._dataset.RefractiveStateSequence]
        return None

    @RefractiveStateSequence.setter
    def RefractiveStateSequence(self, value: Optional[List[RefractiveStateSequenceItem]]):
        if value is None:
            self._RefractiveStateSequence = []
            if "RefractiveStateSequence" in self._dataset:
                del self._dataset.RefractiveStateSequence
        elif not isinstance(value, list) or not all(isinstance(item, RefractiveStateSequenceItem) for item in value):
            raise ValueError(f"RefractiveStateSequence must be a list of RefractiveStateSequenceItem objects")
        else:
            self._RefractiveStateSequence = value
            if "RefractiveStateSequence" not in self._dataset:
                self._dataset.RefractiveStateSequence = pydicom.Sequence()
            self._dataset.RefractiveStateSequence.clear()
            self._dataset.RefractiveStateSequence.extend([item.to_dataset() for item in value])

    def add_RefractiveState(self, item: RefractiveStateSequenceItem):
        if not isinstance(item, RefractiveStateSequenceItem):
            raise ValueError(f"Item must be an instance of RefractiveStateSequenceItem")
        self._RefractiveStateSequence.append(item)
        if "RefractiveStateSequence" not in self._dataset:
            self._dataset.RefractiveStateSequence = pydicom.Sequence()
        self._dataset.RefractiveStateSequence.append(item.to_dataset())

    @property
    def OphthalmicAxialLengthSequence(self) -> Optional[List[OphthalmicAxialLengthSequenceItem]]:
        if "OphthalmicAxialLengthSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthSequence) == len(self._dataset.OphthalmicAxialLengthSequence):
                return self._OphthalmicAxialLengthSequence
            else:
                return [OphthalmicAxialLengthSequenceItem(x) for x in self._dataset.OphthalmicAxialLengthSequence]
        return None

    @OphthalmicAxialLengthSequence.setter
    def OphthalmicAxialLengthSequence(self, value: Optional[List[OphthalmicAxialLengthSequenceItem]]):
        if value is None:
            self._OphthalmicAxialLengthSequence = []
            if "OphthalmicAxialLengthSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthSequence
        elif not isinstance(value, list) or not all(isinstance(item, OphthalmicAxialLengthSequenceItem) for item in value):
            raise ValueError(f"OphthalmicAxialLengthSequence must be a list of OphthalmicAxialLengthSequenceItem objects")
        else:
            self._OphthalmicAxialLengthSequence = value
            if "OphthalmicAxialLengthSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthSequence.clear()
            self._dataset.OphthalmicAxialLengthSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLength(self, item: OphthalmicAxialLengthSequenceItem):
        if not isinstance(item, OphthalmicAxialLengthSequenceItem):
            raise ValueError(f"Item must be an instance of OphthalmicAxialLengthSequenceItem")
        self._OphthalmicAxialLengthSequence.append(item)
        if "OphthalmicAxialLengthSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthSequence.append(item.to_dataset())

    @property
    def IOLFormulaCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "IOLFormulaCodeSequence" in self._dataset:
            if len(self._IOLFormulaCodeSequence) == len(self._dataset.IOLFormulaCodeSequence):
                return self._IOLFormulaCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.IOLFormulaCodeSequence]
        return None

    @IOLFormulaCodeSequence.setter
    def IOLFormulaCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._IOLFormulaCodeSequence = []
            if "IOLFormulaCodeSequence" in self._dataset:
                del self._dataset.IOLFormulaCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"IOLFormulaCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._IOLFormulaCodeSequence = value
            if "IOLFormulaCodeSequence" not in self._dataset:
                self._dataset.IOLFormulaCodeSequence = pydicom.Sequence()
            self._dataset.IOLFormulaCodeSequence.clear()
            self._dataset.IOLFormulaCodeSequence.extend([item.to_dataset() for item in value])

    def add_IOLFormulaCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._IOLFormulaCodeSequence.append(item)
        if "IOLFormulaCodeSequence" not in self._dataset:
            self._dataset.IOLFormulaCodeSequence = pydicom.Sequence()
        self._dataset.IOLFormulaCodeSequence.append(item.to_dataset())

    @property
    def IOLFormulaDetail(self) -> Optional[str]:
        if "IOLFormulaDetail" in self._dataset:
            return self._dataset.IOLFormulaDetail
        return None

    @IOLFormulaDetail.setter
    def IOLFormulaDetail(self, value: Optional[str]):
        if value is None:
            if "IOLFormulaDetail" in self._dataset:
                del self._dataset.IOLFormulaDetail
        else:
            self._dataset.IOLFormulaDetail = value

    @property
    def KeratometerIndex(self) -> Optional[float]:
        if "KeratometerIndex" in self._dataset:
            return self._dataset.KeratometerIndex
        return None

    @KeratometerIndex.setter
    def KeratometerIndex(self, value: Optional[float]):
        if value is None:
            if "KeratometerIndex" in self._dataset:
                del self._dataset.KeratometerIndex
        else:
            self._dataset.KeratometerIndex = value

    @property
    def TargetRefraction(self) -> Optional[float]:
        if "TargetRefraction" in self._dataset:
            return self._dataset.TargetRefraction
        return None

    @TargetRefraction.setter
    def TargetRefraction(self, value: Optional[float]):
        if value is None:
            if "TargetRefraction" in self._dataset:
                del self._dataset.TargetRefraction
        else:
            self._dataset.TargetRefraction = value

    @property
    def RefractiveProcedureOccurred(self) -> Optional[str]:
        if "RefractiveProcedureOccurred" in self._dataset:
            return self._dataset.RefractiveProcedureOccurred
        return None

    @RefractiveProcedureOccurred.setter
    def RefractiveProcedureOccurred(self, value: Optional[str]):
        if value is None:
            if "RefractiveProcedureOccurred" in self._dataset:
                del self._dataset.RefractiveProcedureOccurred
        else:
            self._dataset.RefractiveProcedureOccurred = value

    @property
    def RefractiveSurgeryTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RefractiveSurgeryTypeCodeSequence" in self._dataset:
            if len(self._RefractiveSurgeryTypeCodeSequence) == len(self._dataset.RefractiveSurgeryTypeCodeSequence):
                return self._RefractiveSurgeryTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RefractiveSurgeryTypeCodeSequence]
        return None

    @RefractiveSurgeryTypeCodeSequence.setter
    def RefractiveSurgeryTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RefractiveSurgeryTypeCodeSequence = []
            if "RefractiveSurgeryTypeCodeSequence" in self._dataset:
                del self._dataset.RefractiveSurgeryTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"RefractiveSurgeryTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RefractiveSurgeryTypeCodeSequence = value
            if "RefractiveSurgeryTypeCodeSequence" not in self._dataset:
                self._dataset.RefractiveSurgeryTypeCodeSequence = pydicom.Sequence()
            self._dataset.RefractiveSurgeryTypeCodeSequence.clear()
            self._dataset.RefractiveSurgeryTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_RefractiveSurgeryTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RefractiveSurgeryTypeCodeSequence.append(item)
        if "RefractiveSurgeryTypeCodeSequence" not in self._dataset:
            self._dataset.RefractiveSurgeryTypeCodeSequence = pydicom.Sequence()
        self._dataset.RefractiveSurgeryTypeCodeSequence.append(item.to_dataset())

    @property
    def SurgicallyInducedAstigmatismSequence(self) -> Optional[List[SurgicallyInducedAstigmatismSequenceItem]]:
        if "SurgicallyInducedAstigmatismSequence" in self._dataset:
            if len(self._SurgicallyInducedAstigmatismSequence) == len(self._dataset.SurgicallyInducedAstigmatismSequence):
                return self._SurgicallyInducedAstigmatismSequence
            else:
                return [
                    SurgicallyInducedAstigmatismSequenceItem(x) for x in self._dataset.SurgicallyInducedAstigmatismSequence
                ]
        return None

    @SurgicallyInducedAstigmatismSequence.setter
    def SurgicallyInducedAstigmatismSequence(self, value: Optional[List[SurgicallyInducedAstigmatismSequenceItem]]):
        if value is None:
            self._SurgicallyInducedAstigmatismSequence = []
            if "SurgicallyInducedAstigmatismSequence" in self._dataset:
                del self._dataset.SurgicallyInducedAstigmatismSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SurgicallyInducedAstigmatismSequenceItem) for item in value
        ):
            raise ValueError(
                f"SurgicallyInducedAstigmatismSequence must be a list of SurgicallyInducedAstigmatismSequenceItem objects"
            )
        else:
            self._SurgicallyInducedAstigmatismSequence = value
            if "SurgicallyInducedAstigmatismSequence" not in self._dataset:
                self._dataset.SurgicallyInducedAstigmatismSequence = pydicom.Sequence()
            self._dataset.SurgicallyInducedAstigmatismSequence.clear()
            self._dataset.SurgicallyInducedAstigmatismSequence.extend([item.to_dataset() for item in value])

    def add_SurgicallyInducedAstigmatism(self, item: SurgicallyInducedAstigmatismSequenceItem):
        if not isinstance(item, SurgicallyInducedAstigmatismSequenceItem):
            raise ValueError(f"Item must be an instance of SurgicallyInducedAstigmatismSequenceItem")
        self._SurgicallyInducedAstigmatismSequence.append(item)
        if "SurgicallyInducedAstigmatismSequence" not in self._dataset:
            self._dataset.SurgicallyInducedAstigmatismSequence = pydicom.Sequence()
        self._dataset.SurgicallyInducedAstigmatismSequence.append(item.to_dataset())

    @property
    def TypeOfOpticalCorrection(self) -> Optional[str]:
        if "TypeOfOpticalCorrection" in self._dataset:
            return self._dataset.TypeOfOpticalCorrection
        return None

    @TypeOfOpticalCorrection.setter
    def TypeOfOpticalCorrection(self, value: Optional[str]):
        if value is None:
            if "TypeOfOpticalCorrection" in self._dataset:
                del self._dataset.TypeOfOpticalCorrection
        else:
            self._dataset.TypeOfOpticalCorrection = value

    @property
    def ToricIOLPowerForExactEmmetropiaSequence(self) -> Optional[List[ToricIOLPowerForExactEmmetropiaSequenceItem]]:
        if "ToricIOLPowerForExactEmmetropiaSequence" in self._dataset:
            if len(self._ToricIOLPowerForExactEmmetropiaSequence) == len(
                self._dataset.ToricIOLPowerForExactEmmetropiaSequence
            ):
                return self._ToricIOLPowerForExactEmmetropiaSequence
            else:
                return [
                    ToricIOLPowerForExactEmmetropiaSequenceItem(x)
                    for x in self._dataset.ToricIOLPowerForExactEmmetropiaSequence
                ]
        return None

    @ToricIOLPowerForExactEmmetropiaSequence.setter
    def ToricIOLPowerForExactEmmetropiaSequence(self, value: Optional[List[ToricIOLPowerForExactEmmetropiaSequenceItem]]):
        if value is None:
            self._ToricIOLPowerForExactEmmetropiaSequence = []
            if "ToricIOLPowerForExactEmmetropiaSequence" in self._dataset:
                del self._dataset.ToricIOLPowerForExactEmmetropiaSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ToricIOLPowerForExactEmmetropiaSequenceItem) for item in value
        ):
            raise ValueError(
                f"ToricIOLPowerForExactEmmetropiaSequence must be a list of ToricIOLPowerForExactEmmetropiaSequenceItem objects"
            )
        else:
            self._ToricIOLPowerForExactEmmetropiaSequence = value
            if "ToricIOLPowerForExactEmmetropiaSequence" not in self._dataset:
                self._dataset.ToricIOLPowerForExactEmmetropiaSequence = pydicom.Sequence()
            self._dataset.ToricIOLPowerForExactEmmetropiaSequence.clear()
            self._dataset.ToricIOLPowerForExactEmmetropiaSequence.extend([item.to_dataset() for item in value])

    def add_ToricIOLPowerForExactEmmetropia(self, item: ToricIOLPowerForExactEmmetropiaSequenceItem):
        if not isinstance(item, ToricIOLPowerForExactEmmetropiaSequenceItem):
            raise ValueError(f"Item must be an instance of ToricIOLPowerForExactEmmetropiaSequenceItem")
        self._ToricIOLPowerForExactEmmetropiaSequence.append(item)
        if "ToricIOLPowerForExactEmmetropiaSequence" not in self._dataset:
            self._dataset.ToricIOLPowerForExactEmmetropiaSequence = pydicom.Sequence()
        self._dataset.ToricIOLPowerForExactEmmetropiaSequence.append(item.to_dataset())

    @property
    def ToricIOLPowerForExactTargetRefractionSequence(
        self,
    ) -> Optional[List[ToricIOLPowerForExactTargetRefractionSequenceItem]]:
        if "ToricIOLPowerForExactTargetRefractionSequence" in self._dataset:
            if len(self._ToricIOLPowerForExactTargetRefractionSequence) == len(
                self._dataset.ToricIOLPowerForExactTargetRefractionSequence
            ):
                return self._ToricIOLPowerForExactTargetRefractionSequence
            else:
                return [
                    ToricIOLPowerForExactTargetRefractionSequenceItem(x)
                    for x in self._dataset.ToricIOLPowerForExactTargetRefractionSequence
                ]
        return None

    @ToricIOLPowerForExactTargetRefractionSequence.setter
    def ToricIOLPowerForExactTargetRefractionSequence(
        self, value: Optional[List[ToricIOLPowerForExactTargetRefractionSequenceItem]]
    ):
        if value is None:
            self._ToricIOLPowerForExactTargetRefractionSequence = []
            if "ToricIOLPowerForExactTargetRefractionSequence" in self._dataset:
                del self._dataset.ToricIOLPowerForExactTargetRefractionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ToricIOLPowerForExactTargetRefractionSequenceItem) for item in value
        ):
            raise ValueError(
                f"ToricIOLPowerForExactTargetRefractionSequence must be a list of ToricIOLPowerForExactTargetRefractionSequenceItem objects"
            )
        else:
            self._ToricIOLPowerForExactTargetRefractionSequence = value
            if "ToricIOLPowerForExactTargetRefractionSequence" not in self._dataset:
                self._dataset.ToricIOLPowerForExactTargetRefractionSequence = pydicom.Sequence()
            self._dataset.ToricIOLPowerForExactTargetRefractionSequence.clear()
            self._dataset.ToricIOLPowerForExactTargetRefractionSequence.extend([item.to_dataset() for item in value])

    def add_ToricIOLPowerForExactTargetRefraction(self, item: ToricIOLPowerForExactTargetRefractionSequenceItem):
        if not isinstance(item, ToricIOLPowerForExactTargetRefractionSequenceItem):
            raise ValueError(f"Item must be an instance of ToricIOLPowerForExactTargetRefractionSequenceItem")
        self._ToricIOLPowerForExactTargetRefractionSequence.append(item)
        if "ToricIOLPowerForExactTargetRefractionSequence" not in self._dataset:
            self._dataset.ToricIOLPowerForExactTargetRefractionSequence = pydicom.Sequence()
        self._dataset.ToricIOLPowerForExactTargetRefractionSequence.append(item.to_dataset())

    @property
    def IOLPowerSequence(self) -> Optional[List[IOLPowerSequenceItem]]:
        if "IOLPowerSequence" in self._dataset:
            if len(self._IOLPowerSequence) == len(self._dataset.IOLPowerSequence):
                return self._IOLPowerSequence
            else:
                return [IOLPowerSequenceItem(x) for x in self._dataset.IOLPowerSequence]
        return None

    @IOLPowerSequence.setter
    def IOLPowerSequence(self, value: Optional[List[IOLPowerSequenceItem]]):
        if value is None:
            self._IOLPowerSequence = []
            if "IOLPowerSequence" in self._dataset:
                del self._dataset.IOLPowerSequence
        elif not isinstance(value, list) or not all(isinstance(item, IOLPowerSequenceItem) for item in value):
            raise ValueError(f"IOLPowerSequence must be a list of IOLPowerSequenceItem objects")
        else:
            self._IOLPowerSequence = value
            if "IOLPowerSequence" not in self._dataset:
                self._dataset.IOLPowerSequence = pydicom.Sequence()
            self._dataset.IOLPowerSequence.clear()
            self._dataset.IOLPowerSequence.extend([item.to_dataset() for item in value])

    def add_IOLPower(self, item: IOLPowerSequenceItem):
        if not isinstance(item, IOLPowerSequenceItem):
            raise ValueError(f"Item must be an instance of IOLPowerSequenceItem")
        self._IOLPowerSequence.append(item)
        if "IOLPowerSequence" not in self._dataset:
            self._dataset.IOLPowerSequence = pydicom.Sequence()
        self._dataset.IOLPowerSequence.append(item.to_dataset())

    @property
    def LensConstantSequence(self) -> Optional[List[LensConstantSequenceItem]]:
        if "LensConstantSequence" in self._dataset:
            if len(self._LensConstantSequence) == len(self._dataset.LensConstantSequence):
                return self._LensConstantSequence
            else:
                return [LensConstantSequenceItem(x) for x in self._dataset.LensConstantSequence]
        return None

    @LensConstantSequence.setter
    def LensConstantSequence(self, value: Optional[List[LensConstantSequenceItem]]):
        if value is None:
            self._LensConstantSequence = []
            if "LensConstantSequence" in self._dataset:
                del self._dataset.LensConstantSequence
        elif not isinstance(value, list) or not all(isinstance(item, LensConstantSequenceItem) for item in value):
            raise ValueError(f"LensConstantSequence must be a list of LensConstantSequenceItem objects")
        else:
            self._LensConstantSequence = value
            if "LensConstantSequence" not in self._dataset:
                self._dataset.LensConstantSequence = pydicom.Sequence()
            self._dataset.LensConstantSequence.clear()
            self._dataset.LensConstantSequence.extend([item.to_dataset() for item in value])

    def add_LensConstant(self, item: LensConstantSequenceItem):
        if not isinstance(item, LensConstantSequenceItem):
            raise ValueError(f"Item must be an instance of LensConstantSequenceItem")
        self._LensConstantSequence.append(item)
        if "LensConstantSequence" not in self._dataset:
            self._dataset.LensConstantSequence = pydicom.Sequence()
        self._dataset.LensConstantSequence.append(item.to_dataset())

    @property
    def IOLManufacturer(self) -> Optional[str]:
        if "IOLManufacturer" in self._dataset:
            return self._dataset.IOLManufacturer
        return None

    @IOLManufacturer.setter
    def IOLManufacturer(self, value: Optional[str]):
        if value is None:
            if "IOLManufacturer" in self._dataset:
                del self._dataset.IOLManufacturer
        else:
            self._dataset.IOLManufacturer = value

    @property
    def ImplantName(self) -> Optional[str]:
        if "ImplantName" in self._dataset:
            return self._dataset.ImplantName
        return None

    @ImplantName.setter
    def ImplantName(self, value: Optional[str]):
        if value is None:
            if "ImplantName" in self._dataset:
                del self._dataset.ImplantName
        else:
            self._dataset.ImplantName = value

    @property
    def KeratometryMeasurementTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "KeratometryMeasurementTypeCodeSequence" in self._dataset:
            if len(self._KeratometryMeasurementTypeCodeSequence) == len(self._dataset.KeratometryMeasurementTypeCodeSequence):
                return self._KeratometryMeasurementTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.KeratometryMeasurementTypeCodeSequence]
        return None

    @KeratometryMeasurementTypeCodeSequence.setter
    def KeratometryMeasurementTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._KeratometryMeasurementTypeCodeSequence = []
            if "KeratometryMeasurementTypeCodeSequence" in self._dataset:
                del self._dataset.KeratometryMeasurementTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"KeratometryMeasurementTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._KeratometryMeasurementTypeCodeSequence = value
            if "KeratometryMeasurementTypeCodeSequence" not in self._dataset:
                self._dataset.KeratometryMeasurementTypeCodeSequence = pydicom.Sequence()
            self._dataset.KeratometryMeasurementTypeCodeSequence.clear()
            self._dataset.KeratometryMeasurementTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_KeratometryMeasurementTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._KeratometryMeasurementTypeCodeSequence.append(item)
        if "KeratometryMeasurementTypeCodeSequence" not in self._dataset:
            self._dataset.KeratometryMeasurementTypeCodeSequence = pydicom.Sequence()
        self._dataset.KeratometryMeasurementTypeCodeSequence.append(item.to_dataset())

    @property
    def RefractiveErrorBeforeRefractiveSurgeryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RefractiveErrorBeforeRefractiveSurgeryCodeSequence" in self._dataset:
            if len(self._RefractiveErrorBeforeRefractiveSurgeryCodeSequence) == len(
                self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence
            ):
                return self._RefractiveErrorBeforeRefractiveSurgeryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence]
        return None

    @RefractiveErrorBeforeRefractiveSurgeryCodeSequence.setter
    def RefractiveErrorBeforeRefractiveSurgeryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RefractiveErrorBeforeRefractiveSurgeryCodeSequence = []
            if "RefractiveErrorBeforeRefractiveSurgeryCodeSequence" in self._dataset:
                del self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"RefractiveErrorBeforeRefractiveSurgeryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RefractiveErrorBeforeRefractiveSurgeryCodeSequence = value
            if "RefractiveErrorBeforeRefractiveSurgeryCodeSequence" not in self._dataset:
                self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence = pydicom.Sequence()
            self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence.clear()
            self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence.extend([item.to_dataset() for item in value])

    def add_RefractiveErrorBeforeRefractiveSurgeryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RefractiveErrorBeforeRefractiveSurgeryCodeSequence.append(item)
        if "RefractiveErrorBeforeRefractiveSurgeryCodeSequence" not in self._dataset:
            self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence = pydicom.Sequence()
        self._dataset.RefractiveErrorBeforeRefractiveSurgeryCodeSequence.append(item.to_dataset())

    @property
    def IOLPowerForExactEmmetropia(self) -> Optional[float]:
        if "IOLPowerForExactEmmetropia" in self._dataset:
            return self._dataset.IOLPowerForExactEmmetropia
        return None

    @IOLPowerForExactEmmetropia.setter
    def IOLPowerForExactEmmetropia(self, value: Optional[float]):
        if value is None:
            if "IOLPowerForExactEmmetropia" in self._dataset:
                del self._dataset.IOLPowerForExactEmmetropia
        else:
            self._dataset.IOLPowerForExactEmmetropia = value

    @property
    def IOLPowerForExactTargetRefraction(self) -> Optional[float]:
        if "IOLPowerForExactTargetRefraction" in self._dataset:
            return self._dataset.IOLPowerForExactTargetRefraction
        return None

    @IOLPowerForExactTargetRefraction.setter
    def IOLPowerForExactTargetRefraction(self, value: Optional[float]):
        if value is None:
            if "IOLPowerForExactTargetRefraction" in self._dataset:
                del self._dataset.IOLPowerForExactTargetRefraction
        else:
            self._dataset.IOLPowerForExactTargetRefraction = value

    @property
    def LensThicknessSequence(self) -> Optional[List[LensThicknessSequenceItem]]:
        if "LensThicknessSequence" in self._dataset:
            if len(self._LensThicknessSequence) == len(self._dataset.LensThicknessSequence):
                return self._LensThicknessSequence
            else:
                return [LensThicknessSequenceItem(x) for x in self._dataset.LensThicknessSequence]
        return None

    @LensThicknessSequence.setter
    def LensThicknessSequence(self, value: Optional[List[LensThicknessSequenceItem]]):
        if value is None:
            self._LensThicknessSequence = []
            if "LensThicknessSequence" in self._dataset:
                del self._dataset.LensThicknessSequence
        elif not isinstance(value, list) or not all(isinstance(item, LensThicknessSequenceItem) for item in value):
            raise ValueError(f"LensThicknessSequence must be a list of LensThicknessSequenceItem objects")
        else:
            self._LensThicknessSequence = value
            if "LensThicknessSequence" not in self._dataset:
                self._dataset.LensThicknessSequence = pydicom.Sequence()
            self._dataset.LensThicknessSequence.clear()
            self._dataset.LensThicknessSequence.extend([item.to_dataset() for item in value])

    def add_LensThickness(self, item: LensThicknessSequenceItem):
        if not isinstance(item, LensThicknessSequenceItem):
            raise ValueError(f"Item must be an instance of LensThicknessSequenceItem")
        self._LensThicknessSequence.append(item)
        if "LensThicknessSequence" not in self._dataset:
            self._dataset.LensThicknessSequence = pydicom.Sequence()
        self._dataset.LensThicknessSequence.append(item.to_dataset())

    @property
    def AnteriorChamberDepthSequence(self) -> Optional[List[AnteriorChamberDepthSequenceItem]]:
        if "AnteriorChamberDepthSequence" in self._dataset:
            if len(self._AnteriorChamberDepthSequence) == len(self._dataset.AnteriorChamberDepthSequence):
                return self._AnteriorChamberDepthSequence
            else:
                return [AnteriorChamberDepthSequenceItem(x) for x in self._dataset.AnteriorChamberDepthSequence]
        return None

    @AnteriorChamberDepthSequence.setter
    def AnteriorChamberDepthSequence(self, value: Optional[List[AnteriorChamberDepthSequenceItem]]):
        if value is None:
            self._AnteriorChamberDepthSequence = []
            if "AnteriorChamberDepthSequence" in self._dataset:
                del self._dataset.AnteriorChamberDepthSequence
        elif not isinstance(value, list) or not all(isinstance(item, AnteriorChamberDepthSequenceItem) for item in value):
            raise ValueError(f"AnteriorChamberDepthSequence must be a list of AnteriorChamberDepthSequenceItem objects")
        else:
            self._AnteriorChamberDepthSequence = value
            if "AnteriorChamberDepthSequence" not in self._dataset:
                self._dataset.AnteriorChamberDepthSequence = pydicom.Sequence()
            self._dataset.AnteriorChamberDepthSequence.clear()
            self._dataset.AnteriorChamberDepthSequence.extend([item.to_dataset() for item in value])

    def add_AnteriorChamberDepth(self, item: AnteriorChamberDepthSequenceItem):
        if not isinstance(item, AnteriorChamberDepthSequenceItem):
            raise ValueError(f"Item must be an instance of AnteriorChamberDepthSequenceItem")
        self._AnteriorChamberDepthSequence.append(item)
        if "AnteriorChamberDepthSequence" not in self._dataset:
            self._dataset.AnteriorChamberDepthSequence = pydicom.Sequence()
        self._dataset.AnteriorChamberDepthSequence.append(item.to_dataset())

    @property
    def CalculationCommentSequence(self) -> Optional[List[CalculationCommentSequenceItem]]:
        if "CalculationCommentSequence" in self._dataset:
            if len(self._CalculationCommentSequence) == len(self._dataset.CalculationCommentSequence):
                return self._CalculationCommentSequence
            else:
                return [CalculationCommentSequenceItem(x) for x in self._dataset.CalculationCommentSequence]
        return None

    @CalculationCommentSequence.setter
    def CalculationCommentSequence(self, value: Optional[List[CalculationCommentSequenceItem]]):
        if value is None:
            self._CalculationCommentSequence = []
            if "CalculationCommentSequence" in self._dataset:
                del self._dataset.CalculationCommentSequence
        elif not isinstance(value, list) or not all(isinstance(item, CalculationCommentSequenceItem) for item in value):
            raise ValueError(f"CalculationCommentSequence must be a list of CalculationCommentSequenceItem objects")
        else:
            self._CalculationCommentSequence = value
            if "CalculationCommentSequence" not in self._dataset:
                self._dataset.CalculationCommentSequence = pydicom.Sequence()
            self._dataset.CalculationCommentSequence.clear()
            self._dataset.CalculationCommentSequence.extend([item.to_dataset() for item in value])

    def add_CalculationComment(self, item: CalculationCommentSequenceItem):
        if not isinstance(item, CalculationCommentSequenceItem):
            raise ValueError(f"Item must be an instance of CalculationCommentSequenceItem")
        self._CalculationCommentSequence.append(item)
        if "CalculationCommentSequence" not in self._dataset:
            self._dataset.CalculationCommentSequence = pydicom.Sequence()
        self._dataset.CalculationCommentSequence.append(item.to_dataset())

    @property
    def CornealSizeSequence(self) -> Optional[List[CornealSizeSequenceItem]]:
        if "CornealSizeSequence" in self._dataset:
            if len(self._CornealSizeSequence) == len(self._dataset.CornealSizeSequence):
                return self._CornealSizeSequence
            else:
                return [CornealSizeSequenceItem(x) for x in self._dataset.CornealSizeSequence]
        return None

    @CornealSizeSequence.setter
    def CornealSizeSequence(self, value: Optional[List[CornealSizeSequenceItem]]):
        if value is None:
            self._CornealSizeSequence = []
            if "CornealSizeSequence" in self._dataset:
                del self._dataset.CornealSizeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CornealSizeSequenceItem) for item in value):
            raise ValueError(f"CornealSizeSequence must be a list of CornealSizeSequenceItem objects")
        else:
            self._CornealSizeSequence = value
            if "CornealSizeSequence" not in self._dataset:
                self._dataset.CornealSizeSequence = pydicom.Sequence()
            self._dataset.CornealSizeSequence.clear()
            self._dataset.CornealSizeSequence.extend([item.to_dataset() for item in value])

    def add_CornealSize(self, item: CornealSizeSequenceItem):
        if not isinstance(item, CornealSizeSequenceItem):
            raise ValueError(f"Item must be an instance of CornealSizeSequenceItem")
        self._CornealSizeSequence.append(item)
        if "CornealSizeSequence" not in self._dataset:
            self._dataset.CornealSizeSequence = pydicom.Sequence()
        self._dataset.CornealSizeSequence.append(item.to_dataset())

    @property
    def SteepKeratometricAxisSequence(self) -> Optional[List[SteepKeratometricAxisSequenceItem]]:
        if "SteepKeratometricAxisSequence" in self._dataset:
            if len(self._SteepKeratometricAxisSequence) == len(self._dataset.SteepKeratometricAxisSequence):
                return self._SteepKeratometricAxisSequence
            else:
                return [SteepKeratometricAxisSequenceItem(x) for x in self._dataset.SteepKeratometricAxisSequence]
        return None

    @SteepKeratometricAxisSequence.setter
    def SteepKeratometricAxisSequence(self, value: Optional[List[SteepKeratometricAxisSequenceItem]]):
        if value is None:
            self._SteepKeratometricAxisSequence = []
            if "SteepKeratometricAxisSequence" in self._dataset:
                del self._dataset.SteepKeratometricAxisSequence
        elif not isinstance(value, list) or not all(isinstance(item, SteepKeratometricAxisSequenceItem) for item in value):
            raise ValueError(f"SteepKeratometricAxisSequence must be a list of SteepKeratometricAxisSequenceItem objects")
        else:
            self._SteepKeratometricAxisSequence = value
            if "SteepKeratometricAxisSequence" not in self._dataset:
                self._dataset.SteepKeratometricAxisSequence = pydicom.Sequence()
            self._dataset.SteepKeratometricAxisSequence.clear()
            self._dataset.SteepKeratometricAxisSequence.extend([item.to_dataset() for item in value])

    def add_SteepKeratometricAxis(self, item: SteepKeratometricAxisSequenceItem):
        if not isinstance(item, SteepKeratometricAxisSequenceItem):
            raise ValueError(f"Item must be an instance of SteepKeratometricAxisSequenceItem")
        self._SteepKeratometricAxisSequence.append(item)
        if "SteepKeratometricAxisSequence" not in self._dataset:
            self._dataset.SteepKeratometricAxisSequence = pydicom.Sequence()
        self._dataset.SteepKeratometricAxisSequence.append(item.to_dataset())

    @property
    def FlatKeratometricAxisSequence(self) -> Optional[List[FlatKeratometricAxisSequenceItem]]:
        if "FlatKeratometricAxisSequence" in self._dataset:
            if len(self._FlatKeratometricAxisSequence) == len(self._dataset.FlatKeratometricAxisSequence):
                return self._FlatKeratometricAxisSequence
            else:
                return [FlatKeratometricAxisSequenceItem(x) for x in self._dataset.FlatKeratometricAxisSequence]
        return None

    @FlatKeratometricAxisSequence.setter
    def FlatKeratometricAxisSequence(self, value: Optional[List[FlatKeratometricAxisSequenceItem]]):
        if value is None:
            self._FlatKeratometricAxisSequence = []
            if "FlatKeratometricAxisSequence" in self._dataset:
                del self._dataset.FlatKeratometricAxisSequence
        elif not isinstance(value, list) or not all(isinstance(item, FlatKeratometricAxisSequenceItem) for item in value):
            raise ValueError(f"FlatKeratometricAxisSequence must be a list of FlatKeratometricAxisSequenceItem objects")
        else:
            self._FlatKeratometricAxisSequence = value
            if "FlatKeratometricAxisSequence" not in self._dataset:
                self._dataset.FlatKeratometricAxisSequence = pydicom.Sequence()
            self._dataset.FlatKeratometricAxisSequence.clear()
            self._dataset.FlatKeratometricAxisSequence.extend([item.to_dataset() for item in value])

    def add_FlatKeratometricAxis(self, item: FlatKeratometricAxisSequenceItem):
        if not isinstance(item, FlatKeratometricAxisSequenceItem):
            raise ValueError(f"Item must be an instance of FlatKeratometricAxisSequenceItem")
        self._FlatKeratometricAxisSequence.append(item)
        if "FlatKeratometricAxisSequence" not in self._dataset:
            self._dataset.FlatKeratometricAxisSequence = pydicom.Sequence()
        self._dataset.FlatKeratometricAxisSequence.append(item.to_dataset())

    @property
    def CorneaMeasurementsSequence(self) -> Optional[List[CorneaMeasurementsSequenceItem]]:
        if "CorneaMeasurementsSequence" in self._dataset:
            if len(self._CorneaMeasurementsSequence) == len(self._dataset.CorneaMeasurementsSequence):
                return self._CorneaMeasurementsSequence
            else:
                return [CorneaMeasurementsSequenceItem(x) for x in self._dataset.CorneaMeasurementsSequence]
        return None

    @CorneaMeasurementsSequence.setter
    def CorneaMeasurementsSequence(self, value: Optional[List[CorneaMeasurementsSequenceItem]]):
        if value is None:
            self._CorneaMeasurementsSequence = []
            if "CorneaMeasurementsSequence" in self._dataset:
                del self._dataset.CorneaMeasurementsSequence
        elif not isinstance(value, list) or not all(isinstance(item, CorneaMeasurementsSequenceItem) for item in value):
            raise ValueError(f"CorneaMeasurementsSequence must be a list of CorneaMeasurementsSequenceItem objects")
        else:
            self._CorneaMeasurementsSequence = value
            if "CorneaMeasurementsSequence" not in self._dataset:
                self._dataset.CorneaMeasurementsSequence = pydicom.Sequence()
            self._dataset.CorneaMeasurementsSequence.clear()
            self._dataset.CorneaMeasurementsSequence.extend([item.to_dataset() for item in value])

    def add_CorneaMeasurements(self, item: CorneaMeasurementsSequenceItem):
        if not isinstance(item, CorneaMeasurementsSequenceItem):
            raise ValueError(f"Item must be an instance of CorneaMeasurementsSequenceItem")
        self._CorneaMeasurementsSequence.append(item)
        if "CorneaMeasurementsSequence" not in self._dataset:
            self._dataset.CorneaMeasurementsSequence = pydicom.Sequence()
        self._dataset.CorneaMeasurementsSequence.append(item.to_dataset())
