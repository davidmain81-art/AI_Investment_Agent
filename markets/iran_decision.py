def analyze_iran_market(score):
    """
    Analyze Iran market based on score.
    """

    if score >= 70:
        signal = "BUY 🟢"
        confidence = 90

    elif score >= 55:
        signal = "BUY 🟢"
        confidence = 75

    elif score >= 40:
        signal = "HOLD 🟡"
        confidence = 60

    else:
        signal = "SELL 🔴"
        confidence = 85

    return {
        "signal": signal,
        "confidence": confidence,
    }