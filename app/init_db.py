import sqlite3

conn = sqlite3.connect("logs.db")
cur = conn.cursor()

with open("sql/create_logs_reqs.sql", "r") as f:
    sql_query = f.read()
cur.execute(sql_query)

with open("sql/create_logs_errors.sql", "r") as f:
    sql_query = f.read()
cur.execute(sql_query)
conn.close()
