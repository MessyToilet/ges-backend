import pytest
from db.session import SessionLocal
from db.models import WeightStandard, WeightClass


@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()


def test_ibjjf_standard_exists(db_session):
    ibjjf = db_session.query(WeightStandard).filter_by(name="IBJJF").first()
    assert ibjjf is not None, "IBJJF standard was not seeded"


def test_ibjjf_weight_classes_exist(db_session):
    ibjjf = db_session.query(WeightStandard).filter_by(name="IBJJF").first()
    assert ibjjf is not None, "IBJJF standard missing"

    classes = db_session.query(WeightClass).filter_by(standard_id=ibjjf.id).all()
    assert (
        len(classes) >= 30
    ), f"Expected at least 30 IBJJF weight classes, found {len(classes)}"

    formats = set(c.format for c in classes)
    genders = set(c.gender for c in classes)

    assert "Gi" in formats and "NoGi" in formats, "Missing Gi or NoGi formats"
    assert "Male" in genders and "Female" in genders, "Missing Male or Female divisions"
