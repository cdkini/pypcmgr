import os

from commands import CommandManager
from parser import Parser


def main():
    manager = CommandManager()
    parser = Parser(manager)
    parser.setup()
    args = parser.parse()
    print(args)
    args.func(path=os.getcwd(), flags=args)


if __name__ == "__main__":
    main()

"""
["run", "config", "ls", "hook", "reset"]
config: run, ls, hook, reset
default: run, config, hook
recursive: run
hook: config, reset

- run                 run configured utilities
  -c / --config         call 'config' cmd before running
  -d / --default        set up default configuration (pytest, black, flake8) before running
  -r / --recursive      recursively run all configured tools
- config              generate a prompt to set up user configuration
  -d / --default        set up default configuration (pytest, black, flake8)
- ls                  list out all configured tools and pre-commit hooks
  -c / --config         list out just configured tools
  --hook                list out just hooks
- hook                create pre-commit hooks for all configured tools
  -c / --config         call 'config' cmd before creating hooks
  -d / --default        set up default configuration (pytest, black, flake8) creating hooks
- reset               delete configuration and remove all pre-commit hooks
  -c / --config         only remove configuration
  --hook                only remove pre-commit hooks
- none
  -v / --version        show the current version and exit
  -h / --help           show this help message and exit

If no command is passed, raise an error and show this help message.
"""
