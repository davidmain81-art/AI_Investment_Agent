import sqlite3

DB = "database/investment_agent.db"


def update_trade_result(memory_id, result):

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute(
        """
        UPDATE ai_memory

        SET result=?

        WHERE id=?
        """,
        (
            result,
            memory_id,
        )
    )

    conn.commit()

    conn.close()