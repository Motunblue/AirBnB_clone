#!/usr/bin/env python3
"""
    Contains the Console class for the project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The command interpreter

    Attributes:
        prompt(str): The prompt to use for the interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help(self, arg):
        """Help command"""
        print("")

    def do_EOF(self, arg):
        """CTRL-D command to exit the interpreter"""
        print("")
        return True

    def emptyline(self, line):
        """continue on encounter with an empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
