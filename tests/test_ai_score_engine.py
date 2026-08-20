"""
Tests for AI Score Engine
"""

from analysis.ai_score_engine import AIScoreEngine


def test_ai_score_is_between_0_and_100():

    engine = AIScoreEngine()

    learning = {
        "win_rate": 50,
        "profit_factor": 1,
        "experience": 10,
    }

    score = engine.calculate(
        market_score=50,
        learning=learning,
        confidence=50,
        risk="MEDIUM",
        optimizer_score=0,
        pattern_score=0,
    )

    assert 0 <= score <= 100


def test_low_market_score_should_not_create_high_score():

    engine = AIScoreEngine()

    learning = {
        "win_rate": 50,
        "profit_factor": 1,
        "experience": 10,
    }

    score = engine.calculate(
        market_score=20,
        learning=learning,
        confidence=30,
        risk="HIGH",
        optimizer_score=0,
        pattern_score=0,
    )

    assert score < 50


def test_high_market_score_can_create_high_score():

    engine = AIScoreEngine()

    learning = {
        "win_rate": 60,
        "profit_factor": 1.5,
        "experience": 20,
    }

    score = engine.calculate(
        market_score=80,
        learning=learning,
        confidence=75,
        risk="LOW",
        optimizer_score=5,
        pattern_score=5,
    )

    assert score >= 65


def test_high_risk_bearish_market_should_not_become_strong_buy():

    engine = AIScoreEngine()

    learning = {
        "win_rate": 100,
        "profit_factor": 999,
        "experience": 9,
    }

    score = engine.calculate(
        market_score=40,
        learning=learning,
        confidence=42,
        risk="HIGH",
        optimizer_score=9,
        pattern_score=15,
    )

    assert score < 65