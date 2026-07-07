from config.settings import APP_NAME
from config.settings import VERSION
from config.settings import OWNER

from data.crypto import get_crypto_prices

from analysis.market_analysis import analyze_market

from risk.risk_manager import (
    calculate_stop_loss,
    calculate_take_profit,
)


def print_header():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Developer : {OWNER}")
    print("=" * 50)


def print_crypto(prices):
    print("\nCRYPTO MARKET")
    print("-" * 50)

    for coin, price in prices.items():
        print(f"{coin:<5}: {price} USD")


def print_analysis(signal, risk):
    print("\nMARKET ANALYSIS")
    print("-" * 50)
    print(f"Signal : {signal}")
    print(f"Risk   : {risk}")


def print_risk(stop_loss, take_profit):
    print("\nRISK MANAGEMENT")
    print("-" * 50)
    print(f"Stop Loss  : {stop_loss}")
    print(f"Take Profit: {take_profit}")


def main():

    prices = get_crypto_prices()

    btc_price = prices["BTC"]

    signal, risk = analyze_market(btc_price)

    stop_loss = calculate_stop_loss(btc_price)

    take_profit = calculate_take_profit(btc_price)

    print_header()

    print_crypto(prices)

    print_analysis(signal, risk)

    print_risk(stop_loss, take_profit)


if __name__ == "__main__":
    main()