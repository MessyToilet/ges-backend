import math
import pytest
from elo.utils import (
    expected_score,
    update_rating,
    update_both,
    choose_k,
)

# --- expected_score tests ---

def test_expected_score_symmetry():
    """Expected score should be symmetrical and sum to 1."""
    r1, r2 = 1500, 1600
    e1 = expected_score(r1, r2)
    e2 = expected_score(r2, r1)
    assert math.isclose(e1 + e2, 1.0, rel_tol=1e-9)
    assert 0 < e1 < 1
    assert 0 < e2 < 1

def test_expected_score_monotonic():
    """
    Expected score should:
    1. Be 0.5 for equal ratings
    2. Increase as rating difference increases
    3. Decrease symmetrically for lower-rated player
    """
    # Equal ratings → 0.5
    assert expected_score(1500, 1500) == pytest.approx(0.5, rel=1e-9)

    # Increasing rating gap → expected score increases
    assert expected_score(1600, 1500) > expected_score(1550, 1500)
    assert expected_score(3000, 1000) > expected_score(2000, 1000)

    # Symmetry: flipping ratings → complementary probability
    r_high, r_low = 3000, 1000
    e_high = expected_score(r_high, r_low)
    e_low = expected_score(r_low, r_high)
    assert e_high + e_low == pytest.approx(1.0, rel=1e-9)

    # Monotonicity downward for lower-rated player
    assert expected_score(1000, 3000) < expected_score(1500, 3000)
# --- update_rating tests ---

def test_update_rating_win_increases():
    """Winner should gain points."""
    r1, r2 = 1500, 1600
    new_r1 = update_rating(r1, r2, 1.0)
    assert new_r1 > r1


def test_update_rating_loss_decreases():
    """Loser should lose points."""
    r1, r2 = 1500, 1600
    new_r1 = update_rating(r1, r2, 0.0)
    assert new_r1 < r1


def test_update_rating_draw_midpoint():
    """Draw should move ratings toward each other."""
    r1, r2 = 1500, 1600
    new_r1 = update_rating(r1, r2, 0.5)
    new_r2 = update_rating(r2, r1, 0.5)
    assert new_r1 > r1
    assert new_r2 < r2
    # Difference should shrink
    assert (r2 - r1) > (new_r2 - new_r1)


# --- update_both tests ---

def test_update_both_consistency():
    """update_both should match independent updates."""
    r1, r2 = 1500, 1600
    score_a = 1.0
    new_a, new_b = update_both(r1, r2, score_a)
    # Should be same as doing both manually with original ratings
    manual_a = update_rating(r1, r2, score_a)
    manual_b = update_rating(r2, r1, 1 - score_a)
    assert math.isclose(new_a, manual_a, rel_tol=1e-9)
    assert math.isclose(new_b, manual_b, rel_tol=1e-9)


def test_update_both_draw_symmetry():
    """Draw should keep average rating constant."""
    r1, r2 = 1500, 1600
    new_a, new_b = update_both(r1, r2, 0.5)
    old_avg = (r1 + r2) / 2
    new_avg = (new_a + new_b) / 2
    assert math.isclose(old_avg, new_avg, rel_tol=1e-9)


def test_update_both_round_result():
    """Rounding should return integers."""
    r1, r2 = 1500.0, 1600.0
    new_a, new_b = update_both(r1, r2, 1.0, round_result=True)
    assert isinstance(new_a, int)
    assert isinstance(new_b, int)


# --- choose_k tests ---

def test_choose_k_scale():
    """K should decrease with more matches."""
    assert choose_k(1) > choose_k(20) > choose_k(100)


@pytest.mark.parametrize("matches,expected", [
    (0, 120.0),
    (9, 120.0),
    (10, 40.0),
    (49, 40.0),
    (50, 20.0),
    (100, 20.0),
])
def test_choose_k_thresholds(matches, expected):
    """Test exact thresholds."""
    assert choose_k(matches) == expected
