from pathlib import Path


FILES = [
    "engine/trade_pipeline.py",
    "database/close_trade.py",
    "execution/execution_engine.py",
]


for file in FILES:

    print()
    print("=" * 80)
    print(file)
    print("=" * 80)

    path = Path(file)

    if not path.exists():
        print("FILE NOT FOUND")
        continue

    print(path.read_text(encoding="utf-8"))