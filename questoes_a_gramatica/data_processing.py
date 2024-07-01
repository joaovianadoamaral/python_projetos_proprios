import menu_appearance
def processing_coertion_error_str_to_int(message:str):
    try: 
        str_var = input(menu_appearance.cor.AZUL + 
                        message +
                        menu_appearance.cor.RESET)
        
        int_var = int (str_var)
        return int_var
    
    except ValueError:
        while True:
            menu_appearance.error_message()

            str_var = input(menu_appearance.cor.AZUL + 
                        message +
                        menu_appearance.cor.RESET)
            if str_var.isnumeric():
                int_var = int(str_var)
                return int_var

def negative_number():
    ...

def high_number():
    ...
