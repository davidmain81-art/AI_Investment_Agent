from backtest.backtest_engine import BacktestEngine


def test_backtest_engine_loads_closed_trades():

    results = BacktestEngine().load_results()

    assert isinstance(results, list)

    for trade in results:

        assert trade["id"] is not None

        assert trade["asset"] is not None

        assert trade["signal"] in [
            "BUY",
            "SELL",
            "STRONG BUY",
            "STRONG SELL",
        ]

        assert trade["entry_price"] is not None

        assert trade["exit_price"] is not None

        assert trade["pnl"] is not None

        assert trade["confidence"] is not None

        assert trade["exit_reason"] is not None