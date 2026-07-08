def calculate_market_score(prices):
    """
    Calculate overall market score
    using all tracked cryptocurrencies.
    """

    score = 50

    total_change = 0

    for coin in prices.values():
        total_change += coin["change"]

    average_change = total_change / len(prices)

    if average_change >= 5:
        score += 35

    elif average_change >= 3:
        score += 25

    elif average_change >= 1:
        score += 15

    elif average_change >= 0:
        score += 5

    elif average_change > -2:
        score -= 10

    elif average_change > -5:
        score -= 20

    else:
        score -= 35

    score = max(0, min(score, 100))

    return score