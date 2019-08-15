def options_available():
    return dict({0: 'Close Application', 1: 'Register a New User', 2: 'List all Users'})


def options_numbers():
    return (options_available().items())


def build_menu(menu_part, message='', choosable_menu={}):
    message_types = {'header': '=' * 50, 'title': (f'{message:^50}'), 'options': choosable_menu, 'separator': '-' * 50}
    try:
        if menu_part == 'options':
            return list((list(message_types[menu_part].keys()), list(message_types[menu_part].values())))
        else:
            return message_types[menu_part]
    except KeyError:
        return ''


def show_menu():
    import os

    os.system('clear')
    print(build_menu('header'))
    print(build_menu('title', 'MENU - System User Register'))
    print(build_menu('header'))
    menu_options = options_available()
    menu_options_builded = build_menu('options', choosable_menu=menu_options)
    print('\n'.join(map((lambda index, description: str(index) + ' - ' + str(description)), menu_options_builded[0], menu_options_builded[1])))
    print(build_menu('separator'))
    return list(menu_options.keys())
