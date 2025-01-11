from pynetdicom import AllStoragePresentationContexts
from pydicom.uid import AllTransferSyntaxes

UPS_SOP_CLASSES = {
    "UnifiedProcedureStepPush": "1.2.840.10008.5.1.4.34.6.1",
    "UnifiedProcedureStepWatch": "1.2.840.10008.5.1.4.34.6.2",
    "UnifiedProcedureStepPull": "1.2.840.10008.5.1.4.34.6.3",
    "UnifiedProcedureStepEvent": "1.2.840.10008.5.1.4.34.6.4",
    "UnifiedProcedureStepQuery": "1.2.840.10008.5.1.4.34.6.5",
}


def validate_sop_classes(sop_classes):
    """
    Validate a list of SOP Classes.

    The function will take a list of SOP Classes and validate them against
    the list of all Storage SOP Classes. The function will return two
    dictionaries, one with valid SOP Classes and their corresponding UIDs, and
    one with invalid SOP Classes and None as their values.

    The items of sop_classes can be either a SOP Class UID, Name or Keyword
    from DICOM Part 6 Annex A "Registry of DICOM Unique Identifiers (UIDs)
    (Normative)" for Storage SOP classes defined in Part 4 Annex B.5.

    Parameters
    ----------
    sop_classes : list
        A list of SOP Classes to validate.

    Returns
    -------
    valid_sop_classes : dict
        A dictionary with valid SOP Classes as keys and their corresponding
        UIDs as values.
    invalid_sop_classes : dict
        A dictionary with invalid SOP Classes as keys and None as their values.
    """
    valid_sop_classes = {}
    invalid_sop_classes = {}

    for sop_class in sop_classes:
        # Remove leading and trailing whitespace
        sop_class = sop_class.strip()
        # If the item is an empty string, mark it as invalid
        # and go to the next SOP Class
        if not sop_class:
            invalid_sop_classes[sop_class] = None
            continue

        # Check if the item matches any the abstract syntax
        # of the Storage Presentation Contexts
        for context in AllStoragePresentationContexts:
            if sop_class in (context.abstract_syntax, context.abstract_syntax.name, context.abstract_syntax.keyword):
                valid_sop_classes[sop_class] = context.abstract_syntax
                break
        else:
            invalid_sop_classes[sop_class] = None

    return valid_sop_classes, invalid_sop_classes


def validate_transfer_syntaxes(transfer_syntaxes):
    """
    Validate a list of Transfer Syntaxes.

    The function will take a list of Transfer Syntaxes and validate them against
    the list of all Transfer Syntaxes. The function will return two
    dictionaries, one with valid Transfer Syntaxes and their corresponding UIDs, and
    one with invalid Transfer Syntaxes and None as their values.

    The items of transfer_syntaxes can be either a Transfer Syntax UID, Name or Keyword
    from DICOM Part 6 Annex A "Registry of DICOM Unique Identifiers (UIDs)
    (Normative)" for UIDs of Type "Transfer Syntax".

    Parameters
    ----------
    transfer_syntaxes : list
        A list of Transfer Syntaxes to validate.

    Returns
    -------
    valid_transfer_syntaxes : dict
        A dictionary with valid Transfer Syntaxes as keys and their corresponding
        UIDs as values.
    invalid_transfer_syntaxes : dict
        A dictionary with invalid Transfer Syntaxes as keys and None as their values.
    """
    valid_transfer_syntaxes = {}
    invalid_transfer_syntaxes = {}

    for transfer_syntax in transfer_syntaxes:
        # Remove leading and trailing whitespace
        transfer_syntax = transfer_syntax.strip()
        # If the item is an empty string, mark it as invalid
        if not transfer_syntax:
            invalid_transfer_syntaxes[transfer_syntax] = None
            continue

        # Check if the item matches any the Transfer Syntax
        for valid_transfer_syntax in AllTransferSyntaxes:
            if transfer_syntax in (valid_transfer_syntax, valid_transfer_syntax.name, valid_transfer_syntax.keyword):
                valid_transfer_syntaxes[transfer_syntax] = valid_transfer_syntax
                break
        else:
            invalid_transfer_syntaxes[transfer_syntax] = None
    return valid_transfer_syntaxes, invalid_transfer_syntaxes
