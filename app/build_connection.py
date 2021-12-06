import os
from decouple import config


def get_db_connection():

    #building environment variables from .env file
    db_params = {
        'DB_NAME': config("DB_NAME"),
        'DB_PORT': config("DB_PORT"),
        'DB_HOST': config("DB_HOST"),
        'DB_PASS': config("DB_PASS") ,
        'DB_USER': config("DB_USER"),
        'DB_RDBMS': config("DB_RDBMS")
    }

    #This block of code will replace environment variables from .env file if environment variables are provided in CLI
    #this will ensure it can be run in a docker container where port numbers and host will change
    for key in db_params:
        if type(os.environ.get(key)) != type(None):
            db_params[key] = os.environ.get(key)

    connection_string = f'{config("DB_RDBMS")}://{db_params["DB_USER"]}:{db_params["DB_PASS"]}@{db_params["DB_HOST"]}:{db_params["DB_PORT"]}/{db_params["DB_NAME"]}'

    return connection_string

if __name__ == '__main__':
    conn = get_db_connection()
