import pandas as pd

import analysis.decision_engine as decision_engine


class FakeLearningEngine:

    def analyze(self):

        return {
            "paper_trades": 0,
            "paper_win_rate": 0,
            "paper_total_profit": 0,
            "experience": 0,
            "wins": 0,
            "losses": 0,
            "win_rate": 0,
            "average_win": 0,
            "average_loss": 0,
            "profit_factor": 0,
            "best_asset": None,
            "best_signal": None,
            "gross_profit": 0,
            "gross_loss": 0,
            "net_profit": 0,
            "largest_win": 0,
            "largest_loss": 0,
            "current_win_streak": 0,
            "current_loss_streak": 0,
            "longest_win_streak": 0,
            "longest_loss_streak": 0,
            "average_trade": 0,
            "expectancy": 0,
            "max_drawdown": 0,
            "recovery_factor": 0,
        }


class FakeIndicatorsEngine:

    def calculate(self, df):

        return {

            "RSI": 40,
            "MFI": 50,

            "EMA20": 100,
            "EMA50": 95,
            "EMA200": 90,

            "ATR": 2,

            "MACD": 1,
            "MACD_SIGNAL": 0.5,

            "ADX": 25,

            "OBV": 1000,
        }


class FakePatternEngine:

    def analyze(
        self,
        current_rsi=None,
        current_ema20=None,
        current_ema50=None,
    ):

        return {

            "pattern_score": 15.0,

            "patterns": {

                "RSI": {

                    "pattern": "RSI < 40",

                    "trades": 3,

                    "wins": 3,

                    "win_rate": 100.0,

                },

                "EMA": {

                    "pattern": "EMA20 > EMA50",

                    "trades": 3,

                    "wins": 3,

                    "win_rate": 100.0,

                },

            },

        }

    def close(self):

        pass


class FakeAIOptimizer:

    def optimize(self, learning):

        return 0


class FakeConfidenceEngine:

    def calculate(
        self,
        market_score,
        risk,
    ):

        return 50


class FakeAIScoreEngine:

    received_pattern_score = None

    def calculate(
        self,
        market_score,
        learning,
        confidence,
        risk,
        optimizer_score=0,
        pattern_score=0,
    ):

        FakeAIScoreEngine.received_pattern_score = (
            pattern_score
        )

        return 60


class FakeRiskManager:

    def calculate(
        self,
        ai_score,
        confidence,
        risk,
    ):

        return {

            "position_size": 10,

            "max_open_trades": 3,

            "max_portfolio_risk": 20,

            "stop_loss_percent": 3,

            "take_profit_percent": 10,

        }


class FakeExecutionSafety:

    def check(
        self,
        ai_score,
        confidence,
        latency,
        risk,
    ):

        return {

            "allowed": True

        }


class FakeHealthProvider:

    def get_latency(self):

        return 100


class FakeReasoningEngine:

    def build(
        self,
        signal,
        risk,
        market_score,
        confidence,
        learning,
    ):

        return []


def fake_save_memory(**kwargs):

    pass


def test_pattern_score_reaches_ai_score(
    monkeypatch
):

    monkeypatch.setattr(
        decision_engine,
        "LearningEngine",
        FakeLearningEngine,
    )

    monkeypatch.setattr(
        decision_engine,
        "IndicatorsEngine",
        FakeIndicatorsEngine,
    )

    monkeypatch.setattr(
        decision_engine,
        "PatternEngine",
        FakePatternEngine,
    )

    monkeypatch.setattr(
        decision_engine,
        "AIOptimizer",
        FakeAIOptimizer,
    )

    monkeypatch.setattr(
        decision_engine,
        "ConfidenceEngine",
        FakeConfidenceEngine,
    )

    monkeypatch.setattr(
        decision_engine,
        "AIScoreEngine",
        FakeAIScoreEngine,
    )

    monkeypatch.setattr(
        decision_engine,
        "RiskManager",
        FakeRiskManager,
    )

    monkeypatch.setattr(
        decision_engine,
        "ExecutionSafety",
        FakeExecutionSafety,
    )

    monkeypatch.setattr(
        decision_engine,
        "HealthProvider",
        FakeHealthProvider,
    )

    monkeypatch.setattr(
        decision_engine,
        "ReasoningEngine",
        FakeReasoningEngine,
    )

    monkeypatch.setattr(
        decision_engine,
        "save_memory",
        fake_save_memory,
    )

    df = pd.DataFrame({

        "close": [
            100,
            101,
            102
        ]

    })

    df.attrs["asset"] = "BTC"

    result = decision_engine.make_decision(

        signal="BUY",

        risk="MEDIUM",

        market_score=60,

        df=df,

    )

    assert result["pattern_score"] == 15.0

    assert (
        FakeAIScoreEngine.received_pattern_score
        == 15.0
    )