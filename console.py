#!/usr/bin/python3
""" Create prompt using cmd models """
import cmd
import json
from models import storage
from models.engine import file_storage
# need to import each and every new class created following the BaseModel import style:
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Each command handled by a specific method """

    prompt = '(hbnb) '
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
        # Mikalach add for task 8
        """ if arg == "User":
            obj = User()
            models.storage.new(obj)
            models.storage.save()
            print(obj.id)"""

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
        elif not str(listOfArg[0]) in str(jsonDict):
            print("** class doesn't exist **")
        # test if instance of the class name (ex: models.Basemodel.1234-1234)
        elif not instanc in jsonDict:
            print("** no instance found **")
        else:
            print(jsonDict[instanc])
        #Mikalach added for task 8
        """ if obj_type == "User":
            obj = models.storage.get(User, obj_id)
            print(obj)"""

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
        elif not str(listOfArg[0]) in str(jsonDict):
            print("** class doesn't exist **")
        # test if instance of the class name (ex: models.Basemodel.1234-1234)
        elif not instanc in jsonDict:
            print("** no instance found **")
        else:
            del jsonDict[str(instanc)]
            storage.save()

        #Mikalach added for task 8
        """ if obj_type == "User":
            obj = models.storage.get(User, obj_id)
            models.storage.delete(obj)
            models.storage.save()"""

    # check if line (user input) is 'all'
    def do_all(self, className):
        """ Prints all string representation of all instances """
        jsonDict = storage.all()
        allObj = []
        if className == "":
            """ print every stored instance """
            for instance in jsonDict:
                allObj.append(str(jsonDict[instance]))
        else:
            """ print every stored instance of a specific class"""
            for instance in jsonDict:
                if className in instance:
                    allObj.append(str(jsonDict[instance]))
        print(allObj)
        # Mikalach added for task 8
        """if arg == "User":
            objects = models.storage.all(User)
            print([str(obj) for obj in objects.values()])"""

    # check if line (user input) is 'update'
    def do_update(self, line):
        """ Quit command to exit the program """
        #Mikalach added for task 8
        """ if obj_type == "User":
            obj = models.storage.get(User, obj_id)
            setattr(obj, attr_name, attr_value)"""



if __name__ == '__main__':
    HBNBCommand().cmdloop()
