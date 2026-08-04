"""
Market Analysis
Version 2.0
"""

from analysis.indicators_engine import IndicatorsEngine


def analyze_market(prices, df):

    indicators = IndicatorsEngine().calculate(df)

    print(indicators.keys())

    score = 0

    # ===========================
    # EMA Trend
    # ===========================

    if indicators["EMA20"] > indicators["EMA50"]:
        score += 10
    else:
        score -= 10

    # ===========================
    # RSI
    # ===========================

    if indicators["RSI"] < 30:
        score += 15

    elif indicators["RSI"] > 70:
        score -= 15

    # ===========================
    # MFI
    # ===========================

    if indicators["MFI"] < 20:
        score += 10

    elif indicators["MFI"] > 80:
        score -= 10

    # ===========================
    # BTC Daily Change
    # ===========================

    btc_change = prices["BTC"]["change"]

    if btc_change > 2:
        score += 10

    elif btc_change < -2:
        score -= 10

    # ===========================
    # Trend
    # ===========================

    if indicators["EMA20"] > indicators["EMA50"]:

        score += 10

        trend = "UP"

    else:

        score -= 10

        trend = "DOWN"

    # ===========================
    # Final Signal
    # ===========================

    if score >= 30:

        signal = "STRONG BUY 🟢"
        risk = "LOW"

    elif score >= 15:

        signal = "BUY 🟢"
        risk = "LOW"

    elif score >= 0:

        signal = "HOLD 🟡"
        risk = "MEDIUM"

    else:

        signal = "SELL 🔴"
        risk = "HIGH"

    indicators["trend"] = trend

    return signal, risk, score, indicators