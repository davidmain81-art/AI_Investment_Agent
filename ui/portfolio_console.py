"""
Portfolio Console
"""


def print_exposure(exposure):

    print()

    print("📊 CURRENT EXPOSURE")

    print("-" * 50)

    if not exposure:

        print("No portfolio data.")

        return

    for market, percent in exposure.items():

        print(

            f"{market:<15}"

            f"{percent:.2f}%"

        )