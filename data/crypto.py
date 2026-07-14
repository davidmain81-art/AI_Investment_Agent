"""
Crypto Market Provider
Version 0.7
"""

import requests

from logs.data_logger import (
    load_last_market_data,
)


URL = (
    "https://api.coingecko.com/api/v3/simple/price"
)


PARAMS = {
    "ids": "bitcoin,ethereum,binancecoin,solana,ripple",
    "vs_currencies": "usd",
    "include_24hr_change": "true",
}


def get_crypto_prices():
    """
    Return live crypto prices.
    Uses cached data if API fails.
    """

    try:

        response = requests.get(
            URL,
            params=PARAMS,
            timeout=15,
        )

        response.raise_for_status()

        data = response.json()

        return {
            "BTC": {
                "price": data["bitcoin"]["usd"],
                "change": data["bitcoin"]["usd_24h_change"],
            },
            "ETH": {
                "price": data["ethereum"]["usd"],
                "change": data["ethereum"]["usd_24h_change"],
            },
            "BNB": {
                "price": data["binancecoin"]["usd"],
                "change": data["binancecoin"]["usd_24h_change"],
            },
            "SOL": {
                "price": data["solana"]["usd"],
                "change": data["solana"]["usd_24h_change"],
            },
            "XRP": {
                "price": data["ripple"]["usd"],
                "change": data["ripple"]["usd_24h_change"],
            },
        }

    except Exception as error:

        print()
        print("❌ API Error:", error)

        cached = load_last_market_data()

        if cached:

            print("📦 Using cached market data.")
            return cached

        raise RuntimeError(
            "Unable to retrieve crypto prices and no cache is available."
        )