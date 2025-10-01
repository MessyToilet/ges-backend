from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text 
from sqlalchemy.orm import relationship
from datetime import datetime 
from db.base import Base 

class Fighter(Base):
    __tablename__ = "fighters"

    id                 = Column(Integer, primary_key=True, index=True)
    phone_number       = Column(Integer, nullable=True)
    email              = Column(String, nullable=True)
    birthday           = Column(String, nullable=False)
    first_name         = Column(String, nullable=False)
    last_name          = Column(String, nullable=True)
    gender             = Column(String, nullable=False)
    weight             = Column(Float, nullable=False)
    on_peds            = Column(Boolean, default=False)
    ruleset_preferance = Column(String, nullable=True)
    created_at         = Column(DateTime, default=datetime.utcnow)

    elo_ratings        = relationship("EloRating", back_populates="fighter")

class Division(Base):
    __tablename__ = "divisions"

    id = Column(Integer, primary_key=True)
    weight_class_id = Column(Integer, ForeignKey("weight_classes.id"))
    is_poison = Column(Boolean, default=False)
    is_absolute = Column(Boolean, default=False)

    weight_class = relationship("WeightClass")

class Match(Base):
    __tablename__ = "matches"

    id           = Column(Integer, primary_key=True, index=True)
    is_gi        = Column(Boolean, default=True)
    fighter_a_id = Column(Integer, ForeignKey("fighters.id"))
    fighter_b_id = Column(Integer, ForeignKey("fighters.id"))
    winner_id    = Column(Integer, ForeignKey("fighters.id"))
    division_id  = Column(Integer, ForeignKey("divisions.id"))
    rule_set_id  = Column(Integer, ForeignKey("rule_sets.id"))
    rule_set    = relationship("RuleSet", back_populates="matches")

    date         = Column(DateTime, default=datetime.utcnow)

class RuleSet(Base):
    __tablename__ = "rule_sets"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    match_duration_minutes = Column(Integer)
    overtime_format = Column(String)
    scoring_notes = Column(String)
    standard_id = Column(Integer, ForeignKey("weight_standards.id"), nullable=True)

    standard = relationship("WeightStandard", back_populates="rule_sets")
    matches = relationship("Match", back_populates="rule_set")

class WeightStandard(Base):
    __tablename__ = "weight_standards"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    weight_classes = relationship("WeightClass", back_populates="standard")
    rule_sets = relationship("RuleSet", back_populates="standard")

class WeightClass(Base):
    __tablename__ = "weight_classes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    format = Column(String, nullable=False)
    min_weight_kg = Column(Float, nullable=True)
    max_weight_kg = Column(Float, nullable=True)
    standard_id = Column(Integer, ForeignKey("weight_standards.id"))

    standard = relationship("WeightStandard", back_populates="weight_classes")

class EloRating(Base):
    __tablename__ = "elo_ratings"

    id = Column(Integer, primary_key=True, index=True)
    fighter_id = Column(Integer, ForeignKey("fighters.id"))
    division_id = Column(Integer, ForeignKey("divisions.id"))
    elo_score = Column(Float, default=1000)
    updated_at = Column(DateTime, default=datetime.utcnow)

    fighter = relationship("Fighter", back_populates="elo_ratings")

class EloHistory(Base):
    __tablename__ = "elo_history"

    id = Column(Integer, primary_key=True, index=True)
    fighter_id = Column(Integer, ForeignKey("fighters.id"))
    division_id = Column(Integer, ForeignKey("divisions.id"))
    elo_before = Column(Float)
    elo_after = Column(Float)
    match_id = Column(Integer, ForeignKey("matches.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)