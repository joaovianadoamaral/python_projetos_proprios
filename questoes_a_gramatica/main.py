import menu_appearance
import data_processing
import cases

def menu():
    while True:
        menu_appearance.menu()
        menu_appearance.line()

        int_answer = data_processing.processing_coertion_error_str_to_int(
            menu_appearance.inputs_message.message_option_int)

        match int_answer:
            # o usuário quer uma lista de 1 a n ( tamanho da lista )
            case 1:
                cases.case1()

            case 2:
                cases.case2()

            case 3:
                cases.case3()

            case 4:
                cases.case4()

            case 0:
                menu_appearance.acknowledgment()
                break

            case _:
                menu_appearance.other_wise(int_answer)
        
        menu_appearance.line()

menu()