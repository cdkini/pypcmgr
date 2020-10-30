<h1 align="center">pypcmgr</h2>
<h3 align="center"><i>Static analysis and git-hook management made painless</i></h3>

pypcmgr is a command line utility that consolidates some of the most popular Python static analysis tools to help keep your codebase clean and error free. Either run it manually or have it set up pre-commit hooks to automate testing, linting, and formatting alongside your workflow.

As of version <b>1.0.0</b>, the following plug-ins are supported:
```
TESTING
  pytest           Recommended by pypcmgr team
  unittest         builtin
  
LINTING
  flake8           Wrapper around pyflakes, pycodestyle and mccabe. Also, it augments pyflakes and mccabe with error codes
  pylint           Most intelligent Python linter. It's able to infer a lot using only static analysis, thereby finding subtle bugs
  mypy
  
FORMATTING
  black            uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting
  yapf             Yet another Python formatter
  autopep8         // TODO: Add info!
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
### Workflow
##### Manual

##### Automated

### API
```
Usage: pypcmgr [OPTIONS] [SRC]...

  Generates pre-commits hooks for popular Python static analysis tools.

Options:
  -h, --help              Show this message and exit
  
  -v, --version           Show the version and exit
  
  -i, --interactive       Generate a prompt to set up user config
  
  -c, --config            Read out current configuration if available
  
  -r, --recursive         Recursively run all configured tools
  
  --reset                 Reset any pre-commit hooks made by pypcmgr and delete .pypcmgrconfig
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
