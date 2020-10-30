<h1 align="center">pypcmgr</h2>
<h3 align="center"><i>Static analysis and git-hook management made painless</i></h3>

pypcmgr is a tool that consolidates some of the post popular Python static analysis tools to help keep your codebase clean and error free.

As of version 1.0.0, the following plug-ins are supported:

```
TESTING
  pytest           Recommended by pypcmgr team
  unittest         builtin
  
LINTING
  flake8           Wrapper around pyflakes, pycodestyle and mccabe. Also, it augments pyflakes and mccabe with error codes
  pylint           Most intelligent Python linter. It's able to infer a lot using only static analysis, thereby finding subtle bugs
  
FORMATTING
  black            uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting
  yapf             Yet another Python formatter

MISCELLAENOUS
  vulture          Find dead code
  isort            A Python utility / library to sort imports or check them
  pep8-naming      Naming Convention checker for Python
  pycycle          Tool for pinpointing circular imports in Python
  pydocstyle       Docstring style checker
  dodgy            Looks at Python code to search for things which look "dodgy" such as passwords or diffs
  scspell3k        Spell checker for source code
```

## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Updates](#Updates)
- [Contributing](#Contributing)
- [Credits](#Credits)
- [License](#License)


## Installation
TBD

## Usage
TBD
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

## Updates
TBD

## Contributing
TBD

## Credits
TBD

## License
The pypcmgr project is licensed under the MIT License Copyright (c) 2020.

See the [LICENSE](https://github.com/cdkini/pypcmgr/blob/master/LICENSE) for information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.



---




https://github.com/vintasoftware/python-linters-and-code-analysis


Should add all of these utilities to a pre-commit
Create command line prompt asking which modules the user wants to add to pre-commit
