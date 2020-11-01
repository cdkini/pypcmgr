import argparse
import textwrap
import os

from __init__ import __version__


class Parser:
    def __init__(self, description, command_manager):
        self.command_manager = command_manager
        self.parser = argparse.ArgumentParser(
            prog="pypcmgr",
            description=description,
            formatter_class=argparse.RawTextHelpFormatter,
        )
        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"pypcmgr {__version__}",
            help="show the current version and exit",
        )
        self.subparsers = parser.add_subparsers(
            help="run '[cmd] -h' for additional details and options", metavar="cmd"
        )

    def setup(self):
        flags = {}
        for flag in self.command_manager.supported_flags:
            flag_parser = argparse.ArgumentParser(add_help=False)
            flag_parser.add_argument(
                flag.aliases[0], flag.aliases[1], action="store_true", help=flag.message
            )
            flags[flag] = flag_parser
        for command in self.command_manager.supported_commands:
            command_parser = self.subparsers.add_parser(
                command,
                description=command.description,
                parents=[flags[flag.name] for flag in command.flags],
            )
            command_parser.set_defaults(func=command.method)

    def parse(self):
        args = parser.parse_args()
        args.func()
