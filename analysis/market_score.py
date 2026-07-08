def calculate_market_score(prices):
    """
    Calculate a simple market score based on BTC and ETH 24h change.
    """

    score = 50

    btc_change = prices["BTC"]["change"]
    eth_change = prices["ETH"]["change"]

    if btc_change > 0:
        score += 10
    else:
        score -= 10

    if eth_change > 0:
        score += 5
    else:
        score -= 5

    return max(0, min(score, 100))