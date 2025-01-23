#!/usr/bin/python

# \033[92m \033[0m - Vert clair pour MongoDB, parce que ça ressemble à une mangue verte. Parce qu'il s'appelle MangoDB et non MongoDB. Ça serait débile de l'appeler MongoDB au lieu de MangoDB.

def mongodb_connection(DB_PASS,DB_HOST,DB_USER):
    # Import de la librairie
    import pymongo
    from tqdm import tqdm
    from fonctions.pokemon import generate_random_gen4_pokemon_names

    # Connexion au SGBD
    client = pymongo.MongoClient(f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:27017")
    db = client.pokemon
    collection = db.liste_pokemon2

    # Insertion Pokemon
    poke_insert_choice = input("\033[92mVoulez-vous insérer un Pokemon dans la table liste_pokemon? [y/n]\033[0m ")
    while True:
        if poke_insert_choice == "y" or poke_insert_choice == "Y":
            poke_gen_number = int(input("\033[92mCombien de Pokémon voulez-vous insérez?\033[0m "))
          
            print("\033[93mConnection à PokeAPI en cours...\033[0m")
            for name in tqdm (generate_random_gen4_pokemon_names(poke_gen_number), colour='yellow'):
                #f68c34
                collection.insert_one({"nom": name})
            break
        elif poke_insert_choice == "n" or poke_insert_choice == "N":
            print("Le Pokemon n'a pas été inséré")
            break
        else:
            poke_insert_choice = input("Veuillez entrer une réponse valide. [y/n] ")
    
    # Voir la liste
    while True:
        see_pokemon = input("\033[92mVoulez-vous voir la liste des Pokémon? [y/n]\033[0m ")

        if see_pokemon == "y" or see_pokemon == "Y":
            for pokemon in collection.find():
                print(pokemon)
            break
        elif see_pokemon == "n" or see_pokemon == "N":
            print("La liste des Pokémon n'a pas été affichée")
            break
        else:
            see_pokemon = input("Veuillez entrer une réponse valide. [y/n] ")
   