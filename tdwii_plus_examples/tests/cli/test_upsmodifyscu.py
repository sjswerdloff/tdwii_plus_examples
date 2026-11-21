import contextlib
import io
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from tdwii_plus_examples.cli.upsmodifyscu import _claim_ups, _get_ups_info, _ncreate_sample_ups, main
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TestUpsModifySCU(unittest.TestCase):
    def run_script_with_args(self, test_args, scu_method, expected_args, expected_print=None):
        # Patch sys.argv for argparse
        with (
            patch.object(sys, "argv", test_args),
            patch("tdwii_plus_examples.cli.upsmodifyscu._ncreate_sample_ups", return_value="1.2.3.4.5"),
            patch("tdwii_plus_examples.cli.upsmodifyscu._claim_ups", return_value="1.2.3.4.5.6"),
            patch("tdwii_plus_examples.cli.upsmodifyscu.UPSPullNSetSCU") as mock_scu_class,
            patch("tdwii_plus_examples.cli.upsmodifyscu.dcmread", return_value="mock_ds"),
            patch("builtins.print") as mock_print,
        ):
            # Setup SCU mock
            mock_scu = MagicMock()
            mock_scu_class.return_value = mock_scu
            mock_result = MagicMock()
            mock_result.status_category = "Success"
            mock_result.status_description = "OK"
            getattr(mock_scu, scu_method).return_value = mock_result

            # Import and run main
            from tdwii_plus_examples.cli.upsmodifyscu import main

            main()

            # Assert correct SCU method called
            if scu_method == "update_start_info":
                mock_scu.update_start_info.assert_called_once()
                call_args, call_kwargs = mock_scu.update_start_info.call_args
                self.assertEqual(call_args[0], expected_args[0])
                self.assertEqual(call_args[1], expected_args[1])
                self.assertEqual(call_kwargs["station_name"], expected_args[2])
                self.assertEqual(call_kwargs["workitem_code"], expected_args[3])
                self.assertEqual(call_kwargs["human_performer"], expected_args[4])
                self.assertEqual(call_kwargs["human_performer_name"], expected_args[5])
            else:
                getattr(mock_scu, scu_method).assert_called_once_with(*expected_args)
            # Assert print output
            if expected_print:
                found = any(expected_print in str(call) for call in mock_print.call_args_list)
                self.assertTrue(found, f"Expected print '{expected_print}' in output")

    def test_progress(self):
        self.run_script_with_args(
            ["upsmodifyscu.py", "localhost", "11114", "--create", "--claim", "--progress", "50"],
            "update_progress_information",
            ("1.2.3.4.5", "1.2.3.4.5.6", 50, None),
            "Updating progress info: progress_value=50, progress_description=None",
        )

    def test_start(self):
        self.run_script_with_args(
            ["upsmodifyscu.py", "localhost", "11114", "--create", "--claim", "--start", "A,B,C", "D,E,F"],
            "update_start_info",
            ("1.2.3.4.5", "1.2.3.4.5.6", ("A", "B", "C"), ("D", "E", "F"), None, None),
            (
                "Updating start info: station_name=('A', 'B', 'C'), workitem_code=('D', 'E', 'F'), "
                "human_performer=None, human_performer_name=None"
            ),
        )

    def test_end(self):
        self.run_script_with_args(
            ["upsmodifyscu.py", "localhost", "11114", "--create", "--claim", "--end"],
            "update_end_info",
            ("1.2.3.4.5", "1.2.3.4.5.6"),
            "Updating end info",
        )

    def test_cancel_with_reason(self):
        self.run_script_with_args(
            ["upsmodifyscu.py", "localhost", "11114", "--create", "--claim", "--cancel", "Test reason"],
            "update_cancel_info",
            ("1.2.3.4.5", "1.2.3.4.5.6", "Test reason"),
            "Updating cancel info with reason: Test reason",
        )

    def test_output(self):
        self.run_script_with_args(
            [
                "upsmodifyscu.py",
                "localhost",
                "11114",
                "--create",
                "--claim",
                "--output",
                "AET, 1.2.3, 1.2.4,1.2.840.10008.5.1.4.1.1.2, 1.2.5",
            ],
            "update_output_information",
            ("1.2.3.4.5", "1.2.3.4.5.6", [("AET", "1.2.3", "1.2.4", "1.2.840.10008.5.1.4.1.1.2", "1.2.5")]),
            "Updating output information with: [('AET', '1.2.3', '1.2.4', '1.2.840.10008.5.1.4.1.1.2', '1.2.5')]",
        )

    def test_list(self):
        self.run_script_with_args(
            ["upsmodifyscu.py", "localhost", "11114", "--create", "--claim", "--list", "somefile.dcm"],
            "modify_ups",
            ("1.2.3.4.5", "mock_ds"),
            None,
        )

    def setUp(self):
        class DummyParser:
            def error(self, msg):
                raise ValueError(msg)

        class DummyLogger:
            pass

        self.parser = DummyParser()
        self.logger = DummyLogger()

    def test_get_ups_info_create_and_claim(self):
        with (
            patch("tdwii_plus_examples.cli.upsmodifyscu._ncreate_sample_ups", return_value="created_uid"),
            patch("tdwii_plus_examples.cli.upsmodifyscu._claim_ups", return_value="claimed_tx_uid"),
        ):

            class Args:
                pass

            args = Args()
            args.create = True
            args.claim = True
            args.sop_instance_uid = None
            args.transaction_uid = None
            args.progress = None
            args.start = None
            args.end = False
            args.cancel = None
            args.output = None
            args.list = None
            sop_instance_uid, tx_uid = _get_ups_info(args, self.parser, self.logger, None)
            self.assertEqual(sop_instance_uid, "created_uid")
            self.assertEqual(tx_uid, "claimed_tx_uid")

    def test_get_ups_info_missing_sop_instance_uid(self):
        class Args:
            pass

        args = Args()
        args.create = False
        args.claim = False
        args.sop_instance_uid = None
        args.transaction_uid = "txid"
        args.progress = None
        args.start = None
        args.end = False
        args.cancel = None
        args.output = None
        args.list = None
        with self.assertRaises(ValueError):
            _get_ups_info(args, self.parser, self.logger, None)

    def test_get_ups_info_progress(self):
        class Args:
            pass

        args = Args()
        args.create = False
        args.claim = False
        args.sop_instance_uid = "uid"
        args.transaction_uid = "txid"
        args.progress = ["50"]
        args.start = None
        args.end = False
        args.cancel = None
        args.output = None
        args.list = None
        sop_instance_uid, tx_uid = _get_ups_info(args, self.parser, self.logger, None)
        self.assertEqual(sop_instance_uid, "uid")
        self.assertEqual(tx_uid, "txid")

    def test_get_ups_info_output(self):
        class Args:
            pass

        args = Args()
        args.create = False
        args.claim = False
        args.sop_instance_uid = "uid"
        args.transaction_uid = "txid"
        args.progress = None
        args.start = None
        args.end = False
        args.cancel = None
        args.output = ["AET,1.2.3,1.2.4,1.2.840.10008.5.1.4.1.1.2,1.2.5"]
        args.list = None
        sop_instance_uid, tx_uid = _get_ups_info(args, self.parser, self.logger, None)
        self.assertEqual(sop_instance_uid, "uid")
        self.assertEqual(tx_uid, "txid")


