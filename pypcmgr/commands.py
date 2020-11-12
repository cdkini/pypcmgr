import actions


class CommandManager:
    """Wrapper around all supported pypcmgr commands and their related flags.

    Attributes:
        __supported_flags (Dict[str, _Flag]): Details all supported flags and their attributes.
        __supported_commands (Dict[str, _Command]): Details all supported commands and their attributes.
        __description (str): Message detailing all commands and their usage. To be utilized in --help flag.

    """

    def __init__(self):
        self.__supported_flags = {
            "config": self._Flag(
                name="config",
                aliases=["-c", "--config"],
                description="only apply to configured tools (ls, reset) | call 'config' before running (run, hook)",
            ),
            "default": self._Flag(
                name="default",
                aliases=["-d", "--default"],
                description="set up flake8 and black (config) | \
                    call 'config' with defaults before running (run, hook)",
            ),
            "hook": self._Flag(
                name="hook",
                aliases=["-H", "--hook"],
                description="only apply to pre-commit hooks (ls, reset)",
            ),
        }

        self.__supported_commands = {
            "run": self._Command(
                name="run",
                description="run configured tools",
                flags=[self.__supported_flags[flag] for flag in ["config", "default"]],
                method=actions.run,
            ),
            "config": self._Command(
                name="config",
                description="generate a prompt to set up configuration",
                flags=[self.__supported_flags[flag] for flag in ["default"]],
                method=actions.config,
            ),
            "hook": self._Command(
                name="hook",
                description="create pre-commit hooks for all configured tools",
                flags=[self.__supported_flags[flag] for flag in ["config", "default"]],
                method=actions.hook,
            ),
            "ls": self._Command(
                name="ls",
                description="list out all configured tools and pre-commit hooks",
                flags=[self.__supported_flags[flag] for flag in ["config", "hook"]],
                method=actions.ls,
            ),
            "reset": self._Command(
                name="reset",
                description="delete configuration and remove pre-commit hooks",
                flags=[self.__supported_flags[flag] for flag in ["config", "hook"]],
                method=actions.reset,
            ),
        }

        description = (
            "manage pre-commit hooks for static analysis libs  \n\ncommands:\n"
        )

        for command in self.__supported_commands:
            spacing = " " * (15 - len(command))
            command_description = self.__supported_commands[command].description
            description += "  {}{} {}\n".format(command, spacing, command_description)
        self.__description = description

    @property
    def supported_flags(self):
        """Dict[str, _Flag]: getter for __supported_flags"""
        return self.__supported_flags

    @property
    def supported_commands(self):
        """Dict[str, _Command]: getter for __supported_commands"""
        return self.__supported_commands

    @property
    def description(self):
        """str: getter for __description"""
        return self.__description

    class _Flag:
        """Container around flag or options data to be attached to commands.

        Args:
            name (str): Long form name of flag.
            aliases (List[str]): Identifiers when used in command line (prepended by '-' or '--').
            description (str): Help message to be displayed to user.

        Attributes:
            __name (str): String passed in as an argument.
            __aliases (List[str]): List passed in as an argument.
            __description (str): String passed in as an argument.

        """

        def __init__(self, name, aliases, description):
            self.__name = name
            self.__aliases = aliases
            self.__description = description

        @property
        def name(self):
            """str: getter for __name"""
            return self._Flag__name

        @property
        def aliases(self):
            """List[str]: getter for __aliases"""
            return self._Flag__aliases

        @property
        def description(self):
            """str: getter for __description"""
            return self._Flag__description

    class _Command:
        """Container around flags, actions, and other data relevant to pypcmgr commands.

        Args (__init__):
            name (str): Long form name of command.
            description (str): Help message to be displayed to user.
            flags (List[str]): Names of applicable flags that alter command's functionality.
            method (actions.func): Associated action to be invoked when command is called.

        Attributes:
            __name (str): See 'name' in Args
            __description (str): See 'description' in Args
            __flags (List[str]): See 'flags' in Args
            __method (actions.func): See 'method' in Args

        """

        def __init__(self, name, description, flags, method):
            self.__name = name
            self.__description = description
            self.__flags = flags
            self.__method = method

        @property
        def name(self):
            """str: getter for __name"""
            return self._Command__name

        @property
        def description(self):
            """str: getter for __description"""
            return self._Command__description

        @property
        def flags(self):
            """List[str]: getter for __flags"""
            return self._Command__flags

        @property
        def method(self):
            """func: getter for __method"""
            return self._Command__method
