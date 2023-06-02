# Macro hotkeys



## Usage

Install packages in `requirements.txt` and run `macro_hotkeys.py`.

### Adding macros

Python macro modules are loaded on startup, the name of the module is added to `macro_module_list` in `constants.py`. The macros for a module are defined using a dictionary named `macros`, accessible as `MODULE_NAME.macros` where `MODULE_NAME` is the name of the module that is imported by Python. Each macro is a key-value pair, the key is a string for reading 


## Development

Code is linted with pylint.

### TODOs

These are project scope TODOs. Code files may contain TODOs specific to their purpose.

- Add subdirectory for user defined macros with version control, but not have it be tracked by this project's version control. Might be possible with git submodule, and then adding a file giving the list of submodules, to gitignore
- automatic importing of macro modules, such as by checking a subdirectory storing them, or checking file names. Former is probably tidier and gives freedom for filenames. Removes the need for adding new macros to a constants file
- Enforce more consistent styling
