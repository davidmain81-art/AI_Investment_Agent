from datetime import datetime

from database.database import get_connection


def save_market_history(
    prices,
    crypto_score,
    iran_score,
    crypto_signal,
    iran_signal,
    winner,
):
    """
    Save one execution of the AI Investment Agent.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO market_history (

            created_at,

            btc,
            eth,
            bnb,
            sol,
            xrp,

            crypto_score,
            iran_score,

            crypto_signal,
            iran_signal,

            winner

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            prices["BTC"]["price"],
            prices["ETH"]["price"],
            prices["BNB"]["price"],
            prices["SOL"]["price"],
            prices["XRP"]["price"],

            crypto_score,
            iran_score,

            crypto_signal,
            iran_signal,

            winner,
        ),
    )

    connection.commit()

    connection.close()