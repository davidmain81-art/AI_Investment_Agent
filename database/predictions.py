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
        INSERT INTO predictions(

            created_at,
            asset,
            prediction,
            entry_price,
            confidence

        )

        VALUES(?,?,?,?,?)
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


def get_prediction(
    prediction_id,
):
    """
    Return prediction by id.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            id,
            created_at,
            asset,
            prediction,
            entry_price,
            confidence

        FROM predictions

        WHERE id=?
        """,
        (
            prediction_id,
        ),
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return {

        "id": row[0],
        "created_at": row[1],
        "asset": row[2],
        "prediction": row[3],
        "entry_price": row[4],
        "confidence": row[5],

    }


def save_prediction_result(
    prediction_id,
    exit_price,
    pnl,
    success,
):
    """
    Save prediction result.
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


def get_prediction_results():
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

        ORDER BY prediction_id
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows