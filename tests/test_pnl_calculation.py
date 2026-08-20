import sqlite3

import database.close_trade as close_trade_module


def create_test_database(tmp_path):

    db_path = tmp_path / "test_trades.db"

    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE trades(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            asset TEXT,

            signal TEXT,

            entry_price REAL,

            stop_loss REAL,

            take_profit REAL,

            confidence REAL,

            status TEXT,

            prediction_id INTEGER,

            exit_price REAL,

            closed_at TEXT,

            pnl REAL,

            exit_reason TEXT,

            quantity REAL

        )
        """
    )

    connection.commit()
    connection.close()

    return db_path


def insert_trade(
    db_path,
    signal,
    entry_price=100.0,
):

    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO trades(

            created_at,
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            confidence,
            status,
            quantity

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "2026-08-11 00:00:00",
            "TEST",
            signal,
            entry_price,
            90.0,
            110.0,
            80.0,
            "OPEN",
            1.0,
        ),
    )

    trade_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return trade_id


def test_buy_pnl(
    tmp_path,
    monkeypatch,
):

    db_path = create_test_database(tmp_path)

    monkeypatch.setattr(
        close_trade_module,
        "get_connection",
        lambda: sqlite3.connect(db_path),
    )

    trade_id = insert_trade(
        db_path,
        "BUY",
    )

    result = close_trade_module.close_trade(
        trade_id,
        110.0,
        "TAKE_PROFIT",
    )

    assert result["pnl"] == 10.0

    assert result["result"] == "WIN"


def test_sell_pnl(
    tmp_path,
    monkeypatch,
):

    db_path = create_test_database(tmp_path)

    monkeypatch.setattr(
        close_trade_module,
        "get_connection",
        lambda: sqlite3.connect(db_path),
    )

    trade_id = insert_trade(
        db_path,
        "SELL",
    )

    result = close_trade_module.close_trade(
        trade_id,
        90.0,
        "TAKE_PROFIT",
    )

    assert result["pnl"] == 10.0

    assert result["result"] == "WIN"


def test_strong_buy_pnl(
    tmp_path,
    monkeypatch,
):

    db_path = create_test_database(tmp_path)

    monkeypatch.setattr(
        close_trade_module,
        "get_connection",
        lambda: sqlite3.connect(db_path),
    )

    trade_id = insert_trade(
        db_path,
        "STRONG BUY",
    )

    result = close_trade_module.close_trade(
        trade_id,
        110.0,
        "TAKE_PROFIT",
    )

    assert result["pnl"] == 10.0

    assert result["result"] == "WIN"