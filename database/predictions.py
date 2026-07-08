from datetime import datetime

from database.database import get_connection


def save_prediction(
    asset,
    prediction,
    entry_price,
    confidence,
):
    """
    Save AI prediction.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO predictions (

            created_at,

            asset,

            prediction,

            entry_price,

            confidence

        )

        VALUES (?, ?, ?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            asset,
            prediction,
            entry_price,
            confidence,
        ),
    )

    prediction_id = cursor.lastrowid

    connection.commit()

    connection.close()

    return prediction_id