# app/db.py
import sqlite3

def get_connection(db_path="users.db"):
    """Return a SQLite connection."""
    conn = sqlite3.connect(db_path)
    return conn
