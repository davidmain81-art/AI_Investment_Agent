import sqlite3

DB = "database/investment_agent.db"


class ExperienceManager:

    def get_statistics(self):

        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""
            SELECT
                COUNT(*) as trades,
                SUM(CASE WHEN result='WIN' THEN 1 ELSE 0 END) as wins,
                SUM(CASE WHEN result='LOSS' THEN 1 ELSE 0 END) as losses,
                AVG(pnl) as avg_pnl,
                SUM(pnl) as total_pnl
            FROM paper_trades
        """)

        row = cur.fetchone()

        conn.close()

        trades = row["trades"] or 0
        wins = row["wins"] or 0
        losses = row["losses"] or 0

        if trades > 0:
            win_rate = round((wins / trades) * 100, 2)
        else:
            win_rate = 0

        return {

            "trades": trades,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "avg_pnl": round(row["avg_pnl"] or 0, 2),

            "total_pnl": round(row["total_pnl"] or 0, 2),

        }


    def last_experiences(self, limit=20):

        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM paper_trades
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        rows = cur.fetchall()

        conn.close()

        return [dict(r) for r in rows]