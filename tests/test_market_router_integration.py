from markets.market_router import MarketRouter


def test_router_identifies_supported_markets():

    router = MarketRouter()

    assert router.route("BTCUSDT") == "CRYPTO"
    assert router.route("ETHUSDT") == "CRYPTO"
    assert router.route("XAUUSD") == "PRECIOUS_METAL"
    assert router.route("فولاد") == "IRAN_STOCK"
    assert router.route("شپنا") == "IRAN_STOCK"


def test_router_does_not_create_trade():

    router = MarketRouter()

    result = router.route("BTCUSDT")

    assert result == "CRYPTO"

    assert not hasattr(router, "create_trade")
    assert not hasattr(router, "execute")
