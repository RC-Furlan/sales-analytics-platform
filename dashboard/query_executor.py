import pandas as pd

from database import engine
from sql_loader import load_sql


def run_query(filename: str):

    query = load_sql(filename)

    return pd.read_sql(query, engine)