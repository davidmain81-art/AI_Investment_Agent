"""
AI Journal Writer
Version 0.9
"""

import os


class JournalWriter:

    def __init__(self):

        os.makedirs(
            "journal",
            exist_ok=True,
        )

    def write(
        self,
        trade,
        lesson,
    ):

        filename = (
            f"journal/Trade_{trade['id']}.txt"
        )

        with open(

            filename,

            "w",

            encoding="utf-8",

        ) as file:

            file.write(

f"""Trade ID : {trade['id']}

Asset : {trade['asset']}

Signal : {trade['signal']}

Entry Price : {trade['entry_price']}

Exit Price : {trade['exit_price']}

PnL : {trade['pnl']} %

Status : {trade['status']}

Reason : {trade['exit_reason']}

==================================

AI Lesson

{lesson}

"""
            )