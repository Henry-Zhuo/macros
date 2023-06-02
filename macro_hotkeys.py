import constants
from importlib import import_module
import keyboard


### Constants specific to this file

STOP_LISTENING_HOTKEY = 'grave+esc'

ESCAPE_MACRO_START_SEQUENCE = 'esc'
# Store all macros as 'hotkey_combination': 'macro_function'
""" TODO: Add ability to specify different start sequences for some macros,
    allowing more hotkey combinations. """
MACRO_START_SEQUENCE = 'f1'





### Macro import system

# BUild macro dictionary from list of macro modules
macros = {}
for module_name in constants.macro_module_list:
    try:
        module = import_module(module_name)
        macros.update(module.macros)
    except:
        # TODO: Use a logging framework to print this as a warning
        print(f"Could not load macros for module {module_name}")





### Hotkey system

def main():
    for key, value in macros.items():
        keyboard.add_hotkey(f'{MACRO_START_SEQUENCE}+{key}', value, suppress=True)
    # Add hotkey to escape the macro start sequence for when it is needed
    keyboard.add_hotkey(f'{ESCAPE_MACRO_START_SEQUENCE}+{MACRO_START_SEQUENCE}', lambda: keyboard.write(MACRO_START_SEQUENCE))

    # TODO: Prevent modules from listening to keypresses when STOP_LISTENING_HOTKEY is pressed
    #keyboard.wait(STOP_LISTENING_HOTKEY)
    while True:
        keyboard.wait(MACRO_START_SEQUENCE, suppress=True)



if __name__ == "__main__":
	main()
