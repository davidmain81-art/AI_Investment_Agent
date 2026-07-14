from database.trades import close_trade


class TradeMonitor:
    """
    Monitor OPEN trades.
    """

    def __init__(self, trade):

        self.trade = trade

    def should_close(self, current_price):

        signal = self.trade["signal"]

        if signal == "BUY 🟢":

            if current_price >= self.trade["take_profit"]:

                return True, "TAKE_PROFIT"

            if current_price <= self.trade["stop_loss"]:

                return True, "STOP_LOSS"

        else:

            if current_price <= self.trade["take_profit"]:

                return True, "TAKE_PROFIT"

            if current_price >= self.trade["stop_loss"]:

                return True, "STOP_LOSS"

        return False, None

    def close_if_needed(self, current_price):

        should_close, reason = self.should_close(current_price)

        if not should_close:

            return False

        close_trade(
            self.trade["id"],
            exit_price=current_price,
        )

        print()

        print("✅ TRADE CLOSED")

        print(f"Reason : {reason}")

        print(f"Exit   : {current_price}")

        return True