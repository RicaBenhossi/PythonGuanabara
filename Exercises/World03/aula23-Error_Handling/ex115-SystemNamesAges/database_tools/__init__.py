import os.path as path_file
import os
import json as database_file
import time


def data_base_file(option=0, * data_to_save):
    """Handle with Data Base file (json) for the exercise 15 of Python Guanabara Course

    Arguments:
        option {integer} -- Every option (action) has a code:
            1 - Save data of * data_to_save into de Data Base File
            2 - Load file and return it's content to print
    """

    os.chdir(path_file.dirname(__file__))
    os.chdir('..')
    data_base_name = 'database.json'
    if not path_file.isfile(data_base_name):
        try:
            with open(data_base_name, 'x') as db_file:
                db_file.close()
        except Exception:
            print('Data Base file could not been created.')
        else:
            print('Database file successfuly created.')

    if option == 1:
        # Save data to File
        # with open(data_base_name, 'w') as dbfile_save:
        #     pass
        return 'Data successfuly saved.'
        time.sleep(4)

    elif option == 2:
        # Load file to print
        try:
            with open(data_base_name, 'r') as db_file:
                data_to_print = data_base_file.load(db_file)
                db_file.close()
        except Exception:
            print('Data Base File could not been open.')
        else:
            return data_to_print
