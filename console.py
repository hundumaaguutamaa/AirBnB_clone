#!/usr/bin/python3

import cmd
import json
import sys
import models

from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review

""" HBnB console"""

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    models = {
    "Amenity",
    "BaseModel",
    "City",
    "Place",
    "User",
    "Review"
    "State",

    }

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
    def do_destroy(self, arg):
        """Delete based on a class name of a given id."""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects_dict = models.storage.all()
            instance_key = "{}.{}".format(args[0], args[1])
            instance = objects_dict.get(instance_key)
            if instance:
                del objects_dict[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances
        based on the class name.
        """
        objects_dict = models.storage.all()
        instance_list = []

        if not arg:
            for key in objects_dict:
                instance_list.append(str(objects_dict[key]))
        else:
            class_names = arg.strip()
            if class_names in self.__models:
                for key, value in objects_dict.items():
                    if value.__class__.__name__ == class_names:
                        instance_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return

        print(instance_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id.
            And saves in to JSON file.      
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_names = args[0]
        if class_names not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) <= 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if obj_key not in obj_dict:
            print("** no instance found **")
            return

        instance = obj_dict[obj_key]

        if len(args) <= 2:
            print("** attribute name missing **")
            return

        attrib_name = args[2]
        if len(args) <= 3:
            print("** value missing **")
            return

        attrib_value = args[3]
        setattr(instance, attrib_name, attrib_value)
        instance.save()
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
