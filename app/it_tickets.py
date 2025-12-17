import pandas as pd
def migrate_it_tickets(conn):
    data1 = pd.read_csv('DATA\\it_tickets.csv')
    data1.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data load')