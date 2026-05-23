from Data.questions_data import questions_and_answers as q_a

def get_questions_count() -> int:
    """
    Retrieve count of questions
    """
    return len(q_a)

def get_question_by_id(id:int) -> tuple[str,str]:
    """
    Retrieve single question and answer by id. (question, answer)
    """
    pair = q_a[id]
    return (pair['question'], pair['answer'])


def get_all_questions() -> list[tuple[str,str]]:
    """
    Retrieve all questions and answers as (question, answer) pairs.
    """    
    return [(item['question'], item['answer']) for item in q_a]

