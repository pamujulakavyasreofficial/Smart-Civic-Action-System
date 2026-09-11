import sqlite3
import pandas as pd

def get_report():
    conn = sqlite3.connect("complaints.db")

    df = pd.read_sql_query(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    return df
