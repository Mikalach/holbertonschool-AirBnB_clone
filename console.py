#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models.engine import file_storage
""" Create prompt using cmd models """

class HBNBCommand(cmd.Cmd):
    """ Each command handled by a specific method """

    # {prompt = string} <-- custom prompt name
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
        mdClassName = "models." + str(className)
        with open("file.json", "r", encoding="utf-8") as f:
            jsonString = f.read()
        if className is None or className == "":
            print("** class name missing **")
        elif not className in jsonString:
            print("** class doesn't exist **")
        else:
            new_model = eval(className + str("()"))
            new_model.save()
            print(new_model.id)
        # Mikalach add for task 8
        """if arg == "User":
            obj = User()
            models.storage.new(obj)
            models.storage.save()
            print(obj.id)"""

    # check if line (user input) is 'show'
    def do_show(self, arguments):
        """ Prints the string representation of an instance """

        # separete command arguments in a list (listOfArg[0] == className & listOfArg[1] == id)
        listOfArg = arguments.split(" ")
        mdArg0 = "models." + str(listOfArg[0])
        f = open("file.json", "r", encoding="utf-8")
        jsonDict = json.loads(f.read())
        f.close()
        try:
            mdArg1 = "models." + str(listOfArg[1])
            instanc = str(listOfArg[0]) + "." + str(listOfArg[1])
        except:
            print(listOfArg)
            mdArg1 = "None"
            instanc = "None"
            listOfArg.append("")
        # test if class name exist
        if listOfArg[0] == "":
            print("** class name missing **")

        # test if class name is wrong
        elif not str(listOfArg[0]) in jsonDict:
            print("** class doesn't exist **")

        # test if id is missing
        elif listOfArg[1] == "":
            print("** instance id missing **")

        # test if instance of the class name (ex: models.Basemodel.1234-1234)
        elif not instanc in jsonDict:
            print("** no instance found **")

        else:
            print("[{}] ({}) {}".format(listOfArg[0], listOfArg[1], jsonDict[str(instanc)]))

        #Mikalach added for task 8
        """if obj_type == "User":
            obj = models.storage.get(User, obj_id)
            print(obj)"""

    # check if line (user input) is 'destroy'
    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        # --------------------- COPY PASTE "do_show"
        #Mikalach added for task 8
        if obj_type == "User":
            obj = models.storage.get(User, obj_id)
            models.storage.delete(obj)
            models.storage.save()
    # check if line (user input) is 'all'
    def do_all(self, line):
        """ Quit command to exit the program """
        # Mikalach added for task 8
        if arg == "User":
            objects = models.storage.all(User)
            print([str(obj) for obj in objects.values()])
        return True

    # check if line (user input) is 'update'
    def do_update(self, line):
        """ Quit command to exit the program """
        #Mikalach added for task 8
        if obj_type == "User":
            obj = models.storage.get(User, obj_id)
            setattr(obj, attr_name, attr_value)
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
