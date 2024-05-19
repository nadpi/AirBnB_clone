#!/usr/bin/python3
'''console'''
import cmd, sys
from models.base_model import BaseModel
import models


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

    def do_create(self, line):
        model = BaseModel()
        if len(line) == 0:
            print("** class name missing **")
        elif line != model.__class__.__name__:
            print("** class doesn't exist **")
        else:
            model.save()
            print(model.id)

    def do_show(self, line):
        model = BaseModel()
        if len(line) == 0:
            print("** class name missing **")
            pass
        else:
            strlist = line.split(" ")
            className = strlist[0]
            classID = None
            if len(strlist) == 2:
                classID = strlist[1]
            if className != model.__class__.__name__:
                print("** class doesn't exist **")
            elif classID == None:
                print("** instance id missing **")
            elif className+'.'+classID not in models.storage.all():
                print("** no instance found ** ")
            else:
                dictObj = models.storage.all()
                print(str(dictObj[className+'.'+classID]))

    def do_destroy(self, line):
        model = BaseModel()
        if len(line) == 0:
            print("** class name missing **")
            pass
        else:
            strlist = line.split(" ")
            className = strlist[0]
            classID = None
            if len(strlist) == 2:
                classID = strlist[1]
            if className != model.__class__.__name__:
                print("** class doesn't exist **")
            elif classID == None:
                print("** instance id missing **")
            elif className+'.'+classID not in models.storage.all():
                print("** no instance found ** ")
            else:
                dictObj = models.storage.all()
                del dictObj[className+'.'+classID]
     
    def do_all(self, line):
        model = BaseModel()
        if line != model.__class__.__name__:
                print("** class doesn't exist **")
        else:
            print(list(models.storage.all()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()