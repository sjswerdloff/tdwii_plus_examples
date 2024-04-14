"""Unit tests for nevent_sender.py"""

from time import sleep
import os
import subprocess
import sys
import time

import pytest
from pydicom import Dataset, dcmread
from pydicom.uid import (
    DeflatedExplicitVRLittleEndian,
    ExplicitVRBigEndian,
    ExplicitVRLittleEndian,
    ImplicitVRLittleEndian,
)
from pynetdicom import (
    AE,
    ALL_TRANSFER_SYNTAXES,
    UnifiedProcedurePresentationContexts,
    evt,
)
from pynetdicom.sop_class import UnifiedProcedureStepPush, Verification

# from nevent_receiver_handlers import handle_nevent
from TDWII_PPVS_subscriber.nevent_receiver import NEventReceiver

# debug_logger()


APP_DIR = os.path.join(os.path.dirname(__file__), "../")
APP_FILE = os.path.join(APP_DIR, "./", "nevent_sender.py")
DATA_DIR = os.path.join(APP_DIR, "../", "responses", "dcm")
DATASET_FILE = os.path.join(DATA_DIR, "rsp000001.dcm")
LIB_DIR = os.path.join(APP_DIR, "../")


def start_nevent_sender(args):
    """Start the nevent_sender.py app and return the process."""
    pargs = [sys.executable, APP_FILE] + [*args]
    return subprocess.Popen(pargs)


def default_handle_nevent(event):
    req = event.request
    # attr_list = event.attribute_list
    ds = Dataset()

    # Add the SOP Common module elements (Annex C.12.1)
    ds.AffectedSOPClassUID = UnifiedProcedureStepPush
    ds.AffectedSOPInstanceUID = req.AffectedSOPInstanceUID

    # Update with the requested attributes
    # ds.update(attr_list)
    ds.is_little_endian = True
    ds.is_implicit_VR = True
    ds.Status = 0x0000
    return ds, None


class neventsenderBase:
    """Tests for nevent_sender.py"""

    def setup_method(self):
        """Run prior to each test"""
        self.ae = None
        self.func = None

    def teardown_method(self):
        """Clear any active threads"""
        if self.ae:
            self.ae.shutdown()

    def test_default(self):
        """Test default settings."""

        events = []

        def handle_nevent_receive(event):
            events.append(event)
            yield 0
            yield 0

        def handle_release(event):
            events.append(event)

        handlers = [
            (evt.EVT_N_EVENT_REPORT, handle_nevent_receive),
            (evt.EVT_RELEASED, handle_release),
        ]

        self.ae = ae = AE()
        ae.acse_timeout = 5
        ae.dimse_timeout = 5
        ae.network_timeout = 5
        ae.add_supported_context(UnifiedProcedureStepPush)
        scp = ae.start_server(("localhost", 11115), block=False, evt_handlers=handlers)
  

        p = self.func(["127.0.0.1", "11115"])
        p.wait()
        assert p.returncode == 0
        # sleep(1.0)
        scp.shutdown()
        

        
        assert events[0].event == evt.EVT_N_EVENT_REPORT
        current_event = events[0]
        nevent_primitive = current_event.request
        model = current_event.request.AffectedSOPClassUID
        nevent_type_id = nevent_primitive.EventTypeID
        nevent_information = dcmread(nevent_primitive.EventInformation, force=True)
        assert model.keyword in ["UnifiedProcedureStepPush"]
        assert nevent_type_id == 1
        assert nevent_information.ProcedureStepState == "SCHEDULED"

        assert events[1].event == evt.EVT_N_EVENT_REPORT
        current_event = events[1]
        nevent_primitive = current_event.request
        model = current_event.request.AffectedSOPClassUID
        nevent_type_id = nevent_primitive.EventTypeID
        nevent_information = dcmread(nevent_primitive.EventInformation, force=True)
        assert model.keyword in ["UnifiedProcedureStepPush"]
        assert nevent_type_id == 1
        assert nevent_information.ProcedureStepState == "IN PROGRESS"

        assert events[2].event == evt.EVT_N_EVENT_REPORT
        current_event = events[2]
        nevent_primitive = current_event.request
        model = current_event.request.AffectedSOPClassUID
        nevent_type_id = nevent_primitive.EventTypeID
        nevent_information = dcmread(nevent_primitive.EventInformation, force=True)
        assert model.keyword in ["UnifiedProcedureStepPush"]
        assert nevent_type_id == 1
        assert nevent_information.ProcedureStepState == "COMPLETED"

        assert events[3].event == evt.EVT_RELEASED
        
    # def test_no_peer(self, capfd):
    #     """Test trying to connect to non-existent host."""
    #     p = self.func([DATASET_FILE])
    #     p.wait()
    #     assert p.returncode == 1
    #     out, err = capfd.readouterr()
    #     assert "Association request failed: unable to connect to remote" in err
    #     assert "TCP Initialisation Error" in err


    # def test_bad_input(self, capfd):
    #     """Test being unable to read the input file."""
    #     p = self.func(["no-such-file.dcm", "-d"])
    #     p.wait()
    #     assert p.returncode == 0

    #     out, err = capfd.readouterr()
    #     assert "No suitable DICOM files found" in err
    #     assert "Cannot access path: no-such-file.dcm" in err

    

class Testneventsender(neventsenderBase):
    """Tests for nevent_sender.py"""

    def setup_method(self):
        """Run prior to each test"""
        self.ae = None
        self.func = start_nevent_sender
