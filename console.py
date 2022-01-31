#!/usr/bin/python3
"""command interpreter"""
import cmd
import shlex
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """if end of file exit"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, name):
        """Creates a new instance of BaseModel"""
        if name:
            try:
                cl = eval(name)()
                cl.save()
                print(cl.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """ Prints the string representation of an
        instance based on the class name and id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage.reload()
        d = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        k = args[0] + "." + args[1]
        try:
            print(d[k])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id.'''

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        storage.reload()
        d = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            del d[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        '''
        Prints all string representation of all instances
        based or not on the class name.
        '''
        li = []
        storage.reload()
        d = storage.all()
        try:
            if len(args) > 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in d.items():
            if len(args) > 0:
                if type(val) is eval(args):
                    li.append(str(val))
            else:
                li.append(str(val))
        print(li)

    def do_update(self, args):
        '''
        Update an instance based on the class name and id
        by adding or updating attribute
        '''
        storage.reload()
        d = storage.all()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            value = d[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(value, args[2], args[3])
        value.save()

    def do_count(self, args):
        """retrieve the number of instances of a class"""
        li = []
        storage.reload()
        d = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in d.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    li.append(val)
            else:
                li.append(val)
        print(len(li))

    def default(self, args):
        '''extra modules'''
        m = {"all": self.do_all, "count": self.do_count,
             "show": self.do_show, "update": self.do_update,
             "destroy": self.do_destroy}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            pa = args[0] + " " + args[2]
            m[args[1]](pa)
        except NameError:
            print("*** Unknown syntax:", args[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
