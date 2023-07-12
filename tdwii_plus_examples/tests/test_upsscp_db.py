"""Unit tests for the QRSCP app's database functions."""

import os
import sys
import tempfile
from pathlib import Path

import pytest

try:
    from sqlalchemy import create_engine
    from sqlalchemy.exc import IntegrityError, SAWarning
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.schema import MetaData

    HAVE_SQLALCHEMY = True
except ImportError:
    HAVE_SQLALCHEMY = False

import importlib

import pydicom.config
from pydicom import dcmread
from pydicom.dataset import Dataset
from pydicom.tag import Tag
from pynetdicom.sop_class import UnifiedProcedureStepPush

if HAVE_SQLALCHEMY:
    from tdwii_plus_examples import upsdb as db


TEST_DIR = Path(__file__).parent
DATA_DIR = TEST_DIR.parent.parent / "responses" / "dcm"
DATASETS = {
    "rsp000001.dcm": {
        "patient_id": "202304061",
        "patient_name": "head phantom^Hitachi",
        "study_instance_uid": None,
        "procedure_step_state": "SCHEDULED",
        "start_date_time": None,
        "station_name": "FX1",
        "transaction_uid": None,
        "work_item_code_value": "121726",
        "work_item_scheme_designator": "DCM",
        "work_item_meaning": "RT Treatment with Internal Verification",
        "sop_instance_uid": "1.2.840.113854.19.4.2017747596206021632.638223481578481915",
        "transfer_syntax_uid": "1.2.840.10008.1.2.1",
        "sop_class_uid": "1.2.840.10008.5.1.4.34.6.1",
    },
}


try:
    pydicom.config.settings.writing_validation_mode = 0
    pydicom.config.settings.reading_validation_mode = 0
except AttributeError:
    pass


@pytest.mark.skipif(not HAVE_SQLALCHEMY, reason="Requires sqlalchemy")
class TestConnect:
    """Tests for db.connect()."""

    def test_create_new(self):
        """Test connecting to the instance database if it doesn't exist."""
        db_file = tempfile.NamedTemporaryFile()
        db_location = f"sqlite:///{db_file.name}"
        engine = db.create(db_location)

        # Check exists with tables
        meta = MetaData()
        meta.reflect(bind=engine)
        assert "patient" in meta.tables
        assert "study" in meta.tables
        assert "series" in meta.tables
        assert "image" in meta.tables
        assert "instance" in meta.tables

    def test_create_new_existing(self):
        """Test connecting to the instance database if it exists."""
        db_file = tempfile.NamedTemporaryFile()
        db_location = "sqlite:///{}".format(db_file.name)
        db.create(db_location)
        # Test creating if already exists
        engine = db.create(db_location)

        meta = MetaData()
        meta.reflect(bind=engine)
        assert "patient" in meta.tables
        assert "study" in meta.tables
        assert "series" in meta.tables
        assert "image" in meta.tables
        assert "instance" in meta.tables


