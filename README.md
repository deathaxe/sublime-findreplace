# [FindReplace](https://github.com/deathaxe/sublime-findreplace)

[![License](https://img.shields.io/github/license/deathaxe/sublime-findreplace.svg?style=flat-square)](LICENSE)

A simple plugin for Sublime Text to provide a "find_replace" command, which can be bound to keys or menus or may be used in macros.

```
        Example:

        view.run_command(
            "find_replace", {
                "pattern": "the\s+",
                "replace_by": "THE ",
                "start_pt": 100,
                "flags": ["ALL"]
            }
        )
```
