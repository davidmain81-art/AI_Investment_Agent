from trading.trade_lifecycle import TradeLifecycle


def test_take_profit_close():

    trade = {

        "id": 999,

        "asset": "BTC",

        "signal": "BUY",

        "entry_price": 64000,

        "take_profit": 65000,

        "stop_loss": 62000,

    }


    lifecycle = TradeLifecycle()


    result = lifecycle.evaluate(
        trade,
        65100
    )


    print(result)

    assert result == "TP"