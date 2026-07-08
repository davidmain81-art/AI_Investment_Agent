from logs.data_logger import save_market_data

from data.crypto import get_crypto_prices

from analysis.market_analysis import analyze_market
from analysis.market_score import calculate_market_score
from analysis.decision_engine import make_decision

from risk.risk_manager import (
    calculate_stop_loss,
    calculate_take_profit,
)

from ui.console import (
    print_header,
    print_crypto,
    print_analysis,
    print_score,
    print_decision,
    print_risk,
)


def main():

    prices = get_crypto_prices()

    save_market_data(prices)

    btc_price = prices["BTC"]["price"]

    signal, risk = analyze_market(btc_price)

    market_score = calculate_market_score(prices)

    decision = make_decision(
        signal,
        risk,
        market_score,
    )

    stop_loss = calculate_stop_loss(btc_price)

    take_profit = calculate_take_profit(btc_price)

    print_header()

    print_crypto(prices)

    print_analysis(signal, risk)

    print_score(market_score)

    print_decision(decision)

    print_risk(stop_loss, take_profit)


if __name__ == "__main__":
    main()