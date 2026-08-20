from markets.market_router import MarketRouter

def test_crypto_market():
    router = MarketRouter()
    assert router.route("BTCUSDT") == "CRYPTO"
    assert router.route("ETHUSDT") == "CRYPTO"

def test_precious_metal_market():
    router = MarketRouter()
    assert router.route("XAUUSD") == "PRECIOUS_METAL"
    assert router.route("XAGUSD") == "PRECIOUS_METAL"

def test_iran_stock_market():
    router = MarketRouter()
    assert router.route("\u0641\u0648\u0644\u0627\u062f") == "IRAN_STOCK"
    assert router.route("\u0634\u067e\u0646\u0627") == "IRAN_STOCK"

def test_unknown_market():
    router = MarketRouter()
    assert router.route("UNKNOWN_ASSET") == "UNKNOWN"

def test_invalid_asset():
    router = MarketRouter()
    assert router.route(None) == "UNKNOWN"
    assert router.route("") == "UNKNOWN"
