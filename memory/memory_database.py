import sqlite3

DATABASE = "investment_agent.db"


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

        signal TEXT,

        pnl REAL,

        result TEXT,

        lesson TEXT

    )

    """)

    conn.commit()
    conn.close()


def save_memory(

    asset,

    signal,

    pnl,

    result,

    lesson,

    created_at,

):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(

        """

        INSERT INTO memory(

            created_at,

            asset,

            signal,

            pnl,

            result,

            lesson

        )

        VALUES(

            ?,?,?,?,?,?

        )

        """,

        (

            created_at,

            asset,

            signal,

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