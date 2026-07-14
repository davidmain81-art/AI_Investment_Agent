"""
Performance Analyzer
Version 0.7
"""


class PerformanceAnalyzer:

    def calculate(self, trades):

        total = len(trades)

        wins = 0
        losses = 0

        total_pnl = 0

        total_profit = 0
        total_loss = 0

        max_profit = 0
        max_loss = 0

        for trade in trades:

            pnl = trade["pnl"]

            if pnl is None:
                pnl = 0

            total_pnl += pnl

            if pnl > 0:

                wins += 1

                total_profit += pnl

                if pnl > max_profit:
                    max_profit = pnl

            elif pnl < 0:

                losses += 1

                total_loss += abs(pnl)

                if abs(pnl) > max_loss:
                    max_loss = abs(pnl)

        if total == 0:

            win_rate = 0

        else:

            win_rate = round(
                wins / total * 100,
                2,
            )

        if wins == 0:

            average_profit = 0

        else:

            average_profit = round(
                total_profit / wins,
                2,
            )

        if losses == 0:

            average_loss = 0

        else:

            average_loss = round(
                total_loss / losses,
                2,
            )

        if total_loss == 0:

            profit_factor = 0

        else:

            profit_factor = round(
                total_profit / total_loss,
                2,
            )

        return {

            "trades": total,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "total_pnl": round(
                total_pnl,
                2,
            ),

            "average_profit": average_profit,

            "average_loss": average_loss,

            "profit_factor": profit_factor,

            "max_profit": round(
                max_profit,
                2,
            ),

            "max_loss": round(
                max_loss,
                2,
            ),
        }