from flask import Flask, request
import bjoern
import pickle5
import pandas as pd
import numpy as np
import configs
from tools_db import get_db_connection, add_req, add_error

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

model = pickle5.load(open(configs.model_path, 'rb'))

@app.route("/predict", methods=['POST'])
def predict():
    try:
        in_req = request.get_json(force=True)
        df = pd.DataFrame(in_req)
        df['predict'] = model.predict(df)
        df['predict'] = np.clip(df['predict'], a_min=configs.min_value, a_max=configs.max_value)
        add_req(in_req, df['predict'].tolist())
        return df['predict'].to_json()
    except Exception as err:
        add_error(err)
        return {"predict": 0}


@app.route("/last_reqs", methods=['GET'])
def last_reqs():
    conn = get_db_connection()
    cur = conn.cursor()
    with open("sql/select_reqs.sql", "r") as f:
        sql_query = f.read()
    rows = cur.execute(sql_query).fetchall()
    logs = {}
    for log in rows:
        logs[log[0]] = {}
        logs[log[0]]['time'] = log[1]
        logs[log[0]]['req'] = log[2]
        logs[log[0]]['predict'] = log[3]
    return logs


@app.route("/last_errors", methods=['GET'])
def last_errors():
    conn = get_db_connection()
    cur = conn.cursor()
    with open("sql/select_errors.sql", "r") as f:
        sql_query = f.read()
    rows = cur.execute(sql_query).fetchall()
    logs = {}
    for i, log in enumerate(rows):
        logs[i] = {}
        logs[i]['time'] = log[0]
        logs[i]['type_error'] = log[1]
        logs[i]['log_error'] = log[2]
    return logs


@app.route("/")
def home():
    return {'500'}


if __name__ == "__main__":
    bjoern.run(app, configs.host, configs.port)
