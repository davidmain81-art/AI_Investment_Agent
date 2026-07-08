from database.database import get_connection


def get_open_trades():
    """
    Return all open trades.
    """

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

            status

        FROM trades

        WHERE status='OPEN'
        """
    )

    rows = cursor.fetchall()

    connection.close()

    trades = []

    for row in rows:

        trades.append({

            "id": row[0],

            "asset": row[1],

            "signal": row[2],

            "entry": row[3],

            "stop_loss": row[4],

            "take_profit": row[5],

            "confidence": row[6],

            "status": row[7],

        })

    return trades