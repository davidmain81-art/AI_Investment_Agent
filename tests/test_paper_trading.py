from trading.paper_trading import PaperTrading


def test_paper_trading_buy():

    paper = PaperTrading()

    trade = paper.open_trade(
        asset="BTC",
        signal="BUY",
        entry_price=64000,
        quantity=1,
    )

    result = paper.close_trade(
        trade,
        65000,
    )

    assert result["status"] == "CLOSED"
    assert result["pnl"] == 1000


def test_paper_trading_sell():

    paper = PaperTrading()

    trade = paper.open_trade(
        asset="BTC",
        signal="SELL",
        entry_price=65000,
        quantity=1,
    )

    result = paper.close_trade(
        trade,
        64000,
    )

    assert result["status"] == "CLOSED"
    assert result["pnl"] == 1000