from backtest.performance import PerformanceAnalyzer


def test_performance_analyzer():

    trades = [

        {
            "pnl": 100
        },

        {
            "pnl": 200
        },

        {
            "pnl": -50
        },

        {
            "pnl": -25
        },

    ]

    result = PerformanceAnalyzer().calculate(trades)

    assert result["trades"] == 4

    assert result["wins"] == 2

    assert result["losses"] == 2

    assert result["win_rate"] == 50.0

    assert result["total_pnl"] == 225

    assert result["average_profit"] == 150

    assert result["average_loss"] == 37.5

    assert result["profit_factor"] == 4.0

    assert result["max_profit"] == 200

    assert result["max_loss"] == 50