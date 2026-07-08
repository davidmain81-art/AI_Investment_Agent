"""
Portfolio Exposure
"""


def calculate_exposure(portfolio):

    exposure = {}

    total = 0

    for item in portfolio:

        total += item["amount"]

    if total == 0:

        return exposure

    for item in portfolio:

        market = item["market"]

        percent = round(

            item["amount"] * 100 / total,

            2,

        )

        exposure[market] = (

            exposure.get(

                market,

                0,

            )

            + percent

        )

    return exposure