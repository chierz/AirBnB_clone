#!/usr/bin/python3
"""
This module defines a class MyConsole
"""
import cmd
import sys
import re
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

    def do_count(self, args):
        if args == "":
            print("**class name missing **")
            return(HBNBCommand.check_isatty())
        elif args not in HBNBCommand.class_list():
            print("**class doesn't exist **")
            return (HBNBCommand.check_isatty())
        class_name = HBNBCommand.class_dict()
        class_name = class_name[args]
        class_obj = storage.all()
        obj_list = class_obj.values()
        if obj_list != []:
            count = 0
            for obj in obj_list:
                if type(obj) is class_name:
                    count += 1
            print(count)
            return (HBNBCommand.check_isatty())
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
        class_id = argv[1]
        if '"' in class_id:
            class_id = class_id.split('"')
            class_id = class_id[1]
        for obj in all_obj_dict.values():
            if class_id == obj.id:
                print(obj)
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
        class_id = argv[1]
        
        if '"' in class_id:
            class_id = class_id.split('"')
            class_id = class_id[1]
        class_id = argv[0] + "." + class_id
        try:
            if all_obj_dict[class_id]:
                del all_obj_dict[class_id]
                storage.save()
                return (HBNBCommand.check_isatty())
        except KeyError as e:
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
        class_id = argv[1]
        if '"' in class_id:
            class_id = class_id.split('"')
            class_id = class_id[1]
            class_id = argv[0] + "." + class_id
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

    def precmd(self, line):
        line_list = line.split(" ")
<<<<<<< HEAD
        word_cmd = re.match(r"(\w+)\.(\w+)\(([^)]*)\)", line_list[0])
        if word_cmd is not None:
            line = HBNBCommand.args_formatter(line_list[0])
=======
        word_cmd = re.match(r"(\w+)\.(\w+)\(\s*\"?\w*\"?\s*\)", line_list[0])
        if word_cmd is not None:
            cmd_list = line_list[0].split(".")
            my_list = cmd_list[1].split(')')
            my_list = my_list[0].split('(')
            if my_list[1] != '':
                
                id_obj = my_list[1].split('"')
            print(my_list)
            line = " ".join(line_list)
>>>>>>> f99da3d0e2fb0546fdfcc40e465e3051c3c89292
            return super().precmd(line)
        return super().precmd(line)

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
    @staticmethod
    def args_formatter(my_str): 
        my_str = my_str.split(".")
        cls_name = my_str[0]
        com = my_str[1][: my_str[1].index("(")]
        args = my_str[1][my_str[1].index("("): ]
        string = ""
        for ch in args:
            if ch == "," or ch == "=" or ch == "(" or ch == ")":
                string += " "
                continue
            string += ch 
        cmd_args = com + " " + cls_name + string
        return cmd_args

    @classmethod
    def class_dict(cls):
        return {
                "User": User,
                "Place": Place,
                "Amenity": Amenity,
                "City": City,
                "State": State,
                "Review": Review,
                "BaseModel": BaseModel,
                }


if __name__ == "__main__":
    HBNBCommand().cmdloop()
