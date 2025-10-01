import pytest
from db.session import SessionLocal
from db.models import WeightStandard, WeightClass, RuleSet

@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()

def test_grappling_industries_standard_exists(db_session):
    gi = db_session.query(WeightStandard).filter_by(name="Grappling Industries").first()
    assert gi is not None, "Grappling Industries standard was not seeded"

def test_grappling_industries_weight_classes(db_session):
    gi = db_session.query(WeightStandard).filter_by(name="Grappling Industries").first()
    assert gi is not None

    classes = db_session.query(WeightClass).filter_by(standard_id=gi.id).all()
    assert len(classes) >= 15, f"Expected at least 15 Grappling Industries weight classes, found {len(classes)}"

    formats = set(c.format for c in classes)
    genders = set(c.gender for c in classes)

    assert "Gi" in formats, "Missing Gi format"
    assert "Male" in genders and "Female" in genders, "Missing Male or Female divisions"

def test_grappling_industries_standard_and_ruleset(db_session):
    gi = db_session.query(WeightStandard).filter_by(name="Grappling Industries").first()
    assert gi is not None, "Grappling Industries standard not found"

    ruleset = db_session.query(RuleSet).filter_by(name="Grappling Industries", standard_id=gi.id).first()
    assert ruleset is not None, "Grappling Industries ruleset not found or not linked to standard"
