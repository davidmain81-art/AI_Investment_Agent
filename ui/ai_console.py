"""
AI Performance Console
"""


def print_ai_performance(stats):

    print()

    print("🧠 AI PERFORMANCE")

    print("-" * 50)

    print(

        f"Accuracy        : "

        f"{stats['accuracy']}%"

    )

    print(

        f"Average Profit  : "

        f"{stats['average_profit']}%"

    )

    print(

        f"Wins            : "

        f"{stats['wins']}"

    )

    print(

        f"Losses          : "

        f"{stats['losses']}"

    )

    if stats["best_trade"]:

        print()

        print(

            "Best Trade      : "

            f"{stats['best_trade']['asset']}"

        )

        print(

            "Best Profit     : "

            f"{stats['best_trade']['profit_percent']}%"

        )

    if stats["worst_trade"]:

        print()

        print(

            "Worst Trade     : "

            f"{stats['worst_trade']['asset']}"

        )

        print(

            "Worst Profit    : "

            f"{stats['worst_trade']['profit_percent']}%"

        )