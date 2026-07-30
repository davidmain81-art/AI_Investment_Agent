"""
Decision Engine
Version 6.0 Stable
"""

from analysis.ai_optimizer import AIOptimizer
from learning.learning_engine import LearningEngine
from analysis.ai_score_engine import AIScoreEngine
from analysis.confidence_engine import ConfidenceEngine
from analysis.reasoning_engine import ReasoningEngine
from analysis.execution_safety import ExecutionSafety
from providers.health_provider import HealthProvider


def make_decision(
    signal,
    risk,
    market_score,
):

    learning = LearningEngine().analyze()
    optimizer_score = AIOptimizer().optimize(learning)

    raw_optimizer_score = optimizer_score

    optimizer_score = max(
        -20,
        min(
            20,
            optimizer_score
        )
    )

    confidence = ConfidenceEngine().calculate(
        market_score,
        risk,
    )

    ai_score = AIScoreEngine().calculate(
        market_score=market_score,
        learning=learning,
        confidence=confidence,
        risk=risk,
        optimizer_score=optimizer_score,
    )

    # ===========================================
    # Execution Safety Check
    # ===========================================

    safety = ExecutionSafety().check(
        ai_score=ai_score,
        confidence=confidence,
        latency=HealthProvider().get_latency(),
        risk=risk,
    )

    if ai_score >= 80:
        recommendation = "STRONG BUY"
        position = "10%"
        holding = "Swing"

    elif ai_score >= 65:
        recommendation = "BUY"
        position = "5%"
        holding = "Swing"

    elif ai_score >= 45:
        recommendation = "HOLD"
        position = "2%"
        holding = "Scalp"

    else:
        recommendation = "SELL"
        position = "0%"
        holding = "None"

    reasons = ReasoningEngine().build(
        recommendation,
        risk,
        market_score,
        confidence,
        learning,
    )
  
    result = {
        "recommendation": recommendation,
        "confidence": confidence,
        "ai_score": ai_score,

        "optimizer_score": raw_optimizer_score,
        "optimizer_used": optimizer_score,

        "position": position,
        "holding": holding,
        "market_score": market_score,
        "risk": risk,
        "learning": learning,
        "reasons": reasons,

        "safety": safety,
        
    }

    print("=" * 60)
    print("DECISION DEBUG")
    print(result)
    print("=" * 60)

    return result