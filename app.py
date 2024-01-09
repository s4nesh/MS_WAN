from icmplib import ping
import os

# comment
host = ping('192.168.0.250', count=4, interval=0.2)


typed_quit = False

while not typed_quit:
    user_input = input("> ").lower()
    if user_input == 'check gateway':
        if host.is_alive:
            print('Can reach gateway')
        else:
            print('Host unreachable')
    elif user_input == 'quit':
        break
    elif user_input == "clear":
        os.system('cls')
    else:
        print('Command not found')

