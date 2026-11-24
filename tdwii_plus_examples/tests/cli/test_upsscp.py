import contextlib
import io
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

from pynetdicom import evt

from tdwii_plus_examples.cli.upsscp import upsscp
from tdwii_plus_examples.cli.upsscp.upsscp import main
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage

_SETTINGS = """[DEFAULT]
ae_title: UPSSCP
port: 11114
max_pdu: 16382
acse_timeout: 30
dimse_timeout: 30
network_timeout: 30
bind_address:
instance_location: {instance_location}
database_location: {database_location}
"""


@patch("tdwii_plus_examples.cli.upsscp.upsscp.CEchoSCP")
class TestMainFunctionTLS(unittest.TestCase):
    usage = TLSUsage.SERVER_AUTH | TLSUsage.CLIENT_AUTH

    @classmethod
    def setUpClass(cls):
        # Only the existence of the files is checked by the options, their content is not loaded
        cls.temp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        cls.addClassCleanup(cls.temp_dir.cleanup)
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def setUp(self):
        # Mock the context creation as the certificate files are empty
        patcher = patch.object(TLSConfig, "create_client_ssl_context")
        self.create_client_ssl_context = patcher.start()
        self.addCleanup(patcher.stop)

    def write_config(self, **tls_settings):
        """Write a configuration file with the given TLS settings and return its path."""
        settings = _SETTINGS.format(
            instance_location=os.path.join(self.temp_dir.name, "instances"),
            database_location=os.path.join(self.temp_dir.name, "instances.sqlite"),
        )
        settings += "".join(f"{name}: {value}\n" for name, value in tls_settings.items())
        path = os.path.join(self.temp_dir.name, "upsscp.ini")
        with open(path, "w") as config_file:
            config_file.write(settings)
        return path

    def run_main(self, config, *argv):
        with patch.object(sys, "argv", ["upsscp.py", "-c", config, *argv]):
            main(loop_forever=False)

    def ncreate_handler_ssl_context(self, MockCEchoSCP):
        """Return the TLS context bound to the N-CREATE handler, which sends the event reports."""
        for call in MockCEchoSCP.return_value.handlers.append.call_args_list:
            event, _, handler_args = call.args[0]
            if event == evt.EVT_N_CREATE:
                return handler_args[-1]
        self.fail("no N-CREATE handler")

    def assert_startup_error(self, config, *argv, message):
        """Assert that upsscp refuses to start, with a message mentioning ``message``."""
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.run_main(config, *argv)
        self.assertEqual(raised.exception.code, 2)
        self.assertIn(message, stderr.getvalue())

    def test_no_tls_settings_means_no_tls(self, MockCEchoSCP):
        self.run_main(self.write_config())

        self.assertIsNone(MockCEchoSCP.call_args.kwargs["tls_config"])

    def test_tls_off_means_no_tls(self, MockCEchoSCP):
        self.run_main(self.write_config(tls="off"))

        self.assertIsNone(MockCEchoSCP.call_args.kwargs["tls_config"])

    def test_tls_settings_are_forwarded(self, MockCEchoSCP):
        self.run_main(self.write_config(tls="tls", tls_cert=self.cert, tls_key=self.key, tls_ca=self.ca))

        tls_config = MockCEchoSCP.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, usage=self.usage))

    def test_mtls_settings_are_forwarded(self, MockCEchoSCP):
        self.run_main(self.write_config(tls="mtls", tls_cert=self.cert, tls_key=self.key, tls_ca=self.ca))

        tls_config = MockCEchoSCP.call_args.kwargs["tls_config"]
        expected = TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=self.usage)
        self.assertEqual(tls_config, expected)

    def test_relative_paths_are_relative_to_the_upsscp_directory(self, MockCEchoSCP):
        app_dir = os.path.dirname(os.path.abspath(upsscp.__file__))
        cert, key, ca = (os.path.relpath(path, app_dir) for path in (self.cert, self.key, self.ca))
        self.run_main(self.write_config(tls="tls", tls_cert=cert, tls_key=key, tls_ca=ca))

        cert, key, ca = (os.path.abspath(os.path.join(app_dir, path)) for path in (cert, key, ca))
        tls_config = MockCEchoSCP.call_args.kwargs["tls_config"]
        self.assertEqual(tls_config, TLSConfig(cert_file=cert, key_file=key, ca_cert=ca, usage=self.usage))

    def test_tls_options_override_the_settings(self, MockCEchoSCP):
        config = self.write_config(tls="off", tls_cert="ignored.pem", tls_key="ignored.pem", tls_ca="ignored.pem")
        self.run_main(config, "--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)

        tls_config = MockCEchoSCP.call_args.kwargs["tls_config"]
        expected = TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=self.usage)
        self.assertEqual(tls_config, expected)

    def test_tls_mode_option_keeps_the_file_settings(self, MockCEchoSCP):
        self.run_main(self.write_config(tls="tls", tls_cert=self.cert, tls_key=self.key, tls_ca=self.ca), "--mtls")

        tls_config = MockCEchoSCP.call_args.kwargs["tls_config"]
        expected = TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=self.usage)
        self.assertEqual(tls_config, expected)

    def test_event_reports_are_sent_with_tls(self, MockCEchoSCP):
        self.run_main(self.write_config(tls="tls", tls_cert=self.cert, tls_key=self.key, tls_ca=self.ca))

        self.assertIs(self.ncreate_handler_ssl_context(MockCEchoSCP), self.create_client_ssl_context.return_value)

    def test_event_reports_are_sent_without_tls_when_tls_is_off(self, MockCEchoSCP):
        self.run_main(self.write_config(tls="off"))

        self.assertIsNone(self.ncreate_handler_ssl_context(MockCEchoSCP))

    def test_invalid_tls_mode_prevents_startup(self, MockCEchoSCP):
        config = self.write_config(tls="yes")

        self.assert_startup_error(config, message=f"tls in {config} must be off, tls or mtls")
        MockCEchoSCP.assert_not_called()

    def test_invalid_tls_settings_prevent_startup(self, MockCEchoSCP):
        config = self.write_config(tls="tls", tls_cert=self.cert, tls_key=self.key)

        self.assert_startup_error(config, message="--tls requires --tls-ca")
        MockCEchoSCP.assert_not_called()


if __name__ == "__main__":
    unittest.main()
