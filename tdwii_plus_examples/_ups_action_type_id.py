# tdwii_plus_examples/action_type_id.py
from enum import Enum, unique


@unique
class UPSActionTypeID(Enum):
    CHANGE_UPS_STATE = 1
    REQUEST_UPS_CANCEL = 2
    SUBSCRIBE = 3
    UNSUBSCRIBE = 4
    SUSPEND = 5
