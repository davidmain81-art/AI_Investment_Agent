"""
Close Trade
Version 0.8
"""

import sqlite3
from datetime import datetime

DB_NAME = "investment_agent.db"


def close_trade(
    trade_id,
    exit_price,
    exit_reason,
):

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM trades

        WHERE id=?
        """,
        (trade_id,),
    )

    trade = cursor.fetchone()

    if trade is None:

        conn.close()

        return None

    signal = trade["signal"]

    entry = trade["entry_price"]

    if signal == "BUY":

        pnl = round(
            (exit_price - entry)
            / entry
            * 100,
            2,
        )

    else:

        pnl = round(
            (entry - exit_price)
            / entry
            * 100,
            2,
        )
    if pnl > 0:
        result = "WIN"
    elif pnl < 0:
        result = "LOSS"

    else:
        result = "BREAKEVEN"


    cursor.execute(
        """
        UPDATE trades

        SET

            status='CLOSED',

            exit_price=?,

            closed_at=?,

            pnl=?,

            exit_reason=?

        WHERE id=?
        """,
        (
            exit_price,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            pnl,
            exit_reason,
            trade_id,
        ),
    )

    conn.commit()

    conn.close()

    print("CLOSE TRADE RESULT:")
    print(result, pnl)

    return {

        "id": trade["id"],

        "asset": trade["asset"],

        "market": "CRYPTO",

        "signal": trade["signal"],

        "entry_price": trade["entry_price"],

        "exit_price": exit_price,

        "quantity": 1,

        "gross_pnl": pnl,

        "pnl": pnl,

        "result": result,

        "confidence": trade["confidence"],

        "status": "CLOSED",

        "exit_reason": exit_reason,

    }