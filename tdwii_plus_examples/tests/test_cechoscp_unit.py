import unittest
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
        self.scp_logger.setLevel(logging.ERROR)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

        self.scp = CEchoSCP(logger=self.scp_logger)

    def test_init_params(self):
        self.assertEqual(self.scp.ae_title, "ECHO_SCP")
        self.assertEqual(self.scp.bind_address, "")
        self.assertEqual(self.scp.port, 11112)
        self.assertEqual(self.scp.logger, self.scp_logger)

    def test_add_contexts(self):
        sop_class = [ctx.abstract_syntax
                     for ctx in self.scp.ae.supported_contexts]
        self.assertIn(Verification, sop_class,
                      msg="Verification SOP Class not added to contexts")
        ts = [ctx.transfer_syntax for ctx in self.scp.ae.supported_contexts
              if ctx.abstract_syntax == Verification]
        self.assertEqual(ts[0], ['1.2.840.10008.1.2'],
                         msg="Transfer syntax not as expected")

    def test_add_handlers(self):
        handlers = [(evt.EVT_C_ECHO, handle_cecho, [self.scp_logger])]
        self.assertIn(handlers[0], self.scp.handlers)


if __name__ == '__main__':
    unittest.main()
