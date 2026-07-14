"""
Prediction Results
Version 0.6
"""

from database.database import get_connection


def save_prediction_result(
    prediction_id,
    exit_price,
    pnl,
    success,
):
    """
    Save prediction result after trade closes.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_results(

            prediction_id,

            exit_price,

            pnl,

            success

        )

        VALUES(?,?,?,?)
        """,
        (
            prediction_id,
            exit_price,
            pnl,
            success,
        ),
    )

    connection.commit()

    connection.close()


# ---------------------------------------------------------


def get_all_prediction_results():
    """
    Return all prediction results.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            prediction_id,

            exit_price,

            pnl,

            success

        FROM prediction_results

        ORDER BY id
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


# ---------------------------------------------------------


def get_prediction_statistics():
    """
    Return statistics.
    """

    rows = get_all_prediction_results()

    total = len(rows)

    wins = sum(
        row[3]
        for row in rows
    )

    losses = total - wins

    pnl = sum(
        row[2]
        for row in rows
    )

    if total == 0:

        win_rate = 0

    else:

        win_rate = round(
            wins / total * 100,
            2,
        )

    return {

        "trades": total,

        "wins": wins,

        "losses": losses,

        "win_rate": win_rate,

        "total_pnl": round(
            pnl,
            2,
        ),
    }