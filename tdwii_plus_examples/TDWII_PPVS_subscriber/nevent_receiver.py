from time import sleep

from pynetdicom import ALL_TRANSFER_SYNTAXES, UnifiedProcedurePresentationContexts, evt

from tdwii_plus_examples.TDWII_PPVS_subscriber.basescp import BaseSCP
from tdwii_plus_examples.TDWII_PPVS_subscriber.echoscp import EchoSCP
from tdwii_plus_examples.TDWII_PPVS_subscriber.nevent_receiver_handlers import (
    handle_nevent,
)


def nevent_cb(**kwargs):
    logger = None
    if "logger" in kwargs.keys():
        logger = kwargs["logger"]
    if logger:
        logger.info("nevent_cb invoked")
    event_type_id = 0  # not a valid type ID
    if logger:
        logger.info("TODO: Invoke application response appropriate to content of N-EVENT-REPORT-RQ")
    if "type_id" in kwargs.keys():
        event_type_id = kwargs["type_id"]
        if logger:
            logger.info(f"Event Type ID is: {event_type_id}")
    if "information_ds" in kwargs.keys():
        information_ds = kwargs["information_ds"]
        if logger:
            logger.info("Dataset in N-EVENT-REPORT-RQ: ")
            logger.info(f"{information_ds}")
    # TODO: replace if/elif with dict of {event_type_id,application_response_functions}
    if event_type_id == 1:
        if logger:
            logger.info("UPS State Report")
            logger.info("Probably time to do a C-FIND-RQ")
    elif event_type_id == 2:
        if logger:
            logger.info("UPS Cancel Request")
    elif event_type_id == 3:
        if logger:
            logger.info("UPS Progress Report")
            logger.info("Probably time to see if the Beam (number) changed, or if adaptation is taking or took place")
    elif event_type_id == 4:
        if logger:
            logger.info("SCP Status Change")
            logger.info(
                "Probably a good time to check if this is a Cold Start and then re-subscribe \
                    for specific UPS instances if this application has/had instance specific subscriptions"
            )
    elif event_type_id == 5:
        if logger:
            logger.info("UPS Assigned")
            logger.info(
                "Not too interesting for TDW-II, UPS are typically assigned at the time of scheduling, \
                    but a matching class of machines might make for a different approach"
            )
    else:
        if logger:
            logger.warning(f"Unknown Event Type ID: {event_type_id}")


class NEventReceiver(EchoSCP):
    def __init__(
        self, nevent_callback=None, ae_title: str = "NEVENT_RECEIVER", port: int = 11115, logger=None, bind_address: str = ""
    ):
        if nevent_callback is None:
            self.nevent_callback = nevent_cb  # fallback to something that just logs incoming events
        else:
            self.nevent_callback = nevent_callback
        EchoSCP.__init__(self, ae_title=ae_title, port=port, logger=logger, bind_address=bind_address)

    def _add_contexts(self):
        EchoSCP._add_contexts(self)
        for cx in UnifiedProcedurePresentationContexts:
            self.ae.add_supported_context(cx.abstract_syntax, ALL_TRANSFER_SYNTAXES, scp_role=True, scu_role=False)

    def _add_handlers(self):
        EchoSCP._add_handlers(self)
        self.handlers.append((evt.EVT_N_EVENT_REPORT, handle_nevent, [self.nevent_callback, None, self.logger]))

    def run(self):
        BaseSCP.run(self)


if __name__ == "__main__":
    my_scp = NEventReceiver()
    my_scp.run()
    while True:
        sleep(100)  # sleep forever
