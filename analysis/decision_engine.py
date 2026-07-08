def make_decision(signal, risk, market_score):
    """
    Create an investment decision based on
    signal, risk and market score.
    """

    confidence = market_score

    reasons = []

    if signal.startswith("BUY"):
        reasons.append("Trend is bullish.")
    elif signal.startswith("SELL"):
        reasons.append("Trend is bearish.")
    else:
        reasons.append("Market is neutral.")

    if risk == "LOW":
        reasons.append("Market risk is low.")
    elif risk == "MEDIUM":
        reasons.append("Market risk is moderate.")
    else:
        reasons.append("Market risk is high.")

    if market_score >= 70:
        position = "20%"
        holding = "7-30 Days"
    elif market_score >= 50:
        position = "10%"
        holding = "3-7 Days"
    else:
        position = "5%"
        holding = "Wait / Short-Term"

    return {
        "recommendation": signal,
        "confidence": confidence,
        "reasons": reasons,
        "position": position,
        "holding": holding,
    }