from database.database import get_connection


def show_history(limit=20):
    """
    Display the latest saved market history.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            created_at,
            btc,
            crypto_score,
            iran_score,
            crypto_signal,
            iran_signal,
            winner
        FROM market_history
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    )

    rows = cursor.fetchall()

    connection.close()

    print("=" * 80)
    print("AI INVESTMENT HISTORY")
    print("=" * 80)

    if not rows:
        print("No history found.")
        return

    for row in rows:

        print(f"Time          : {row[0]}")
        print(f"BTC           : {row[1]:,.2f}")
        print(f"Crypto Score  : {row[2]}")
        print(f"Iran Score    : {row[3]}")
        print(f"Crypto Signal : {row[4]}")
        print(f"Iran Signal   : {row[5]}")
        print(f"Winner        : {row[6]}")
        print("-" * 80)


if __name__ == "__main__":
    show_history()