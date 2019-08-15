import database_tools as dbtools
import menu_tools as menu
import validation_data_inputs.validations as validate_input

dbtools.data_base_file()

while True:
    menu_options = menu.show_menu()
    try:
        selected_menu = menu_options[int(input('Type the menu option you want to access: '))]
    except ValueError:
        print('The option must be an integer number.')
    except IndexError:
        print('Invalid menu option.')
    else:
        if selected_menu == 0:
            print((menu.build_menu('separator')))
            print(menu.build_menu('title', 'Thank you for using our System'))
            print((menu.build_menu('separator')))
            break
        elif selected_menu == 1:
            while True:
                name = input('Type the name of the person: ').strip().upper()
                (name_is_valid, warn_message) = validate_input.validated_name(name)
                if name_is_valid:
                    print(f'Name: {name}')
                    break
                else:
                    print(warn_message)

            while True:
                age = input('Type the person\'s age: ')
                valid_age = validate_input.validated_age(age)
                if type(valid_age) == int:
                    print(f'Age: {valid_age}')
                    break
                else:
                    print(valid_age)

            dbtools.data_base_file(1, name, age)

        elif selected_menu == 2:
            data_to_print = dbtools.data_base_file(2)

            print(data_to_print)
        print(f'{("*" * 5 + " Press any key to return. " + "*" * 5):^50}')
        input()
