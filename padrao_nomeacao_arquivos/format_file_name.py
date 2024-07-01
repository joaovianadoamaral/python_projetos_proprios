class UNWANTED_TEXT:
    DELETE = ''
    special_characters = { # refatore isso de forma que não precise escrever todos à mão
        'à' : 'a',
        'á' : 'a',
        'ã' : 'a',
        'ó' : 'o',
        'õ' : 'o',
        'í' : 'i',
        'é' : 'e',
        'ê' : 'e',
        'ú' : 'u', 
        'ç' : 'c',
        "`" : DELETE,
        '~' : DELETE,
        '^' : DELETE,
        '<' : DELETE,
        '>' : DELETE,
        '/' : DELETE,
        '\\': DELETE,
        '?' : DELETE,
        '!' : DELETE,
        '@' : DELETE,
        '#' : DELETE,
        '$' : DELETE,
        '%' : DELETE,
        '&' : DELETE,
        '¨' : DELETE,
        '*' : DELETE,
        '[' : DELETE,
        ']' : DELETE,
        '(' : DELETE,
        ')' : DELETE,
        '{' : DELETE,
        '}' : DELETE,
        '.' : DELETE,
        ',' : DELETE,
        ';' : DELETE,
        '-' : DELETE,
        '_' : DELETE,
        '+' : DELETE,
        '=' : DELETE, 
    }
    words = {
        'apostila' : DELETE,
    }

def replace_text(text_lower:str) -> str:
    for character in UNWANTED_TEXT.special_characters:
        text_lower = text_lower.replace(character, UNWANTED_TEXT.special_characters[character])

    for word in UNWANTED_TEXT.words:
        text_lower = text_lower.replace(word, UNWANTED_TEXT.words[word])

    return text_lower

def join_text_with_caracter(text:str, caracter:str) -> str:
    text_list = text.split()    
    format_text = caracter.join(text_list)
    
    return format_text

def format_file_name(text:str, add_id_prefix = True) -> str:
    ID = '_X_'

    text_lower = text.lower()
    format_text_lower = replace_text(text_lower)

    format_text_lower = join_text_with_caracter(format_text_lower, '_')

    if add_id_prefix:
        text = ID + format_text_lower
    
    if not add_id_prefix:
        text =  format_text_lower

    return text
