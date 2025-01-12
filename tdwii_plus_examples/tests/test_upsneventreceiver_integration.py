import unittest
from parameterized import parameterized
import logging
from logging.handlers import MemoryHandler
import subprocess
import time

from pydicom.dataset import Dataset
from pydicom import uid

from tdwii_plus_examples.upsneventreceiver import UPSNEventReceiver
from tdwii_plus_examples._dicom_uids import UPS_SOP_CLASSES
from pynetdicom import AE, evt
from pynetdicom.sop_class import UnifiedProcedureStepEvent


class TestUPSNEventReceiver(unittest.TestCase):

    def setUp(self):
        # Set up loggers
        self.memory_handler = MemoryHandler(100)
        self.rcv_logger = self._setup_logger(
            'neventreceiver', logging.DEBUG, self.memory_handler)
        self.test_logger = self._setup_logger(
            'test_neventreceiver', logging.DEBUG, logging.StreamHandler())

    def _setup_logger(self, name, level, handler):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger

    def tearDown(self):
        # Remove the memory handler from the logger
        self.memory_handler.close()
        self.rcv_logger.removeHandler(self.memory_handler)

    @parameterized.expand([
        ([],),
        ([uid.ExplicitVRLittleEndian],),
        ([uid.ImplicitVRLittleEndian],),
        ([uid.ExplicitVRLittleEndian, uid.ImplicitVRLittleEndian],),
        ([uid.ExplicitVRBigEndian, uid.ImplicitVRLittleEndian],),
        ([uid.ImplicitVRLittleEndian, uid.ExplicitVRLittleEndian],),
    ])
    def test_run_and_check_log(self, transfer_syntaxes):
        # Create a UPSNEventReceiver instance
        self.receiver = UPSNEventReceiver(
            bind_address="localhost",
            logger=self.rcv_logger,
            transfer_syntaxes=transfer_syntaxes
        )
        # Run the receiver
        self.receiver.run()
        self.test_logger.info("Receiver started successfully")

        # Create a mock UPS State Report Event dataset
        event_info_ds = Dataset()
        event_info_ds.ProcedureStepState = "SCHEDULED"
        event_info_ds.InputReadinessState = "READY"

        # send an N-EVENT-REPORT request
        soclassuid = UPS_SOP_CLASSES["UnifiedProcedureStepPush"]
        sopinstanceuid = uid.generate_uid()
        eventtypeid = 1

        # Create an AE and associate with the receiver
        ae = AE()
        ae.add_requested_context(UnifiedProcedureStepEvent)
        assoc = ae.associate('localhost', 11112, ae_title='EVENT_REPORT_RCV')

        if assoc.is_established:
            # Send the N-EVENT-REPORT request
            status = assoc.send_n_event_report(
                dataset=event_info_ds,
                event_type=eventtypeid,
                class_uid=soclassuid,
                instance_uid=sopinstanceuid
            )
            self.test_logger.info(f"N-EVENT-REPORT status: {status}")
            assoc.release()
        else:
            self.test_logger.error("Association with receiver failed")

        # Wait for 1 second to ensure the logs are generated
        time.sleep(1)

        # Get the log messages
        log_messages = [record.getMessage() for record
                        in self.memory_handler.buffer]
        self.test_logger.debug(f"Log messages: {log_messages}")

        # Check that the log messages contain the expected message
        self.assertIn(
            f"Processing Status Change for UPS Instance {sopinstanceuid}",
            log_messages,
            "Log messages do not contain the expected message"
        )

        # Stop the receiver
        self.receiver.stop()


if __name__ == "__main__":
    unittest.main()
