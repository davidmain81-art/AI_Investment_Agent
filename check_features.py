from learning.pattern_engine import PatternEngine


engine = PatternEngine()

df = engine.load_features()


print(
    df[
        [
            "asset",
            "result",
            "rsi",
            "mfi",
            "macd",
            "ema20",
            "ema50",
            "ema200",
            "adx",
            "volume"
        ]
    ]
)


engine.close()