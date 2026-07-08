def make_decision(signal, risk, market_score):
    """
    Create an investment decision based on
    signal, risk and market score.
    """

    reasons = []

    # ---------- Signal ----------

    if signal.startswith("STRONG BUY"):
        reasons.append("Strong bullish momentum.")

    elif signal.startswith("BUY"):
        reasons.append("Trend is bullish.")

    elif signal.startswith("HOLD"):
        reasons.append("Market is waiting for direction.")

    else:
        reasons.append("Trend is bearish.")

    # ---------- Risk ----------

    if risk == "LOW":
        reasons.append("Market risk is low.")

    elif risk == "MEDIUM":
        reasons.append("Market risk is moderate.")

    else:
        reasons.append("Market risk is high.")

    # ---------- Confidence ----------

    confidence = market_score

    if signal.startswith("STRONG BUY"):
        confidence += 15

    elif signal.startswith("BUY"):
        confidence += 10

    elif signal.startswith("SELL"):
        confidence += 5

    if risk == "LOW":
        confidence += 10

    elif risk == "HIGH":
        confidence -= 10

    confidence = max(0, min(confidence, 100))

    # ---------- Position ----------

    if signal.startswith("SELL"):

        position = "0%"
        holding = "Stay in Cash"

    elif signal.startswith("HOLD"):

        position = "5%"
        holding = "Wait"

    elif market_score >= 70:

        position = "20%"
        holding = "7-30 Days"

    elif market_score >= 50:

        position = "10%"
        holding = "3-7 Days"

    else:

        position = "5%"
        holding = "Short-Term"

    return {
        "recommendation": signal,
        "market_score": market_score,
        "confidence": confidence,
        "reasons": reasons,
        "position": position,
        "holding": holding,
    }