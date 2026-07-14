"""
AI Memory Engine
Version 0.8
"""

from datetime import datetime

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
        print(trade)

        lesson = self.generate_lesson(
            trade
        )

        save_memory(

            asset=trade["asset"],

            signal=trade["signal"],

            pnl=trade["pnl"],

            result=self.get_result(
                trade["pnl"]
            ),

            lesson=lesson,

            created_at=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

    def get_result(
        self,
        pnl,
    ):

        if pnl >= 0:

            return "WIN"

        return "LOSS"

    def generate_lesson(
        self,
        trade,
    ):

        pnl = trade["pnl"]

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

        total = len(rows)

        wins = 0

        losses = 0

        pnl = 0

        for row in rows:

            pnl += row["pnl"]

            if row["result"] == "WIN":

                wins += 1

            else:

                losses += 1

        if total == 0:

            win_rate = 0

        else:

            win_rate = round(
                wins / total * 100,
                2,
            )

        return {

            "total": total,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "total_pnl": round(
                pnl,
                2,
            ),

        }