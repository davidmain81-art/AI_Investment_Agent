import sqlite3

from engine.trade_pipeline import TradePipeline
from memory.memory_engine import MemoryEngine


def test_trade_pipeline_memory_and_feature_store():

    trade_id = 999

    # ==========================================
    # Prepare Entry Features
    # ==========================================

    connection = sqlite3.connect("investment_agent.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM trade_features
        WHERE trade_id=?
        """,
        (trade_id,),
    )

    cursor.execute(
        """
        INSERT INTO trade_features(

            trade_id,
            created_at,
            asset,
            signal,
            entry,
            ai_score,
            confidence,
            risk,
            market_score,
            learning,
            optimizer,
            pattern_score,
            position_size,
            stop_loss,
            take_profit,
            rsi,
            mfi,
            macd,
            macd_signal,
            ema20,
            ema50,
            ema200,
            atr,
            adx,
            obv

        )

        VALUES(
            ?, datetime('now'),
            ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """,
        (
            trade_id,

            "BTC",
            "BUY",
            64000,

            80,
            80,
            "LOW",
            20,
            0,
            5,
            70,
            10,
            62000,
            70000,

            55,
            55,
            100,
            90,
            64000,
            63500,
            62000,
            500,
            25,
            1000000,
        ),
    )

    connection.commit()
    connection.close()

    # ==========================================
    # Closed Trade
    # ==========================================

    trade = {

        "id": trade_id,

        "asset": "BTC",

        "market": "CRYPTO",

        "signal": "BUY",

        "entry_price": 64000,

        "exit_price": 65000,

        "quantity": 1,

        "gross_pnl": 1000,

        "pnl": 1000,

        "pnl_percent": 1.56,

        "result": "WIN",

        "confidence": 80,

        "status": "CLOSED",

        "exit_reason": "TEST",
    }

    # ==========================================
    # Process Pipeline
    # ==========================================

    pipeline = TradePipeline()

    pipeline.process(trade)

    # ==========================================
    # Verify FeatureStore
    # ==========================================

    connection = sqlite3.connect(
        "database/feature_store.db"
    )

    cursor = connection.cursor()

    row = cursor.execute(
        """
        SELECT
            asset,
            signal,
            entry,
            exit,
            pnl,
            result,
            ai_score,
            confidence,
            pattern_score,
            rsi,
            mfi,
            macd,
            ema20,
            ema50,
            ema200,
            atr,
            adx,
            obv

        FROM feature_store

        WHERE asset=?
        AND signal=?
        AND entry=?

        ORDER BY rowid DESC

        LIMIT 1
        """,
        (
            "BTC",
            "BUY",
            64000,
        ),
    ).fetchone()

    connection.close()

    # ==========================================
    # Assertions
    # ==========================================

    assert row is not None

    assert row[0] == "BTC"
    assert row[1] == "BUY"

    assert row[2] == 64000
    assert row[3] == 65000

    assert row[4] == 1000
    assert row[5] == "WIN"

    assert row[6] == 80
    assert row[7] == 80
    assert row[8] == 70

    assert row[9] == 55
    assert row[10] == 55
    assert row[11] == 100

    assert row[12] == 64000
    assert row[13] == 63500
    assert row[14] == 62000

    assert row[15] == 500
    assert row[16] == 25
    assert row[17] == 1000000

    # ==========================================
    # Verify Memory
    # ==========================================

    memory = MemoryEngine()

    stats = memory.statistics()

    print(stats)

    assert stats["total"] >= 1

    # ==========================================
    # Cleanup
    # ==========================================

    connection = sqlite3.connect(
        "investment_agent.db"
    )

    connection.execute(
        """
        DELETE FROM trade_features
        WHERE trade_id=?
        """,
        (trade_id,),
    )

    connection.commit()
    connection.close()