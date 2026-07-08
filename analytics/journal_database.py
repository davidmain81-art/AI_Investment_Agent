"""
Decision Journal Database
"""

import sqlite3


DATABASE = "investment.db"


def create_journal_table():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(

        """

        CREATE TABLE IF NOT EXISTS decision_journal(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            time TEXT,

            market TEXT,

            asset TEXT,

            signal TEXT,

            confidence REAL,

            score REAL,

            reasons TEXT

        )

        """

    )

    conn.commit()

    conn.close()


def save_decision(entry):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO decision_journal(

        time,

        market,

        asset,

        signal,

        confidence,

        score,

        reasons

        )

        VALUES(

        ?,?,?,?,?,?,?

        )

        """,

        (

            entry["time"],

            entry["market"],

            entry["asset"],

            entry["signal"],

            entry["confidence"],

            entry["score"],

            "\n".join(entry["reasons"]),

        ),

    )

    conn.commit()

    conn.close()