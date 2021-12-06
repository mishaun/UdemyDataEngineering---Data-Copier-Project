import sys
from decouple import config
from read import get_json_reader
from write import load_to_table
from build_connection import get_db_connection

def main():
    conn = get_db_connection()

    rel_dir = config('REL_DATA_DIR')
    table_names = sys.argv[1].split(',')

    for table in table_names:
        json_reader = get_json_reader(rel_dir, table, chunksize=1000)

        for df in json_reader:
            try:
                load_to_table(df, conn, table, df.columns[0])
            except Exception as e:
                print(e)
                continue

if __name__ == '__main__':
    main()