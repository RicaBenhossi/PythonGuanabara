import os.path as path_file
import os
import json as database_file


def data_base_file(option=0, * data_to_save):
    """Handle with Data Base file (json) for the exercise 15 of Python Guanabara Course

    Arguments:
        option {integer} -- Every option (action) has a code:
            1 - Save data of * data_to_save into de Data Base File
            2 - Load file and return it's content to print
    """

    os.chdir(path_file.dirname(__file__))
    os.chdir('..')
    data_base_dir = os.getcwd()
    if not path_file.isfile('database.json'):
        with open(data_base_dir + '/database.json', 'x') as dbfile:
            dbfile.close()
            print('Database file successfuly created.')

    if option == 1:
        # Save data to File
        pass
        return 'Data successfuly saved.'
    elif option == 2:
        # Load file to print
        pass


def save_data():
    pass


def load_data():
    pass
