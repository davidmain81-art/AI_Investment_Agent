import sqlite3

from config.database import get_database

DATABASE = get_database()


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_memory():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS memory(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TEXT,

        asset TEXT,

        market TEXT,

        signal TEXT,

        entry_price REAL,

        exit_price REAL,

        quantity REAL,

        gross_pnl REAL,

        cost REAL,

        pnl REAL,

        result TEXT,

        lesson TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_memory(

    created_at,
    asset,
    market,
    signal,
    entry_price,
    exit_price,
    quantity,
    gross_pnl,
    cost,
    pnl,
    result,
    lesson,

):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(

        """
        INSERT INTO memory(

            created_at,
            asset,
            market,
            signal,
            entry_price,
            exit_price,
            quantity,
            gross_pnl,
            cost,
            pnl,
            result,
            lesson

        )

        VALUES(

            ?,?,?,?,?,?,?,?,?,?,?,?

        )
        """,

        (

            created_at,
            asset,
            market,
            signal,
            entry_price,
            exit_price,
            quantity,
            gross_pnl,
            cost,
            pnl,
            result,
            lesson,

        ),

    )

    conn.commit()
    conn.close()


def load_memory():
     
    
    conn = get_connection()

    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute("""

        SELECT *

        FROM memory

        ORDER BY id ASC

    """)

    rows = [dict(r) for r in cur.fetchall()]

    conn.close()

    return rows