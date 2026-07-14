"""
Trade Lifecycle
Version 1.0
"""

from database.close_trade import close_trade
from memory.memory_engine import MemoryEngine


class TradeLifecycle:

    def __init__(self):

        self.memory = MemoryEngine()

    def evaluate(
        self,
        trade,
        current_price,
    ):

        if trade is None:
            return None

        signal = trade["signal"]

        # ==========================================
        # TEST MODE
        # فقط برای تست Memory
        # ==========================================

        TEST_MODE = True

        if TEST_MODE:

            closed_trade = close_trade(

                trade["id"],

                current_price,

                "TEST",

            )

            if closed_trade:

                self.memory.remember_trade(

                    closed_trade

                )

            return "TEST"

        # ==========================================
        # BUY
        # ==========================================

        if signal == "BUY":

            if current_price >= trade["take_profit"]:

                closed_trade = close_trade(

                    trade["id"],

                    current_price,

                    "TAKE_PROFIT",

                )

                if closed_trade:

                    self.memory.remember_trade(

                        closed_trade

                    )

                return "TP"

            if current_price <= trade["stop_loss"]:

                closed_trade = close_trade(

                    trade["id"],

                    current_price,

                    "STOP_LOSS",

                )

                if closed_trade:

                    self.memory.remember_trade(

                        closed_trade

                    )

                return "SL"

        # ==========================================
        # SELL
        # ==========================================

        if signal == "SELL":

            if current_price <= trade["take_profit"]:

                closed_trade = close_trade(

                    trade["id"],

                    current_price,

                    "TAKE_PROFIT",

                )

                if closed_trade:

                    self.memory.remember_trade(

                        closed_trade

                    )

                return "TP"

            if current_price >= trade["stop_loss"]:

                closed_trade = close_trade(

                    trade["id"],

                    current_price,

                    "STOP_LOSS",

                )

                if closed_trade:

                    self.memory.remember_trade(

                        closed_trade

                    )

                return "SL"

        return None