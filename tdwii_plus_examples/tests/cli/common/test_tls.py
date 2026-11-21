import argparse
import contextlib
import io
import os
import tempfile
import unittest

from tdwii_plus_examples.cli.common.tls import add_tls_arguments, tls_config_from_args
from tdwii_plus_examples.tls_config import TLSConfig, TLSUsage


class TLSOptionsTestCase(unittest.TestCase):
    """Helpers and the rules shared by the SCP and the SCU, the subclasses set the ``usage``."""

    usage = None

    @classmethod
    def setUpClass(cls):
        # Only the existence of the files is checked here, their content is not loaded
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp_dir.cleanup)
        for name in ("cert", "key", "ca"):
            path = os.path.join(cls.temp_dir.name, f"{name}.pem")
            open(path, "w").close()
            setattr(cls, name, path)

    def setUp(self):
        self.parser = argparse.ArgumentParser(prog="app")
        add_tls_arguments(self.parser, usage=self.usage)

    def config_from(self, *argv):
        return tls_config_from_args(self.parser, self.parser.parse_args(list(argv)), usage=self.usage)

    def help_text(self):
        """Return the help of the parser, on one line."""
        return " ".join(self.parser.format_help().split())

    def assert_error(self, *argv, message):
        """Assert that the options are reported as invalid, with a message mentioning ``message``."""
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.config_from(*argv)
        self.assertEqual(raised.exception.code, 2)
        self.assertIn(message, stderr.getvalue())


class TestSCPTLSOptions(TLSOptionsTestCase):
    usage = TLSUsage.SERVER_AUTH

    def test_help_states_the_scp_requirements(self):
        self.assertIn("--tls Use TLS, needs --tls-cert and --tls-key", self.help_text())
        self.assertIn("--mtls Use mutual TLS, needs --tls-cert, --tls-key and --tls-ca", self.help_text())

    def test_no_options_means_no_tls(self):
        self.assertIsNone(self.config_from())

    def test_tls(self):
        config = self.config_from("--tls", "--tls-cert", self.cert, "--tls-key", self.key)
        self.assertEqual(config, TLSConfig(cert_file=self.cert, key_file=self.key))

    def test_mtls(self):
        config = self.config_from("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)
        self.assertEqual(config, TLSConfig(cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True))

    def test_tls_and_mtls_are_exclusive(self):
        self.assert_error("--tls", "--mtls", message="not allowed with argument")

    def test_tls_options_without_a_mode(self):
        self.assert_error(
            "--tls-cert", self.cert, "--tls-key", self.key, message="--tls-cert, --tls-key requires --tls or --mtls"
        )
        self.assert_error("--tls-ca", self.ca, message="--tls-ca requires --tls or --mtls")

    def test_tls_without_certificate_or_key(self):
        self.assert_error("--tls", message="--tls requires --tls-cert, --tls-key")
        self.assert_error("--tls", "--tls-cert", self.cert, message="--tls requires --tls-key")
        self.assert_error("--tls", "--tls-key", self.key, message="--tls requires --tls-cert")

    def test_mtls_without_certificate_authority(self):
        self.assert_error("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, message="--mtls requires --tls-ca")

    def test_certificate_authority_needs_mtls(self):
        self.assert_error(
            "--tls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca, message="requires --mtls"
        )

    def test_missing_file(self):
        missing = os.path.join(self.temp_dir.name, "missing.pem")
        self.assert_error(
            "--tls", "--tls-cert", missing, "--tls-key", self.key, message=f"--tls-cert: file not found: {missing}"
        )


class TestSCUTLSOptions(TLSOptionsTestCase):
    usage = TLSUsage.CLIENT_AUTH

    def test_help_states_the_scu_requirements(self):
        self.assertIn("--tls Use TLS, needs --tls-ca", self.help_text())
        self.assertIn("--mtls Use mutual TLS, needs --tls-ca, --tls-cert and --tls-key", self.help_text())

    def test_no_options_means_no_tls(self):
        self.assertIsNone(self.config_from())

    def test_tls(self):
        config = self.config_from("--tls", "--tls-ca", self.ca)
        self.assertEqual(config, TLSConfig(ca_cert=self.ca, usage=TLSUsage.CLIENT_AUTH))

    def test_mtls(self):
        config = self.config_from("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)
        expected = TLSConfig(
            cert_file=self.cert, key_file=self.key, ca_cert=self.ca, require_mtls=True, usage=TLSUsage.CLIENT_AUTH
        )
        self.assertEqual(config, expected)

    def test_tls_and_mtls_are_exclusive(self):
        self.assert_error("--tls", "--mtls", message="not allowed with argument")

    def test_tls_options_without_a_mode(self):
        self.assert_error("--tls-ca", self.ca, message="--tls-ca requires --tls or --mtls")
        self.assert_error(
            "--tls-cert", self.cert, "--tls-key", self.key, message="--tls-cert, --tls-key requires --tls or --mtls"
        )

    def test_tls_without_certificate_authority(self):
        self.assert_error("--tls", message="--tls requires --tls-ca")

    def test_mtls_without_certificate_authority(self):
        self.assert_error("--mtls", "--tls-cert", self.cert, "--tls-key", self.key, message="--mtls requires --tls-ca")

    def test_mtls_without_certificate_or_key(self):
        self.assert_error("--mtls", "--tls-ca", self.ca, message="--mtls requires --tls-cert, --tls-key")

    def test_certificate_and_key_need_mtls(self):
        self.assert_error(
            "--tls",
            "--tls-ca",
            self.ca,
            "--tls-cert",
            self.cert,
            "--tls-key",
            self.key,
            message="--tls-cert, --tls-key requires --mtls",
        )

    def test_missing_file(self):
        missing = os.path.join(self.temp_dir.name, "missing.pem")
        self.assert_error("--tls", "--tls-ca", missing, message=f"--tls-ca: file not found: {missing}")


class TestUnsupportedUsage(TLSOptionsTestCase):
    usage = TLSUsage.SERVER_AUTH | TLSUsage.CLIENT_AUTH

    def setUp(self):
        # The options themselves refuse the combined usage, so they are added with a supported one
        self.parser = argparse.ArgumentParser(prog="app")
        add_tls_arguments(self.parser, usage=TLSUsage.SERVER_AUTH)

    def test_combined_usage_is_refused_when_adding_the_options(self):
        with self.assertRaisesRegex(ValueError, "unsupported usage"):
            add_tls_arguments(argparse.ArgumentParser(prog="app"), usage=self.usage)

    def test_combined_usage_is_refused(self):
        with self.assertRaisesRegex(ValueError, "unsupported usage"):
            self.config_from("--tls", "--tls-cert", self.cert, "--tls-key", self.key, "--tls-ca", self.ca)


if __name__ == "__main__":
    unittest.main()
