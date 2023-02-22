#!/usr/bin/python3
"""  Test test test test test test test test EExtended discussion of my module. """


import cmd
import json
from models import storage
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Each command handled by a specific method """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ Quit command to exit the program """
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_create(self, className=None):
        """ Create a new instance of a class, save instance info to json.file
        and print id """
        if className is None or className == "":
            print("** class name missing **")
        else:
            try:
                new_model = eval(className + str("()"))
                new_model.save()
                print(new_model.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arguments):
        """ Prints the string representation of an instance """

        listOfArg = arguments.split(" ")
        jsonDict = storage.all()
        try:
            instanc = str(listOfArg[0]) + "." + str(listOfArg[1])
        except:
            instanc = "None"
            listOfArg.append("")

        if listOfArg[0] == "":
            print("** class name missing **")
        elif listOfArg[1] == "":
            print("** instance id missing **")
        elif not str(listOfArg[0]) in str(jsonDict):
            print("** class doesn't exist **")
        elif not instanc in jsonDict:
            print("** no instance found **")
        else:
            print(jsonDict[instanc])

    def do_destroy(self, arguments):
        """ Deletes an instance based on the class name and id """

        listOfArg = arguments.split(" ")
        jsonDict = storage.all()
        try:
            instanc = str(listOfArg[0]) + "." + str(listOfArg[1])
        except:
            instanc = "None"
            listOfArg.append("")

        if listOfArg[0] == "":
            print("** class name missing **")
        elif listOfArg[1] == "":
            print("** instance id missing **")
        elif not str(listOfArg[0]) in str(jsonDict):
            print("** class doesn't exist **")
        elif not instanc in jsonDict:
            print("** no instance found **")
        else:
            del jsonDict[str(instanc)]
            storage.save()

    def do_all(self, className):
        """ Prints all string representation of all instances """
        jsonDict = storage.all()
        allObj = []
        if className == "":
            for instance in jsonDict:
                allObj.append(str(jsonDict[instance]))
        else:
            for instance in jsonDict:
                if className in instance:
                    allObj.append(str(jsonDict[instance]))
        print(allObj)

    def do_update(self, line):
        """ Quit command to exit the program """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
