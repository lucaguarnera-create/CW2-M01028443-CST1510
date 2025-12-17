# app/db.py
import sqlite3

def get_connection(db_path=r"C:\Users\lucag\OneDrive\Desktop\CW2-M01028443-CST1510\Code\CW2-M01028443-CST1510\DATA\inteligence_platform.db"):
    """Return a SQLite connection."""
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn
