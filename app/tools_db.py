import json
from typing import List
from datetime import datetime
import sqlite3
import configs


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(configs.db_name)
    conn.row_factory = sqlite3.Row
    return conn


def add_req(in_req: dict, predicts: List[float]) -> None:
    conn = get_db_connection()
    cur = conn.cursor()
    with open("sql/insert_reqs.sql", "r") as f:
        sql_query = f.read()
    cur.execute(sql_query,
                (datetime.now(), json.dumps(in_req), json.dumps(predicts))
                )
    conn.commit()
    conn.close()


def add_error(error: BaseException) -> None:
    conn = get_db_connection()
    cur = conn.cursor()
    with open("sql/insert_errors.sql", "r") as f:
        sql_query = f.read()
    cur.execute(sql_query,
                (datetime.now(), str(type(error)), str(error))
                )
    conn.commit()
    conn.close()
