import math
from time import time

def save_emails(email_string_arr, providers, collection, pocet_znaku, collection_check):   #ulozi vygenerovane emaily pro vsechny zadane poskytovatele, po ulozeni vsech kompinaci je ulozem zaznam o ukonceni iterace

    loop_counter = 0

    start = time()

    print("start")

    for valid_string in email_string_arr:

        email_first_half = ''.join(valid_string)

        collection.insert_one({"email": email_first_half, "pocet_znaku": pocet_znaku, "check_count": 0})

        loop_counter = loop_counter + 1

        if(loop_counter % 100 == 0):
            print(loop_counter, "/", len(email_string_arr), "(", math.floor((loop_counter / len(email_string_arr) * 100) * 100) / 100, "% )")

    collection_check.insert_one({"pocet_znaku": pocet_znaku, "pocet_zaznamu": len(email_string_arr)})

    end = time()

    print("Emails saved")

    print("Run time:", (math.floor((end - start) * 100) / 100) / 60, "m")

 