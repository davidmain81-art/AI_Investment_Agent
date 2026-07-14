"""
Market Data Logger
Version 0.8
"""

import json
import os
from datetime import datetime

DATA_FILE = "logs/market_cache.json"


def save_market_data(prices):
    """
    Save latest market data.
    """

    os.makedirs("logs", exist_ok=True)

    data = {
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "prices": prices,
    }

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )


def load_last_market_data():
    """
    Load cached market data.
    """

    if not os.path.exists(DATA_FILE):
        return None

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        return data.get("prices")

    except Exception:

        return None


def get_last_update():
    """
    Return cache timestamp.
    """

    if not os.path.exists(DATA_FILE):
        return None

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        return data.get("updated_at")

    except Exception:

        return None