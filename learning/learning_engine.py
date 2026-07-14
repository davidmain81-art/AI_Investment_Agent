"""
AI Learning Engine
Version 2.0
"""

from memory.memory_database import load_memory


class LearningEngine:

    def __init__(self):

        self.memory = load_memory()

    def analyze(self):

        rows = self.memory

        total = len(rows)

        if total == 0:

            return {

                "experience": 0,

                "wins": 0,

                "losses": 0,

                "win_rate": 0,

                "confidence": 50,

                "average_win": 0,

                "average_loss": 0,

                "profit_factor": 1,

                "best_asset": "UNKNOWN",

                "best_signal": "UNKNOWN",

            }

        wins = 0
        losses = 0

        total_win = 0
        total_loss = 0

        asset_score = {}
        signal_score = {}

        for row in rows:

            asset = row["asset"]
            signal = row["signal"]
            pnl = float(row["pnl"])

            asset_score.setdefault(asset, 0)
            asset_score[asset] += pnl

            signal_score.setdefault(signal, 0)
            signal_score[signal] += pnl

            if pnl > 0:

                wins += 1
                total_win += pnl

            else:

                losses += 1
                total_loss += abs(pnl)

        win_rate = round((wins / total) * 100, 2)

        average_win = round(

            total_win / wins,

            2,

        ) if wins else 0

        average_loss = round(

            total_loss / losses,

            2,

        ) if losses else 0

        if total_loss == 0:

            profit_factor = round(total_win, 2)

        else:

            profit_factor = round(

                total_win / total_loss,

                2,

            )

        # ------------------------
        # AI Confidence
        # ------------------------

        confidence = 50

        confidence += (win_rate - 50) * 0.30

        confidence += (profit_factor - 1) * 15

        confidence += min(total, 100) * 0.20

        confidence = max(

            20,

            min(

                95,

                round(confidence),

            ),

        )

        return {

            "experience": total,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "confidence": confidence,

            "average_win": average_win,

            "average_loss": average_loss,

            "profit_factor": profit_factor,

            "best_asset": max(

                asset_score,

                key=asset_score.get,

            ),

            "best_signal": max(

                signal_score,

                key=signal_score.get,

            ),

        }