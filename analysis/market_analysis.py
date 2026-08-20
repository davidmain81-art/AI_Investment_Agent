"""
Market Analysis
Version 2.2
"""

from analysis.indicators_engine import IndicatorsEngine


def analyze_market(prices, df):

    indicators = IndicatorsEngine().calculate(df)

    # ==========================================
    # Raw Technical Score
    # ==========================================

    score = 0

    # ==========================================
    # EMA Trend
    # ==========================================

    if indicators["EMA20"] > indicators["EMA50"]:

        score += 10
        trend = "UP"

    else:

        score -= 10
        trend = "DOWN"

    # ==========================================
    # RSI
    # ==========================================

    if indicators["RSI"] < 30:

        score += 15

    elif indicators["RSI"] > 70:

        score -= 15

    # ==========================================
    # MFI
    # ==========================================

    if indicators["MFI"] < 20:

        score += 10

    elif indicators["MFI"] > 80:

        score -= 10

    # ==========================================
    # BTC Daily Change
    # ==========================================

    btc_change = prices["BTC"]["change"]

    if btc_change > 2:

        score += 10

    elif btc_change < -2:

        score -= 10

    # ==========================================
    # Final Signal
    # ==========================================

    if score >= 30:

        signal = "STRONG BUY"
        risk = "LOW"

    elif score >= 15:

        signal = "BUY"
        risk = "LOW"

    elif score >= 0:

        signal = "HOLD"
        risk = "MEDIUM"

    else:

        signal = "SELL"
        risk = "HIGH"

    # ==========================================
    # Add Trend
    # ==========================================

    indicators["trend"] = trend

    # ==========================================
    # Normalize Technical Market Score
    #
    # Raw Score:
    # approximately -45 .. +45
    #
    # AI / Confidence:
    # expected 0 .. 100
    #
    # Mapping:
    # -10 -> 40
    #   0 -> 50
    # +10 -> 60
    # ==========================================

    market_score = max(
        0,
        min(
            100,
            50 + score
        )
    )

    # ==========================================
    # Return
    # ==========================================

    return signal, risk, market_score, indicators