from check_string import check_string

def correct_emails(email_strings):
    
    valid_email_strings = []

    for string in email_strings:
        if(check_string(string) == True):
            valid_email_strings.append(string)

    print("Emails corrected")

    return valid_email_strings 