import argparse
import textwrap
import os

from __init__ import __version__


class Parser:
    """TODO: Add class description!

    Attributes:
        __command_manager (commands.CommandManager):

    """

    def __init__(self, command_manager):
        self.__command_manager = command_manager
        self.__parser = argparse.ArgumentParser(
            prog="pypcmgr",
            description=command_manager.description,
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self.__parser.add_argument(
            "-v",
            "--version",
            action="version",
            version="pypcmgr {}".format(__version__),
            help="show the current version and exit",
        )
        self.__subparsers = self.__parser.add_subparsers(
            help="run '[cmd] -h' for additional details and options", metavar="cmd"
        )

    def setup(self):
        """TODO: Add method docstring!

        Args:
            None

        Returns:
            None

        """
        flags = {}
        for flag, attrs in self.__command_manager.supported_flags.items():
            flag_parser = argparse.ArgumentParser(add_help=False)
            flag_parser.add_argument(
                attrs.aliases[0],
                attrs.aliases[1],
                action="store_true",
                help=attrs.message,
            )
            flags[flag] = flag_parser
        for command, attrs in self.__command_manager.supported_commands.items():
            command_parser = self.__subparsers.add_parser(
                command,
                description=attrs.description,
                parents=[flags[flag.name] for flag in attrs.flags],
            )
            command_parser.set_defaults(func=attrs.method)

    def parse(self):
        """TODO: Add method docstring!

        Args:
            None

        Returns:
            None
        
        """
        args = self.__parser.parse_args()
        if "func" not in args:
            raise ValueError("No valid command or flag passed")
        return args
