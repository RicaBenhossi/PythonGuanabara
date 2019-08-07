import menu_tools as menu
import database_tools as dbtools


dbtools.create_data_base_file()
menu_options = menu.show_menu()

while True:
    try:
        selected_menu = menu_options[int(input('Type the menu option you want to access: '))]
    except ValueError:
        print('The option must be an integer number.')
    except IndexError:
        print('Invalid menu option.')
    else:
        if selected_menu == 0:
            print((menu.build_menu('separator')))
            print(menu.build_menu('title' , 'Thanks for using our System'))
            print((menu.build_menu('separator')))
            break
        elif selected_menu == 1:
            pass
        elif selected_menu == 2:
            pass
