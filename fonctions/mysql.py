#!/usr/bin/python

def mysql_connection(DB_PASS, DB_HOST):
    # Import de la librairie
    import mysql.connector
    from tqdm import tqdm
    from fonctions.pokemon import generate_random_gen4_pokemon_names

    # Connexion au SGBD
    cnx = mysql.connector.connect(
        host=DB_HOST,
        port="3306" ,
        user="root",
        password=DB_PASS)

    #Création de la BDD Pokemon
    poke_bdd_choice_mysql = input("Voulez-vous créer la BDD Pokemon? [y/n] ")
    while True:
        if poke_bdd_choice_mysql == "y" and "Y":
            cursor = cnx.cursor()
            cursor.execute("CREATE DATABASE pokemon;")
            cnx.commit()
            cursor.close()
            break
        elif poke_bdd_choice_mysql == "n" and "N":
            print("La BDD Pokemon n'a pas été créée")
            cursor = cnx.cursor()
            cursor.close()
            break
        else:
            poke_bdd_choice_mysql = input("Veuillez entrer une réponse valide. [y/n] ")

    #Création de la table liste_pokemon
    poke_table_choice = input("Voulez-vous créer la table liste_pokemon? [y/n] ")
    while True:
        if poke_table_choice == "y" and "Y":
            cnx = mysql.connector.connect(
                host=DB_HOST,
                port="3306",
                user="root",
                password=DB_PASS,
                database="pokemon")
            cursor = cnx.cursor()
            cursor.execute("""CREATE TABLE liste_pokemon (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50));""")
            cnx.commit()
            cursor.close()
            break
        elif poke_table_choice == "n" and "N":
            print("La table liste_pokemon n'a pas été créée")
            break
        else:
            poke_table_choice = input("Veuillez entrer une réponse valide. [y/n] ")
       
    # Insertion Pokemon
    poke_insert_choice = input("Voulez-vous insérer un Pokemon dans la table liste_pokemon? [y/n] ")
    while True:
        if poke_insert_choice == "y" and "Y":
            poke_gen_number = int(input("Combien de Pokémon voulez-vous insérez? "))
            cnx = mysql.connector.connect(
                    host=DB_HOST,
                    port="3306" ,
                    user="root",
                    password=DB_PASS,
                    database="pokemon")
            cursor = cnx.cursor()
            #for name in generate_random_gen4_pokemon_names(poke_gen_number):
            print("Connection à PokeAPI en cours...")
            for name in tqdm(generate_random_gen4_pokemon_names(poke_gen_number)):
                poke_insert = "INSERT INTO liste_pokemon (nom) VALUES (%s)"
                cursor.execute(poke_insert, (name,))
            cnx.commit()
            cursor.close()
            break
        elif poke_insert_choice == "n" and "N":
            print("Le Pokemon n'a pas été inséré")
            break
        else:
            poke_insert_choice = input("Veuillez entrer une réponse valide. [y/n] ")

    # Voir la liste
    while True:
        see_pokemon = input("Voulez-vous voir la liste des Pokémon? [y/n] ")

        if see_pokemon == "y" and "Y":
            cnx = mysql.connector.connect(
                host=DB_HOST,
                port="3306" ,
                user="root",
                password=DB_PASS,
                database="pokemon")
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM liste_pokemon")
            rows = cursor.fetchall()  # Récupérer tous les résultats
            for row in rows:
                print(f"ID: {row[0]}, Nom: {row[1]}")
            #cnx.commit()
            cursor.close()
            break
        elif see_pokemon == "n" and "N":
            print("La liste des Pokémon n'a pas été affichée")
            break
        else:
            see_pokemon = input("Veuillez entrer une réponse valide. [y/n] ")
       