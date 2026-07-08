"""
AI Market Memory
Version 0.1
"""

import sqlite3


DATABASE = "investment.db"


def create_memory_table():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS market_memory(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            market TEXT,

            asset TEXT,

            signal TEXT,

            confidence REAL,

            score REAL,

            result TEXT,

            profit_percent REAL

        )
        """
    )

    conn.commit()
    conn.close()


def save_memory(memory):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO market_memory(

            created_at,
            market,
            asset,
            signal,
            confidence,
            score,
            result,
            profit_percent

        )

        VALUES(?,?,?,?,?,?,?,?)

        """,
        (

            memory["created_at"],
            memory["market"],
            memory["asset"],
            memory["signal"],
            memory["confidence"],
            memory["score"],
            memory["result"],
            memory["profit_percent"],

        ),
    )

    conn.commit()
    conn.close()


def load_memory():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *

        FROM market_memory

        ORDER BY id DESC

        """

    )

    rows = cursor.fetchall()

    conn.close()

    return rows