"""
Prediction Results
Version 0.7
"""

from database.database import get_connection


def save_prediction_result(
    prediction_id,
    exit_price,
    pnl,
    success,
):
    """
    Save exactly one prediction result.

    Integrity rules:
    1. Prediction must exist.
    2. Prediction can have only one result.
    3. Invalid result must never be inserted.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        # ==========================================
        # Prediction existence check
        # ==========================================

        cursor.execute(
            """
            SELECT id
            FROM predictions
            WHERE id=?
            """,
            (
                prediction_id,
            ),
        )

        prediction = cursor.fetchone()

        if prediction is None:

            print(
                "PREDICTION RESULT BLOCKED: "
                f"Prediction {prediction_id} does not exist."
            )

            return False

        # ==========================================
        # Duplicate result protection
        # ==========================================

        cursor.execute(
            """
            SELECT id
            FROM prediction_results
            WHERE prediction_id=?
            LIMIT 1
            """,
            (
                prediction_id,
            ),
        )

        existing_result = cursor.fetchone()

        if existing_result is not None:

            print(
                "PREDICTION RESULT BLOCKED: "
                f"Prediction {prediction_id} already has a result."
            )

            return False

        # ==========================================
        # Validate values
        # ==========================================

        if exit_price is None:

            print(
                "PREDICTION RESULT BLOCKED: "
                "exit_price is None."
            )

            return False

        if pnl is None:

            print(
                "PREDICTION RESULT BLOCKED: "
                "pnl is None."
            )

            return False

        success = 1 if success else 0

        # ==========================================
        # Insert result
        # ==========================================

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

        return True

    except Exception:

        connection.rollback()

        raise

    finally:

        connection.close()


# ---------------------------------------------------------


def get_all_prediction_results():
    """
    Return all prediction results.
    """

    connection = get_connection()

    try:

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

        return rows

    finally:

        connection.close()


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