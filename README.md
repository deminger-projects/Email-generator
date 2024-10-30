Projekt se dělí na dvě části.

První část generuje emailové adresy na základě délky, poskytovatele domény a možných kombinací znaků. 
Tyto záznamy jsou následně uloženy do databáze. Pokud některá iterace není dokončena, všechny záznamy z této iterace jsou smazány.

Druhá část má za úkol kontrolovat existenci emailových adres. 
Bere data z databáze a následně ověřuje jejich platnost. Pokud emailová adresa neprojde kontrolou, záznam je upraven. Pokud adresa selže v kontrole vícekrát, záznam je smazán.

###
spusteni generatoru: py handle_email_generation.py
spusteni validatoru: py handle_email_validation.py

python verze:
mongoDB verze: 
pip verze: 