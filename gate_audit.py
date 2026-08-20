from pathlib import Path


FILES = [
    "trading/trade_manager.py",
    "analysis/decision_engine.py",
    "analysis/execution_safety.py",
    "engine/services/trade_service.py",
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