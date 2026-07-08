import sqlite3


DATABASE_NAME = "investment_agent.db"


def get_connection():
    """
    Create SQLite connection.
    """

    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    """
    Create required tables.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS market_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            btc REAL,
            eth REAL,
            bnb REAL,
            sol REAL,
            xrp REAL,

            crypto_score REAL,
            iran_score REAL,

            crypto_signal TEXT,
            iran_signal TEXT,

            winner TEXT

        )
        """
    )

    connection.commit()

    connection.close()