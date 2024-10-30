from connect import connect
from check_if_email_is_valid import check_if_email_is_valid
from update_email_record import update_email_record

from set_settings import set_settings

def handle_email_validation():

    settings = set_settings()

    providers = settings[0]
    
    pripojeni_colekci = connect()
    
    collection_email = pripojeni_colekci[0]
    collection_check = pripojeni_colekci[1]

    res = collection_email.find({"check_count": 0})

    for data in res:
        valid_email_arr = check_if_email_is_valid(data["email"], providers)
        update_email_record(data["_id"], valid_email_arr, collection_email, data["check_count"])
        


handle_email_validation()