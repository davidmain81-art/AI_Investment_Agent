"""
Trade Statistics
Version 0.1
"""


def calculate_trade_statistics(trades):

    stats = {

        "total": 0,

        "open": 0,

        "closed": 0,

        "wins": 0,

        "losses": 0,

        "win_rate": 0,

    }

    stats["total"] = len(trades)

    for trade in trades:

        if trade["status"] == "OPEN":

            stats["open"] += 1

            continue

        stats["closed"] += 1

        pnl = trade.get("profit_percent", 0)

        if pnl >= 0:

            stats["wins"] += 1

        else:

            stats["losses"] += 1

    if stats["closed"]:

        stats["win_rate"] = round(

            stats["wins"] * 100 /

            stats["closed"],

            2,

        )

    return stats