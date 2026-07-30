"""
Live Trade Statistics
Version 1.0
"""


def calculate_trade_statistics(trade, current_price):
    """
    Calculate live trade statistics.
    """

    entry = float(trade["entry_price"])

    signal = str(trade["signal"]).upper().strip()

    if signal.startswith("BUY"):

        pnl = ((current_price - entry) / entry) * 100

    else:

        pnl = ((entry - current_price) / entry) * 100

    distance_tp = (
        abs(trade["take_profit"] - current_price)
        / current_price
    ) * 100

    distance_sl = (
        abs(current_price - trade["stop_loss"])
        / current_price
    ) * 100

    return {

        "current_price": round(current_price, 2),

        "pnl": round(pnl, 2),

        "distance_tp": round(distance_tp, 2),

        "distance_sl": round(distance_sl, 2),

    }