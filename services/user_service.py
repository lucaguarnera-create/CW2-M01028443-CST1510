#user_services.py Migration
import pandas as pd
from app.users import add_user
from app.db import get_connection
conn = get_connection()

def migrate_users():
    with open('DATA\\user.txt', 'r')as f:
        users = f.readlines()
    for user in users:
        name, hash = user.strip().split(',')
        add_user(conn, name, hash)

    conn.close()