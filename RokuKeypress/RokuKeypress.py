import subprocess
from time import sleep
import requests


class RokuKeypress(object):
    command_string = 'http://%s:8060/keypress/%s'
    last_command = False

    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __command(self, keypress):

        if keypress is None:
            return

        command_string = self.command_string % (self.ip_address, keypress)
        requests.post(command_string)
        sleep(0.5)

    def __forwards(self, command_list=[]):
        for x in command_list:
            if x is None:
                continue
            else:
                self.__command(x)

    def __backwards(self, command_list):
        backwards = {
            'down': 'up',
            'up': 'down',
            'right': 'left',
            'left': 'right',
            'select': None,
        }
        new_list = list()
        [new_list.append(backwards[x]) for x in command_list]
        new_list.reverse()
        self.__forwards(new_list)

    def key(self, commands):
        self.__forwards(commands)

        if self.last_command is False:
            self.__backwards(commands)

    def key_0(self):
        commands = ['down', 'right', 'right', 'right', 'select']
        self.key(commands)

    def key_1(self):
        commands = ['select']
        self.key(commands)

    def key_2(self):
        commands = ['right', 'select']
        self.key(commands)

    def key_3(self):
        commands = ['right', 'right', 'select']
        self.key(commands)

    def key_4(self):
        commands = ['right', 'right', 'right', 'select']
        self.key(commands)

    def key_5(self):
        commands = ['right', 'right', 'right', 'right', 'select']
        self.key(commands)

    def key_6(self):
        commands = ['down', 'select']
        self.key(commands)

    def key_7(self):
        commands = ['down', 'right', 'select']
        self.key(commands)

    def key_8(self):
        commands = ['down', 'right', 'right', 'select']
        self.key(commands)

    def key_9(self):
        commands = ['down', 'right', 'right', 'select']
        self.key(commands)

    def command_list(self, numbers=list()):
        last_index = len(numbers)
        for x in numbers:
            print('key_%s' % str(x))
            temp = numbers.index(x)
            if numbers.index(x) == last_index-1:
                self.last_command = True

            getattr(self, 'key_%s' % str(x))()

    def end(self):
        self.__command('select')


if __name__ == "__main__":
    temp = RokuKeypress('192.168.1.250')
    temp.command_list([0, 1, 5, 2, 9])
    temp.end()
