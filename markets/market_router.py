"""
Market Router
Version 1.1
"""


class MarketRouter:

    CRYPTO_SUFFIXES = ("USDT", "USDC", "BUSD")

    PRECIOUS_METALS = (
        "XAUUSD",
        "XAGUSD",
        "GOLD",
        "SILVER",
    )

    IRAN_STOCKS = (
        "فولاد",
        "شپنا",
        "Fملی",
        "وبملت",
        "شستا",
        "اهرم",
        "FOLD",
        "FMELI",
        "WEBMELAT",
        "SHASTA",
        "AHROM",
    )

    def route(self, asset):

        if not asset or not isinstance(asset, str):
            return "UNKNOWN"

        asset = asset.strip().upper()

        if asset in self.PRECIOUS_METALS:
            return "PRECIOUS_METAL"

        if asset in self.IRAN_STOCKS:
            return "IRAN_STOCK"

        if asset.endswith(self.CRYPTO_SUFFIXES):
            return "CRYPTO"

        return "UNKNOWN"