import logging
import os
import shutil
import signal
import tempfile
import unittest
from logging import StreamHandler
from subprocess import TimeoutExpired

import psutil
from parameterized import parameterized
from pydicom import Dataset
from pydicom.uid import generate_uid
from pynetdicom.sop_class import CTImageStorage, UnifiedProcedureStepPush

from tdwii_plus_examples._dicom_macros import create_code_seq_item
from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.tests.utils.utils import get_configured_logger, start_scp
from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU
from tdwii_plus_examples.upspullnsetscu import UPSPullNSetSCU
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


class TestUPSPullNSetSCUIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for the SCU to DEBUG level with a stream handler
        cls.scu_logger, cls.stream_handler = get_configured_logger(
            "upspullnsetscu", level=logging.INFO, handler_class=StreamHandler
        )

        # Set up the logger for this test to DEBUG level
        cls.test_logger, cls.stream_handler = get_configured_logger("test_upspullnsetscu", level=logging.DEBUG)

        # Create a temporary directory for UPSSCP staging area
        cls.temp_dir = tempfile.mkdtemp()
        cls.test_logger.info(f"{cls.temp_dir} directory created")

        # Start the UPS SCP Server (replace with your actual SCP command)
        command = [
            "./tdwii_plus_examples/cli/upsscp/upsscp.py",
            "-d",
            "--database-location",
            f"{cls.temp_dir}/test.sqlite",
            "--instance-location",
            cls.temp_dir,
        ]

        cls.upsscp_started, cls.process, cls.stdout_thread, cls.stdout_lines = start_scp(command, cls.test_logger)
        cls.test_logger.info(f"Started process with PID: {cls.process.pid}")

        if not cls.upsscp_started:
            raise RuntimeError("upsscp server failed to start.")

        # Create the UPSPullNSetSCU instance
        cls.scu = UPSPullNSetSCU(
            calling_ae_title="UPSPULLSCU",
            called_ae_title="ANYSCP",
            called_ip="localhost",
            called_port=11114,
            logger=cls.scu_logger,
        )

        # Create a UPS in the SCP
        cls.ups_instance = generate_ups()
        push_scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSH",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=cls.scu_logger,
        )
        num_created_instances = push_scu.create_ups_instances([cls.ups_instance])

        if num_created_instances != 1:
            raise RuntimeError("failed to create UPS.")

        cls.sop_instance_uid = cls.ups_instance.SOPInstanceUID

        change_state_scu = UPSPullNActionSCU(
            calling_ae_title="UPSPULL",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=cls.scu_logger,
        )
        cls.tx_uid = change_state_scu.claim_ups(cls.sop_instance_uid)

        if not cls.tx_uid:
            raise RuntimeError("failed to claim UPS.")

    @classmethod
    def tearDownClass(cls):
        # Try to gracefully terminate the process.
        cls.test_logger.info(f"Terminating process with PID: {cls.process.pid}")
        try:
            cls.process.terminate()
            cls.process.wait(timeout=1)
            cls.test_logger.info("Process terminated gracefully.")
        except (ChildProcessError, TimeoutExpired):
            cls.test_logger.warning("Process termination timed out or process already finished.")

        # Try to kill child processes.
        try:
            parent = psutil.Process(cls.process.pid)
            for child in parent.children(recursive=True):
                child.kill()
            cls.test_logger.info("Child processes terminated.")
        except psutil.NoSuchProcess:
            cls.test_logger.warning("Error killing subprocesses. Parent process not found. Probably already terminated.")

        # Try to forcefully kill the process.
        try:
            os.kill(cls.process.pid, signal.SIGKILL)
            cls.process.wait(timeout=1)  # Ensure process termination
            cls.test_logger.info("Process forcefully terminated.")
        except OSError:
            cls.test_logger.warning("Error killing process. Probably already terminated.")

        finally:
            # Ensure the stdout thread has finished
            if cls.stdout_thread:
                cls.stdout_thread.join(timeout=1.0)

        # Print the SCP server output
        if hasattr(cls, "stdout_lines"):
            print(
                "\n"
                + "*" * 80
                + "\n*** BEGIN SCP SERVER OUTPUT ***\n"
                + "\n".join(cls.stdout_lines)
                + "\n*** END SCP SERVER OUTPUT ***\n"
                + "*" * 80
                + "\n"
            )

        # Remove the temporary directory and its contents
        files_in_temp_dir = os.listdir(cls.temp_dir)
        shutil.rmtree(cls.temp_dir)
        cls.test_logger.info(f"Removed the temp directory: {cls.temp_dir} and its contents: {files_in_temp_dir}")

        # Remove and close the handlers for scu and test loggers
        for logger, handler in [(cls.scu_logger, cls.stream_handler), (cls.test_logger, cls.stream_handler)]:
            logger.removeHandler(handler)
            handler.close()

    def test_modify_ups_integration(self):
        """Integration test for modifying a UPS instance using N-SET."""

        # Create the modification list dataset
        modification_list = Dataset()
        modification_list.AffectedSOPInstanceUID = type(self).sop_instance_uid
        modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
        modification_list.TransactionUID = type(self).tx_uid
        # Create the sequence item
        sequence_item = Dataset()
        sequence_item.ProcedureStepProgress = "10"
        # Add the sequence item to the sequence
        modification_list.ProcedureStepProgressInformationSequence = [sequence_item]

        # Try to modify the UPS
        result = type(self).scu.modify_ups(type(self).sop_instance_uid, modification_list)

        self.assertEqual(result.status_category, "Success")
        type(self).test_logger.info("Modified UPS successfully.")

    @parameterized.expand(
        [
            ("description_not_present", None),
            ("description_empty", ""),
            ("description_filled", "Some progress"),
        ]
    )
    def test_update_progress_integration(self, name, description):
        """Integration test for modifying a UPS instance using N-SET."""

        # Try to update the UPS progress
        if description is None:
            result = self.scu.update_progress_information(self.sop_instance_uid, self.tx_uid, 10)
        else:
            result = self.scu.update_progress_information(self.sop_instance_uid, self.tx_uid, 10, description)

        self.assertEqual(result.status_category, "Success")
        self.test_logger.info("Update UPS progress successfully.")

    from tdwii_plus_examples._dicom_macros import create_code_seq_item

    @parameterized.expand(
        [
            ("no_human_performer", None, None),
            ("with_human_performer", ("AS", "TDD", "Human Performer"), None),
            ("with_human_performer_and_name", ("AS", "TDD", "Human Performer"), "Alice Smith"),
            ("with_human_performer_name_only", None, "Bob Jones"),
        ]
    )
    def test_update_start_info(self, name, human_performer, human_performer_name):
        """Integration test for update_start_info with station_name, workitem_code, and optional human_performer and name."""

        station_name = ("GTR", "TMS", "Gantry")  # tuple
        workitem_code = create_code_seq_item("121726", "DCM", "RT Treatment with Internal Verification")  # Dataset

        result = self.scu.update_start_info(
            self.sop_instance_uid,
            self.tx_uid,
            station_name=station_name,
            workitem_code=workitem_code,
            human_performer=human_performer,
            human_performer_name=human_performer_name,
        )

        self.assertEqual(result.status_category, "Success")
        self.test_logger.info("Update UPS start info successfully.")

    def test_update_output_information(self):
        """Integration test for update_output_information (UPS output information N-SET)."""

        output_information_args = [
            (
                "OST",  # retrieve_ae_title
                generate_uid(),  # study_instance_uid
                generate_uid(),  # series_instance_uid
                CTImageStorage,  # sop_class_uid (CT Image Storage)
                generate_uid(),  # sop_instance_uid
            )
        ]

        result = self.scu.update_output_information(
            self.sop_instance_uid,
            self.tx_uid,
            output_information_args,
        )

        self.assertEqual(result.status_category, "Success")
        self.test_logger.info("Update UPS output information successfully.")

    def test_update_end_info(self):
        """Integration test for update_end_info (UPS end information N-SET)."""

        result = self.scu.update_end_info(self.sop_instance_uid, self.tx_uid)

        self.assertEqual(result.status_category, "Success")
        self.test_logger.info("Update UPS end info successfully.")

    @parameterized.expand(
        [
            ("description_not_present", None),
            ("description_empty", ""),
            ("description_filled", "Some good reason"),
        ]
    )
    def test_update_cancel_info(self, name, reason):
        """Integration test for modifying a UPS instance using N-SET."""

        # Try to update the UPS progress
        result = self.scu.update_cancel_info(self.sop_instance_uid, self.tx_uid, reason)

        self.assertEqual(result.status_category, "Success")
        self.test_logger.info("Update UPS progress successfully.")
