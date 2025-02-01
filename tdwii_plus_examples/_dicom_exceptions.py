from pydicom.uid import UID


class AssociationError(Exception):
    """Custom exception for association errors."""

    pass


class ContextWarning(Exception):
    """Custom exception for context warnings."""

    def __init__(self, message: str, accepted_sop_classes: list[UID], refused_sop_classes: list[UID]):
        refused_sop_names = [f"[{UID(uid).name}]" for uid in refused_sop_classes]
        full_message = f"{message}: {', '.join(refused_sop_names)}"
        super().__init__(full_message)
        self.accepted_sop_classes: list[UID] = accepted_sop_classes
        self.refused_sop_classes: list[UID] = refused_sop_classes


class ResponseWarning(Exception):
    """Custom exception for response warnings."""

    def __init__(self, status_code, message):
        status_code_hex = f"{status_code:#06x}"
        super().__init__(f"{message} (Status Code: {status_code_hex})")
        self.status_code = status_code
        self.message = message


class ResponseError(Exception):
    """Custom exception for response errors"""

    def __init__(self, status_code, message):
        status_code_hex = f"{status_code:#06x}"
        super().__init__(f"{message} (Status Code: {status_code_hex})")
        self.status_code = status_code
        self.message = message


class ResponseUnknown(Exception):
    """Custom exception for response of unknown status."""

    def __init__(self, status_code, message):
        status_code_hex = f"{status_code:#06x}"
        super().__init__(f"{message} (Status Code: {status_code_hex})")
        self.status_code = status_code
        self.message = message


class ResponsePending(Exception):
    """Custom exception for response pending status"""

    def __init__(self, status_code, message):
        status_code_hex = f"{status_code:#06x}"
        super().__init__(f"{message} (Status Code: {status_code_hex})")
        self.status_code = status_code
        self.message = message
