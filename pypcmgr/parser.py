import argparse
import textwrap
import os

from __init__ import __version__


class Parser:
    """TODO: Add class description!

    Attributes:
        __description (str):
        __command_manager (CommandManager):

    """

    def __init__(self, description, command_manager):
        self.__command_manager = command_manager
        self.__parser = argparse.ArgumentParser(
            prog="pypcmgr",
            description=description,
            formatter_class=argparse.RawTextHelpFormatter,
        )
        __parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"pypcmgr {__version__}",
            help="show the current version and exit",
        )
        self.__subparsers = __parser.add_subparsers(
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
        for flag in self.__command_manager.supported_flags:
            flag_parser = argparse.ArgumentParser(add_help=False)
            flag_parser.add_argument(
                flag.aliases[0], flag.aliases[1], action="store_true", help=flag.message
            )
            flags[flag] = flag_parser
        for command in self.__command_manager.supported_commands:
            command_parser = self.__subparsers.add_parser(
                command,
                description=command.description,
                parents=[flags[flag.name] for flag in command.flags],
            )
            command_parser.set_defaults(func=command.method)

    def parse(self):
        """TODO: Add method docstring!

        Args:
            None

        Returns:
            None
        
        """
        args = __parser.parse_args()
        args.func()
