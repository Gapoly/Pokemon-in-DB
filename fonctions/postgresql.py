#!/usr/bin/python

# \033[32m \033[0m - Vert pour PostgreSQL


def postgresql_connection(DB_PASS,DB_HOST):
    # Import de la librairie
    import psycopg
    from tqdm import tqdm
    from fonctions.pokemon import generate_random_gen4_pokemon_names

    # Connexion au SGBD
    conn = psycopg.connect(user="postgres",
        password=DB_PASS,
        host=DB_HOST,
        port="5432")
        
    # Création de la BDD Pokemon
    poke_bdd_choice_psql = input("\033[32mVoulez-vous créer la BDD Pokemon? [y/n]\033[0m ")
    while True:
        if poke_bdd_choice_psql == "y" or poke_bdd_choice_psql == "Y":
            cur = conn.cursor()
            conn.autocommit = True
            cur.execute("CREATE DATABASE pokemon;")
            conn.commit()
            conn.close()
            break
        elif poke_bdd_choice_psql == "n" or poke_bdd_choice_psql == "N":
            print("La BDD Pokemon n'a pas été créée")
            conn.commit()
            conn.close()
            break
        else:
            poke_bdd_choice_psql = input("Veuillez entrer une réponse valide. [y/n] ")

    # Création de la table liste_pokemon
    poke_table_choice = input("\033[32mVoulez-vous créer la table liste_pokemon? [y/n]\033[0m ")
    while True:
        if poke_table_choice == "y" or poke_table_choice == "Y":
            conn = psycopg.connect(dbname="pokemon",
                user="postgres",
                password=DB_PASS,
                host=DB_HOST,
                port="5432")
            cur = conn.cursor()
            cur.execute("""CREATE TABLE liste_pokemon (id serial PRIMARY KEY, nom VARCHAR(50));""")
            conn.commit()
            #conn.close()
            break
        elif poke_table_choice == "n" or poke_table_choice == "N":
            print("La table liste_pokemon n'a pas été créée")
            break
        else:
            poke_table_choice = input("Veuillez entrer une réponse valide. [y/n] ")

    # Insertion Pokemon
    poke_insert_choice = input("\033[32mVoulez-vous insérer un Pokemon dans la table liste_pokemon? [y/n]\033[0m ")
    while True:
        if poke_insert_choice == "y" or poke_insert_choice == "Y":
            poke_gen_number = int(input("\033[32mCombien de Pokémon voulez-vous insérez?\033[0m "))
            conn = psycopg.connect(dbname="pokemon",
                user="postgres",
                password=DB_PASS,
                host=DB_HOST,
                port="5432")
            cur = conn.cursor()
            print("\033[93mConnection à PokeAPI en cours...\033[0m")
            for name in tqdm (generate_random_gen4_pokemon_names(poke_gen_number),colour='yellow'):
                poke_insert = "INSERT INTO liste_pokemon (nom) VALUES (%s)"
                cur.execute(poke_insert, (name,))
            conn.commit()
            cur.close()
            break
        elif poke_insert_choice == "n" or poke_insert_choice == "N":
            print("Le Pokemon n'a pas été inséré")
            break
        else:
            poke_insert_choice = input("Veuillez entrer une réponse valide. [y/n] ")

    # Voir la liste
    while True:
        see_pokemon = input("\033[32mVoulez-vous voir la liste des Pokémon? [y/n]\033[0m ")

        if see_pokemon == "y" or see_pokemon == "Y":
            conn = psycopg.connect(
                host=DB_HOST,
                port="5432" ,
                user="postgres",
                password=DB_PASS,
                dbname="pokemon")
            cur = conn.cursor()
            cur.execute("SELECT * FROM liste_pokemon")
            rows = cur.fetchall()  # Récupérer tous les résultats
            for row in rows:
                print(f"ID: {row[0]}, Nom: {row[1]}")
            #conn.commit()
            cur.close()
            break
        elif see_pokemon == "n" or see_pokemon == "N":
            print("La liste des Pokémon n'a pas été affichée")
            break
        else:
            see_pokemon = input("Veuillez entrer une réponse valide. [y/n] ")
   
