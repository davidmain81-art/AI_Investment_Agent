"""
Iran Stock Analyzer
"""


def analyze_stock_market(data):

    score = 50

    reasons = []

    if data["index"]["change"] > 0:

        score += 10

        reasons.append(
            "TEDPIX is positive."
        )

    else:

        score -= 10

        reasons.append(
            "TEDPIX is negative."
        )

    if data["equal_weight"]["change"] > 0:

        score += 10

        reasons.append(
            "Equal Weight is positive."
        )

    if data["real_money"]["value"] > 0:

        score += 15

        reasons.append(
            "Real money entered market."
        )

    if data["buy_queue"] > data["sell_queue"]:

        score += 10

        reasons.append(
            "Buy queues dominate."
        )

    if data["trade_value"]["value"] > 15000:

        score += 10

        reasons.append(
            "Liquidity is strong."
        )

    score = max(
        0,
        min(
            100,
            score,
        ),
    )

    return {

        "score": score,

        "reasons": reasons,

    }