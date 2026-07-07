def analyze_market(price):

    if price > 60000:
        return "BUY 🟢"

    elif price > 50000:
        return "HOLD 🟡"

    else:
        return "SELL 🔴"