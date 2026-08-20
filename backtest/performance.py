"""
Performance Analyzer
Version 1.0
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
                max_profit = max(max_profit, pnl)

            elif pnl < 0:

                losses += 1
                loss = abs(pnl)
                total_loss += loss
                max_loss = max(max_loss, loss)

        win_rate = (
            round(wins / total * 100, 2)
            if total
            else 0
        )

        average_profit = (
            round(total_profit / wins, 2)
            if wins
            else 0
        )

        average_loss = (
            round(total_loss / losses, 2)
            if losses
            else 0
        )

        profit_factor = (
            round(total_profit / total_loss, 2)
            if total_loss
            else 0
        )

        return {

            "trades": total,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "total_pnl": round(total_pnl, 2),
            "average_profit": average_profit,
            "average_loss": average_loss,
            "profit_factor": profit_factor,
            "max_profit": round(max_profit, 2),
            "max_loss": round(max_loss, 2),
        }