from time import sleep


def interactive_help(command=''):
    HeadersColours(('Accessing the manual of ' + command), process_color)
    sleep(3)
    print(command_color)
    print(help(command))
    print(end_color)


def HeadersColours(message, color):
    len_message = len(message) + 8
    print(color)
    print('~' * len_message)
    print(' ' * ((len_message - (len(message))) // 2), end='')
    print(f'{message}', end='')
    print(' ' * ((len_message - (len(message))) // 2))
    print('~' * len_message)
    print(end_color)


system_start_color = '\033[1;32;40m'
command_color = '\033[7;;40m'
process_color = '\033[0;37;46m'
end_color = '\033[0m'

while True:
    HeadersColours('HELP SYSTEM PYHELP', system_start_color)
    command = str(input('Informe o commando ou biblioteca para o qual deseja ajuda.')).strip().lower()
    if command == 'fim':
        break
    else:
        interactive_help(command)

print('\nSystem Finished...')
