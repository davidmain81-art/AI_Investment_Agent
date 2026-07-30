import requests

url = "https://api.binance.com/api/v3/ping"

try:
    r = requests.get(url, timeout=10)

    print("Status Code:", r.status_code)
    print("Response:", r.text)

except Exception as e:
    print(type(e))
    print(e)