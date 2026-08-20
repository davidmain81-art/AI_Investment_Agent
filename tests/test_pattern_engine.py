import sqlite3
from pathlib import Path

from learning.pattern_engine import PatternEngine


TEST_DB = Path("database/test_feature_store.db")


def create_test_database():
    """
    Create isolated feature store database
    for PatternEngine tests.
    """

    if TEST_DB.exists():
        TEST_DB.unlink()

    conn = sqlite3.connect(TEST_DB)

    conn.execute("""
        CREATE TABLE feature_store(

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

            news_score REAL,

            pattern_score REAL,

            macd_signal REAL
        )
    """)

    rows = [

        (
            "BTCUSDT",
            "BUY",
            "WIN",
            32,
            60500,
            59000,
        ),

        (
            "BTCUSDT",
            "BUY",
            "WIN",
            35,
            60500,
            59000,
        ),

        (
            "BTCUSDT",
            "BUY",
            "WIN",
            35,
            60500,
            59000,
        ),

    ]

    for asset, signal, result, rsi, ema20, ema50 in rows:

        conn.execute(
            """
            INSERT INTO feature_store(

                asset,
                signal,
                result,
                rsi,
                ema20,
                ema50

            )

            VALUES(?,?,?,?,?,?)
            """,
            (
                asset,
                signal,
                result,
                rsi,
                ema20,
                ema50,
            ),
        )

    conn.commit()
    conn.close()


def test_pattern_engine(monkeypatch):

    create_test_database()

    # ------------------------------------------
    # Force PatternEngine to use test database
    # ------------------------------------------

    monkeypatch.setattr(
        "learning.pattern_engine.DB",
        str(TEST_DB),
    )

    engine = PatternEngine()

    result = engine.analyze()

    assert result is not None

    assert "pattern_score" in result

    assert "patterns" in result

    assert "RSI" in result["patterns"]

    assert "EMA" in result["patterns"]

    # ==========================================
    # Raw Pattern Statistics
    # ==========================================

    rsi = result["patterns"]["RSI"]
    ema = result["patterns"]["EMA"]

    assert rsi["trades"] == 3
    assert rsi["wins"] == 3
    assert rsi["win_rate"] == 100.0

    assert ema["trades"] == 3
    assert ema["wins"] == 3
    assert ema["win_rate"] == 100.0

    # ==========================================
    # Sample Size Adjustment
    #
    # 3 / 20 = 0.15
    #
    # 100 * 0.15 = 15
    # ==========================================

    assert result["pattern_score"] == 15.0

    engine.close()

    if TEST_DB.exists():
        TEST_DB.unlink()


def test_pattern_score_respects_current_market_context(
    monkeypatch
):

    create_test_database()

    # ------------------------------------------
    # Force PatternEngine to use test database
    # ------------------------------------------

    monkeypatch.setattr(
        "learning.pattern_engine.DB",
        str(TEST_DB),
    )

    engine = PatternEngine()

    # ==========================================
    # Current Market
    # ==========================================
    #
    # Current RSI = 55
    # Historical pattern = RSI < 40
    #
    # Current EMA20 < EMA50
    # Historical pattern = EMA20 > EMA50
    #
    # Neither historical pattern matches
    # the current market.
    # ==========================================

    result = engine.analyze(
        current_rsi=55,
        current_ema20=100,
        current_ema50=110,
    )

    assert result is not None

    assert "pattern_score" in result

    assert result["pattern_score"] == 0

    engine.close()

    if TEST_DB.exists():
        TEST_DB.unlink()