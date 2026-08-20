import sqlite3
import os


DATABASES = {
    "ROOT": "investment_agent.db",
    "DATABASE": "database/investment_agent.db",
}


TABLES = [
    "memory",
    "trades",
    "trade_features",
    "paper_trades",
    "ai_memory",
]


def show_table_schema(conn, table):

    print()
    print(f"--- {table} ---")

    exists = conn.execute(
        "SELECT COUNT(*) "
        "FROM sqlite_master "
        "WHERE type='table' AND name=?",
        (table,),
    ).fetchone()[0]

    if not exists:
        print("TABLE NOT FOUND")
        return

    rows = conn.execute(
        f"PRAGMA table_info([{table}])"
    ).fetchall()

    for row in rows:

        cid = row[0]
        name = row[1]
        column_type = row[2]
        not_null = row[3]
        default = row[4]
        primary_key = row[5]

        print(
            f"{cid}: "
            f"{name} | "
            f"{column_type} | "
            f"NOT_NULL={not_null} | "
            f"DEFAULT={default} | "
            f"PK={primary_key}"
        )


def audit_database(name, path):

    print()
    print("=" * 70)
    print(f"{name}")
    print(os.path.abspath(path))
    print("=" * 70)

    if not os.path.exists(path):

        print("FILE NOT FOUND")
        return

    conn = sqlite3.connect(path)

    for table in TABLES:
        show_table_schema(conn, table)

    conn.close()


for name, path in DATABASES.items():
    audit_database(name, path)