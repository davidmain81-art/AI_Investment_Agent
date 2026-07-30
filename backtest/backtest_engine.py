"""
Backtest Engine
Version 0.9
"""

from config.database import get_database
from database.database import get_connection


class BacktestEngine:

    def __init__(self):
        pass

    # ----------------------------------------------------

    def load_results(self):
        """
        Load all CLOSED trades.
        """

        self.connection = get_connection(get_database())

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT

                id,
                asset,
                signal,
                entry_price,
                exit_price,
                pnl,
                confidence,
                exit_reason,
                created_at,
                closed_at

            FROM trades

            WHERE status='CLOSED'

            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        results = []

        for row in rows:

            results.append(

                {

                    "id": row[0],
                    "asset": row[1],
                    "signal": row[2],
                    "entry_price": row[3],
                    "exit_price": row[4],
                    "pnl": row[5],
                    "confidence": row[6],
                    "exit_reason": row[7],
                    "created_at": row[8],
                    "closed_at": row[9],

                }

            )

        self.connection.close()

        return results