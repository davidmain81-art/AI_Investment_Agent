import csv
import os
from datetime import datetime

LOG_FILE = "logs/market_data.csv"


def save_market_data(prices):

    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Date",
                "BTC",
                "ETH",
                "BNB",
                "SOL",
                "XRP",
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            prices["BTC"],
            prices["ETH"],
            prices["BNB"],
            prices["SOL"],
            prices["XRP"],
        ])