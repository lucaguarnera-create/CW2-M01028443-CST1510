import sqlite3
import pandas as pd
import hashlib

def create_users_table(conn):
    curr = conn.cursor()
    curr.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    """)
    conn.commit()


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(conn, username, password_hash):
    curr = conn.cursor()
    sql = """INSERT INTO users (username, password_hash) VALUES (?, ?)"""
    curr.execute(sql, (username, password_hash))
    conn.commit()

def get_user(conn, username):
    curr = conn.cursor()
    sql = """SELECT id, username, password_hash FROM users WHERE username = ?"""
    curr.execute(sql, (username,))
    return curr.fetchone()

def get_all_users(conn):
    curr = conn.cursor()
    sql = """SELECT * FROM users"""
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return users

def get_all_users_pandas(conn):
    query = "SELECT * FROM users"
    return pd.read_sql(query, conn)
