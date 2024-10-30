from generate_emails import generate_emails
from correct_emails import correct_emails
from save_emails import save_emails
from connect import connect
from get_last_generated_len import get_last_generated_len
from set_settings import set_settings

def handle_email_generation(): # vygeneruje emaily pro vsechny varianty a delky

    settings = set_settings()

    providers = settings[0]
    all_posible_characters = settings[4]
    max_string_email_len = settings[5] #max pocet generovanych znaku
    min_string_email_len = settings[6] #min pocet generovanych znaku

    pripojeni_colekci = connect() #vygeneruje pripojeni ke kolekcim

    collection_email = pripojeni_colekci[0]
    collection_check = pripojeni_colekci[1]

    last_generated_len = get_last_generated_len(collection_email, min_string_email_len, max_string_email_len, collection_check) #zjisti jak dlouhy byl posledni ulozeny email
    
    len_index = last_generated_len #zvisi pocet genorovanych znaku

    while len_index <= max_string_email_len:

        email_strings = generate_emails(len_index, all_posible_characters) #vygeneruje emaily

        valid_email_strings = correct_emails(email_strings) #upravi emaily

        print("Generace začala pro emaily s " + str(len_index) + " znaky")

        save_emails(valid_email_strings, providers, collection_email, len_index, collection_check) #ulozi emaily

        print("Emaily s " + str(len_index) + " znaky vygenerovany")

        len_index = len_index + 1

handle_email_generation()


