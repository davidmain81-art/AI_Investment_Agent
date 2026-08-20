"""
Trades Database
Version 0.9
"""

from datetime import datetime

from database.database import get_connection


# --------------------------------------------------------
# Save Trade Features
# --------------------------------------------------------

def save_trade_features(
    trade_id,
    asset,
    signal,
    entry_price,
    stop_loss,
    take_profit,
    decision,
):
    connection = get_connection()
    cursor = connection.cursor()

    indicators = decision.get("indicators", {})

    learning = decision.get("learning")

    if isinstance(learning, dict):
        learning = learning.get("experience")

    cursor.execute(
        """
        INSERT OR REPLACE INTO trade_features(

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
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
        )
        """,
        (
            trade_id,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            asset,
            signal,
            entry_price,

            decision.get("ai_score"),
            decision.get("confidence"),
            decision.get("risk"),
            decision.get("market_score"),

            learning,

            decision.get("optimizer_used"),
            decision.get("pattern_score"),

            decision.get("position_size"),

            stop_loss,
            take_profit,

            indicators.get("RSI"),
            indicators.get("MFI"),
            indicators.get("MACD"),
            indicators.get("MACD_SIGNAL"),

            indicators.get("EMA20"),
            indicators.get("EMA50"),
            indicators.get("EMA200"),

            indicators.get("ATR"),
            indicators.get("ADX"),
            indicators.get("OBV"),
        ),
    )

    connection.commit()
    connection.close()


# --------------------------------------------------------
# Save Trade
# --------------------------------------------------------

def save_trade(
    asset,
    signal,
    entry_price,
    stop_loss,
    take_profit,
    confidence,
    prediction_id=None,
    status="OPEN",
):

    connection = get_connection()
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
            prediction_id,
            status

        )

        VALUES(?,?,?,?,?,?,?,?,?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            confidence,
            prediction_id,
            status,
        ),
    )

    trade_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return trade_id


# --------------------------------------------------------
# Close Trade
# --------------------------------------------------------

def close_trade(
    trade_id,
    exit_price=None,
    pnl=None,
    exit_reason=None,
    status="CLOSED",
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE trades

        SET

            status=?,
            exit_price=?,
            pnl=?,
            exit_reason=?,
            closed_at=?

        WHERE id=?

        """,
        (
            status,
            exit_price,
            pnl,
            exit_reason,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            trade_id,
        ),
    )

    connection.commit()

    cursor.execute(
        """
        SELECT

            id,
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            exit_price,
            pnl,
            exit_reason,
            status

        FROM trades

        WHERE id=?

        """,
        (trade_id,),
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "asset": row[1],
        "signal": row[2],
        "entry_price": row[3],
        "stop_loss": row[4],
        "take_profit": row[5],
        "exit_price": row[6],
        "pnl": row[7],
        "exit_reason": row[8],
        "status": row[9],
    }


# --------------------------------------------------------
# Update Trade Result
# --------------------------------------------------------

def update_trade_result(
    trade_id,
    exit_price,
    pnl,
    exit_reason,
):

    close_trade(
        trade_id=trade_id,
        exit_price=exit_price,
        pnl=pnl,
        exit_reason=exit_reason,
    )


# --------------------------------------------------------
# Get Last Open Trade
# --------------------------------------------------------

def get_last_open_trade():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            id,
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            confidence,
            prediction_id,
            status

        FROM trades

        WHERE status='OPEN'

        ORDER BY id DESC

        LIMIT 1
        """
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "asset": row[1],
        "signal": row[2],
        "entry_price": row[3],
        "stop_loss": row[4],
        "take_profit": row[5],
        "confidence": row[6],
        "prediction_id": row[7],
        "status": row[8],
    }


# --------------------------------------------------------
# Get All Trades
# --------------------------------------------------------

def get_all_trades():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *

        FROM trades

        ORDER BY id
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows