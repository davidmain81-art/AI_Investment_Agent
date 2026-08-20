from config.database import get_database
from database.database import get_connection


connection = get_connection(get_database())
cursor = connection.cursor()

cursor.execute(
    """
    SELECT
        id,
        asset,
        signal,
        status,
        entry_price,
        exit_price,
        pnl,
        exit_reason
    FROM trades
    WHERE status = 'CLOSED'
    AND (exit_price IS NULL OR pnl IS NULL)
    """
)

rows = cursor.fetchall()

print("BROKEN CLOSED TRADES:", len(rows))

for row in rows:
    print(tuple(row))

connection.close()