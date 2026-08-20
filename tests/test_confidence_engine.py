from analysis.confidence_engine import ConfidenceEngine


def test_confidence_engine_sample_size(monkeypatch):

    class FakeLearningEngine:

        def analyze(self):

            return {
                "experience": 0,
                "win_rate": 50,
                "profit_factor": 1,
            }

    monkeypatch.setattr(
        "analysis.confidence_engine.LearningEngine",
        FakeLearningEngine,
    )

    engine = ConfidenceEngine()

    confidence = engine.calculate(
        market_score=40,
        risk="MEDIUM",
    )

    assert confidence == 45
    assert confidence < 50