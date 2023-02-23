#!/usr/bin/python3
""" Create prompt using cmd models """
import cmd
import json
from models import storage
from models.engine import file_storage
# need to import each and every new class created following the BaseModel import style:
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Each command handled by a specific method """

    prompt = '(hbnb) '
    __classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
    # ---------- Quit commands

    # check if line (user input) is EOF (ctrl + d) or 'quit'
    def do_EOF(self, line):
        """ Quit command to exit the program """
        print()
        return True

    # check if line (user input) is EOF (ctrl + d) or 'quit'
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        return 0
    # ---------- Other commands

    # check if line (user input) is 'create'
    def do_create(self, className=None):
        """ Create a new instance of a class, save instance info to json.file and print id """
        if className is None or className == "":
            print("** class name missing **")
        else:
            try:
                new_model = eval(className + str("()"))
                new_model.save()
                print(new_model.id)
            except:
                print("** class doesn't exist **")

    # check if line (user input) is 'show'
    def do_show(self, arguments):
        """ Prints the string representation of an instance """


        """ initialisation """
        # separete command arguments in a list (listOfArg[0] == className & listOfArg[1] == id)
        listOfArg = arguments.split(" ")
        jsonDict = storage.all()
        try:
            instanc = str(listOfArg[0]) + "." + str(listOfArg[1])
        except:
            instanc = "None"
            listOfArg.append("")

        """ All the tests + final print """
        # test if class name exist
        if listOfArg[0] == "":
            print("** class name missing **")
        # test if id is missing
        elif listOfArg[1] == "":
            print("** instance id missing **")
        # test if class name is wrong
        elif not str(listOfArg[0]) in HBNBCommand.__classes:
            print("** class doesn't exist **")
        # test if instance of the class name (ex: models.Basemodel.1234-1234)
        elif not instanc in jsonDict:
            print("** no instance found **")
        else:
            print(jsonDict[instanc])

    # check if line (user input) is 'destroy'
    def do_destroy(self, arguments):
        """ Deletes an instance based on the class name and id """


        """ initialisation """
        # separete command arguments in a list (listOfArg[0] == className & listOfArg[1] == id)
        listOfArg = arguments.split(" ")
        jsonDict = storage.all()
        try:
            instanc = str(listOfArg[0]) + "." + str(listOfArg[1])
        except:
            instanc = "None"
            listOfArg.append("")

        """ All the tests + final print """
        # test if class name exist
        if listOfArg[0] == "":
            print("** class name missing **")
        # test if id is missing
        elif listOfArg[1] == "":
            print("** instance id missing **")
        # test if class name is wrong
        elif not str(listOfArg[0]) in HBNBCommand.__classes:
            print("** class doesn't exist **")
        # test if instance of the class name (ex: models.Basemodel.1234-1234)
        elif not instanc in jsonDict:
            print("** no instance found **")
        else:
            del jsonDict[str(instanc)]
            storage.save()

    # check if line (user input) is 'all'
    def do_all(self, className):
        """ Prints all string representation of all instances """
        jsonDict = storage.all()
        allObj = []
        if className == "":
            """ print every stored instance """
            for instance in jsonDict:
                allObj.append(str(jsonDict[instance]))
                print(allObj)
        else:
            """ print every stored instance of a specific class"""
            if not className in jsonDict:
                print("** class doesn't exist **")
            for instance in jsonDict:
                if className in instance:
                    allObj.append(str(jsonDict[instance]))
                    print(allObj)

    # check if line (user input) is 'update'
    def do_update(self, arguments):
        """ Update an instance """
        listOfArg = arguments.split(" ")
        jsonDict = storage.all()
        try:
            instanc = str(listOfArg[0]) + "." + str(listOfArg[1])
        except:
            instanc = "None"
            listOfArg.append("")

        """ error handle """
        # test if class name exist
        if listOfArg[0] == "":
            print("** class name missing **")
        # test if id is missing
        elif listOfArg[1] == "":
            print("** instance id missing **")
        # test if class name is wrong
        elif not str(listOfArg[0]) in str(jsonDict):
            print("** class doesn't exist **")
        # test if instance of the class name (ex: models.Basemodel.1234-1234)
        elif not instanc in jsonDict:
            print("** no instance found **")
        # test if attribute name is missing
        elif len(listOfArg) == 2:
            print("** attribute name missing **")
        # test if attribute value is missing
        elif len(listOfArg) == 3:
            print("** value missing **")

            """ update function """
        elif len(listOfArg) == 4:
            jsonDict[instanc].__dict__[listOfArg[2]] = listOfArg[3]
            storage.all()[instanc].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
