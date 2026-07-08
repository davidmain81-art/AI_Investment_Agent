from database.database import get_connection


def calculate_accuracy():
    """
    Calculate simple AI performance statistics.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            crypto_signal,
            winner
        FROM market_history
        """
    )

    rows = cursor.fetchall()

    connection.close()

    total = len(rows)

    if total == 0:

        return {
            "total": 0,
            "correct": 0,
            "accuracy": 0,
        }

    correct = 0

    for signal, winner in rows:

        if signal.startswith("BUY") and winner == "CRYPTO 🌍":
            correct += 1

        elif signal.startswith("SELL") and winner == "IRAN 🇮🇷":
            correct += 1

        elif signal.startswith("HOLD") and winner == "BOTH":
            correct += 1

    accuracy = round(correct / total * 100, 2)

    return {
        "total": total,
        "correct": correct,
        "accuracy": accuracy,
    }


if __name__ == "__main__":

    result = calculate_accuracy()

    print("=" * 50)
    print("AI BACKTEST")
    print("=" * 50)

    print(f"Total Decisions : {result['total']}")
    print(f"Correct         : {result['correct']}")
    print(f"Accuracy        : {result['accuracy']}%")