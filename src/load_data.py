import pandas as pd
import sqlite3 as sql

def load_from_csv(path):
    return pd.read_csv(path)

def load_from_sqlite(db_path, table_name="wmp_bf_efficiency"):
    conn = sql.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df