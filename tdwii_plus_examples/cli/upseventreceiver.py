#!/usr/bin/env python
import argparse
import logging
import time

from tdwii_plus_examples.upsneventreceiver import UPSNEventReceiver
from tdwii_plus_examples.upsneventhandler import UPS_EVENT_TYPES


def my_upsevent_callback(
    ups_instance, ups_event_type, ups_event_info, app_logger
):
    """
    Example of a UPS Event callback for processing incoming UPS events.

    This callback processes UPS State Change events. It does only log
    the received UPS Event Type and a message suggesting what behavior
    could be implemented. It's meant to be used as a starting point for
    writing your own callback.

    Parameters
    ----------
    ups_instance : pydicom.uid.UID
        The UPS SOP Instance UID.
    ups_event_type : int
        The UPS Event Type ID.
    ups_event_info : pydicom.dataset.Dataset
        The N-EVENT-REPORT-RQ Event Information dataset.
    app_logger : logging.Logger
        The application's logger instance
    """
    app_logger.info(f"Processing {UPS_EVENT_TYPES[ups_event_type]} Event")

    # Define the processing functions
    def process_ups_state_report(upsinstance, upseventinfo):
        """
        Process the UPS State Report Event.

        This function is called by the UPS Event Handler callback
        when a UPS State Report Event is received. It processes the
        received event information and takes appropriate actions.

        Parameters
        ----------
        upsinstance : pydicom.uid.UID
            The UPS SOP Instance UID.
        upseventinfo : pydicom.dataset.Dataset
            The received UPS Event Information dataset.
            +-------------------------------------------------+------+
            | Attribute Keyword                               | Type |
            +=================================================+======+
            | ProcedureStepState                              | 1    |
            +-------------------------------------------------+------+
            | InputReadinessState                             | 1    |
            +-------------------------------------------------+------+
            | ReasonForCancellation                           | 3    |
            +-------------------------------------------------+------+
            | ProcedureStepDiscontinuationReason​Code​Sequence  | 3    |
            +-------------------------------------------------+------+
            | >Include Table 8-3a “Enhanced SCU/SCP Coded     |      |
            | Entry Macro with no SCU Support and no Matching |      |
            | Key Support”                                    |      |
            +-------------------------------------------------+------+
            adapted from PS3.4 Table CC.2.4-1

        Returns
        -------
        None
        """
        state = upseventinfo.ProcedureStepState
        readiness = upseventinfo.InputReadinessState
        if state == 'SCHEDULED' and readiness != 'READY':
            app_logger.info(
                f"Waiting for UPS {upsinstance} inputs to be ready"
            )
        elif state == 'SCHEDULED' and readiness == 'READY':
            app_logger.info(
                f"Time to C-FIND UPS {upsinstance} and check if assigned "
                f"to my station name"
            )
        elif state == 'IN PROGRESS':
            app_logger.info(
                f"Time to C-FIND UPS {upsinstance} and check if assigned "
                f"to the station name I work with"
            )
        elif state == 'COMPLETED' or state == 'CANCELLED':
            app_logger.info(
                f"Time to close my session linked to UPS {upsinstance}"
            )

    def process_ups_cancel_request(upsinstance, upseventinfo):
        """
        Process the UPS Cancel Request Event.

        This function is called by the UPS Event Handler callback
        when a UPS Cancel Request Event is received. It processes the
        received event information and takes appropriate actions.

        Parameters
        ----------
        upsinstance : pydicom.uid.UID
            The UPS SOP Instance UID.
        upseventinfo : pydicom.dataset.Dataset
            The received UPS Event Information dataset.
            +-------------------------------------------------+------+
            | Attribute Keyword                               | Type |
            +=================================================+======+
            | RequestingAE                                    | 1    |
            +-------------------------------------------------+------+
            | ReasonForCancellation                           | 1C   |
            +-------------------------------------------------+------+
            | ProcedureStepDiscontinuationReasonCodeSequence  | 1C   |
            +-------------------------------------------------+------+
            | >Include Table 8-3a “Enhanced SCU/SCP Coded     |      |
            | Entry Macro with no SCU Support and no Matching |      |
            | Key Support”                                    |      |
            +-------------------------------------------------+------+
            | ContactURI                                      | 1C   |
            +-------------------------------------------------+------+
            | ContactDisplayName                              | 1C   |
            +-------------------------------------------------+------+
            adapted from PS3.4 Table CC.2.4-1

        Returns
        -------
        None
        """
        requesting_ae = upseventinfo.RequestingAE
        app_logger.info(
            f"Time to accept cancellation of UPS {upsinstance} "
            f"if {requesting_ae} was its creator and reject "
            f"otherwise"
        )

    def process_ups_progress_report(upsinstance, upseventinfo):
        """
        Process the UPS Progress Report Event.

        This function is called by the UPS Event Handler callback
        when a UPS Progress Report Event is received. It processes the
        received event information and takes appropriate actions.

        Parameters
        ----------
        upsinstance : pydicom.uid.UID
            The UPS SOP Instance UID.
        upseventinfo : pydicom.dataset.Dataset
            The received UPS Event Information dataset.
            +-------------------------------------------------+------+
            | Attribute Keyword                               | Type |
            +=================================================+======+
            | ProcedureStepProgressInformationSequence        | 1    |
            +-------------------------------------------------+------+
            | >ProcedureStepProgress                          | 3    |
            +-------------------------------------------------+------+
            | >ProcedureStepProgressDescription               | 3    |
            +-------------------------------------------------+------+
            | >ProcedureStepProgressParametersSequence        | 3    |
            +-------------------------------------------------+------+
            | >ProcedureStepCommunicationsURISequence         | 3    |
            +-------------------------------------------------+------+
            | >>ContactURI                                    | 1    |
            +-------------------------------------------------+------+
            | >>ContactDisplayName                            | 3    |
            +-------------------------------------------------+------+
            adapted from PS3.4 Table CC.2.4-1

        Returns
        -------
        None
        """

        app_logger.info(
            f"Time to check if the Beam (number) changed "
            f"if working with UPS {upsinstance}"
        )

    def process_scp_status_change(upsinstance, upseventinfo):
        """
        Process the SCP Status Change Event.

        This function is called by the UPS Event Handler callback
        when an SCP Status Change Event is received. It processes the
        received event information and takes appropriate actions.

        Parameters
        ----------
        upsinstance : pydicom.uid.UID
            The UPS SOP Instance UID.
        upseventinfo : pydicom.dataset.Dataset
            The received UPS Event Information dataset.
            +-------------------------------------------------+------+
            | Attribute Keyword                               | Type |
            +=================================================+======+
            | SCPStatus                                       | 1    |
            +-------------------------------------------------+------+
            | SubscriptionListStatus                          | 1    |
            +-------------------------------------------------+------+
            | UnifiedProcedureStepListStatus                  | 1    |
            +-------------------------------------------------+------+
            adapted from PS3.4 Table CC.2.4-1

        Returns
        -------
        None
        """
        scpstatus = upseventinfo.SCPStatus
        subscriptionstatus = upseventinfo.SubscriptionListStatus

        if scpstatus == "RESTARTED" and subscriptionstatus == "COLD START":
            app_logger.info(
                f"Time to check if this is a Cold Start and then re-subscribe "
                f"for specific UPS instances if this application has/had "
                f"instance specific subscriptions {upsinstance}"
            )
        elif scpstatus == "GOING DOWN":
            app_logger.info(
                "Time to warn the user that the Worklist Manager is "
                "going down "
            )

    def process_ups_assigned(upsinstance, upseventinfo):
        """
        Process the UPS Assigned Event.

        This function is called by the UPS Event Handler callback
        when a UPS Assigned Event is received. It processes the
        received event information and takes appropriate actions.

        Parameters
        ----------
        upsinstance : pydicom.uid.UID
            The UPS SOP Instance UID.
        upseventinfo : pydicom.dataset.Dataset
            The received UPS Event Information dataset.
            +-------------------------------------------------+------+
            | Attribute Keyword                               | Type |
            +=================================================+======+
            | ScheduledStationNameCodeSequence                | 1C   |
            +-------------------------------------------------+------+
            | >Include Table 8-3a “Enhanced SCU/SCP Coded     |      |
            | Entry Macro with no SCU Support and no Matching |      |
            | Key Support”                                    |      |
            +-------------------------------------------------+------+
            | HumanPerformerCodeSequence                      | 1C   |
            +-------------------------------------------------+------+
            | >Include Table 8-3a “Enhanced SCU/SCP Coded     |      |
            | Entry Macro with no SCU Support and no Matching |      |
            | Key Support”                                    |      |
            +-------------------------------------------------+------+
            | HumanPerformerOrganization                      | 1C   |
            +-------------------------------------------------+------+
            adapted from PS3.4 Table CC.2.4-1

        Returns
        -------
        None
        """

        app_logger.info(f"UPS {upsinstance} Assigned")
        app_logger.info(
            "Not too interesting for TDW-II, UPS are typically assigned at "
            "the time of scheduling, but a matching class of machines might "
            "make for a different approach"
        )

    # Dictionary to map event types to processing functions
    upsevent_process_functions = {
        "UPS State Report": process_ups_state_report,
        "UPS Cancel Request": process_ups_cancel_request,
        "UPS Progress Report": process_ups_progress_report,
        "SCP Status Change": process_scp_status_change,
        "UPS Assigned": process_ups_assigned
    }

    # Get the event type
    event_type = UPS_EVENT_TYPES[ups_event_type]

    # Call the appropriate processing function
    process_upsevent = upsevent_process_functions.get(
        event_type,
        lambda upsinstance, upseventinfo: app_logger.info(
            f"Unsupported UPS event type {event_type} for UPS {upsinstance}"
        )
    )
    process_upsevent(ups_instance, ups_event_info)


