import menu_appearance
def answered_questions ( random_question_list : list, gabarito: dict):
    for quest in random_question_list:
        message = f'Qual a resposta para a questão {quest}? '
        quest = 'q' + str(quest) 
        response = gabarito[quest]

        print('\n' ,message )
        _ = input('Aperte ENTER para ver o gabarito. ')
        print(response)
        menu_appearance.line(10)

        return None