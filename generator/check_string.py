

def check_string(string):

    is_valid = True

    string_len = len(string)
    string_index = 0

    characters = [".", "-", "_"]

    while(string_index < string_len):

        for my_char in characters:

            if(my_char == string[0] and string_index == 0): # kontroluje jestli je prvni charakter valid
                is_valid = False
                break

            if(string_index > 0): # kontroluje jestli jsou charaktery vedle sebe
                if(string[string_index] == my_char and string[string_index - 1] == my_char):
                    is_valid = False
                    break

                if(string_index < string_len - 1):
                    if(string[string_index] == my_char and string[string_index + 1] == my_char):
                        is_valid = False
                        break

        string_index = string_index + 1

    return is_valid
