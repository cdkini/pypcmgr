flake8 - Wrapper around pyflakes, pycodestyle and mccabe. Considered a single tool here because it's a must for every Python project to use those tools combined. Also, it augments pyflakes and mccabe with error codes.

pylint - Most intelligent Python linter. It's able to infer a lot using only static analysis, thereby finding subtle bugs.

pytest - Recommended

unittest - builtin

black - uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting.

yapf - Yet another Python formatter

vulture - Find dead code

isort - A Python utility / library to sort imports or check them

pep8-naming: Naming Convention checker for Python

pycycle - Tool for pinpointing circular imports in Python

pydocstyle - Docstring style checker

dodgy - Looks at Python code to search for things which look "dodgy" such as passwords or diffs.

scspell3k - Spell checker for source code



https://github.com/vintasoftware/python-linters-and-code-analysis

```
Usage: pypcmgr [OPTIONS] [SRC]...

  Generates pre-commits hooks for popular Python static analysis tools.

Options:
  -h, --help              Show this message and exit
  
  -v, --version           Show the version and exit
  
  -i, --interactive       Generate a prompt to set up user config
  
  -c, --config            Read out current configuration if available
  
  -r, --recursive         Recursively run all configured tools
  
  --reset                 Resets any pre-commit hooks made by pypcmgr and deletes .pypcmgrconfig
```



Should add all of these utilities to a pre-commit
Create command line prompt asking which modules the user wants to add to pre-commit
