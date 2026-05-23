import Data.questions_access as d_access
import random
import Functionality.Display.d_user_interface as i_user
import Functionality.Display.d_questions_and_answers as i_data


def start_quiz():
    i_user.print_starting_menu()
    i_user.get_user_input()
    menu_choise = i_user.get_menu_prompt(i_user.MAIN_MENU_OPTIONS)
    match menu_choise:
        case 1:
            answer_questions()
        case 2:
            inspect_questions()

    i_user.print_ending_menu()
    i_user.get_user_input()
    i_user.clear_screen()
    

def answer_questions():
    cnt_elements = d_access.get_questions_count()
    # include all questions from data in random order
    question_order = random.sample(range(cnt_elements),cnt_elements)
    for q_id,q_index in enumerate(question_order, 1):
        i_user.print_submenu1()
        # hold question & answer
        q_text = d_access.get_question_by_id(q_index)
        i_data.print_question(q_text[0],q_id)
        user_answer = i_user.get_user_input('Answer:\n')
        
        #= Get answer and reprint everything without the message for user input
        i_user.clear_screen()
        i_user.print_submenu1()
        i_data.print_question(q_text[0],q_id)
        i_data.print_answer(user_answer)
        i_data.print_answer(q_text[1])
        i_user.get_user_input()
        i_user.clear_screen()
    
    i_user.get_user_input()
    


def inspect_questions():
    for q_id, dict in enumerate(d_access.get_all_questions(), 1):
        i_user.print_submenu2()
        i_data.print_question(dict[0], q_id)
        i_data.print_answer(dict[1])
        i_user.get_user_input()
    
    

    
    