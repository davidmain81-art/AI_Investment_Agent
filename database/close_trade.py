"""
Close Trade
Version 0.9.2

Closes an existing trade and calculates:
- Gross PnL in money
- PnL percentage
- Result
"""

from datetime import datetime
import sqlite3

from database.database import get_connection


def close_trade(
    trade_id,
    exit_price,
    exit_reason,
):

    connection = get_connection()

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    # ==========================================
    # Get Trade
    # ==========================================

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

        return None



    # ==========================================
    # Prevent Double Close
    # ==========================================

    if trade["status"] != "OPEN":

        return None

    # ==========================================
    # Trade Data
    # ==========================================

    signal = trade["signal"]

    entry_price = float(
        trade["entry_price"]
    )

    exit_price = float(exit_price)

    quantity = float(
        trade["quantity"]
        if trade["quantity"] is not None
        else 1
    )

    # ==========================================
    # Calculate Gross PnL
    # ==========================================

    if "SELL" in signal:

        gross_pnl = (
            entry_price - exit_price
        ) * quantity

    else:

        gross_pnl = (
            exit_price - entry_price
        ) * quantity

    gross_pnl = round(
        gross_pnl,
        2,
    )

    # ==========================================
    # Calculate PnL Percentage
    # ==========================================

    if entry_price != 0:

        pnl_percent = round(
            (
                gross_pnl
                / (entry_price * quantity)
            ) * 100,
            2,
        )

    else:

        pnl_percent = 0

    # ==========================================
    # Result
    # ==========================================

    if gross_pnl > 0:

        result = "WIN"

    elif gross_pnl < 0:

        result = "LOSS"

    else:

        result = "BREAKEVEN"

    # ==========================================
    # Update Trade
    # ==========================================

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

        AND status='OPEN'
        """,
        (
            exit_price,

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            gross_pnl,

            exit_reason,

            trade_id,
        ),
    )

    connection.commit()

    # ==========================================
    # Read Closed Trade
    # ==========================================

    cursor.execute(
        """
        SELECT *

        FROM trades

        WHERE id=?
        """,
        (trade_id,),
    )

    closed_trade = cursor.fetchone()

    # ==========================================
    # Safety Check
    # ==========================================

    if closed_trade is None:

        return None

    # ==========================================
    # Result Output
    # ==========================================

    print("CLOSE TRADE RESULT:")
    print("Trade ID    :", closed_trade["id"])
    print("Result      :", result)
    print("Gross PnL   :", gross_pnl)
    print("PnL %       :", pnl_percent)
    print("Quantity    :", quantity)

    # ==========================================
    # Close Connection
    # ==========================================
    
    # Connection lifecycle is managed by caller.
    
    # ==========================================
    # Return
    # ==========================================

    return {

        "id": closed_trade["id"],

        "asset": closed_trade["asset"],

        "market": "CRYPTO",

        "signal": closed_trade["signal"],

        "entry_price": closed_trade["entry_price"],

        "exit_price": exit_price,

        "quantity": quantity,

        "gross_pnl": gross_pnl,

        "pnl": gross_pnl,

        "pnl_percent": pnl_percent,

        "result": result,

        "confidence": closed_trade["confidence"],

        "status": "CLOSED",

        "exit_reason": exit_reason,

    }