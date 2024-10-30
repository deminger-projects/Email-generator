def get_last_generated_len(collection, min_chars, max_chars, collection_check): #vrati posledni pocet generovanych znaku, pokud byla aplikace prerusena v cesti generovani aplikace smaze jiz vygenerovane zaznami z dane iterace

    loop_index = min_chars

    last_pocet_znaku = min_chars

    while loop_index <= max_chars:

        res = collection_check.find_one({"pocet_znaku": loop_index})

        if res: #pokud naslo
            last_pocet_znaku = loop_index
        else: #pokud nic nenaslo v iteraci
            collection.delete_many({"pocet_znaku": loop_index})

            print("Data smazána pro", loop_index, "znaků")

            if loop_index == min_chars:#pokud nic nenaslo ve funkci
                return min_chars
            
            return last_pocet_znaku + 1

        loop_index = loop_index + 1