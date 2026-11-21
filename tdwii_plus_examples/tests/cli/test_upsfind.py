import contextlib
import io
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from pydicom import Dataset
from pydicom.uid import generate_uid
from pynetdicom.sop_class import UnifiedProcedureStepPush

from tdwii_plus_examples.cli.upsfind import main as upsfind_main
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TestUpsFindSCU(unittest.TestCase):
    def test_no_ups_found(self):
        with (
            patch.object(sys, "argv", ["upsfind.py", "localhost", "11114"]),
            patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU") as mock_scu_class,
            patch("builtins.print") as mock_print,
        ):
            mock_scu = MagicMock()
            mock_scu_class.return_value = mock_scu
            mock_query = Dataset()
            mock_scu.create_ups_query.return_value = mock_query
            mock_scu.get_ups.return_value = []

            with self.assertRaises(SystemExit) as cm:
                upsfind_main()
            self.assertEqual(cm.exception.code, 1)

            mock_scu.create_ups_query.assert_called_once()
            mock_scu.get_ups.assert_called_once_with(mock_query)
            found = any("No UPS instances found matching the query." in str(call) for call in mock_print.call_args_list)
            self.assertTrue(found, "Expected print for no UPS found")

    def test_ups_found_and_save_part10(self):
        # This test covers both the default save (Part 10) and the "happy path" for multiple results.
        with (
            patch.object(sys, "argv", ["upsfind.py", "localhost", "11114", "--save", "testdir"]),
            patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU") as mock_scu_class,
            patch("builtins.print") as mock_print,
            patch("os.makedirs") as mock_makedirs,
        ):
            mock_scu = MagicMock()
            mock_scu_class.return_value = mock_scu
            mock_query = Dataset()
            mock_scu.create_ups_query.return_value = mock_query
            ds1 = Dataset()
            ds1.SOPInstanceUID = generate_uid()
            ds1.SOPClassUID = UnifiedProcedureStepPush
            ds1.save_as = MagicMock()
            ds2 = Dataset()
            ds2.SOPInstanceUID = generate_uid()
            ds2.SOPClassUID = UnifiedProcedureStepPush
            ds2.save_as = MagicMock()
            mock_scu.get_ups.return_value = [ds1, ds2]

            with self.assertRaises(SystemExit) as cm:
                upsfind_main()
            self.assertEqual(cm.exception.code, 0)

            mock_scu.create_ups_query.assert_called_once()
            mock_scu.get_ups.assert_called_once_with(mock_query)
            found = any("Found 2 UPS instance(s):" in str(call) for call in mock_print.call_args_list)
            self.assertTrue(found, "Expected print for found UPS instances")
            mock_makedirs.assert_called_with("testdir", exist_ok=True)
            ds1.save_as.assert_called_with(unittest.mock.ANY, write_like_original=False)
            ds2.save_as.assert_called_with(unittest.mock.ANY, write_like_original=False)

    def test_raw_save_option(self):
        # Test that --raw triggers save_as(write_like_original=True)
        ds = Dataset()
        ds.save_as = MagicMock()

        with (
            patch.object(sys, "argv", ["upsfind.py", "localhost", "11114", "--raw", "--save", "outdir"]),
            patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU") as mock_scu_class,
            patch("builtins.print"),
            patch("os.makedirs"),
        ):
            mock_scu = MagicMock()
            mock_scu.create_ups_query.return_value = Dataset()
            mock_scu.get_ups.return_value = [ds]
            mock_scu_class.return_value = mock_scu
            from tdwii_plus_examples.cli.upsfind import main as upsfind_main

            with self.assertRaises(SystemExit) as cm:
                upsfind_main()
            self.assertEqual(cm.exception.code, 0)

        # Verify save_as was invoked with write_like_original=True
        ds.save_as.assert_called_once()
        _, kwargs = ds.save_as.call_args
        self.assertTrue(kwargs.get("write_like_original", False))

    def test_ups_found_missing_sopinstanceuid(self):
        # Test a dataset without SOPInstanceUID (should use index in filename)
        with (
            patch.object(sys, "argv", ["upsfind.py", "localhost", "11114", "--save", "testdir"]),
            patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU") as mock_scu_class,
            patch("builtins.print") as mock_print,
        ):
            mock_scu = MagicMock()
            mock_scu_class.return_value = mock_scu
            mock_query = Dataset()
            mock_scu.create_ups_query.return_value = mock_query
            ds = Dataset()
            ds.SOPClassUID = UnifiedProcedureStepPush
            ds.SOPInstanceUID = ""
            ds.save_as = MagicMock()
            mock_scu.get_ups.return_value = [ds]

            with self.assertRaises(SystemExit) as cm:
                upsfind_main()
            self.assertEqual(cm.exception.code, 0)

            # Check that the fallback filename (using index) is used in print output
            found = any("UPS_1.dcm" in str(call) for call in mock_print.call_args_list)
            self.assertTrue(found, "Expected fallback filename 'UPS_1.dcm' in output")

    def test_custom_query_args(self):
        # Test that custom query args are passed to create_ups_query
        uid = generate_uid()
        with (
            patch.object(
                sys,
                "argv",
                [
                    "upsfind.py",
                    "localhost",
                    "11114",
                    "--ups_uid",
                    uid,
                    "--machine",
                    "GTR1",
                    "--state",
                    "IN PROGRESS",
                    "--start",
                    "202501010000",
                    "--end",
                    "202501011200",
                ],
            ),
            patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU") as mock_scu_class,
            patch("builtins.print"),
            patch("os.makedirs"),
        ):
            mock_scu = MagicMock()
            mock_scu_class.return_value = mock_scu
            mock_query = Dataset()
            mock_scu.create_ups_query.return_value = mock_query
            mock_scu.get_ups.return_value = [Dataset()]  # Return a non-empty list to avoid exit(1)

            with self.assertRaises(SystemExit) as cm:
                upsfind_main()
            self.assertEqual(cm.exception.code, 0)

            mock_scu.create_ups_query.assert_called_once_with(
                ups_uid=uid,
                machine_name="GTR1",
                procedure_step_state="IN PROGRESS",
                scheduled_no_sooner_than="202501010000",
                scheduled_no_later_than="202501011200",
            )


