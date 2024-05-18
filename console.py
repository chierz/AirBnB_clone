#!/usr/bin/python3
"""
This module defines a class MyConsole
"""
import cmd
import sys
from shlex import split
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models import storage


# precmd --> parseline ---> onecmd --> postcmd
class HBNBCommand(cmd.Cmd):
    """Defines a class MyConsole"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit the command line intepreter\n"""
        return True

    def do_EOF(self, args):
        """exit the command line interpreter on keyboard interrupt\n"""
        print()
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)\n
        """
        if args == "":
            print("** class name missing **")
            return (HBNBCommand.check_isatty())
        elif args not in HBNBCommand.class_list():
            print("** class doesn't exist **")
            return (HBNBCommand.check_isatty())
        if args == "User":
            my_model = User()
        elif args == "BaseModel":
            # create object of BaseModel
            my_model = BaseModel()
        elif args == "Place":
            my_model = Place()
        elif args == "Amenity":
            my_model = Amenity()
        elif args == "State":
            my_model = State()
        elif args == "City":
            my_model = City()
        elif args == "Review":
            my_model = Review()
        my_model.save()
        print(my_model.id)
        return (HBNBCommand.check_isatty())

    def do_show(self, args):
        """Prints the string representation of an instance\n
        """
        if len(args) == 0:
            print("** class name missing **")
            return (HBNBCommand.check_isatty())
        argv = args.split(" ")
        if argv[0] not in HBNBCommand.class_list():
            print("** class doesn't exist **")
            return (HBNBCommand.check_isatty())
        elif len(argv) == 1:
            print("** instance id missing **")
            return (HBNBCommand.check_isatty())
        storage.reload()
        all_obj_dict = storage.all()
        class_id = argv[0] + "." + argv[1]
        for key in all_obj_dict.keys():
            if class_id == key:
                print(all_obj_dict[key])
                return (HBNBCommand.check_isatty())
            continue
        print("** no instance found **")
        return (HBNBCommand.check_isatty())

    def do_destroy(self, args):
        """Deletes an instance based on the class name\n
        """
        if args == "":
            print("** class name missing **")
            return (HBNBCommand.check_isatty())
        argv = args.split(" ")
        if argv[0] not in HBNBCommand.class_list():
            print("** class doesn't exist **")
            return (HBNBCommand.check_isatty())
        elif len(argv) == 1:
            print("** instance id missing **")
            return (HBNBCommand.check_isatty())
        storage.reload()
        all_obj_dict = storage.all()
        class_id = argv[0] + "." + argv[1]
        for key in all_obj_dict.keys():
            if key == class_id:
                del all_obj_dict[key]
                storage.save()
                return (HBNBCommand.check_isatty())
            continue
        print("** no instance found **")
        return (HBNBCommand.check_isatty())

    def do_all(self, args):
        """Prints all string representation of all instances\n
        """
        if args not in HBNBCommand.class_list() and args != "":
            print("** class doesn't exist **")
            return (HBNBCommand.check_isatty())
        storage.reload()
        all_obj_dict = storage.all()
        all_obj_list = []
        for key in all_obj_dict.keys():
            all_obj_list.append(str(all_obj_dict[key]))
        print(all_obj_list)
        return (HBNBCommand.check_isatty())

    def do_update(self, args):
        """Updates an instance based on the class name\n
        """
        if args == "":
            print("** class name missing **")
            return (HBNBCommand.check_isatty())
        argv = args.split(" ")
        if argv[0] not in HBNBCommand.class_list():
            print("** class doesn't exist **")
            return (HBNBCommand.check_isatty())
        elif len(argv) == 1:
            print("** instance id missing **")
            return (HBNBCommand.check_isatty())
        storage.reload
        all_obj_dict = storage.all()
        class_id = argv[0] + "." + argv[1]
        for key in all_obj_dict.keys():
            if class_id == key:
                if len(argv) == 2:
                    print("** attribute name missing **")
                    return (HBNBCommand.check_isatty())
                elif len(argv) == 3:
                    print("** value missing **")
                    return (HBNBCommand.check_isatty())
                setattr(all_obj_dict[key], argv[2], argv[3])
                all_obj_dict[key].save()
                return (HBNBCommand.check_isatty())
        print("** no instance found **")
        return (HBNBCommand.check_isatty())

    def default(self, line):
        super().default(line)
        return (HBNBCommand.check_isatty())

    def emptyline(self):
        """does nothing"""
        pass

    @classmethod
    def check_isatty(cls):
        """check if standard input is issued from the terminal\n"""
        if not sys.stdin.isatty():
            return True
        return False

    @classmethod
    def class_list(cls):
        cl1 = ["BaseModel", "Review", "User"]
        cl2 = ["Place", "City", "Amenity", "State"]
        cl2.extend(cl1)
        return cl2


if __name__ == "__main__":
    HBNBCommand().cmdloop()
