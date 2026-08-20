"""
Decision Engine
Version 7.0 Stable
"""

from analysis.ai_optimizer import AIOptimizer
from learning.learning_engine import LearningEngine
from analysis.ai_score_engine import AIScoreEngine
from analysis.confidence_engine import ConfidenceEngine
from analysis.reasoning_engine import ReasoningEngine
from analysis.execution_safety import ExecutionSafety
from analysis.risk_manager import RiskManager
from analysis.indicators_engine import IndicatorsEngine
from learning.pattern_engine import PatternEngine

from providers.health_provider import HealthProvider

from database.ai_memory import save_memory


def make_decision(
    signal,
    risk,
    market_score,
    df,
):

    learning = LearningEngine().analyze()
    # ==============================
    # Market Indicators
    # ==============================

    indicators = IndicatorsEngine().calculate(df)

    # ==============================
    # Merge Indicators
    # ==============================

    flat_indicators = {

        "rsi": indicators["RSI"],
        "mfi": indicators["MFI"],

        "ema20": indicators["EMA20"],
        "ema50": indicators["EMA50"],
        "ema200": indicators["EMA200"],

        "atr": indicators["ATR"],

        "macd": indicators["MACD"],
        "macd_signal": indicators["MACD_SIGNAL"],

        "adx": indicators["ADX"],

        "obv": indicators["OBV"],

    }
    
    # ==============================
    # Pattern Recognition
    # ==============================

    pattern_engine = PatternEngine()

    pattern_result = pattern_engine.analyze(
        current_rsi=indicators["RSI"],
        current_ema20=indicators["EMA20"],
        current_ema50=indicators["EMA50"],
    )

    pattern_score = pattern_result["pattern_score"]

    pattern_analysis = pattern_result["patterns"]

    pattern_engine.close()


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
        pattern_score=pattern_score,
    )

    # ===========================================
    # Risk Manager
    # ===========================================

    risk_manager = RiskManager().calculate(
        ai_score=ai_score,
        confidence=confidence,
        risk=risk,
    )

    # ===========================================
    # Execution Safety
    # ===========================================

    safety = ExecutionSafety().check(
        ai_score=ai_score,
        confidence=confidence,
        latency=HealthProvider().get_latency(),
        risk=risk,
    )

    # ===========================================
    # Recommendation
    # ===========================================

    if ai_score >= 80:

        recommendation = "STRONG BUY"

        holding = "Swing"

    elif ai_score >= 65:

        recommendation = "BUY"

        holding = "Swing"

    elif ai_score >= 45:

        recommendation = "HOLD"

        holding = "Scalp"

    else:

        recommendation = "SELL"

        holding = "None"

    # Position از Risk Manager می‌آید

    position = f'{risk_manager["position_size"]}%'

    reasons = ReasoningEngine().build(
        signal,
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

        "risk_manager": risk_manager,

        "safety": safety,

        "indicators": indicators,

        "pattern_score": pattern_score,

        "pattern_analysis": pattern_analysis,

    }

    result.update(flat_indicators)

    print("=" * 60)
    print("DECISION DEBUG")
    print(result)
    print("=" * 60)

    # ===========================================
    # AI Memory
    # ===========================================

    save_memory(
        market_score=market_score,
        ai_score=ai_score,
        confidence=confidence,
        recommendation=recommendation,
        result="PENDING",
    )

    # =====================================
    # آماده برای Paper Trading
    # =====================================

    result["asset"] = df.attrs.get("asset", "BTC")

    result["signal"] = signal

    result["entry"] = df["close"].iloc[-1]

    result["stop_loss"] = result["entry"] * 0.97

    result["take_profit"] = result["entry"] * 1.10

    result["position_size"] = risk_manager["position_size"]

    result["market_score"] = market_score

    result["learning"] = learning["experience"]

    result["optimizer"] = optimizer_score


    return result