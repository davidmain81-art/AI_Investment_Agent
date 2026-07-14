"""
AI Performance Dashboard
Version 1.0
"""


def print_performance(stats):

    print()

    print("=" * 52)
    print("📊 AI PERFORMANCE DASHBOARD")
    print("=" * 52)

    print()

    print(f"Experience        : {stats['experience']}")
    print(f"Wins              : {stats['wins']}")
    print(f"Losses            : {stats['losses']}")

    print()

    print(f"Win Rate          : {stats['confidence']} %")

    print()

    print(f"Best Asset        : {stats['best_asset']}")
    print(f"Best Signal       : {stats['best_signal']}")

    print("=" * 52)