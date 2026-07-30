"""
Trade Service
Version 2.0
"""

from trading.trade_statistics import calculate_trade_statistics
from trading.trade_lifecycle import TradeLifecycle
from trading.trade_manager import (
    create_trade,
    get_current_trade,
)


class TradeService:

    def __init__(self):

        self.lifecycle = TradeLifecycle()

    def execute(

        self,

        decision,

        asset,

        current_price,

        stop_loss,

        take_profit,

    ):

        current_trade = get_current_trade()

        # -----------------------------
        # Create new trade only if none exists
        # -----------------------------

        if (

            current_trade is None

            and decision["recommendation"] != "HOLD"

        ):

            current_trade = create_trade(

                asset=asset,

                decision=decision,

                entry_price=current_price,

                stop_loss=stop_loss,

                take_profit=take_profit,

            )

        # -----------------------------
        # Evaluate existing trade
        # -----------------------------

        if current_trade:

            self.lifecycle.evaluate(

                current_trade,

                current_price,

            )

        # -----------------------------
        # Reload trade
        # -----------------------------

        current_trade = get_current_trade()

        # -----------------------------
        # Statistics
        # -----------------------------

        stats = None

        if current_trade:

            stats = calculate_trade_statistics(

                current_trade,

                current_price,

            )

        return current_trade, stats

    def process(

        self,

        decision,

        asset,

        current_price,

        stop_loss,

        take_profit,

    ):

        return self.execute(

            decision,

            asset,

            current_price,

            stop_loss,

            take_profit,

        )