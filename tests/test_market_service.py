import pandas as pd

import engine.services.market_service as market_service


class FakeBinanceCandleProvider:

    def load(self):

        return pd.DataFrame({
            "close": [100, 101, 102],
        })


def fake_get_crypto_prices():

    return {
        "BTC": {
            "price": 100,
            "change": 2.0,
        },

        "ETH": {
            "price": 50,
            "change": 1.0,
        },
    }


def fake_save_market_data(prices):
    pass


def fake_analyze_market(prices, df):

    return (
        "BUY",
        "LOW",
        15,
        {
            "RSI": 40,
            "MFI": 50,
            "EMA20": 105,
            "EMA50": 100,
            "EMA200": 95,
            "ATR": 2,
            "MACD": 1,
            "MACD_SIGNAL": 0.5,
            "ADX": 25,
            "OBV": 1000,
            "trend": "UP",
        },
    )


def fake_calculate_market_score(prices):

    return 75


def test_market_service_separates_scores(monkeypatch):

    monkeypatch.setattr(
        market_service,
        "get_crypto_prices",
        fake_get_crypto_prices,
    )

    monkeypatch.setattr(
        market_service,
        "save_market_data",
        fake_save_market_data,
    )

    monkeypatch.setattr(
        market_service,
        "BinanceCandleProvider",
        FakeBinanceCandleProvider,
    )

    monkeypatch.setattr(
        market_service,
        "analyze_market",
        fake_analyze_market,
    )

    monkeypatch.setattr(
        market_service,
        "calculate_market_score",
        fake_calculate_market_score,
    )

    result = market_service.MarketService().load()

    # ==========================================
    # Technical Analysis
    # ==========================================

    assert result["signal"] == "BUY"

    assert result["risk"] == "LOW"

    assert result["technical_score"] == 15

    # ==========================================
    # Global Market Score
    # ==========================================

    assert result["market_score"] == 75

    # ==========================================
    # Scores must be independent
    # ==========================================

    assert result["technical_score"] != result["market_score"]

    # ==========================================
    # Other required fields
    # ==========================================

    assert "prices" in result

    assert "df" in result

    assert "indicators" in result

    assert "btc_price" in result