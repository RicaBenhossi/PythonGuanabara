from time import sleep


def interactive_help(command=''):
    HeadersColours(f'Accessing the manual of \'{command}\'', process_color)
    sleep(2)
    print(command_color, end='')
    help(command)
    print(end_color, end='')


def HeadersColours(message, color):
    len_message = len(message) + 4
    print(color, end='')
    print('~' * len_message)
    print(f'  {message}')
    print('~' * len_message)
    print(end_color, end='')


system_start_color = '\033[1;32;40m'
command_color = '\033[7;34;40m'
process_color = '\033[0;37;46m'
end_color = '\033[m'

while True:
    HeadersColours('HELP SYSTEM PYHELP', system_start_color)
    command = str(input('Informe o commando ou biblioteca para o qual deseja ajuda.')).strip().lower()
    if command == 'fim':
        break
    else:
        interactive_help(command)

print('\nSystem Finished...')
