import actions


class CommandManager:
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
                flags=[self.__supported_flags[flag] for flag in ["config", "default"]],
                method=actions.ls,
            ),
            "reset": self._Command(
                name="reset",
                description="delete configuration and remove pre-commit hooks",
                flags=[self.__supported_flags[flag] for flag in ["config", "hook"]],
                method=actions.reset,
            ),
        }

    def generate_description(self):
        description = "Manage pre-commit hooks for static analysis and testing libs  \n\ncommands:\n"
        for command in self.__supported_commands:
            description += f"  {command}{' '*(15-len(command))} {self.__supported_commands[command].description}\n"
        return description

    @property
    def supported_flags(self):
        return self.__supported_flags

    @property
    def supported_commands(self):
        return self.__supported_commands

    class _Flag:
        def __init__(self, name, aliases, message):
            self.__name = name
            self.__aliases = aliases
            self.__message = message

        @property
        def name(self):
            return self._Flag__name

        @property
        def aliases(self):
            return self._Flag__aliases

        @property
        def message(self):
            return self._Flag__message

    class _Command:
        def __init__(self, name, description, flags, method):
            self.__name = name
            self.__description = description
            self.__flags = flags
            self.__method = method

        @property
        def name(self):
            return self._Command__name

        @property
        def description(self):
            return self._Command__description

        @property
        def flags(self):
            return self._Command__flags

        @property
        def method(self):
            return self._Command__method
