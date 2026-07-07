def analyze_market(price):

    if price >= 60000:
        signal = "BUY 🟢"
        risk = "LOW"

    elif price >= 50000:
        signal = "HOLD 🟡"
        risk = "MEDIUM"

    else:
        signal = "SELL 🔴"
        risk = "HIGH"

    return signal, risk