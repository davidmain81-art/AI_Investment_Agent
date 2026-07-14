"""
History Viewer
Version 0.5
"""

import os
import sys

# اضافه کردن پوشه اصلی پروژه به مسیر Python
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from database.database import get_connection


def show_trades():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

        SELECT

            id,
            created_at,
            asset,
            signal,
            entry_price,
            stop_loss,
            take_profit,
            confidence,
            status

        FROM trades

        ORDER BY id

    """)

    rows = cursor.fetchall()

    connection.close()

    print()

    print("=" * 80)

    print("TRADE HISTORY")

    print("=" * 80)

    if not rows:

        print("No trades found.")

        return

    for row in rows:

        print(f"""
ID          : {row[0]}
Date        : {row[1]}
Asset       : {row[2]}
Signal      : {row[3]}
Entry       : {row[4]}
Stop Loss   : {row[5]}
Take Profit : {row[6]}
Confidence  : {row[7]}
Status      : {row[8]}
{"-" * 80}
""")


if __name__ == "__main__":
    show_trades()