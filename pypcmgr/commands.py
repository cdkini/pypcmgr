import actions


class CommandManager:
    """Wrapper around all supported pypcmgr commands and their related flag_names.

    Attributes:
        __supported_flags (Dict[str, _Flag]): Details all supported flag_names and their attributes.
        __supported_commands (Dict[str, _Command]): Details all supported commands and their attributes.
        __description (str): Message detailing all commands and their usage. To be utilized in --help flag.

    """

    def __init__(self):
        self.__supported_flags = {
            "config": self._Flag(
                name="config",
                aliases=["-c", "--config"],
                description="Open to implement!",
            ),
            "default": self._Flag(
                name="default",
                aliases=["-d", "--default"],
                description="Open to implement!",
            ),
            "recursive": self._Flag(
                name="recursive",
                aliases=["-r", "--recursive"],
                description="Open to implement!",
            ),
            "hook": self._Flag(
                name="hook", aliases=["-H", "--hook"], description="Open to implement!"
            ),
        }

        self.__supported_commands = {
            "run": self._Command(
                name="run",
                description="run configured tools",
                flag_names=[
                    self.__supported_flags[flag]
                    for flag in ["config", "default", "recursive"]
                ],
                method=actions.run,
            ),
            "config": self._Command(
                name="config",
                description="generate a prompt to set up configuration",
                flag_names=[self.__supported_flags[flag] for flag in ["default"]],
                method=actions.config,
            ),
            "hook": self._Command(
                name="hook",
                description="create pre-commit hooks for all configured tools",
                flag_names=[
                    self.__supported_flags[flag] for flag in ["config", "default"]
                ],
                method=actions.hook,
            ),
            "ls": self._Command(
                name="ls",
                description="list out all configured tools and pre-commit hooks",
                flag_names=[
                    self.__supported_flags[flag] for flag in ["config", "default"]
                ],
                method=actions.ls,
            ),
            "reset": self._Command(
                name="reset",
                description="delete configuration and remove pre-commit hooks",
                flag_names=[
                    self.__supported_flags[flag] for flag in ["config", "hook"]
                ],
                method=actions.reset,
            ),
        }

        description = "Manage pre-commit hooks for static analysis and testing libs  \n\ncommands:\n"
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
            flag_names (List[str]): Names of applicable flags that alter command's functionality.
            method (actions.func): Associated action to be invoked when command is called.

        Attributes:
            __name (str): See 'name' in Args
            __description (str): See 'description' in Args
            __flag_names (List[str]): See 'flag_names' in Args
            __method (actions.func): See 'method' in Args

        """

        def __init__(self, name, description, flag_names, method):
            self.__name = name
            self.__description = description
            self.__flag_names = flag_names
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
        def flag_names(self):
            """List[str]: getter for __flag_names"""
            return self._Command__flags

        @property
        def method(self):
            """func: getter for __method"""
            return self._Command__method
