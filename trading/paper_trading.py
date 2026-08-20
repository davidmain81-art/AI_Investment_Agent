"""
Paper Trading
Version 1.0
"""


class PaperTrading:

    def __init__(self):

        self.positions = []

    def open_trade(
        self,
        asset,
        signal,
        entry_price,
        quantity=1,
    ):

        trade = {

            "asset": asset,
            "signal": signal,
            "entry_price": entry_price,
            "quantity": quantity,
            "status": "OPEN",

        }

        self.positions.append(trade)

        return trade

    def close_trade(
        self,
        trade,
        exit_price,
    ):

        if trade["status"] != "OPEN":

            return None

        entry = trade["entry_price"]
        quantity = trade["quantity"]

        if "SELL" in trade["signal"]:

            pnl = (
                entry - exit_price
            ) * quantity

        else:

            pnl = (
                exit_price - entry
            ) * quantity

        trade["exit_price"] = exit_price
        trade["pnl"] = round(pnl, 2)
        trade["status"] = "CLOSED"

        return trade