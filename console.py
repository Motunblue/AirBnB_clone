#!/usr/bin/env python3
"""
    Contains the Console class for the project
"""


class HBNBCommand(cmd.Cmd):
    """The command interpreter"""
    def do_quit(self):
        """Exit the interpreter on encounter with quit command"""
        return True

    def do_EOF(self):
        """CTRL-D to exit the interpreter"""
        return True

    def help(self):
        """

