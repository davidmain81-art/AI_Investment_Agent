from datetime import datetime

from database.database import get_connection


def save_trade(
    asset,
    signal,
    entry_price,
    stop_loss,
    take_profit,
    confidence,
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
            status

        )

        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            confidence,
            status,
        ),
    )

    trade_id = cursor.lastrowid

    connection.commit()

    connection.close()

    return trade_id


def close_trade(
    trade_id,
    status="CLOSED",
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE trades

        SET status=?

        WHERE id=?
        """,
        (
            status,
            trade_id,
        ),
    )

    connection.commit()

    connection.close()