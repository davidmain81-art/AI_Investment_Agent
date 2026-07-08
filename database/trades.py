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
    """
    Save trade into database.
    """

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