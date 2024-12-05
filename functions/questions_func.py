from settings import ANSWERS, GENERAL_QUESTION, QUESTION_FOR_MENU
from functions.open_folder_func import open_folder


def start_questions_func() -> int | None:
    for q in GENERAL_QUESTION:

        index = GENERAL_QUESTION.index(q)
        answer_user = questions(q, QUESTION_FOR_MENU[index])

        if answer_user is None or (answer_user > 3 and GENERAL_QUESTION[0]):
            print('Stop.')
            return None

        if index == 0 and answer_user == 1:
            open_folder()

        if index == 1:
            return answer_user


def questions(question: str, menu: str) -> int | None:
    try:
        answer = int(input(f'{question} {menu}'))
    except (ValueError, KeyboardInterrupt, TypeError):
        return None

    return answer
