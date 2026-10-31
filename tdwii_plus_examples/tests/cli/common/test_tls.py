import argparse
import contextlib
import io
import os
import tempfile
import unittest

from tdwii_plus_examples.basescp import TLSConfig
from tdwii_plus_examples.cli.common.tls import add_tls_arguments, tls_config_from_args


class TestTLSOptions(unittest.TestCase):
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
        add_tls_arguments(self.parser)

    def config_from(self, *argv):
        return tls_config_from_args(self.parser, self.parser.parse_args(list(argv)))

    def assert_error(self, *argv, message):
        """Assert that the options are reported as invalid, with a message mentioning ``message``."""
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            self.config_from(*argv)
        self.assertEqual(raised.exception.code, 2)
        self.assertIn(message, stderr.getvalue())

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


if __name__ == "__main__":
    unittest.main()
