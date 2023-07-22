# Macro hotkeys



## Usage

Install packages in `requirements.txt`.

### Windows

Run `macro_hotkeys.py`. Hotkeys will be the hotkey start sequence then the key specified for each macro function.

### Linux

Hotkey support is done using AutoKey. Run `macro_scripts_generator.py` to generate the scripts, and copy the generated scripts into the script folder AutoKey uses. Configure AutoKey to recognize the build folder as its User Module Folder so it can import the macro functions for the generated scripts.



### Adding macros

Python macro modules are loaded on startup, the name of the module is added to `macro_module_list` in `constants.py`. The macros for a module are defined using a dictionary named `macros`, accessible as `MODULE_NAME.macros` where `MODULE_NAME` is the name of the module that is imported by Python. Each macro is a key-value pair, the key is a string for reading 


## Development

Code is linted with pylint.

### TODOs

These are project scope TODOs. Code files may contain TODOs specific to their purpose.

- Add subdirectory for user defined macros with version control, but not have it be tracked by this project's version control. Might be possible with git submodule, and then adding a file giving the list of submodules, to gitignore
- automatic importing of macro modules, such as by checking a subdirectory storing them, or checking file names. Former is probably tidier and gives freedom for filenames. Removes the need for adding new macros to a constants file
- Enforce more consistent styling
- Add a script to automatically import scripts into AutoKey with the corresponding hotkeys (Linux)
