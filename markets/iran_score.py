def calculate_iran_score(market):
    """
    Calculate Iran market score.
    """

    score = 50

    avg_change = (
        market["gold18"]["change"]
        + market["usd"]["change"]
        + market["coin"]["change"]
    ) / 3

    if avg_change >= 3:
        score += 30

    elif avg_change >= 1:
        score += 15

    elif avg_change >= 0:
        score += 5

    elif avg_change > -2:
        score -= 10

    else:
        score -= 25

    score = max(0, min(score, 100))

    return score