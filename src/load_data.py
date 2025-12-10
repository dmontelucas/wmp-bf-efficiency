import pandas as pd
import sqlite3 as sql

def load_from_csv(path, **read_csv_kwargs):
    try:
        return pd.read_csv(path, **read_csv_kwargs)
    except Exception as e:
        raise RuntimeError(f"Failed to load CSV file from {path}: {e}")
    
    df.attrs["source"] = {"type": "csv", "path": path}
    return df

def load_from_sqlite(db_path, table_name="wmp_bf_efficiency", columns=None):
    if not table_name.isidentifier():
        raise ValueError(f"Invalid table name: {table_name}")
    
    cols = "*" if columns is None else ", ".join(columns)
    query = f"SELECT * FROM {table_name}"
    
    try:
        with sql.connect(db_path) as conn:
            df = pd.read_sql(query, conn)
    except Exception as e:
        raise RuntimeError(f"Failed to load {table_name} from {db_path}: {e}")
    
    df.attrs["source"] = {
        "type": "sqlite",
        "db_path": db_path,
        "table": table_name,
        "columns": columns,
    }
    return df
