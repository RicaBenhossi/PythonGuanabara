"""
System is designed to save and list people names and age. Data are stored in a text file.
"""


def build_menu(menu_part, message=''):
    message_types = {'header': '=' * 50, 'title': (f'{message:^50}'), 'options': message, 'separator': '-' * 50}
    try:
        return message_types[menu_part]
    except KeyError:
        return ''


def show_menu():
    print(build_menu('header'))
    print(build_menu('title', 'MENU - System User Register'))
    print(build_menu('header'))
    print()
    print(build_menu('options', '1 - Register a New User'))
    print(build_menu('options', '2 - List all Users'))
    print(build_menu('options', '0 - Close Application'))
    print(build_menu('separator'))


show_menu()
# selected_option =
