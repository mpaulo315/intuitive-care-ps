import sqlite3
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_connection():
    db = getenv("DATABASE")
    return sqlite3.connect(db)