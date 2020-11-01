from actions import Action


class CommandManager:
    """TODO: Add class docstring

    Attributes:
        __supported_flags (Dict[_Flag]):
        __supported_commands (Dict[_Command]): 

    """

    def __init__(self):
        self.__supported_flags = {
            "config": self._Flag("config", ["-c", "--config"], "Open to implement!"),
            "default": self._Flag("default", ["-d", "--default"], "Open to implement!"),
            "recursive": self._Flag(
                "recursive", ["-r", "--recursive"], "Open to implement!"
            ),
            "hook": self._Flag("hook", ["-H", "--hook"], "Open to implement!"),
        }

        self.__supported_commands = {
            "run": self._Command(
                name="run",
                description="run configured tools",
                flags=[
                    self.__supported_flags[flag]
                    for flag in ["config", "default", "recursive"]
                ],
                method=Action.run,
            ),
            "config": self._Command(
                name="config",
                description="generate a prompt to set up configuration",
                flags=[self.__supported_flags[flag] for flag in ["default"]],
                method=Action.config,
            ),
            "hook": self._Command(
                name="hook",
                description="create pre-commit hooks for all configured tools",
                flags=[self.__supported_flags[flag] for flag in ["config", "default"]],
                method=Action.hook,
            ),
            "ls": self._Command(
                name="ls",
                description="list out all configured tools and pre-commit hooks",
                flags=[self.__supported_flags[flag] for flag in ["config", "default"]],
                method=Action.ls,
            ),
            "reset": self._Command(
                name="reset",
                description="delete configuration and remove pre-commit hooks",
                flags=[self.__supported_flags[flag] for flag in ["config", "hook"]],
                method=Action.reset,
            ),
        }

    def generate_description(self):
        """TODO: Add method docstring

        Args:
            None

        Returns:
            str: 

        """
        description = "Manage pre-commit hooks for static analysis and testing libs  \n\ncommands:\n"
        for command in self.__supported_commands:
            description += f"  {command}{' '*(15-len(command))} {self.__supported_commands[command].description}\n"
        return description

    @property
    def supported_flags(self):
        """Dict[_Flag]: getter for __supported_flags"""
        return self.__supported_flags

    @property
    def supported_commands(self):
        """Dict[_Command]: getter for __supported_commands"""
        return self.__supported_commands

    class _Flag:
        """TODO: Add class docstring

        Attributes:
            __name (str):
            __aliases (List[str]):
            __message (str):

        """

        def __init__(self, name, aliases, message):
            self.__name = name
            self.__aliases = aliases
            self.__message = message

        @property
        def name(self):
            """str: getter for __name"""
            return self._Flag__name

        @property
        def aliases(self):
            """List[str]: getter for __aliases"""
            return self._Flag__aliases

        @property
        def message(self):
            """str: getterfor __message"""
            return self._Flag__message

    class _Command:
        """TODO: Add class description!

        Attributes:
            __name (str):
            __description (str):
            __flags (List[str]):
            __method (Action.function):

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
            """function: getter for __method"""
            return self._Command__method
