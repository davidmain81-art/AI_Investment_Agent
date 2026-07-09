from pathlib import Path
from datetime import datetime


JOURNAL_DIR = Path("journal")

JOURNAL_DIR.mkdir(exist_ok=True)


def save_journal(

    prices,

    decision,

    iran_decision,

    global_result,

    stop_loss,

    take_profit,

):

    today = datetime.now().strftime(

        "%Y-%m-%d"

    )

    filename = JOURNAL_DIR / f"{today}.txt"

    btc = prices["BTC"]["price"]

    with open(

        filename,

        "w",

        encoding="utf-8",

    ) as file:

        file.write("=" * 45 + "\n")

        file.write("AI DAILY JOURNAL\n")

        file.write("=" * 45 + "\n\n")

        file.write(f"Date : {today}\n\n")

        file.write("CRYPTO\n")

        file.write(

            f"Signal : {decision['recommendation']}\n"

        )

        file.write(

            f"Confidence : {decision['confidence']}%\n\n"

        )

        file.write("IRAN\n")

        file.write(

            f"Signal : {iran_decision['signal']}\n"

        )

        file.write(

            f"Confidence : {iran_decision['confidence']}%\n\n"

        )

        file.write("GLOBAL\n")

        file.write(

            f"Best Market : {global_result['market']}\n"

        )

        file.write(

            f"Reason : {global_result['reason']}\n\n"

        )

        file.write("BTC\n")

        file.write(

            f"Price : {btc}\n"

        )

        file.write(

            f"Stop Loss : {stop_loss:.2f}\n"

        )

        file.write(

            f"Take Profit : {take_profit:.2f}\n\n"

        )

        file.write("Reasons\n")

        for reason in decision["reasons"]:

            file.write(

                f"- {reason}\n"

            )