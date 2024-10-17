from pynetdicom import AE, evt
from pynetdicom.sop_class import (
    CTImageStorage,
    RTIonPlanStorage,
    RTPlanStorage,
    RTStructureSetStorage,
)


class MockDicomServer:
    def __init__(self, port=11112, handler_tuples=None):
        self.ae = AE()
        self.ae.add_supported_context(CTImageStorage)
        self.ae.add_supported_context(RTIonPlanStorage)
        self.ae.add_supported_context(RTPlanStorage)
        self.ae.add_supported_context(RTStructureSetStorage)
        self.threaded_server = self.ae.start_server(("localhost", port), block=False, evt_handlers=handler_tuples)

    def stop(self):
        self.ae.shutdown()


def handle_store(event):
    return 0x0000  # Success


def start_mock_server(port=11112):
    handler_tuples = [(evt.EVT_C_STORE, handle_store)]
    server = MockDicomServer(port, handler_tuples)
    return server
