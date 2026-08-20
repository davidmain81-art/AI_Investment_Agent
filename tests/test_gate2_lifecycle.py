import sqlite3

from database import close_trade as close_trade_module


def create_test_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    conn.execute("""
        CREATE TABLE trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset TEXT,
            signal TEXT,
            entry_price REAL,
            stop_loss REAL,
            take_profit REAL,
            quantity REAL,
            confidence REAL,
            prediction_id INTEGER,
            status TEXT,
            exit_price REAL,
            closed_at TEXT,
            pnl REAL,
            exit_reason TEXT
        )
    """)

    conn.commit()

    return conn


def insert_open_trade(
    conn,
    asset,
    signal,
    entry_price,
    quantity,
    stop_loss,
    take_profit,
):
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO trades (
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            quantity,
            confidence,
            prediction_id,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            quantity,
            80,
            None,
            "OPEN",
        ),
    )

    conn.commit()

    return cursor.lastrowid


def test_gate2_buy_take_profit():
    conn = create_test_db()

    trade_id = insert_open_trade(
        conn=conn,
        asset="TEST_GATE2_WIN",
        signal="BUY",
        entry_price=100.0,
        quantity=1.0,
        stop_loss=97.0,
        take_profit=110.0,
    )

    original_get_connection = close_trade_module.get_connection

    try:
        close_trade_module.get_connection = lambda: conn

        result = close_trade_module.close_trade(
            trade_id=trade_id,
            exit_price=110.0,
            exit_reason="TEST_TAKE_PROFIT",
        )

    finally:
        close_trade_module.get_connection = original_get_connection

    assert result is not None
    assert result["id"] == trade_id
    assert result["status"] == "CLOSED"
    assert result["entry_price"] == 100.0
    assert result["exit_price"] == 110.0
    assert result["quantity"] == 1.0
    assert result["gross_pnl"] == 10.0
    assert result["pnl"] == 10.0
    assert result["pnl_percent"] == 10.0
    assert result["result"] == "WIN"

    row = conn.execute(
        """
        SELECT
            status,
            exit_price,
            pnl,
            exit_reason
        FROM trades
        WHERE id=?
        """,
        (trade_id,),
    ).fetchone()

    assert row["status"] == "CLOSED"
    assert row["exit_price"] == 110.0
    assert row["pnl"] == 10.0
    assert row["exit_reason"] == "TEST_TAKE_PROFIT"

    conn.close()


def test_gate2_buy_stop_loss():
    conn = create_test_db()

    trade_id = insert_open_trade(
        conn=conn,
        asset="TEST_GATE2_LOSS",
        signal="BUY",
        entry_price=100.0,
        quantity=1.0,
        stop_loss=97.0,
        take_profit=110.0,
    )

    original_get_connection = close_trade_module.get_connection

    try:
        close_trade_module.get_connection = lambda: conn

        result = close_trade_module.close_trade(
            trade_id=trade_id,
            exit_price=97.0,
            exit_reason="TEST_STOP_LOSS",
        )

    finally:
        close_trade_module.get_connection = original_get_connection

    assert result is not None
    assert result["id"] == trade_id
    assert result["status"] == "CLOSED"
    assert result["entry_price"] == 100.0
    assert result["exit_price"] == 97.0
    assert result["quantity"] == 1.0
    assert result["gross_pnl"] == -3.0
    assert result["pnl"] == -3.0
    assert result["pnl_percent"] == -3.0
    assert result["result"] == "LOSS"

    row = conn.execute(
        """
        SELECT
            status,
            exit_price,
            pnl,
            exit_reason
        FROM trades
        WHERE id=?
        """,
        (trade_id,),
    ).fetchone()

    assert row["status"] == "CLOSED"
    assert row["exit_price"] == 97.0
    assert row["pnl"] == -3.0
    assert row["exit_reason"] == "TEST_STOP_LOSS"

    conn.close()