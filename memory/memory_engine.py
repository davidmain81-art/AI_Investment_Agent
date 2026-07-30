"""
AI Memory Engine
Version 1.1
"""

from datetime import datetime

from engine.cost_engine import CostEngine

from memory.memory_database import (
    initialize_memory,
    save_memory,
    load_memory,
)


class MemoryEngine:

    def __init__(self):

        initialize_memory()


    def remember_trade(
        self,
        trade,
    ):

        if trade is None:

            return


        print("MEMORY ENGINE EXECUTED")
        print("Saving Trade...")
        print(trade)



        # ==========================
        # TEST Trade Filter
        # ==========================

        exit_reason = trade.get("exit_reason", "")

        if "TEST" in exit_reason:

            lesson = "TEST"

        else:

            lesson = self.generate_lesson(trade)



        # ==========================
        # Trading Cost
        # ==========================


        cost_engine = CostEngine()

        market = trade.get("market", "CRYPTO")

        # کارمزد ورود و خروج (درصد)

        entry_fee = cost_engine.calculate(market)

        exit_fee = cost_engine.calculate(market)

        total_cost = round(

            entry_fee + exit_fee,

            2,

        )

        gross_pnl = trade.get(

            "gross_pnl",

            trade.get("pnl", 0),

        )

        net_pnl = round(

            gross_pnl - total_cost,

            2,

        )

        trade["net_pnl"] = net_pnl


        save_memory(

            created_at=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),


            asset=trade.get(
                "asset",
                "UNKNOWN",
            ),


            market=market,


            signal=trade.get(
                "signal",
                "HOLD",
            ),


            entry_price=trade.get("entry_price", 0),


            exit_price=trade.get(
                "exit_price",
                trade.get("entry_price", 0),
            ),

            quantity=trade.get("quantity", 1),


            gross_pnl=gross_pnl,


            cost=total_cost,


            pnl=net_pnl,


            result=self.get_result(
                net_pnl
            ),

            lesson=lesson,

        )



    def get_result(
        self,
        pnl,
    ):

        if pnl > 0:

            return "WIN"


        elif pnl < 0:

            return "LOSS"


        else:

            return "BREAKEVEN"



    def generate_lesson(
        self,
        trade,
    ):


        pnl = trade.get(
            "net_pnl",
            trade.get(
                "pnl",
                0
            ),
        )



        if pnl >= 5:

            return (
                "Excellent trade. Trend confirmation worked well."
            )


        if pnl >= 2:

            return (
                "Good trade. Entry timing was acceptable."
            )


        if pnl >= 0:

            return (
                "Small profit. Consider holding longer."
            )


        if pnl >= -2:

            return (
                "Minor loss. Entry may have been early."
            )


        return (
            "Large loss. Review strategy before repeating."
        )



    def statistics(self):

        rows = load_memory()

        total = 0

        wins = 0
        losses = 0
        pnl = 0


        for row in rows:


            if row.get("lesson") == "TEST":

                continue

            total += 1

            pnl += row["pnl"]



            if row["result"] == "WIN":

                wins += 1


            elif row["result"] == "LOSS":

                losses += 1


        real_trades = wins + losses


        if real_trades == 0:

            win_rate = 0

        else:

            win_rate = round(
                wins / real_trades * 100,
                2
            )


        return {

            "total": total,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "total_pnl": round(
                pnl,
                2
            ),

        }