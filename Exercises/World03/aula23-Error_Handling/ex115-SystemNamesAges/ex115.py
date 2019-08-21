import database_tools as db_tools
import menu_tools as menu
import check_inputs.validate_name as check_name
import check_inputs.validate_age as check_age
import time
import getch


db_tools.data_base_file()

while True:
    menu_options = menu.show_menu()
    try:
        selected_menu = menu_options[int(input('Type the menu option you want to access: '))]
    except ValueError:
        print(menu.build_menu('separator'))
        print(menu.build_menu('title', 'The option must be an integer number.'))
        print(menu.build_menu('separator'))
        getch.pause(f'{("*" * 5 + " Press any key to return. " + "*" * 5):^50}')
    except IndexError:
        print(menu.build_menu('separator'))
        print(menu.build_menu('title', 'Invalid menu option.'))
        print(menu.build_menu('separator'))
        getch.pause(f'{("*" * 5 + " Press any key to return. " + "*" * 5):^50}')
    else:
        if selected_menu == 0:
            print(menu.build_menu('separator'))
            print(menu.build_menu('title', 'Thank you for using our System'))
            print(menu.build_menu('separator'))
            break
        elif selected_menu == 1:
            while True:
                name = input('Type the NAME of the person or 0 to return the menu: ').strip().upper()
                (result_name, return_data) = check_name.validated_name(name)
                if return_data is None:
                    break
                else:
                    print(return_data)
                    if not result_name:
                        continue
                    else:
                        while True:
                            age = input('Type the AGE of the person or 0 to return the menu: ')
                            (result_age, return_data) = check_age.validated_age(age)
                            if return_data is None:
                                break
                            else:
                                print(return_data)
                                if not result_age:
                                    continue
                                else:
                                    break
                        print(menu.build_menu('separator'))
                        print(menu.build_menu('title', db_tools.data_base_file(1, name, age)))
                        print(menu.build_menu('separator'))
                        time.sleep(3)
                        break

        elif selected_menu == 2:
            data_to_print = db_tools.data_base_file(2)
            print(data_to_print)
            getch.pause(f'{("*" * 5 + " Press any key to return. " + "*" * 5):^50}')
