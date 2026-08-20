from engine.services.backtest_service import BacktestService


def test_backtest_service_summary():

    result = BacktestService().summary()

    assert isinstance(result, dict)

    assert "trades" in result
    assert "wins" in result
    assert "losses" in result
    assert "win_rate" in result
    assert "total_pnl" in result
    assert "average_profit" in result
    assert "average_loss" in result
    assert "profit_factor" in result
    assert "max_profit" in result
    assert "max_loss" in result