import sqlite3

conn = sqlite3.connect("investment_agent.db")
conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("SELECT * FROM memory")

rows = cur.fetchall()

print(f"Rows: {len(rows)}")

for row in rows:
    print(dict(row))

conn.close()