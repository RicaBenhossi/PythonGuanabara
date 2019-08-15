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
                data_to_print = database_file.load(db_file)
                db_file.close()
        except Exception:
            print('Data Base File could not been open.')
        else:
            return format_data_to_print(data_to_print)


def format_data_to_print(data_to_print):
    str_main_separator = ('=' * 50 + '\n')
    str_separator = ('-' * 50 + '\n')
    str_title = ((f'{"LIST OF PERSON IN DATA BASE":^50}\n'))
    str_legend = (f'{"NAME":<47}{"AGE":>3}\n')
    str_content = str('\n'.join(map(lambda x: f'{x[0]:<47}{x[1]:>3}', data_to_print)) + '\n')

    to_print_string = str_main_separator + str_title + str_separator + str_legend + str_separator + str_content + str_separator + str_main_separator

    return to_print_string
