import menu_tools as menu
import database_tools as dbtools
import validation_data_inputs as valid_input


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
                # name = input('Type the name of the person: ')
                break
            while True:
                age = input('Type the person\'s age: ')
                valid_age = valid_input.validated_age(age)
                if type(valid_age) == int:
                    break
                else:
                    os.
                    print(valid_age)

        elif selected_menu == 2:
            pass
