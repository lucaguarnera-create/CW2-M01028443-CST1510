import pandas as pd
def migrate_datasets_metadata(conn):
    data1 = pd.read_csv('DATA\\datasets_metadata.csv')
    data1.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    print('Data load')