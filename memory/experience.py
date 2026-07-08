"""
AI Experience
"""


def summarize_experience(memories):

    summary = {

        "total": len(memories),

        "wins": 0,

        "losses": 0,

        "average_profit": 0,

    }

    if not memories:

        return summary

    total_profit = 0

    for row in memories:

        profit = row[8]

        total_profit += profit

        if profit >= 0:

            summary["wins"] += 1

        else:

            summary["losses"] += 1

    summary["average_profit"] = round(

        total_profit /

        len(memories),

        2,

    )

    return summary