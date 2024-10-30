providers_cz = ["seznam.cz"]
providers_ww = ["gmail.com", "outlook.com", "yahoo.com", "icloud.com"]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7" , "8", "9"]
characters = [".", "-", "_"]

all_posible_characters = letters + numbers + characters

max_len = 30
min_len = 2

current_len = 2

#max email len = 64
#min recomandat = 10

results = []

string_test = "test"

index = 0
index_in_new_email = 1

for my_char in all_posible_characters:
    while index < max_len:
        index = index + 1


max_len_index = 0





def create_ciselnik(pocet_ciselniku):
    ciselniky = []

    while pocet_ciselniku > 0:
        ciselniky.append([all_posible_characters[0]])
        pocet_ciselniku = pocet_ciselniku - 1

    return ciselniky

moje_ciselniky = create_ciselnik(10)



def get_ciselnik_num(ciselniky):
    pocet_iteraci = 0
    pocet_ciselniku = len(ciselniky)
    pocet_charakteru = len(all_posible_characters)

    data = []

    for char_index in range(len(all_posible_characters)):
    
        for i in range(pocet_ciselniku):
            print(ciselniky[i])
            ciselniky[i] = all_posible_characters[char_index]

        for index in range(pocet_ciselniku):
            pocet_charakteru_index = 0

            while pocet_charakteru_index < pocet_charakteru:
                ciselniky[index] = all_posible_characters[pocet_charakteru_index]

                ciselnik_data = ""

                for ciselnik in ciselniky:
                    ciselnik_data = ciselnik_data + ciselnik[0]

                data.append(ciselnik_data)

                pocet_charakteru_index = pocet_charakteru_index + 1

            ciselniky[index] = all_posible_characters[0]


    return data




def dalsi_funkce_s_ciselniky():
    ciselniky = []
    create_ciselnik()


def generate_dial_templace(number_of_dials):
    
    all_dials_tampletes = []

    for char_index in range(len(all_posible_characters)):
        dials_arr = []
        skip = False
        
        for dial_index in range(number_of_dials):

            if(dial_index == 0 and check_if_char_is_special(all_posible_characters[char_index]) == True): #specialni charekter nemuze byt prvni
                skip = True
                break
            elif(dial_index > 0 and check_if_char_is_special(dials_arr[dial_index - 1]) == True and check_if_char_is_special(all_posible_characters[char_index]) == True): #specialni charaktery nemuzou byt za sebou
                skip = True
                break
            else:
                dials_arr.append(all_posible_characters[char_index])

        if(skip == False):
            all_dials_tampletes.append({"dial": dials_arr, "char_index": char_index})

    return all_dials_tampletes


def check_if_char_is_special(char):
    for special_char in characters:
        if(special_char == char):
            return True


def get_dial_combinations(number_of_dials):
    dial_template = generate_dial_templace(number_of_dials)

    dials_data = []

    for dial_index in range(len(dial_template)):
        dial = dial_template[dial_index]["dial"]
        start_char = dial_template[dial_index]["char_index"]
        
        for dial_position in range(len(dial)):
            for char in range(len(all_posible_characters)):
                dial_template[dial_index]["dial"][dial_position] = char

                dial_string = ""

                for dial_one in dial:
                    print(dial)
                    dial_string = dial_string + dial_one

                dials_data.append(dial_string)

    return dials_data

template = get_dial_combinations(4)

print(template)