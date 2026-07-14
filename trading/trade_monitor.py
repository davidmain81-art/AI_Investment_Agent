"""
Trade Monitor
Version 0.6
"""

from trading.trade_manager import (
    get_current_trade,
    create_trade,
)

from database.trades import (
    close_trade,
    update_trade_result,
)

from database.prediction_results import (
    save_prediction_result,
)


class TradeMonitor:

    def __init__(self):

        self.current_trade = get_current_trade()

    # ----------------------------------------------------

    def check_open_trade(self):
        """
        Return latest OPEN trade.
        """

        self.current_trade = get_current_trade()

        return self.current_trade

    # ----------------------------------------------------

    def check_price(self, current_price):
        """
        Check if TP or SL has been reached.
        """

        trade = self.check_open_trade()

        if trade is None:
            return None

        # ==========================
        # BUY Trade
        # ==========================

        if trade["signal"] == "BUY":

            # Take Profit

            if current_price >= trade["take_profit"]:

                pnl = (
                    (current_price - trade["entry"])
                    / trade["entry"]
                ) * 100

                update_trade_result(
                    trade["id"],
                    current_price,
                    pnl,
                    "TAKE_PROFIT",
                )

                save_prediction_result(
                    trade["prediction_id"],
                    current_price,
                    pnl,
                    1,
                )

                close_trade(trade["id"])

                return "TAKE_PROFIT"

            # Stop Loss

            if current_price <= trade["stop_loss"]:

                pnl = (
                    (current_price - trade["entry"])
                    / trade["entry"]
                ) * 100

                update_trade_result(
                    trade["id"],
                    current_price,
                    pnl,
                    "STOP_LOSS",
                )

                save_prediction_result(
                    trade["prediction_id"],
                    current_price,
                    pnl,
                    0,
                )

                close_trade(trade["id"])

                return "STOP_LOSS"

        # ==========================
        # SELL Trade
        # ==========================

        elif trade["signal"] == "SELL":

            # Take Profit

            if current_price <= trade["take_profit"]:

                pnl = (
                    (trade["entry"] - current_price)
                    / trade["entry"]
                ) * 100

                update_trade_result(
                    trade["id"],
                    current_price,
                    pnl,
                    "TAKE_PROFIT",
                )

                save_prediction_result(
                    trade["prediction_id"],
                    current_price,
                    pnl,
                    1,
                )

                close_trade(trade["id"])

                return "TAKE_PROFIT"

            # Stop Loss

            if current_price >= trade["stop_loss"]:

                pnl = (
                    (trade["entry"] - current_price)
                    / trade["entry"]
                ) * 100

                update_trade_result(
                    trade["id"],
                    current_price,
                    pnl,
                    "STOP_LOSS",
                )

                save_prediction_result(
                    trade["prediction_id"],
                    current_price,
                    pnl,
                    0,
                )

                close_trade(trade["id"])

                return "STOP_LOSS"

        return None

    # ----------------------------------------------------

    def evaluate_signal(
        self,
        asset,
        decision,
        entry_price,
        stop_loss,
        take_profit,
    ):
        """
        Compare AI signal with current trade.
        """

        trade = self.check_open_trade()

        if trade is None:

            return create_trade(
                asset,
                decision,
                entry_price,
                stop_loss,
                take_profit,
            )

        if trade["signal"] == decision["recommendation"]:

            return trade

        close_trade(trade["id"])

        return create_trade(
            asset,
            decision,
            entry_price,
            stop_loss,
            take_profit,
        )