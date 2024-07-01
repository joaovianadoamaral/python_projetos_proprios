from random import shuffle
import data_processing
import menu_appearance
import do_questions
import answers
import main

def random_list_range_m_n(start_list_int : int, end_list_int: int):
    number_list = [i for i in range(start_list_int, end_list_int + 1)]

    shuffle(number_list)
    print(number_list)

    return number_list

# faz aleatoriamente as listas de um determinado range(m,n)
def case1():
    menu_appearance.menu_answers_query()
    int_choose_chapter = data_processing.processing_coertion_error_str_to_int(
            menu_appearance.inputs_message.message_option_int)
    
    answer_is_zero = not int_choose_chapter
    if answer_is_zero:
        main.menu()

    int_start_list = data_processing.processing_coertion_error_str_to_int(
        menu_appearance.inputs_message.input_message_m
    )
    int_end_list = data_processing.processing_coertion_error_str_to_int(
        menu_appearance.inputs_message.input_message_n
    )
    random_number_list = random_list_range_m_n(int_start_list, int_end_list)
    
    dict_answer = answers.dict_choose_options()
    do_questions.answered_questions(random_number_list)


def case2():
    exit_query_question = False
    while not exit_query_question:
        menu_appearance.menu_answers_query()
        menu_appearance.line()

        int_option_answer = data_processing.processing_coertion_error_str_to_int(
            menu_appearance.inputs_message.message_option_int
        )
        
        if int_option_answer:
            exit_query_question = True

        dict_answer = answers.dict_choose_options(int_option_answer)
        menu_appearance.line()

        choose_question_int = data_processing.processing_coertion_error_str_to_int(
            menu_appearance.inputs_message.choose_question
        )
        
        choose_question_str = str(choose_question_int)
        question = 'q' + choose_question_str
        menu_appearance.line()

        menu_appearance.response_question(question, dict_answer)


def case3():
    ...

def case4():
    ...

case2()
