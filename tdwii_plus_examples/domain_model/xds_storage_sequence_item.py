from typing import Any, List, Optional  # noqa

import pydicom


class XDSStorageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RepositoryUniqueID(self) -> Optional[str]:
        if "RepositoryUniqueID" in self._dataset:
            return self._dataset.RepositoryUniqueID
        return None

    @RepositoryUniqueID.setter
    def RepositoryUniqueID(self, value: Optional[str]):
        if value is None:
            if "RepositoryUniqueID" in self._dataset:
                del self._dataset.RepositoryUniqueID
        else:
            self._dataset.RepositoryUniqueID = value

    @property
    def HomeCommunityID(self) -> Optional[str]:
        if "HomeCommunityID" in self._dataset:
            return self._dataset.HomeCommunityID
        return None

    @HomeCommunityID.setter
    def HomeCommunityID(self, value: Optional[str]):
        if value is None:
            if "HomeCommunityID" in self._dataset:
                del self._dataset.HomeCommunityID
        else:
            self._dataset.HomeCommunityID = value
