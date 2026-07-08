from ui.console import (
    print_header,
    print_crypto,
    print_analysis,
    print_score,
    print_risk,
)
from analysis.market_score import calculate_market_score
from ui.console import (
    print_header,
    print_crypto,
    print_analysis,
    print_risk,
)
from datetime import datetime

from config.settings import APP_NAME, VERSION, OWNER

from data.crypto import get_crypto_prices

from analysis.market_analysis import analyze_market

from risk.risk_manager import (
    calculate_stop_loss,
    calculate_take_profit,
)

from logs.data_logger import save_market_data


def print_header():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Developer : {OWNER}")
    print(f"Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


def print_crypto(prices):
    print("\nCRYPTO MARKET")
    print("-" * 50)

    for coin, data in prices.items():
        print(
            f"{coin:<5}: "
            f"{data['price']} USD   "
            f"({data['change']:.2f}%)"
        )


def print_analysis(signal, risk):
    print("\nMARKET ANALYSIS")
    print("-" * 50)
    print(f"Signal : {signal}")
    print(f"Risk   : {risk}")


def print_risk(stop_loss, take_profit):
    print("\nRISK MANAGEMENT")
    print("-" * 50)
    print(f"Stop Loss  : {stop_loss:.2f}")
    print(f"Take Profit: {take_profit:.2f}")


def main():

    prices = get_crypto_prices()

    save_market_data(prices)

    btc_price = prices["BTC"]["price"]

    signal, risk = analyze_market(btc_price)
    market_score = calculate_market_score(prices)

    stop_loss = calculate_stop_loss(btc_price)

    take_profit = calculate_take_profit(btc_price)

    print_header()

    print_crypto(prices)

    print_analysis(signal, risk)
    print_score(market_score)

    print_risk(stop_loss, take_profit)


if __name__ == "__main__":
    main()