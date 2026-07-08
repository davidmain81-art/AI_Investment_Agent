def analyze_market(prices):
    """
    Analyze market using BTC price and daily change.
    """

    btc_price = prices["BTC"]["price"]
    btc_change = prices["BTC"]["change"]

    if btc_price >= 60000:

        if btc_change >= 2:
            signal = "STRONG BUY 🟢"
            risk = "LOW"

        elif btc_change >= 0:
            signal = "BUY 🟢"
            risk = "LOW"

        elif btc_change > -2:
            signal = "HOLD 🟡"
            risk = "MEDIUM"

        else:
            signal = "SELL 🔴"
            risk = "HIGH"

    elif btc_price >= 50000:

        if btc_change >= 2:
            signal = "BUY 🟢"
            risk = "MEDIUM"

        elif btc_change >= 0:
            signal = "HOLD 🟡"
            risk = "MEDIUM"

        else:
            signal = "SELL 🔴"
            risk = "HIGH"

    else:

        signal = "SELL 🔴"
        risk = "HIGH"

    return signal, risk