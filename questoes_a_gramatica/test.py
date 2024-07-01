import os

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

    
lista = [8, 1, 3, 5, 6, 7, 10]
lista_ordenada = lista.BubbleSort()