class TestUpsModifySCUWithTLS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        # Create empty certificate, key and CA files, as only their existence is checked
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def setUp(self):
        scu_patch = patch("tdwii_plus_examples.cli.upsmodifyscu.UPSPullNSetSCU")
        self.mock_scu_class = scu_patch.start()
        self.addCleanup(scu_patch.stop)

    def run_main(self, *argv):
        base_argv = ["upsmodifyscu.py", "localhost", "11114", "--sop_instance_uid", "1.2.3", "--transaction_uid", "4.5.6"]
        with patch.object(sys, "argv", [*base_argv, "--progress", "50", *argv]), patch("builtins.print"):
            main()

    def test_tls_options_are_forwarded(self):
        self.run_main("--tls", "--tls-ca", self.ca)

        tls_config = self.mock_scu_class.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(ca_cert=self.ca, usage=TLSUsage.CLIENT_AUTH))

    def test_mtls_options_are_forwarded(self):
        self.run_main("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = self.mock_scu_class.call_args.kwargs["tls_config"]
        self.assertEqual(
            tls_config,
            TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=TLSUsage.CLIENT_AUTH),
        )

    def test_no_tls_options_means_no_tls(self):
        self.run_main()

        self.assertIsNone(self.mock_scu_class.call_args.kwargs["tls_config"])

    def test_invalid_tls_options_prevent_the_association(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.run_main("--tls")

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--tls requires --tls-ca", stderr.getvalue())
        self.mock_scu_class.assert_not_called()

    def test_tls_configuration_is_forwarded_to_the_helper_scus(self):
        tls_config = TLSConfig(ca_cert=self.ca, usage=TLSUsage.CLIENT_AUTH)
        args = MagicMock(ae_title="UPSSCP", ip="localhost", port=11114)

        with (
            patch("tdwii_plus_examples.cli.upsmodifyscu.UPSPushNCreateSCU") as mock_push_scu_class,
            patch("tdwii_plus_examples.cli.upsmodifyscu.UPSPullNActionSCU") as mock_change_state_scu_class,
            patch("builtins.print"),
        ):
            mock_push_scu_class.return_value.create_ups_instances.return_value = 1
            _ncreate_sample_ups(args, MagicMock(), tls_config)
            _claim_ups(args, "1.2.3", MagicMock(), tls_config)

        self.assertEqual(mock_push_scu_class.call_args.kwargs["tls_config"], tls_config)
        self.assertEqual(mock_change_state_scu_class.call_args.kwargs["tls_config"], tls_config)


if __name__ == "__main__":
    unittest.main()
