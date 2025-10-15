import math
from typing import Tuple

# --- Core Elo math ---

def expected_score(r_a: float, r_b: float, c: float = 667.0) -> float:
    """
    Compute expected win probability of player A vs B.
    r_a, r_b: current ratings
    c: scale constant (default 400 like in chess)
    """
    return 1.0 / (1.0 + math.pow(10.0, (r_b - r_a) / c))


def update_rating(r_a: float, r_b: float, score_a: float,
                  k: float = 20.0, c: float = 667.0) -> float:
    """
    Update rating for player A after one match.
    score_a = 1.0 (win), 0.5 (draw), 0.0 (loss)
    Returns a *new rating*, not in-place.
    """
    expected = expected_score(r_a, r_b, c)
    return r_a + k * (score_a - expected)


def update_both(r_a: float, r_b: float, score_a: float,
                k_a: float = 20.0, k_b: float = 20.0, c: float = 667.0,
                round_result: bool = False) -> Tuple[float, float]:
    """
    Update both players simultaneously using *original ratings*.
    score_a is player A's score (1/0.5/0), player B’s score = 1 - score_a.
    """
    new_a = update_rating(r_a, r_b, score_a, k_a, c)
    new_b = update_rating(r_b, r_a, 1.0 - score_a, k_b, c)
    if round_result:
        return round(new_a), round(new_b)
    return new_a, new_b


# --- dynamic K-factor (provisional logic) ---

def choose_k(matches_played: int) -> float:
    """
    Higher K for new players, lower for experienced.
    """
    if matches_played < 10:
        return 120.0     # new fighter (fast adjustment)
    elif matches_played < 50:
        return 40.0      # regular competitor
    else:
        return 20.0      # stable veteran

