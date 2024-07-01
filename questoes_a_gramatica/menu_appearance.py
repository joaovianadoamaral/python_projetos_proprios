from time import sleep
import os

class cor:
    # Definindo códigos de escape ANSI para cores
    RESET = '\033[0m'
    PRETO = '\033[30m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'
    
    BRILHO_PRETO = '\033[90m'
    BRILHO_VERMELHO = '\033[91m'
    BRILHO_VERDE = '\033[92m'
    BRILHO_AMARELO = '\033[93m'
    BRILHO_AZUL = '\033[94m'
    BRILHO_MAGENTA = '\033[95m'
    BRILHO_CIANO = '\033[96m'
    BRILHO_BRANCO = '\033[97m'

    FUNDO_PRETO = '\033[40m'
    FUNDO_VERMELHO = '\033[41m'
    FUNDO_VERDE = '\033[42m'
    FUNDO_AMARELO = '\033[43m'
    FUNDO_AZUL = '\033[44m'
    FUNDO_MAGENTA = '\033[45m'
    FUNDO_CIANO = '\033[46m'
    FUNDO_BRANCO = '\033[47m'
    FUNDO_BRILHO_PRETO = '\033[100m'
    FUNDO_BRILHO_VERMELHO = '\033[101m'
    FUNDO_BRILHO_VERDE = '\033[102m'
    FUNDO_BRILHO_AMARELO = '\033[103m'
    FUNDO_BRILHO_AZUL = '\033[104m'
    FUNDO_BRILHO_MAGENTA = '\033[105m'
    FUNDO_BRILHO_CIANO = '\033[106m'
    FUNDO_BRILHO_BRANCO = '\033[107m'

class options_list:
    # primeiro item lista = título
    # último item lista = mensagem de saída
    options_list_menu = [
        'MENU - A gramática', 
        'Lista aleatoria de um range de questões(M -> N)', 
        'Questoes em ordem ( fornecer )',
        'Questoes embaralhadas ( fornecer )',
        'Consultar gabarito',
        'SAIR'
    ]

    options_answers_list_menu = [
            'CAPITULOS - A gramática',
            'fonologia',
            'acentuacao_grafica', 
            'ortografia',
            'semantica_lexicologia',
            'morfologia',
            'formacao_palavras' ,
            'substantivo' ,
            'adjetivo' ,
            'artigo' ,
            'numeral' ,
            'pronome' ,
            'verbo' ,
            'adverbio' ,
            'preposicao' ,
            'conjuncao' ,
            'interjeicao' , 
            'sintaxe' ,
            'frase_oracao_periodo' ,
            'termos_essenciais_oracao' ,
            'termos_integrantes_oracao' , 
            'termos_acessorios_oracao' ,
            'oracoes_coordenadas' ,
            'oracoes_subordinadas' ,
            'oracoes_reduzidas'  ,
            'oracoes_intercaladas' ,
            'periodo_misto' ,
            'pontuacao' ,
            'concordancia' ,
            'regencia' ,
            'que_se_como' ,
            'estilistica' ,
            'teoria_comunicacao' ,
            'compreensao_interpretacao_texto_tipologia_textual' ,
            'coesao_coerencia' ,
            'dominio_registro_culto' ,
            'reescritura_frases' ,
            'questoes_comentadas_banca_cqip',
            'voltar', 
    ]

class inputs_message:
    input_message_m = (f'{cor.AZUL}Digite qual a primeira' 
            f' questão do range(M) (M - N): {cor.RESET}')

    input_message_n = (f'{cor.AZUL}Digite qual a última' 
            f' questão do range(N) (M - N): {cor.RESET}')
    
    message_option_int = 'Digite a opção desejada: '

    choose_question = 'Digite a questão desejada: '

def line(n : int = 30):
    print (cor.VERMELHO +  n * '-=-' + cor.RESET)
    sleep(0.75)

def format_menu_options(options_list : list, 
                        menu_pharse : bool, 
                        exit_pharse : bool):
    # o primeiro item é o título do MENU
    # o ultímo deve conter a frase de saída

    for count,option in enumerate(options_list):
        first_item_list = (count == 0)
        format_menu = first_item_list and menu_pharse

        last_item_list = (count == len(options_list) - 1)
        format_exit = last_item_list and exit_pharse

        if format_menu:
            print(f'\t\t{cor.BRILHO_VERMELHO}{option}{cor.RESET}')
            
            count += 1
            continue

        if format_exit:
            number_option_exit = 0
            print(f'( {cor.AZUL}{number_option_exit}{cor.RESET} ) - '
                  f'{cor.AMARELO}{options_list[-1]}{cor.RESET}')
            
            break
        
        print(f'( {cor.AZUL}{count}{cor.RESET} ) - {cor.AMARELO}{option}'
              f'{cor.RESET}')
        
        count += 1

def menu():
    limpar_terminal()
    format_menu_options(options_list.options_list_menu, True, True)

def menu_answers_query():
    limpar_terminal()
    format_menu_options(options_list.options_answers_list_menu, True, True)   

def error_message():
    limpar_terminal()
    line()
    print(f'{cor.BRILHO_VERMELHO}Algo ocorreu errado'
            f'... Digite certo dessa vez.{cor.RESET}')
    line()

def acknowledgment():
    limpar_terminal()
    line()
    print(cor.VERDE +'Obrigado....')
    print('Volte sempre' + cor.RESET)

def other_wise(answer: int):
    limpar_terminal()
    line()
    print(cor.AMARELO + f'A opção {cor.VERMELHO}{answer}{cor.AMARELO}' 
          ' não está disponível')
    print(cor.AZUL + 'Tente novamente' + cor.RESET)

def response_question(question: str, dict_answer: dict):
    print(f'A resposta para a questão {question} é: {dict_answer[question]}')

def limpar_terminal():
    # Verifica o sistema operacional
    sistema_operacional = os.name
    
    # Limpa o terminal de acordo com o sistema operacional
    if sistema_operacional == 'posix': # Para sistemas Unix (Linux, macOS)
        os.system('clear')
    elif sistema_operacional == 'nt': # Para sistemas Windows
        os.system('cls')
    else:
        print("Sistema operacional não suportado para limpeza do terminal.")

