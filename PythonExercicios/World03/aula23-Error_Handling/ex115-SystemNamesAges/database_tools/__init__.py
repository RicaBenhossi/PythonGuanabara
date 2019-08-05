import os.path as path_file
import json as database_file


def data_base_file_exists():
    return path_file.isfile('database.json')


def create_data_base_file():
    if not data_base_file_exists():
        with open('database.json', 'x') as dbfile:
            dbfile.close()
            print('Database file successfuly created.')


def save_data():
    pass


def load_data():
    pass
