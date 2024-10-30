
def update_email_record(record_id, valid_email_arr, email_collection, check_count):

    email_collection.update_one({"_id": record_id}, {"$set": {"check_count": check_count + 1, "valid_emails": valid_email_arr}})