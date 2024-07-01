def space_betwen_character(spaces: int) -> None:
    for _ in range(spaces):
        print(' ', end = '')

def break_row()-> None:
    print()

def inversed_letter(end, character, spaces): 
    for count in range(1, end + 1):
        for _ in range ( count ):
            print(character, end = '')
            space_betwen_character(spaces)
        break_row()

CHARACTER = '*'
end = 5
spaces = 2

inversed_letter(end, CHARACTER, spaces)