class TestUpsFindSCUWithTLS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        # Create empty certificate, key and CA files, as only their existence is checked
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def run_main(self, *argv):
        with (
            patch.object(sys, "argv", ["upsfind.py", "localhost", "11114", *argv]),
            patch("builtins.print"),
            self.assertRaises(SystemExit),
        ):
            upsfind_main()

    @patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU")
    def test_tls_options_are_forwarded(self, mock_scu_class):
        mock_scu_class.return_value.get_ups.return_value = []

        self.run_main("--tls", "--tls-ca", self.ca)

        tls_config = mock_scu_class.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(ca_cert=self.ca, usage=TLSUsage.CLIENT_AUTH))

    @patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU")
    def test_mtls_options_are_forwarded(self, mock_scu_class):
        mock_scu_class.return_value.get_ups.return_value = []

        self.run_main("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = mock_scu_class.call_args.kwargs["tls_config"]
        self.assertEqual(
            tls_config,
            TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=TLSUsage.CLIENT_AUTH),
        )

    @patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU")
    def test_no_tls_options_means_no_tls(self, mock_scu_class):
        mock_scu_class.return_value.get_ups.return_value = []

        self.run_main()

        self.assertIsNone(mock_scu_class.call_args.kwargs["tls_config"])

    @patch("tdwii_plus_examples.cli.upsfind.UPSPullCFindSCU")
    def test_invalid_tls_options_prevent_the_association(self, mock_scu_class):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as raised:
                with patch.object(sys, "argv", ["upsfind.py", "localhost", "11114", "--tls"]):
                    upsfind_main()

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--tls requires --tls-ca", stderr.getvalue())
        mock_scu_class.assert_not_called()


if __name__ == "__main__":
    unittest.main()
