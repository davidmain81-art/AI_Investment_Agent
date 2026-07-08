from datetime import datetime

from config.settings import APP_NAME, VERSION, OWNER
from utils.formatter import format_price


def print_header():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Developer : {OWNER}")
    print(f"Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


def print_crypto(prices):
    print("\n📈 CRYPTO MARKET")
    print("-" * 50)

    for coin, data in prices.items():
        print(
            f"{coin:<5}: "
            f"{format_price(data['price'])} USD   "
            f"({data['change']:.2f}%)"
        )


def print_analysis(signal, risk):
    print("\n📊 MARKET ANALYSIS")
    print("-" * 50)
    print(f"Signal : {signal}")
    print(f"Risk   : {risk}")


def print_score(score):
    print("\n⭐ MARKET SCORE")
    print("-" * 50)
    print(f"Overall Score : {score}/100")


def print_risk(stop_loss, take_profit):
    print("\n🛡 RISK MANAGEMENT")
    print("-" * 50)
    print(f"Stop Loss  : {format_price(stop_loss)}")
    print(f"Take Profit: {format_price(take_profit)}")