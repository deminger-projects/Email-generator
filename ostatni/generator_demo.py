import random

def demo():

    providers = ["gmail.com", "seznam.cz", "yahoo.com"]

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7" , "8", "9"]
    characters = [".", "-", "_"]

    all_posible_characters = letters + numbers + characters

    emails = []

    for provider in providers:
        my_string = ""
        n=0

        while n <= 3:
            my_string = my_string + all_posible_characters[random.randint(0, len(all_posible_characters) - 1)]
            n = n + 1
        
        my_string = my_string + "@" + provider
        emails.append(my_string)

    return emails
