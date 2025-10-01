import pytest
from db.session import SessionLocal
from db.models import WeightStandard, WeightClass, RuleSet

@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()

def test_adcc_standard_exists(db_session):
    adcc = db_session.query(WeightStandard).filter_by(name="ADCC").first()
    assert adcc is not None, "ADCC standard was not seeded"

def test_adcc_weight_classes(db_session):
    adcc = db_session.query(WeightStandard).filter_by(name="ADCC").first()
    assert adcc is not None

    classes = db_session.query(WeightClass).filter_by(standard_id=adcc.id).all()
    assert len(classes) == 7, f"Expected 7 ADCC weight classes, found {len(classes)}"

    formats = set(c.format for c in classes)
    genders = set(c.gender for c in classes)

    assert formats == {"NoGi"}, "ADCC should only have NoGi format"
    assert "Male" in genders and "Female" in genders, "Missing Male or Female divisions"

def test_adcc_standard_and_ruleset(db_session):
    adcc = db_session.query(WeightStandard).filter_by(name="ADCC").first()
    assert adcc is not None, "ADCC standard not found"

    ruleset = db_session.query(RuleSet).filter_by(name="ADCC", standard_id=adcc.id).first()
    assert ruleset is not None, "ADCC ruleset not found or not linked to standard"

