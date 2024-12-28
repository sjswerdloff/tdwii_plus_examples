import unittest
from parameterized import parameterized
import logging
from logging.handlers import MemoryHandler
from pynetdicom import evt
from pynetdicom.sop_class import Verification

from tdwii_plus_examples.cechohandler import handle_cecho
from tdwii_plus_examples.cechoscp import CEchoSCP


class TestCEchoSCP(unittest.TestCase):

    def setUp(self):
        # Set up the logger for the BaseSCP to DEBUG level
        # with a memory handler to store up to 100 log messages
        self.scp_logger = logging.getLogger('test_cechoscp')
        self.scp_logger.setLevel(logging.DEBUG)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

        self.scp = CEchoSCP(logger=self.scp_logger)

    @parameterized.expand([
        ("ECHO_SCP", "", 11112, ""),
        ("MY_SCP", "", 11112, "scp_logger"),
        ("", "", 11112, "scp_logger"),
        (None, "", 11112, "scp_logger"),
    ])
    def test_init_params(self, ae_title, bind_address, port, logger_name):
        if logger_name:
            logger = getattr(self, logger_name)
        else:
            logger = None

        scp = CEchoSCP(ae_title=ae_title, bind_address=bind_address,
                       port=port, logger=logger)

        self.assertEqual(scp.ae_title, "ECHO_SCP" if not ae_title else ae_title)
        self.assertEqual(scp.bind_address, bind_address)
        self.assertEqual(scp.port, port)
        self.assertEqual(
            scp.logger.name, "test_cechoscp" if logger_name else "base_scp")

    def test_add_contexts(self):
        sop_class = [ctx.abstract_syntax
                     for ctx in self.scp.ae.supported_contexts]
        self.assertIn(Verification, sop_class,
                      msg="Verification SOP Class not supported")
        ts = [ctx.transfer_syntax for ctx in self.scp.ae.supported_contexts
              if ctx.abstract_syntax == Verification]
        self.assertEqual(ts[0], ['1.2.840.10008.1.2'],
                         msg="Transfer syntax not as expected")

    def test_add_handlers(self):
        handlers = [(evt.EVT_C_ECHO, handle_cecho, [self.scp_logger])]
        self.assertIn(handlers[0], self.scp.handlers)


if __name__ == '__main__':
    unittest.main()
