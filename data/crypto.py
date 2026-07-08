from services.api_client import APIClient


def get_crypto_prices():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum,binancecoin,solana,ripple",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    data = APIClient.get(url, params)

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