@pytest.mark.skipif(not HAVE_SQLALCHEMY, reason="Requires sqlalchemy")
class TestAddInstance:
    """Tests for db.add_instance()."""

    def setup_method(self):
        """Run prior to each test"""
        engine = db.create("sqlite:///:memory:")

        pydicom.config.use_none_as_empty_text_VR_value = True

        ds = Dataset()
        ds.PatientID = "1234"
        ds.StudyInstanceUID = "1.2"
        ds.SOPInstanceUID = "1.2.3.4"
        ds.SOPClassUID = "1.2.840.10008.5.1.4.34.6.1"
        ds.ProcedureStepState = "SCHEDULED"
        self.minimal = ds

        self.session = sessionmaker(bind=engine)()

    def test_add_instance(self):
        """Test adding to the instance database."""
        ds = dcmread(os.fspath(DATA_DIR / "rsp000001.dcm"))
        db.add_instance(ds, self.session)

        obj = self.session.query(db.Instance).all()
        assert 1 == len(obj)
        for kk, vv in DATASETS["rsp000001.dcm"].items():
            assert vv == getattr(obj[0], kk)

    def test_add_multiple_instances(self):
        """Test adding multiple data to the instance database."""
        for fname in DATASETS:
            ds = dcmread(os.fspath(DATA_DIR / fname))
            db.add_instance(ds, self.session)

        obj = self.session.query(db.Instance).all()
        assert 1 == len(obj)
        obj = self.session.query(db.Instance, db.Instance.patient_name).all()
        names = [val[1] for val in obj]
        assert "head phantom^Hitachi" in names
        # assert "CompressedSamples^MR1" in names
        # assert "ANON^A^B^C^D" in names
        # assert "^^^^" in names

    def test_add_minimal(self):
        """Test adding a minimal dataset."""
        db.add_instance(self.minimal, self.session)

        obj = self.session.query(db.Instance).all()
        assert 1 == len(obj)
        assert "1234" == obj[0].patient_id
        assert "1.2" == obj[0].study_instance_uid
        assert "1.2.3.4" == obj[0].sop_instance_uid
        assert "1.2.840.10008.5.1.4.34.6.1" == obj[0].sop_class_uid
        assert "SCHEDULED" == obj[0].procedure_step_state

        rest = [
            "patient_name",
            "start_date_time",
            "station_name",
            "work_item_code_value",
            "work_item_scheme_designator",
            "work_item_meaning",
            "transfer_syntax_uid",
            "transaction_uid",
        ]
        for attr in rest:
            assert getattr(obj[0], attr) is None

    def test_bad_instance(self):
        """Test that instances with bad data aren't added."""
        keywords = [
            ("PatientID", 64),
            ("PatientName", 400),
            ("StudyInstanceUID", 64),
            ("StudyDate", 8),
            ("StudyTime", 14),
            ("AccessionNumber", 16),
            ("StudyID", 16),
            ("SeriesInstanceUID", 64),
            ("Modality", 16),
            # ('SeriesNumber', None),
            ("SOPInstanceUID", 64),
            # ('InstanceNumber', None),
        ]
        ds = self.minimal[:]
        for kw, max_len in keywords:
            setattr(ds, kw, "a" * (max_len + 1))
            with pytest.raises(AssertionError):
                db.add_instance(ds, self.session)

        assert not self.session.query(db.Instance).all()

    def test_bad_instance_none(self):
        """Test that instances with bad data aren't added."""
        keywords = [
            ("PatientID", 64),
            ("PatientName", 64),
            ("StudyInstanceUID", 64),
            ("StudyDate", 8),
            ("StudyTime", 14),
            ("AccessionNumber", 16),
            ("StudyID", 16),
            ("SeriesInstanceUID", 64),
            ("Modality", 16),
            # ('SeriesNumber', None),
            ("SOPInstanceUID", 64),
            # ('InstanceNumber', None),
        ]
        ds = Dataset()
        ds.PatientID = None
        ds.StudyInstanceUID = None
        ds.SeriesInstanceUID = None
        ds.SOPInstanceUID = None
        with pytest.raises(IntegrityError):
            msg = r"Column 'instance.sop_instance_uid' is marked as a"
            with pytest.warns(SAWarning, match=msg):
                db.add_instance(ds, self.session)

        self.session.rollback()

        assert not self.session.query(db.Instance).all()

    def test_instance_exists(self):
        """Test that adding already existing instance updates it."""
        db.add_instance(self.minimal, self.session)

        result = self.session.query(db.Instance).all()
        assert 1 == len(result)
        assert None == result[0].transaction_uid
        self.minimal.TransactionUID = "1.2.3.4.5.6.7"

        db.add_instance(self.minimal, self.session)
        self.session.commit()
        result = self.session.query(db.Instance).all()
        assert 1 == len(result)
        assert "1.2.3.4.5.6.7" == result[0].transaction_uid


@pytest.mark.skipif(not HAVE_SQLALCHEMY, reason="Requires sqlalchemy")
class TestRemoveInstance:
    """Tests for db.remove_instance()."""

    def setup_method(self):
        """Run prior to each test"""
        engine = db.create("sqlite:///:memory:")

        pydicom.config.use_none_as_empty_text_VR_value = True

        self.session = sessionmaker(bind=engine)()
        ds = Dataset()
        ds.PatientID = "1234"
        ds.StudyInstanceUID = "1.2"
        ds.SeriesInstanceUID = "1.2.3"
        ds.SOPInstanceUID = "1.2.3.4"
        db.add_instance(ds, self.session)

        self.minimal = ds

    def test_remove_existing(self):
        """Test removing if exists in database."""

        obj = self.session.query(db.Instance).all()
        assert 1 == len(obj)
        assert "1.2.3.4" == obj[0].sop_instance_uid

        db.remove_instance("1.2.3.4", self.session)

        assert not self.session.query(db.Instance).all()
        assert not self.session.query(db.Patient).all()
        assert not self.session.query(db.Study).all()
        assert not self.session.query(db.Series).all()
        assert not self.session.query(db.Image).all()

    def test_remove_not_existing(self):
        """Test removing if doesn't exist in database."""

        obj = self.session.query(db.Instance).all()
        assert 1 == len(obj)
        assert "1.2.3.4" == obj[0].sop_instance_uid

        db.remove_instance("1.2.3.5", self.session)

        assert self.session.query(db.Instance).all()


