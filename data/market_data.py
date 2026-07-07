from datetime import datetime


def get_market_status():
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Market Data System Ready"
    }