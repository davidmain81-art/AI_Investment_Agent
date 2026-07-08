from providers.mock_stock_provider import (
    MockStockProvider,
)


def get_stock_market():

    provider = MockStockProvider()

    return provider.get_data()