#!/usr/bin/python3
'''console'''
import cmd, sys


class HBNBCommand(cmd.Cmd):
    '''cmd'''
    prompt = '(hbnb) '
    file = None

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
