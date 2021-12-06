import os
import pandas as pd

def get_json_reader(base_dir, table_name, chunksize = 1000):

    filename = os.listdir(os.path.join(base_dir, table_name))[0]
    filepath = os.path.join(base_dir, table_name, filename)

    json_reader = pd.read_json(filepath, lines = True, chunksize=chunksize)
    return json_reader


if __name__ == '__main__':
    from decouple import config
    import sys

    BASE_DIR = config('BASE_DIR')

    table_names = sys.argv[1].split(',')
    print('Runtime Args')
    print(table_names)

    table_name = table_names[0]

    json_reader = get_json_reader(BASE_DIR, table_name)
    type(json_reader)

    for df in json_reader:
        minkey = df[df.columns[0]].min()
        maxkey = df[df.columns[0]].max()
        print('table is: ' + table_name)
        print(f'order chunk range from orders {minkey} to {maxkey}')
