"""
AI Learning Engine
Version 3.0 Stable
"""

from memory.memory_database import load_memory


class LearningEngine:

    def __init__(self):
        pass

    def analyze(self):

        rows = load_memory()

        wins = 0
        losses = 0

        total_win = 0
        total_loss = 0

        gross_profit = 0
        gross_loss = 0

        experience = 0

        largest_win = 0
        largest_loss = 0

        current_win_streak = 0
        current_loss_streak = 0

        longest_win_streak = 0
        longest_loss_streak = 0

        equity = 0
        peak_equity = 0
        max_drawdown = 0

        asset_score = {}
        signal_score = {}

        for row in rows:

            if row.get("lesson") == "TEST":
                continue

            experience += 1

            asset = row["asset"]
            signal = row["signal"]
            pnl = float(row["pnl"])

            equity += pnl

            if equity > peak_equity:
                peak_equity = equity

            drawdown = peak_equity - equity

            if drawdown > max_drawdown:
                max_drawdown = drawdown

            asset_score.setdefault(asset, 0)
            asset_score[asset] += pnl

            signal_score.setdefault(signal, 0)
            signal_score[signal] += pnl

            if pnl > 0:

                wins += 1

                total_win += pnl
                gross_profit += pnl

                current_win_streak += 1
                current_loss_streak = 0

                longest_win_streak = max(
                    longest_win_streak,
                    current_win_streak,
                )

                largest_win = max(
                    largest_win,
                    pnl,
                )

            elif pnl < 0:

                losses += 1

                total_loss += abs(pnl)
                gross_loss += abs(pnl)

                current_loss_streak += 1
                current_win_streak = 0

                longest_loss_streak = max(
                    longest_loss_streak,
                    current_loss_streak,
                )

                largest_loss = max(
                    largest_loss,
                    abs(pnl),
                )

        if experience == 0:

            return {

                "experience": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0,
                "average_win": 0,
                "average_loss": 0,
                "profit_factor": 1,
                "best_asset": "UNKNOWN",
                "best_signal": "UNKNOWN",

                "gross_profit": 0,
                "gross_loss": 0,
                "net_profit": 0,

                "largest_win": 0,
                "largest_loss": 0,

                "current_win_streak": 0,
                "current_loss_streak": 0,
                "longest_win_streak": 0,
                "longest_loss_streak": 0,

                "average_trade": 0,
                "expectancy": 0,
                "max_drawdown": 0,
                "recovery_factor": 0,

            }

        win_rate = round(
            wins / experience * 100,
            2,
        )

        average_win = round(
            total_win / wins,
            2,
        ) if wins else 0

        average_loss = round(
            total_loss / losses,
            2,
        ) if losses else 0

        profit_factor = (
            round(gross_profit / gross_loss, 4)
            if gross_loss
            else 1
        )

        net_profit = round(
            gross_profit - gross_loss,
            2,
        )

        average_trade = round(
            net_profit / experience,
            2,
        )

        expectancy = round(
            (wins / experience) * average_win
            -
            (losses / experience) * average_loss,
            2,
        )

        recovery_factor = (
            round(net_profit / max_drawdown, 2)
            if max_drawdown
            else 0
        )

        print("=" * 60)
        print("LEARNING DEBUG")
        print("Experience    :", experience)
        print("Wins          :", wins)
        print("Losses        :", losses)
        print("Gross Profit  :", gross_profit)
        print("Gross Loss    :", gross_loss)
        print("Net Profit    :", net_profit)
        print("Profit Factor :", profit_factor)
        print("Largest Win   :", largest_win)
        print("Largest Loss  :", largest_loss)
        print("Drawdown      :", max_drawdown)
        print("=" * 60)

        return {

            "experience": experience,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,

            "average_win": average_win,
            "average_loss": average_loss,

            "profit_factor": profit_factor,

            "best_asset": max(
                asset_score,
                key=asset_score.get,
            ) if asset_score else "UNKNOWN",

            "best_signal": max(
                signal_score,
                key=signal_score.get,
            ) if signal_score else "UNKNOWN",

            "gross_profit": round(gross_profit, 2),
            "gross_loss": round(gross_loss, 2),
            "net_profit": net_profit,

            "largest_win": round(largest_win, 2),
            "largest_loss": round(largest_loss, 2),

            "current_win_streak": current_win_streak,
            "current_loss_streak": current_loss_streak,

            "longest_win_streak": longest_win_streak,
            "longest_loss_streak": longest_loss_streak,

            "average_trade": average_trade,
            "expectancy": expectancy,

            "max_drawdown": round(max_drawdown, 2),
            "recovery_factor": recovery_factor,

        }