def main(loop_forever=True):  # Add a parameter to control the loop
    parser = argparse.ArgumentParser(
        description="Run a DICOM UPS Event Receiver (SCU)."
    )
    parser.add_argument(
        '-a', '--ae_title', type=str, default='UPSEVENT_RCV',
        help='Application Entity Title'
    )
    parser.add_argument(
        '-b', '--bind_address', type=str, default='',
        help='Specific IP address or hostname, omit to bind to all interfaces'
    )
    parser.add_argument(
        '-p', '--port', type=int, default=11112,
        help='Port number'
    )
    parser.add_argument(
        '-t', '--transfer_syntaxes', nargs='+',
        help='List of Transfer syntax to support'
    )
    parser.add_argument(
        '-c', '--callback', type=str,
        help='UPS Event callback function'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Set log level to INFO'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Set log level to DEBUG'
    )

    args = parser.parse_args()

    log_level = logging.WARNING
    if args.verbose:
        log_level = logging.INFO
    elif args.debug:
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level)
    logger = logging.getLogger('upseventreceiver')

    if args.callback:
        # Callback should be a function defined in the global namespace
        # at the module level, so we use globals() to look it up.
        # This allows passing a function name as a string argument.
        callback = globals().get(args.callback)
    else:
        callback = None

    logger.info("Starting up the DICOM UPS Event Receiver (SCU) ...")
    upsneventrcv = UPSNEventReceiver(
        ae_title=args.ae_title,
        bind_address=args.bind_address,
        port=args.port,
        logger=logger,
        transfer_syntaxes=args.transfer_syntaxes,
        ups_event_callback=callback,
    )
    upsneventrcv.run()
    logger.info("DICOM UPS Event Receiver (SCU) is running...")
    # Keep the main application running
    try:
        while loop_forever:
            time.sleep(1)  # Sleep to prevent high CPU usage
    except KeyboardInterrupt:
        logger.info("Shutting down the UPS Event Receiver (SCU) ...")


if __name__ == "__main__":
    main()
