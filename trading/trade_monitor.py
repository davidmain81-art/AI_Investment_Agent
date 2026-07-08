from database.trades import close_trade
from database.predictions import save_prediction_result
from database.database import get_connection


def get_open_trades():
    """
    Return all open trades.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            confidence,
            status

        FROM trades

        WHERE status='OPEN'
    """)

    rows = cursor.fetchall()

    connection.close()

    trades = []

    for row in rows:

        trades.append({

            "id": row[0],
            "asset": row[1],
            "signal": row[2],
            "entry": row[3],
            "stop_loss": row[4],
            "take_profit": row[5],
            "confidence": row[6],
            "status": row[7],

        })

    return trades


def check_trade(trade, current_price):
    """
    Check if trade should be closed.
    """

    signal = trade["signal"]

    if "BUY" in signal:

        if current_price <= trade["stop_loss"]:

            return "LOSS"

        if current_price >= trade["take_profit"]:

            return "WIN"

    elif "SELL" in signal:

        if current_price >= trade["stop_loss"]:

            return "LOSS"

        if current_price <= trade["take_profit"]:

            return "WIN"

    return None


def calculate_pnl(trade, exit_price):

    if "BUY" in trade["signal"]:

        return (
            (exit_price - trade["entry"])
            / trade["entry"]
        ) * 100

    return (
        (trade["entry"] - exit_price)
        / trade["entry"]
    ) * 100


def process_trade(trade, current_price):
    """
    Process a single trade.
    """

    result = check_trade(
        trade,
        current_price,
    )

    if result is None:
        return None

    pnl = calculate_pnl(
        trade,
        current_price,
    )

    close_trade(trade["id"])

    save_prediction_result(
        prediction_id=trade["id"],
        exit_price=current_price,
        pnl=pnl,
        success=1 if pnl > 0 else 0,
    )

    return {

        "trade_id": trade["id"],

        "result": result,

        "pnl": round(pnl, 2),

    }