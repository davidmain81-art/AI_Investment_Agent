from providers.binance_provider import BinanceProvider
from providers.mock_crypto_provider import MockCryptoProvider


class ProviderManager:

    def __init__(self):

        self.provider_name = "MOCK"
        self.provider = MockCryptoProvider()


    def connect(self):

        try:

            test = BinanceProvider().get_price("BTCUSDT")

            if test:

                self.provider = BinanceProvider()
                self.provider_name = "BINANCE"
                return


        except Exception:

            pass


        self.provider = MockCryptoProvider()
        self.provider_name = "MOCK"


    def get_provider_name(self):

        return self.provider_name


    def get_provider(self):

        return self.provider