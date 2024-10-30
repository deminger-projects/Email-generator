import json

def set_settings():

    with open("settings.json", "r") as file:
    
        settings_data = json.load(file)

    providers = settings_data["providers"]
    letters = settings_data["letters"]
    numbers = settings_data["numbers"]
    characters = settings_data["characters"]
    all_posible_characters = settings_data["all_posible_characters"]
    max_string_email_len = settings_data["max"]
    min_string_email_len = settings_data["min"]

    return [providers, letters, numbers, characters, all_posible_characters, max_string_email_len, min_string_email_len]