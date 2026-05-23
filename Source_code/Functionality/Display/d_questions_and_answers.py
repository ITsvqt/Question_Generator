"""
    This file contains logic for displaying The program Data which has 2 main components:
    1. QUESTIONS
    2. ANSWERS
"""

import Data.questions_access as q_access


# requires calling question_access and passing the #=QUESTION string
def print_question(q_text:str, q_id = -1):
    '''Prints string formated as question.\n
    If q_id is >= 0, add '{number}. ' before it.'''
    question_display_text = q_text.strip(" ?!.-").capitalize() + '?'
    if q_id >= 0:
        question_display_text = f"{q_id}. " + question_display_text
    print(question_display_text, end='\n\n')
    
# requires calling question_access and passing the #=ANSWER string
def print_answer(a_text:str):
    '''Prints string formated as answer.'''
    lines = ('-' + text.strip(" ?!.-").capitalize() + '.' for text in a_text.split('\n') if text)
    print('\n'.join(lines), end='\n\n')





def print_all_questions(show_answers = False):
    """Prints all questions to the console"""
    for index, q_a in enumerate(q_access.get_all_questions()):
        print(f"{index}. ", end = "")
        print_question(q_a[0])
        if show_answers:
            print_answer(q_a[1])
            print()
        


