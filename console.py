#!/usr/bin/python3

""" HBnB console"""

import cmd
import json
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Signals end of command line"""
        return True

    def emptyline(self):
        """Nothing done when entering empty command"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, and saves it
        to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            print(new_instnce.id)
        
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")  
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects_dict = models.storage.all()
            instance_key = "{}.{}".format(args[0], args[1])
            instance = objects_dict.get(instance_key)
            if instance:
                print(instance)
            else:
                print("Instance Found!")
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
