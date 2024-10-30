import itertools

def generate_emails(pocet_znaku, all_characters):

    result = itertools.combinations(all_characters, pocet_znaku)

    print("Emails generated")

    return result
 