def analyze_market(btc_price):
    """
    Simple market analysis based on Bitcoin price.
    """

    if btc_price >= 60000:
        signal = "BUY 🟢"
        risk = "LOW"
    elif btc_price >= 50000:
        signal = "HOLD 🟡"
        risk = "MEDIUM"
    else:
        signal = "SELL 🔴"
        risk = "HIGH"

    return signal, risk