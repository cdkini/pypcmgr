import argparse

from __init__ import __version__


class Parser:
    """Wrapper around argparse.ArgumentParser.

    Responsible for instantiating ArgumentParser, updating description, and creating commands and related flags.

    Args (__init__):
        command_manager (commands.CommandManager): All supported commands and flags and their related actions.

    Attributes:
        __command_manager (commands.CommandManager): See 'command_manager' in Args
        __parser (argparse.ArgumentParser): Parent parser responsible for --help and --version.
        __subparsers (argparse.ArgumentParser): Parsers for individual commands and flags.

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
        """Links flags and actions to supported commands.

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
        """Parses command line input to identify appropriate command and flags passed by user.

        Returns:
            argparse.Namespace: Contains flags and action for parsed command.

        Raises:
            ValueError: Raised if an invalid command or flag is passed.

        """
        args = self.__parser.parse_args()
        if "func" not in args:
            raise ValueError("No valid command or flag passed")
        return args
