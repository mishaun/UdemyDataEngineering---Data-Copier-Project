def load_to_table(df, db_connection, table_name,  key):

    minkey = df[key].min()
    maxkey = df[key].max()

    print(f'Loading Records {table_name} Table from {minkey} to {maxkey}')
    df.to_sql(table_name, db_connection, if_exists= 'append', index = False)


if __name__ == '__main__':

    print('write.py ran is main')

    from decouple import config
    from read import get_json_reader
    import sys
    import os
    import pandas as pd


    base_dir = config('BASE_DIR')
    table_names = sys.argv[1].split(',')
    conn = config('DB_CONN')

    test_table = 'customers'

    json_reader = get_json_reader(base_dir, test_table, chunksize = 1000)

    # ## manually testing load_to_table function
    # users = [
    #     {'id': 1, 'fname': 'John', 'lname': 'woods'},
    #     {'id': 2, 'fname': 'tiger', 'lname': 'mickelson'},
    # ]

    for df in json_reader:
        load_to_table(df, conn, test_table, df.columns[0])

    # pd.read_sql(f'select * from {test_table}', conn)

    #
    # testDF = pd.DataFrame(users)
    #
    # load_to_table(testDF, conn, 'users', 'id')
    # pd.read_sql(f'select * from users', conn)