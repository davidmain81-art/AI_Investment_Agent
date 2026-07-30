"""
Trade Lifecycle
Version 1.2
"""

from database.close_trade import close_trade
from engine.trade_pipeline import TradePipeline


class TradeLifecycle:

    def __init__(self):

        self.pipeline = TradePipeline()

    def evaluate(
        self,
        trade,
        current_price,
    ):

        if trade is None:
            return None

        signal = trade["signal"]

        print("=" * 60)
        print("TRADE LIFECYCLE")
        print(f"Trade ID : {trade['id']}")
        print(f"Signal   : {signal}")
        print(f"Current  : {current_price}")
        print(f"Entry    : {trade['entry_price']}")
        print(f"TP       : {trade['take_profit']}")
        print(f"SL       : {trade['stop_loss']}")
        print("=" * 60)
        
        # ==========================================
        # BUY
        # ==========================================

        if signal == "BUY":

            print("Checking BUY trade...")

            if current_price >= trade["take_profit"]:

                print(">>> TAKE PROFIT HIT <<<")

                closed_trade = close_trade(
                    trade["id"],
                    current_price,
                    "TAKE_PROFIT",
                )

                print("Returned from close_trade()")
                print(closed_trade)

                if closed_trade:

                    self.pipeline.process(
                        closed_trade
                    )

                return "TP"

            if current_price <= trade["stop_loss"]:

                print(">>> STOP LOSS HIT <<<")

                closed_trade = close_trade(
                    trade["id"],
                    current_price,
                    "STOP_LOSS",
                )

                print("Returned from close_trade()")
                print(closed_trade)

                if closed_trade:

                    self.pipeline.process(
                        closed_trade
                    )

                return "SL"

        # ==========================================
        # SELL
        # ==========================================

        elif signal == "SELL":

            print("Checking SELL trade...")

            if current_price <= trade["take_profit"]:

                print(">>> TAKE PROFIT HIT <<<")

                closed_trade = close_trade(
                    trade["id"],
                    current_price,
                    "TAKE_PROFIT",
                )

                print("Returned from close_trade()")
                print(closed_trade)

                if closed_trade:

                    self.pipeline.process(
                        closed_trade
                    )

                return "TP"

            if current_price >= trade["stop_loss"]:

                print(">>> STOP LOSS HIT <<<")

                closed_trade = close_trade(
                    trade["id"],
                    current_price,
                    "STOP_LOSS",
                )

                print("Returned from close_trade()")
                print(closed_trade)

                if closed_trade:

                    self.pipeline.process(
                        closed_trade
                    )

                return "SL"

        print("Trade still OPEN")

        return None