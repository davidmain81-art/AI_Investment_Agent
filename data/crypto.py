from services.api_client import APIClient


def get_crypto_prices():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum,binancecoin,solana,ripple",
        "vs_currencies": "usd"
    }

    data = APIClient.get(url, params)

    return {
        "BTC": data["bitcoin"]["usd"],
        "ETH": data["ethereum"]["usd"],
        "BNB": data["binancecoin"]["usd"],
        "SOL": data["solana"]["usd"],
        "XRP": data["ripple"]["usd"],
    }