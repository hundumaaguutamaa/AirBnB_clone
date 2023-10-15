#!/usr/bin/python3

""" HBnB console"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Signals end of command line"""
        return True

    def emptyline(self):
        """Nothing done when entering empty command"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
