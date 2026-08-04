import sqlite3
from pathlib import Path

DB_PATH = Path("database/feature_store.db")


class FeatureStore:

    def __init__(self):

        self.conn = sqlite3.connect(DB_PATH)
        self.create_table()

    def create_table(self):

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS feature_store(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            asset TEXT,

            signal TEXT,

            entry REAL,

            exit REAL,

            pnl REAL,

            result TEXT,

            ai_score REAL,

            confidence REAL,

            risk TEXT,

            market_score REAL,

            learning REAL,

            optimizer REAL,

            position_size REAL,

            stop_loss REAL,

            take_profit REAL,

            rsi REAL,

            mfi REAL,

            macd REAL,

            ema20 REAL,

            ema50 REAL,

            ema200 REAL,

            atr REAL,

            adx REAL,

            obv REAL,

            vwap REAL,

            volume REAL,

            spread REAL,

            volatility REAL,

            trend TEXT,

            funding_rate REAL,

            open_interest REAL,

            fear_greed REAL,

            news_score REAL

        )
        """)

        self.conn.commit()

    def save(self, data):

        columns = ",".join(data.keys())

        placeholders = ",".join(["?"] * len(data))

        values = list(data.values())

        self.conn.execute(
            f"""
            INSERT INTO feature_store
            ({columns})
            VALUES
            ({placeholders})
            """,
            values,
        )

        self.conn.commit()

    def close(self):

        self.conn.close()