@pytest.mark.skipif(not HAVE_SQLALCHEMY, reason="Requires sqlalchemy")
class TestClear:
    """Tests for db.clear()."""

    def setup_method(self):
        """Run prior to each test"""
        engine = db.create("sqlite:///:memory:")

        pydicom.config.use_none_as_empty_text_VR_value = True

        self.session = sessionmaker(bind=engine)()
        for fname in DATASETS:
            ds = dcmread(os.fspath(DATA_DIR / fname))
            db.add_instance(ds, self.session)

    def test_clear(self):
        """Test removing if exists in database."""
        assert 1 == len(self.session.query(db.Instance).all())

        db.clear(self.session)
        assert not self.session.query(db.Instance).all()


@pytest.mark.skipif(not HAVE_SQLALCHEMY, reason="Requires sqlalchemy")
class TestSearch:
    """Tests for db.search()."""

    def setup_method(self):
        """Run prior to each test"""
        engine = db.create("sqlite:///:memory:")
        pydicom.config.use_none_as_empty_text_VR_value = True

        self.session = sessionmaker(bind=engine)()

        for fname in DATASETS:
            ds = dcmread(os.fspath(DATA_DIR / fname))
            db.add_instance(ds, self.session)

    def test_search(self):
        """Test simple search."""
        pass

    def test_search_range_both(self):
        """Test searching a range with both start and end."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.StudyDate = "20000101-20200101"

        q = db._search_range(query["StudyDate"], self.session)
        assert 4 == len(q.all())

        query.StudyDate = "20000101-20150101"
        q = db._search_range(query["StudyDate"], self.session)
        assert 3 == len(q.all())

        query.StudyDate = "20000101-20010101"
        q = db._search_range(query["StudyDate"], self.session)
        assert not q.all()

    def test_search_range_both_subquery(self):
        """Test searching within an existing query."""
        pass

    def test_search_range_start(self):
        """Test searching a range with only start."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.StudyDate = "20000101-"

        q = db._search_range(query["StudyDate"], self.session)
        assert 4 == len(q.all())

        query.StudyDate = "20150101-"
        q = db._search_range(query["StudyDate"], self.session)
        assert 1 == len(q.all())

        query.StudyDate = "20200101-"
        q = db._search_range(query["StudyDate"], self.session)
        assert not q.all()

    def test_search_range_start_subquery(self):
        """Test searching within an existing query."""
        pass

    def test_search_range_end(self):
        """Test searching a range with only end."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.StudyDate = "-20200101"

        q = db._search_range(query["StudyDate"], self.session)
        assert 4 == len(q.all())

        query.StudyDate = "-20150101"
        q = db._search_range(query["StudyDate"], self.session)
        assert 3 == len(q.all())

        query.StudyDate = "-20010101"
        q = db._search_range(query["StudyDate"], self.session)
        assert not q.all()

    def test_search_range_end_subquery(self):
        """Test searching within an existing query."""
        pass

    def test_search_range_neither(self):
        """Test searching a range with only end."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.StudyDate = "-"

        with pytest.raises(ValueError):
            db._search_range(query["StudyDate"], self.session)

    def test_search_range_neither_subquery(self):
        """Test searching within an existing query."""
        pass

    def test_search_single_value(self):
        """Test search using a single value."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.PatientName = "CompressedSamples^CT1"

        q = db._search_single_value(query["PatientName"], self.session)
        assert 1 == len(q.all())

    def test_search_single_value_subquery(self):
        """Test searching using a single value within an existing query."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.PatientName = None

        q = db._search_universal(query["PatientName"], self.session)
        assert 5 == len(q.all())

        query.PatientName = "CompressedSamples^CT1"
        q = db._search_single_value(query["PatientName"], self.session, q)
        assert 1 == len(q.all())

    def test_search_wildcard_asterisk(self):
        """Test search using a * wildcard."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.PatientName = "*"

        q = db._search_wildcard(query["PatientName"], self.session)
        assert 5 == len(q.all())

        query.PatientName = "CompressedSamples*"
        q = db._search_wildcard(query["PatientName"], self.session)
        assert 3 == len(q.all())

    def test_search_wildcard_asterisk_subquery(self):
        """Test searching within an existing query."""
        pass

    def test_search_wildcard_qmark(self):
        """Test search using a ? wildcard."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.PatientName = "CompressedSamples^??1"

        q = db._search_wildcard(query["PatientName"], self.session)
        assert 3 == len(q.all())

    def test_search_wildcard_qmark_subquery(self):
        """Test searching within an existing query."""
        pass

    def test_search_uid_list(self):
        """Test search using a UID list."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.SOPInstanceUID = None

        q = db._search_uid_list(query["SOPInstanceUID"], self.session)
        assert 5 == len(q.all())

        query.SOPInstanceUID = ["1.3.6.1.4.1.5962.1.1.4.1.1.20040826185059.5457"]
        q = db._search_uid_list(query["SOPInstanceUID"], self.session)
        assert 1 == len(q.all())

        query.SOPInstanceUID = [
            "1.3.6.1.4.1.5962.1.1.4.1.1.20040826185059.5457",
            "1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322",
        ]
        q = db._search_uid_list(query["SOPInstanceUID"], self.session)
        assert 2 == len(q.all())

        query.SOPInstanceUID = [
            "1.3.6.1.4.1.5962.1.1.4.1.1.20040826185059.5457",
            "1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322",
            "1.3.46.423632.132218.1415242681.6",
        ]
        q = db._search_uid_list(query["SOPInstanceUID"], self.session)
        assert 2 == len(q.all())

    def test_search_uid_list_subquery(self):
        """Test searching within an existing query."""
        pass

    def test_search_uid_list_empty(self):
        """Test searching an empty UID element works correctly."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.SOPInstanceUID = None

        q = db._search_uid_list(query["SOPInstanceUID"], self.session)
        assert 5 == len(q.all())

    @pytest.mark.skip("probably obsolete")
    def test_combine_queries(self):
        """Test combining queries."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.PatientName = "CompressedSamples*"
        query.StudyDate = "20000101-20040119"

        q1 = db._search_wildcard(query["PatientName"], self.session)
        q2 = db._search_range(query["StudyDate"], self.session)
        q = q1.intersect(q2)
        assert 1 == len(q.all())


IDENTIFIERS = [
    (
        "PATIENT",
        [],
        r"The Identifier contains no keys",
        r"The Identifier's Query Retrieve Level value is invalid",
    ),
    (
        "PATIENT",
        ["PatientName"],
        None,
        r"The Identifier's Query Retrieve Level value is invalid",
    ),
    (
        "PATIENT",
        ["PatientID"],
        None,
        r"The Identifier's Query Retrieve Level value is invalid",
    ),
    (
        "PATIENT",
        ["PatientID", "SOPInstanceUID"],
        r"contains keys below the level specified by the Query Retrieve",
        r"The Identifier's Query Retrieve Level value is invalid",
    ),
    (
        "STUDY",
        [],
        r"The Identifier contains no keys",
        r"The Identifier contains no keys",
    ),
    ("STUDY", ["PatientName"], r"missing a unique key for the 'PATIENT' level", None),
    ("STUDY", ["PatientID"], None, None),
    ("STUDY", ["PatientID", "PatientName"], None, None),
    ("STUDY", ["PatientID", "StudyInstanceUID"], None, None),
    (
        "STUDY",
        ["PatientID", "StudyInstanceUID", "SOPInstanceUID"],
        r"contains keys below the level specified by the Query Retrieve",
        r"contains keys below the level specified by the Query Retrieve",
    ),
    (
        "SERIES",
        [],
        r"The Identifier contains no keys",
        r"The Identifier contains no keys",
    ),
    (
        "SERIES",
        ["PatientID"],
        r"missing a unique key for the 'STUDY' level",
        r"missing a unique key for the 'STUDY' level",
    ),
    (
        "SERIES",
        ["StudyInstanceUID"],
        r"missing a unique key for the 'PATIENT' level",
        None,
    ),
    ("SERIES", ["PatientID", "StudyInstanceUID"], None, None),
    (
        "SERIES",
        ["PatientID", "StudyInstanceUID", "SOPInstanceUID"],
        r"contains keys below the level specified by the Query Retrieve",
        r"contains keys below the level specified by the Query Retrieve",
    ),
    (
        "IMAGE",
        [],
        r"The Identifier contains no keys",
        r"The Identifier contains no keys",
    ),
    (
        "IMAGE",
        ["PatientID"],
        r"missing a unique key for the 'STUDY' level",
        r"missing a unique key for the 'STUDY' level",
    ),
    (
        "IMAGE",
        ["PatientID", "StudyInstanceUID"],
        r"missing a unique key for the 'SERIES' level",
        r"missing a unique key for the 'SERIES' level",
    ),
    ("IMAGE", ["PatientID", "StudyInstanceUID", "SeriesInstanceUID"], None, None),
    (
        "DUMMY",
        [],
        r"The Identifier's Query Retrieve Level value is invalid",
        r"The Identifier's Query Retrieve Level value is invalid",
    ),
]


@pytest.mark.skipif(not HAVE_SQLALCHEMY, reason="Requires sqlalchemy")
class TestSearchFind:
    """Tests for running C-FIND queries against the database."""

    def setup_method(self):
        """Run prior to each test"""
        engine = db.create("sqlite:///:memory:")
        pydicom.config.use_none_as_empty_text_VR_value = True

        self.session = sessionmaker(bind=engine)()
        for fname in DATASETS:
            ds = dcmread(DATA_DIR / fname)
            db.add_instance(ds, self.session)

    def test_no_attributes(self):
        """Test searching with no attributes."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"

        model = PatientRootQueryRetrieveInformationModelFind

        msg = r"The Identifier contains no keys"
        with pytest.raises(db.InvalidIdentifier, match=msg):
            db._search_qr(model, query, self.session)

    def test_patient_minimal(self):
        """Test query at PATIENT level for Patient Root."""
        query = Dataset()
        query.QueryRetrieveLevel = "PATIENT"
        query.PatientID = None
        query.PatientName = "CompressedSamples^??1"

        model = PatientRootQueryRetrieveInformationModelFind

        result = db._search_qr(model, query, self.session)
        assert 3 == len(result)

    def test_check_identifier_patient(self):
        """Tests for check_find_identifier()."""
        ds = Dataset()
        ds.QueryRetrieveLevel = "PATIENT"
        ds.PatientName = None
        patient = PatientRootQueryRetrieveInformationModelFind

        db._check_identifier(ds, patient)

        ds.QueryRetrieveLevel = "STUDY"
        msg = r"The Identifier is missing a unique key for the 'PATIENT' level"
        with pytest.raises(db.InvalidIdentifier, match=msg):
            db._check_identifier(ds, patient)

        ds.PatientID = "12345"
        db._check_identifier(ds, patient)

    @pytest.mark.parametrize("level, identifier, pt, st", IDENTIFIERS)
    def test_check_identifier_param_patient(self, level, identifier, pt, st):
        """Tests for check_identifier()."""
        ds = Dataset()
        ds.QueryRetrieveLevel = level
        for kw in identifier:
            setattr(ds, kw, None)

        model = PatientRootQueryRetrieveInformationModelFind
        if pt:
            with pytest.raises(db.InvalidIdentifier, match=pt):
                db._check_identifier(ds, model)
        else:
            db._check_identifier(ds, model)

    def test_check_identifier_study(self):
        """Tests for check_find_identifier()."""
        ds = Dataset()
        ds.QueryRetrieveLevel = "PATIENT"
        ds.PatientName = None
        study = StudyRootQueryRetrieveInformationModelFind

        msg = r"The Identifier's Query Retrieve Level value is invalid"
        with pytest.raises(db.InvalidIdentifier, match=msg):
            db._check_identifier(ds, study)

        ds.QueryRetrieveLevel = "STUDY"
        db._check_identifier(ds, study)

        ds.QueryRetrieveLevel = "SERIES"
        msg = r"The Identifier is missing a unique key for the 'STUDY' level"
        with pytest.raises(db.InvalidIdentifier, match=msg):
            db._check_identifier(ds, study)
        ds.PatientID = None
        with pytest.raises(db.InvalidIdentifier, match=msg):
            db._check_identifier(ds, study)

        ds.StudyInstanceUID = "12345"
        db._check_identifier(ds, study)

    @pytest.mark.parametrize("level, identifier, pt, st", IDENTIFIERS)
    def test_check_identifier_param_study(self, level, identifier, pt, st):
        """Tests for check_identifier()."""
        ds = Dataset()
        ds.QueryRetrieveLevel = level
        for kw in identifier:
            setattr(ds, kw, None)

        model = StudyRootQueryRetrieveInformationModelFind
        if st:
            with pytest.raises(db.InvalidIdentifier, match=st):
                db._check_identifier(ds, model)
        else:
            db._check_identifier(ds, model)

    def test_check_identifier_raises(self):
        """Check raises if no QueryRetrieveLevel element."""
        model = PatientRootQueryRetrieveInformationModelFind
        msg = r"The Identifier contains no Query Retrieve Level element"
        with pytest.raises(db.InvalidIdentifier, match=msg):
            db._check_identifier(Dataset(), model)
