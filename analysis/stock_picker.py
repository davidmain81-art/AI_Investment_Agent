"""
Iran Stock Picker

Ranks stocks based on a simple scoring model.
"""


def score_symbol(symbol):

    score = 50

    reasons = []

    if symbol["change"] > 0:

        score += 20

        reasons.append("Positive daily trend.")

    else:

        score -= 10

        reasons.append("Negative daily trend.")

    if symbol["volume"] > 700000000:

        score += 20

        reasons.append("High trading volume.")

    elif symbol["volume"] > 300000000:

        score += 10

        reasons.append("Good liquidity.")

    if symbol["change"] > 3:

        score += 10

        reasons.append("Strong momentum.")

    score = max(
        0,
        min(
            100,
            score,
        ),
    )

    return {

        "symbol": symbol["symbol"],

        "name": symbol["name"],

        "price": symbol["price"],

        "change": symbol["change"],

        "volume": symbol["volume"],

        "score": score,

        "reasons": reasons,

    }


def rank_symbols(stock_market):

    ranked = []

    for symbol in stock_market["symbols"]:

        ranked.append(

            score_symbol(symbol)

        )

    ranked.sort(

        key=lambda x: x["score"],

        reverse=True,

    )

    return ranked