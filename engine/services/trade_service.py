"""
Trade Service
Version 2.2
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

        # -----------------------------
        # Get existing trade
        # -----------------------------

        current_trade = get_current_trade()

        # -----------------------------
        # Evaluate existing trade
        # -----------------------------

        if current_trade:

            self.lifecycle.evaluate(
                current_trade,
                current_price,
            )

            # Reload after lifecycle evaluation
            current_trade = get_current_trade()

            # -----------------------------------------
            # Reverse Signal
            # -----------------------------------------

            if (
                current_trade
                and decision.get("recommendation")
                != current_trade.get("signal")
                and decision.get("recommendation")
                != "HOLD"
            ):

                current_trade = create_trade(
                    asset=asset,
                    decision=decision,
                    entry_price=current_price,
                    stop_loss=stop_loss,
                    take_profit=take_profit,
                )

                if current_trade:

                    stats = calculate_trade_statistics(
                        current_trade,
                        current_price,
                    )

                    return current_trade, stats

        # -----------------------------
        # No existing trade
        # -----------------------------

        if current_trade is None:

            # -------------------------
            # HOLD = do nothing
            # -------------------------

            if decision["recommendation"] == "HOLD":

                return None, None

            # -------------------------
            # Execution Safety Gate
            # -------------------------

            if not decision.get(
                "safety",
                {}
            ).get(
                "allowed",
                False
            ):

                print(
                    "TRADE BLOCKED BY EXECUTION SAFETY"
                )

                return None, None

            # -------------------------
            # Create new trade
            # -------------------------

            current_trade = create_trade(
                asset=asset,
                decision=decision,
                entry_price=current_price,
                stop_loss=stop_loss,
                take_profit=take_profit,
            )

        # -----------------------------
        # Statistics
        # -----------------------------

        stats = None

        if current_trade:

            stats = calculate_trade_statistics(
                current_trade,
                current_price,
            )

        # -----------------------------
        # Return
        # -----------------------------

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