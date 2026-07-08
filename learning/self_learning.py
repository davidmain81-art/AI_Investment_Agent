"""
Self Learning Engine
Version 0.1
"""


from learning.weights import normalize


def update_weights(

    weights,

    trade,

):

    pnl = trade.get(

        "profit_percent",

        0,

    )

    signal = trade.get(

        "signal",

        "",

    )

    if pnl > 0:

        weights["trend"] += 2

        weights["volume"] += 1

        weights["confidence"] += 1

    else:

        weights["risk"] += 2

        weights["momentum"] -= 1

        weights["confidence"] -= 1

    if signal.startswith("SELL"):

        weights["risk"] += 1

    for key in weights:

        if weights[key] < 5:

            weights[key] = 5

    return normalize(weights)