import sqlite3

DB = "database/investment_agent.db"


def save_memory(
    market_score,
    ai_score,
    confidence,
    recommendation,
    result,
):

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ai_memory(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

            market_score REAL,

            ai_score REAL,

            confidence REAL,

            recommendation TEXT,

            result TEXT

        )
        """
    )

    cur.execute(
        """
        INSERT INTO ai_memory(

            market_score,

            ai_score,

            confidence,

            recommendation,

            result

        )

        VALUES(?,?,?,?,?)
        """,
        (
            market_score,

            ai_score,

            confidence,

            recommendation,

            result,

        ),
    )

    conn.commit()

    conn.close()


def load_memory(limit=100):

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *

        FROM ai_memory

        ORDER BY id DESC

        LIMIT ?
        """,
        (limit,),
    )

    rows = cur.fetchall()

    conn.close()

    return rows