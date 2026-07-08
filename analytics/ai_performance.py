"""
AI Performance Engine
Version 0.1
"""


def calculate_ai_performance(trades):

    result = {

        "accuracy": 0,

        "average_profit": 0,

        "best_trade": None,

        "worst_trade": None,

        "wins": 0,

        "losses": 0,

    }

    closed = [

        t

        for t in trades

        if t["status"] == "CLOSED"

    ]

    if not closed:

        return result

    total_profit = 0

    best = None

    worst = None

    for trade in closed:

        profit = trade.get(

            "profit_percent",

            0,

        )

        total_profit += profit

        if profit >= 0:

            result["wins"] += 1

        else:

            result["losses"] += 1

        if best is None:

            best = trade

        elif profit > best["profit_percent"]:

            best = trade

        if worst is None:

            worst = trade

        elif profit < worst["profit_percent"]:

            worst = trade

    result["accuracy"] = round(

        result["wins"]

        * 100

        / len(closed),

        2,

    )

    result["average_profit"] = round(

        total_profit

        / len(closed),

        2,

    )

    result["best_trade"] = best

    result["worst_trade"] = worst

    return result