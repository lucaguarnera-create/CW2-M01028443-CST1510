import sqlite3
import pandas as pd
from app.db import get_connection   
conn = get_connection() 


def migrate_datasets_metadata(conn):
    path = r"C:\Users\lucag\OneDrive\Desktop\CW2-M01028443-CST1510\Code\CW2-M01028443-CST1510\DATA\datasets_metadata.csv"
    df = pd.read_csv(path)
    print(df.head())
    df.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    print('Data loaded successfully !')

def migrate_it_tickets(conn):
    path = r"C:\Users\lucag\OneDrive\Desktop\CW2-M01028443-CST1510\Code\CW2-M01028443-CST1510\DATA\it_tickets.csv"
    df = pd.read_csv(path)
    print(df.head())
    df.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data loaded successfully !')

#--------------get data-----------------