import os
import sys
import time

def validate_int_input(prompt):
    while True:
        try:
            response = int(input(prompt))
            return response
        except:
            prompt = "Enter a number "

def validate_index(prompt, list):
    response = validate_int_input(prompt)
    while response < 1 or response > len(list):
        prompt = f"Please enter a number between 1 and {len(list)}: "
        response = validate_int_input(prompt)
    return response - 1

def validate_yes_or_no(prompt):
    while True:
        response = input(prompt)[0].lower()
        match response:
            case 'y': return True
            case 'n': return False
            case _: prompt = 'Please enter yes or no: '

def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"): command = "cls"
    os.system(command)

def pause():
    time.sleep(3)

def append_line(string, separator = ''):
        sys.stdout.write(string + separator)