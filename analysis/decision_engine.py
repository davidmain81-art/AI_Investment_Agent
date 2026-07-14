"""
Decision Engine
Version 2.0
"""

from analysis.confidence_engine import ConfidenceEngine


def make_decision(
    signal,
    risk,
    market_score,
):

    confidence_engine = ConfidenceEngine()

    confidence = confidence_engine.calculate(
        market_score,
        risk,
    )

    reasons = []

    # -----------------------------
    # Market Description
    # -----------------------------

    if signal == "STRONG BUY 🟢":
        reasons.append("Strong bullish trend detected.")

    elif signal == "BUY 🟢":
        reasons.append("Bullish trend detected.")

    elif signal == "SELL 🔴":
        reasons.append("Bearish trend detected.")

    elif signal == "STRONG SELL 🔴":
        reasons.append("Strong bearish trend detected.")

    else:
        reasons.append("Sideway market detected.")

    reasons.append(f"Risk level is {risk}.")
    reasons.append(f"Market Score = {market_score}/100")

    # -----------------------------
    # Decision Logic
    # -----------------------------

    if signal == "STRONG BUY 🟢":

        recommendation = "BUY"

        if confidence >= 80:

            position = "15%"
            holding = "5-10 Days"

        elif confidence >= 60:

            position = "10%"
            holding = "3-7 Days"

        else:

            position = "5%"
            holding = "1-3 Days"

    elif signal == "BUY 🟢":

        recommendation = "BUY"

        if confidence >= 70:

            position = "10%"

        else:

            position = "5%"

        holding = "2-5 Days"

    elif signal == "STRONG SELL 🔴":

        recommendation = "SELL"

        position = "15%"
        holding = "5-10 Days"

    elif signal == "SELL 🔴":

        recommendation = "SELL"

        position = "10%"
        holding = "2-5 Days"

    else:

        recommendation = "HOLD"

        position = "2%"
        holding = "Scalp"

    # -----------------------------
    # Confidence explanation
    # -----------------------------

    reasons.append(f"Final Confidence = {confidence}%")

    return {

        "recommendation": recommendation,

        "confidence": confidence,

        "position": position,

        "holding": holding,

        "market_score": market_score,

        "risk": risk,

        "reasons": reasons,

    }