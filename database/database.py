import sqlite3

DATABASE_NAME = "investment_agent.db"


def get_connection(database_name=None):

    if database_name is None:
        database_name = DATABASE_NAME

    return sqlite3.connect(database_name)


def add_column_if_not_exists(cursor, table, column, definition):

    cursor.execute(f"PRAGMA table_info({table})")

    columns = [c[1] for c in cursor.fetchall()]

    if column not in columns:

        cursor.execute(

            f"ALTER TABLE {table} ADD COLUMN {column} {definition}"

        )

        print(f"[Migration] {table}.{column} added.")


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    # ===================================================
    # Market History
    # ===================================================

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

    # ===================================================
    # Predictions
    # ===================================================

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

    # ===================================================
    # Prediction Results
    # ===================================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS prediction_results(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        prediction_id INTEGER,

        exit_price REAL,

        pnl REAL,

        success INTEGER

    )

    """)

    # ===================================================
    # Trades
    # ===================================================

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

    # ===================================================
    # AI Memory
    # ===================================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS ai_memory(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        asset TEXT,

        signal TEXT,

        confidence REAL,

        market_score REAL,

        risk TEXT,

        pnl REAL,

        result TEXT

    )

    """)
# ===================================================
# Trade Features
# ===================================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS trade_features(

        trade_id INTEGER PRIMARY KEY,

        created_at TEXT,

        asset TEXT,

        signal TEXT,

        entry REAL,

        ai_score REAL,

        confidence REAL,

        risk TEXT,

        market_score REAL,

        learning REAL,

        optimizer REAL,

        pattern_score REAL,

        position_size REAL,

        stop_loss REAL,

        take_profit REAL,

        rsi REAL,

        mfi REAL,

        macd REAL,

        macd_signal REAL,

        ema20 REAL,

        ema50 REAL,

        ema200 REAL,

        atr REAL,

        adx REAL,

        obv REAL

    )

    """)
    # ===================================================
    # Auto Migration
    # ===================================================

    add_column_if_not_exists(
        cursor,
        "trades",
        "prediction_id",
        "INTEGER",
    )

    add_column_if_not_exists(
        cursor,
        "trades",
        "exit_price",
        "REAL",
    )

    add_column_if_not_exists(
        cursor,
        "trades",
        "closed_at",
        "TEXT",
    )

    add_column_if_not_exists(
        cursor,
        "trades",
        "pnl",
        "REAL",
    )

    add_column_if_not_exists(
        cursor,
        "trades",
        "exit_reason",
        "TEXT",
    )

    add_column_if_not_exists(
        cursor,
        "trades",
        "quantity",
        "REAL DEFAULT 1",
    )

    connection.commit()

    connection.close()