def allocate_assets(decision):
    """
    Allocate portfolio based on
    recommendation and confidence.
    """

    signal = decision["recommendation"]
    confidence = decision["confidence"]

    if signal.startswith("SELL"):

        return {
            "BTC": 0,
            "ETH": 0,
            "USDT": 100,
        }

    if signal.startswith("HOLD"):

        return {
            "BTC": 20,
            "ETH": 10,
            "USDT": 70,
        }

    if confidence >= 90:

        return {
            "BTC": 60,
            "ETH": 30,
            "USDT": 10,
        }

    elif confidence >= 75:

        return {
            "BTC": 50,
            "ETH": 25,
            "USDT": 25,
        }

    elif confidence >= 60:

        return {
            "BTC": 40,
            "ETH": 20,
            "USDT": 40,
        }

    else:

        return {
            "BTC": 30,
            "ETH": 10,
            "USDT": 60,
        }