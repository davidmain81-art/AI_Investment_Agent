"""
Trade Service
Version 1.1
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

    # ==========================================
    # Execute
    # ==========================================

    def execute(

        self,

        decision,

        asset,

        current_price,

        stop_loss,

        take_profit,

    ):

        current_trade = get_current_trade()

        # ------------------------------

        if decision["recommendation"] != "HOLD":

            trade = create_trade(

                asset=asset,

                decision=decision,

                entry_price=current_price,

                stop_loss=stop_loss,

                take_profit=take_profit,

            )

            if trade:

                current_trade = trade

        # ------------------------------

        self.lifecycle.evaluate(

            current_trade,

            current_price,

        )

        current_trade = get_current_trade()

        # ------------------------------

        if current_trade:

            stats = calculate_trade_statistics(

                current_trade,

                current_price,

            )

        else:

            stats = None

        return current_trade, stats

    # ==========================================
    # Backward Compatibility
    # ==========================================

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