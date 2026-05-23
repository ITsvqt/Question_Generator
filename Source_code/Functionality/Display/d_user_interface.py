"""
    This file contains methods and variables for the user interface display logic an input validation
"""

import os
import Data.inf_program_data as prog_core
from Data.questions_access import get_questions_count

CNT_QUESTIONS = get_questions_count()
UI_LINE_SIZE = 65 

ERROR_MESSAGE_BASE =               "INVALID INPUT ERROR: "
ERROR_MESSAGE_EMPTY_INPUT =         ERROR_MESSAGE_BASE + "Empty line not acceptable"
ERROR_MESSAGE_NON_ALNUMERIC_INPUT = ERROR_MESSAGE_BASE + "Not a single number or letter in answer"
ERROR_MESSAGE_NON_DIGIT_INPUT =     ERROR_MESSAGE_BASE + "Input must be digit (0-9)"
ERROR_MESSAGE_INVALID_MENU_OPTION = ERROR_MESSAGE_BASE + "Input digit is not valid menu choise"

MESSAGE_GREETINGS = " Welcome to the trivia program ! ".center(UI_LINE_SIZE, '*')
MESSAGE_FOOTER = f"(vers. {prog_core.VERSION.lower()}; crea. {prog_core.CREATOR.upper()})\n".rjust(UI_LINE_SIZE, '.')
MESSAGE_HEADER = ' Trivia program '.center(UI_LINE_SIZE, '*')
MESSAGE_SUBMENU1 = 'Knowledge cheking'.center(UI_LINE_SIZE)
MESSAGE_SUBMENU2 =  'Questions expedition'.center(UI_LINE_SIZE)
MESSAGE_GOODBYE = "Thank you for using my program".center(UI_LINE_SIZE, '-')

MAIN_MENU_OPTIONS = {
    1: "Check your knowledge of the questions",
    2: "Go quickly through all the questions"
}
# MAIN_MENU1_SUB_OPTIONS = {} #! not needed for now
# MAIN_MENU2_SUB_OPTIONS = {} #! not needed for now


def clear_screen():
    os.system('cls')
    
# Starting Menu
def print_starting_menu():
    clear_screen()
    print(MESSAGE_GREETINGS)
    print()
    for opt_id, opt_value in MAIN_MENU_OPTIONS.items():
        print(f"{opt_id}. {opt_value}")
    print()
    print(MESSAGE_FOOTER)

def print_submenu1():
    clear_screen()
    print(MESSAGE_HEADER)
    print(MESSAGE_SUBMENU1)
    print()

def print_submenu2():
    clear_screen()
    print(MESSAGE_HEADER)
    print(MESSAGE_SUBMENU2)
    print()
    
def print_ending_menu():
    clear_screen()
    print(MESSAGE_HEADER)
    print()
    print(MESSAGE_GOODBYE)
    print()
    print(MESSAGE_FOOTER)
    

    
    

def get_menu_prompt(menu:dict[int,str]) -> int:
    error_msg = ""
    while True:
        print_starting_menu()
        if error_msg:
            print(error_msg)
        user_input_line = get_user_input("Please enter menu option:\n")
        
        if validate_input_charecter_type(user_input_line) != 1:
            error_msg = ERROR_MESSAGE_NON_DIGIT_INPUT
            continue
        
        user_input_num = int(user_input_line)
        if not validate_users_menu_selection(user_input_num, MAIN_MENU_OPTIONS):
            error_msg = ERROR_MESSAGE_INVALID_MENU_OPTION
            continue
        
        return user_input_num
            
        

def get_user_input(msg = "Press Enter to continue:\n") -> str:
    """
        Ask user to enter something with msg and return it.
    """
    return input(msg)




# ****************** Input Validation ******************

def validate_input_charecter_type(input_str:str) -> int:
    """
        Return 0 if the string is empty\n
        Return -1 if the string consists of only non alpha and numeric charecters\n
        Return 1 if the string is digit only\n
        Return 2 otherwise
    """
    if not len(input_str):
        return 0
    elif not any(c.isalnum() for c in input_str):
        return -1
    elif input_str.isdigit():
        return 1
    return 2

def validate_users_menu_selection(menu_option:int,menu:dict[int,str]) -> bool:
    """
        Checks if menu_option is valid menu key
    """
    return True if menu_option in menu.keys() else False    

