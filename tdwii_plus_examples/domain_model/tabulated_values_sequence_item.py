from typing import Any, List, Optional

import pydicom

from .cell_values_sequence_item import CellValuesSequenceItem
from .table_column_definition_sequence_item import TableColumnDefinitionSequenceItem
from .table_row_definition_sequence_item import TableRowDefinitionSequenceItem


class TabulatedValuesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TableRowDefinitionSequence: List[TableRowDefinitionSequenceItem] = []
        self._TableColumnDefinitionSequence: List[TableColumnDefinitionSequenceItem] = []
        self._CellValuesSequence: List[CellValuesSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NumberOfTableRows(self) -> Optional[int]:
        if "NumberOfTableRows" in self._dataset:
            return self._dataset.NumberOfTableRows
        return None

    @NumberOfTableRows.setter
    def NumberOfTableRows(self, value: Optional[int]):
        if value is None:
            if "NumberOfTableRows" in self._dataset:
                del self._dataset.NumberOfTableRows
        else:
            self._dataset.NumberOfTableRows = value

    @property
    def NumberOfTableColumns(self) -> Optional[int]:
        if "NumberOfTableColumns" in self._dataset:
            return self._dataset.NumberOfTableColumns
        return None

    @NumberOfTableColumns.setter
    def NumberOfTableColumns(self, value: Optional[int]):
        if value is None:
            if "NumberOfTableColumns" in self._dataset:
                del self._dataset.NumberOfTableColumns
        else:
            self._dataset.NumberOfTableColumns = value

    @property
    def TableRowDefinitionSequence(self) -> Optional[List[TableRowDefinitionSequenceItem]]:
        if "TableRowDefinitionSequence" in self._dataset:
            if len(self._TableRowDefinitionSequence) == len(self._dataset.TableRowDefinitionSequence):
                return self._TableRowDefinitionSequence
            else:
                return [TableRowDefinitionSequenceItem(x) for x in self._dataset.TableRowDefinitionSequence]
        return None

    @TableRowDefinitionSequence.setter
    def TableRowDefinitionSequence(self, value: Optional[List[TableRowDefinitionSequenceItem]]):
        if value is None:
            self._TableRowDefinitionSequence = []
            if "TableRowDefinitionSequence" in self._dataset:
                del self._dataset.TableRowDefinitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, TableRowDefinitionSequenceItem) for item in value):
            raise ValueError(f"TableRowDefinitionSequence must be a list of TableRowDefinitionSequenceItem objects")
        else:
            self._TableRowDefinitionSequence = value
            if "TableRowDefinitionSequence" not in self._dataset:
                self._dataset.TableRowDefinitionSequence = pydicom.Sequence()
            self._dataset.TableRowDefinitionSequence.clear()
            self._dataset.TableRowDefinitionSequence.extend([item.to_dataset() for item in value])

    def add_TableRowDefinition(self, item: TableRowDefinitionSequenceItem):
        if not isinstance(item, TableRowDefinitionSequenceItem):
            raise ValueError(f"Item must be an instance of TableRowDefinitionSequenceItem")
        self._TableRowDefinitionSequence.append(item)
        if "TableRowDefinitionSequence" not in self._dataset:
            self._dataset.TableRowDefinitionSequence = pydicom.Sequence()
        self._dataset.TableRowDefinitionSequence.append(item.to_dataset())

    @property
    def TableColumnDefinitionSequence(self) -> Optional[List[TableColumnDefinitionSequenceItem]]:
        if "TableColumnDefinitionSequence" in self._dataset:
            if len(self._TableColumnDefinitionSequence) == len(self._dataset.TableColumnDefinitionSequence):
                return self._TableColumnDefinitionSequence
            else:
                return [TableColumnDefinitionSequenceItem(x) for x in self._dataset.TableColumnDefinitionSequence]
        return None

    @TableColumnDefinitionSequence.setter
    def TableColumnDefinitionSequence(self, value: Optional[List[TableColumnDefinitionSequenceItem]]):
        if value is None:
            self._TableColumnDefinitionSequence = []
            if "TableColumnDefinitionSequence" in self._dataset:
                del self._dataset.TableColumnDefinitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, TableColumnDefinitionSequenceItem) for item in value):
            raise ValueError(f"TableColumnDefinitionSequence must be a list of TableColumnDefinitionSequenceItem objects")
        else:
            self._TableColumnDefinitionSequence = value
            if "TableColumnDefinitionSequence" not in self._dataset:
                self._dataset.TableColumnDefinitionSequence = pydicom.Sequence()
            self._dataset.TableColumnDefinitionSequence.clear()
            self._dataset.TableColumnDefinitionSequence.extend([item.to_dataset() for item in value])

    def add_TableColumnDefinition(self, item: TableColumnDefinitionSequenceItem):
        if not isinstance(item, TableColumnDefinitionSequenceItem):
            raise ValueError(f"Item must be an instance of TableColumnDefinitionSequenceItem")
        self._TableColumnDefinitionSequence.append(item)
        if "TableColumnDefinitionSequence" not in self._dataset:
            self._dataset.TableColumnDefinitionSequence = pydicom.Sequence()
        self._dataset.TableColumnDefinitionSequence.append(item.to_dataset())

    @property
    def CellValuesSequence(self) -> Optional[List[CellValuesSequenceItem]]:
        if "CellValuesSequence" in self._dataset:
            if len(self._CellValuesSequence) == len(self._dataset.CellValuesSequence):
                return self._CellValuesSequence
            else:
                return [CellValuesSequenceItem(x) for x in self._dataset.CellValuesSequence]
        return None

    @CellValuesSequence.setter
    def CellValuesSequence(self, value: Optional[List[CellValuesSequenceItem]]):
        if value is None:
            self._CellValuesSequence = []
            if "CellValuesSequence" in self._dataset:
                del self._dataset.CellValuesSequence
        elif not isinstance(value, list) or not all(isinstance(item, CellValuesSequenceItem) for item in value):
            raise ValueError(f"CellValuesSequence must be a list of CellValuesSequenceItem objects")
        else:
            self._CellValuesSequence = value
            if "CellValuesSequence" not in self._dataset:
                self._dataset.CellValuesSequence = pydicom.Sequence()
            self._dataset.CellValuesSequence.clear()
            self._dataset.CellValuesSequence.extend([item.to_dataset() for item in value])

    def add_CellValues(self, item: CellValuesSequenceItem):
        if not isinstance(item, CellValuesSequenceItem):
            raise ValueError(f"Item must be an instance of CellValuesSequenceItem")
        self._CellValuesSequence.append(item)
        if "CellValuesSequence" not in self._dataset:
            self._dataset.CellValuesSequence = pydicom.Sequence()
        self._dataset.CellValuesSequence.append(item.to_dataset())
