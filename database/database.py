import sqlite3

DATABASE_NAME = "investment_agent.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS market_history(

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
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TEXT,

        asset TEXT,

        prediction TEXT,

        entry_price REAL,

        confidence REAL

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_results(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        prediction_id INTEGER,

        exit_price REAL,

        pnl REAL,

        success INTEGER

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TEXT,

        asset TEXT,

        signal TEXT,

        entry_price REAL,

        stop_loss REAL,

        take_profit REAL,

        confidence REAL,

        status TEXT
    )
    """)

    connection.commit()
    connection.close()