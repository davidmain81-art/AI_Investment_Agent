from analysis.market_analysis import analyze_market
from config.settings import APP_NAME
from config.settings import VERSION
from config.settings import OWNER

from data.crypto import get_bitcoin_price
from data.gold import get_gold_price
from data.dollar import get_dollar_price

print("=" * 45)
print(APP_NAME)
print("Version:", VERSION)
print("Developer:", OWNER)
print("=" * 45)

btc = get_bitcoin_price()
gold = get_gold_price()
dollar = get_dollar_price()

print(f"BTC    : {btc} USD")
print(f"Gold   : {gold} USD")
print(f"Dollar : {dollar} Toman")
signal = analyze_market(btc)

print()
print("Market Analysis")
print("----------------")
print("BTC Signal :", signal)