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


def print_decision(decision):

    print("\n🤖 AI INVESTMENT DECISION")
    print("-" * 50)

    print(f"Recommendation : {decision['recommendation']}")
    print(f"Confidence     : {decision['confidence']}%")

    print("\nReasons")

    for reason in decision["reasons"]:
        print(f"✓ {reason}")

    print("\nSuggested Position")
    print(decision["position"])

    print("\nHolding Time")
    print(decision["holding"])


def print_portfolio(portfolio):

    print("\n💼 PORTFOLIO ADVISOR")
    print("-" * 50)

    print(
        f"Capital : {portfolio['capital']:,} "
        f"{portfolio['currency']}"
    )

    for asset, info in portfolio["portfolio"].items():

        print(
            f"{asset:<5}"
            f"{info['percent']:>4}%   "
            f"{info['amount']:,.0f} "
            f"{portfolio['currency']}"
        )


def print_iran_market(market, score, decision):

    print("\n🇮🇷 IRAN MARKET")
    print("-" * 50)

    print(
        f"Gold 18K : {market['gold18']['price']:,} IRR"
        f"   ({market['gold18']['change']:+.2f}%)"
    )

    print(
        f"USD      : {market['usd']['price']:,} IRR"
        f"   ({market['usd']['change']:+.2f}%)"
    )

    print(
        f"Coin     : {market['coin']['price']:,} IRR"
        f"   ({market['coin']['change']:+.2f}%)"
    )

    print()

    print(f"Market Score : {score}/100")
    print(f"Signal       : {decision['signal']}")
    print(f"Confidence   : {decision['confidence']}%")


def print_global_recommendation(result):

    print("\n🌍 GLOBAL AI RECOMMENDATION")
    print("-" * 50)

    print(f"Best Market : {result['market']}")
    print(f"Signal      : {result['signal']}")
    print(f"Confidence  : {result['confidence']}%")
    print(f"Final Score : {result['final_score']}")

    print()

    print(f"Crypto Score : {result['crypto_score']}")
    print(f"Iran Score   : {result['iran_score']}")
    print(f"Difference   : {result['difference']}")

    print("\nReason")
    print(result["reason"])


def print_allocations(allocations):

    print("\n💰 CAPITAL ALLOCATION")
    print("-" * 50)

    for item in allocations:

        print(
            f"{item['market']:<15}"
            f"{item['allocation']:>6}%"
            f"   {item['signal']}"
        )


def print_risk(stop_loss, take_profit):

    print("\n🛡 RISK MANAGEMENT")
    print("-" * 50)

    print(f"Stop Loss  : {format_price(stop_loss)}")
    print(f"Take Profit: {format_price(take_profit)}")