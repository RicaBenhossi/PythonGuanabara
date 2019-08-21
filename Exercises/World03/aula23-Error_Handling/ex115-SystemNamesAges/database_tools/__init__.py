import os.path as path_file
import os
import json as database_file


def format_data_to_print(data_to_print):
    str_main_separator = ('=' * 50 + '\n')
    str_separator = ('-' * 50 + '\n')
    str_title = ((f'{"LIST OF PERSON IN DATA BASE":^50}\n'))
    str_legend = (f'{"NAME":<47}{"AGE":>3}\n')
    str_content = str('\n'.join(map(lambda x: f'{x[0]:<47}{x[1]:>3}', data_to_print)) + '\n')

    to_print_string = str_main_separator + str_title + str_separator + str_legend + str_separator + str_content + str_separator + str_main_separator

    return to_print_string


def data_base_file(option=0, * data_to_save):
    """Handle with Data Base file (json) for the exercise 15 of Python Guanabara Course

    Arguments:
        option {integer} -- Every option (action) has a code:
            1 - Save data of * data_to_save into de Data Base File
            2 - Load file and return it's content to print
    """
    def load_from_file(file_name):
        with open(file_name, 'r') as db_file_load:
            return database_file.load(db_file_load)
            db_file_load.close()

    def save_data_to_file(db_file_to_load_saved_data):
        try:
            saved_data = list()
            if os.stat(db_file_to_load_saved_data).st_size > 0:
                saved_data = load_from_file(db_file_to_load_saved_data)

            saved_data.append(data_to_save)
            with open(data_base_name, 'w') as db_file_save:
                database_file.dump(saved_data, db_file_save)

        except Exception as error:
            return f'An error has ocurred. {error}'
        else:
            return 'Data successfuly saved.'

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

    elif option == 1:
        # Save data to File
        return save_data_to_file(data_base_name)

    elif option == 2:
        # Load file to print
        try:
            data_to_print = load_from_file(data_base_name)
        except Exception:
            print('Data Base File could not been open.')
        else:
            return format_data_to_print(data_to_print)
