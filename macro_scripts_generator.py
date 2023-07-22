''' Generates Python scripts for all macros, for use by AutoKey on Linux.

Usage:
- Run script using Python in project's root directory.
- Scripts for each macro function will be in GENERATED_SCRIPT_DIR
- Scripts need to import modules so they need to be copied from
    MACRO_MODULE_DIR to GENERATED_SCRIPT_DIR
    TODO: Resolve this by importing modules from outside script directory.
        Copying the modules to the script directory, can mess with
        scripts using the files in the script directory.

Problems:
- Generated scripts need to import function used by them,
    otherwise script won't be able to find and call it.
    So we need to know where each function came from,
    or make generated scripts import all modules.
    This isn't a problem with AutoKey, as it's User Module Folder can be set
    to a directory holding all the modules for its scripts to import from

Note that macro functions can't be anonymous, as then we can't find the
function for the script to use.
'''

import constants
import macro_hotkeys
import os


# Directories must end with a slash
BUILD_DIR = 'build/'
GENERATED_SCRIPT_DIR = BUILD_DIR + 'macro_scripts/'
MACRO_MODULE_DIR = BUILD_DIR + 'macro_modules/'

# If True, hardlinks macros modules listed in constants.py from the build
# directory, allowing AutoKey to autoimport their functions as needed
HARD_LINK_MACRO_MODULES_TO_GENERATED_DIR = True


def get_function_name(func):
    ''' Returns name of the function used by func '''
    STRING_PRECEEDING_FUNCTION_NAME = 'function'
    # Angled brackets in string representation are excluded
    func_strings = str(func)[1:-2].split()
    name_substr_index = func_strings.index(STRING_PRECEEDING_FUNCTION_NAME) + 1
    return func_strings[name_substr_index]



def generate_script_name(func_name: str):
    return func_name + '.py'



def main():
    # Create build directories
    for path in [BUILD_DIR, GENERATED_SCRIPT_DIR, MACRO_MODULE_DIR]:
        if not os.path.exists(path):
            os.makedirs(path)

    for key, value in macro_hotkeys.macros.items():
        func_name = get_function_name(value)
        script_file_name = generate_script_name(func_name)

        # Add all macro modules to each macro
        # Could be more precise if we know which module each macro function
        # came from
        imports_string = ''
        for module in constants.macro_module_list:
            imports_string += f'from {module} import *\n'

        try:
            script_file = open(GENERATED_SCRIPT_DIR + script_file_name, 'w')
            script_file.write(f'{imports_string}\n{func_name}()')
        except IOError:
            print('Error on interacting with script file for ' + func_name)
        finally:
            script_file.close()

    # Add modules used by macro functions
    if HARD_LINK_MACRO_MODULES_TO_GENERATED_DIR:
        for module in constants.macro_module_list:
            module_file_name = f'{module}.py'
            try:
                os.link(module_file_name, MACRO_MODULE_DIR + module_file_name)
            except FileExistsError:
                print(f"Link or file already exists, skipping {module_file_name}")



if __name__ == '__main__':
    main()
