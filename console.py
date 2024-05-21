#!/usr/bin/python3
'''console'''
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    '''cmd'''
    prompt = '(hbnb) '
    file = None
    classes = {"User": User, "BaseModel": BaseModel, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            model = self.classes[line]()
            model.save()
            print(model.id)

    def do_show(self, line):
        if len(line) == 0:
            print("** class name missing **")
            pass
        else:
            strlist = line.split(" ")
            className = strlist[0]
            classID = None
            if len(strlist) == 2:
                classID = strlist[1]
            if className not in self.classes.keys():
                print("** class doesn't exist **")
            elif classID is None:
                print("** instance id missing **")
            elif className+'.'+classID not in models.storage.all():
                print("** no instance found **")
            else:
                dictObj = models.storage.all()
                print(str(dictObj[className+'.'+classID]))

    def do_update(self, line):
        if len(line) == 0:
            print("** class name missing **")
            pass
        else:
            strlist = line.split(" ")
            className = strlist[0]
            classID = None
            attrName = None
            attrValue = None
            if len(strlist) == 1:
                print("** instance id missing **")
                pass
            elif len(strlist) < 3:
                print("** attribute name missing **")
                pass
            elif len(strlist) == 3:
                print("** value missing **")
                pass
            elif len(strlist) >= 4:
                classID = strlist[1]
                attrName = strlist[2]
                attrValue = strlist[3]
                if className not in self.classes.keys():
                    print("** class doesn't exist **")
                elif className+'.'+classID not in models.storage.all():
                    print("** no instance found **")
                else:
                    model = self.classes[className]()
                    model.attrName = attrValue

    def do_destroy(self, line):
        if len(line) == 0:
            print("** class name missing **")
            return
        else:
            strlist = line.split(" ")
            className = strlist[0]
            classID = None
            if len(strlist) == 2:
                classID = strlist[1]
                return
            if className not in self.classes.keys():
                print("** class doesn't exist **")
            elif classID is None:
                print("** instance id missing **")
            elif className+'.'+classID not in models.storage.all():
                print("** no instance found **")
            else:
                dictObj = models.storage.all()
                del dictObj[className+'.'+classID]
                models.storage.save()

    def do_all(self, line):
        if line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            print(list(models.storage.all()))


