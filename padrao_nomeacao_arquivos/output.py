from format_file_name import format_file_name

TEXTO = 'Apostila - Gerenciamento de Qualidade e Melhoria dos Processos'

text = format_file_name(TEXTO, add_id_prefix = True)
print(text)
