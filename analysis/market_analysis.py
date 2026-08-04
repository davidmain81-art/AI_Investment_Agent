"""
Market Analysis
Version 2.0
"""

from analysis.indicators_engine import IndicatorsEngine


def analyze_market(prices, df):

    indicators = IndicatorsEngine().calculate(df)

    score = 0

    # ===========================
    # EMA Trend
    # ===========================

    if indicators["ema20"] > indicators["ema50"]:
        score += 10
    else:
        score -= 10

    # ===========================
    # RSI
    # ===========================

    if indicators["rsi"] < 30:
        score += 15

    elif indicators["rsi"] > 70:
        score -= 15

    # ===========================
    # MFI
    # ===========================

    if indicators["mfi"] < 20:
        score += 10

    elif indicators["mfi"] > 80:
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

    if indicators["trend"] == "UP":
        score += 10

    elif indicators["trend"] == "DOWN":
        score -= 10

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

    return signal, risk, score, indicators