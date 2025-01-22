import pypokedex
import random
from getpass import getpass
from tqdm import tqdm

def get_random_gen4_pokemon_name():
    # Définir les limites pour la génération 4
    gen4_start = 387
    gen4_end = 493

    # Générer un numéro d'index aléatoire dans les limites de la génération 4
    random_index = random.randint(gen4_start, gen4_end)

    # Récupérer le Pokémon correspondant à cet index
    pokemon = pypokedex.get(dex=random_index)

    # Retourner le nom du Pokémon
    return pokemon.name.capitalize()

def generate_random_gen4_pokemon_names(n):
    pokemon_names = []
    for _ in range(n):
        name = get_random_gen4_pokemon_name()
        pokemon_names.append(name)
    return pokemon_names

def pokemon_generator():
    random_gen4_pokemon_names = generate_random_gen4_pokemon_names(20)
    for name in random_gen4_pokemon_names:
        print(name)
 
choice=int(input("""Quel SGBD comptez-vous utiliser?
                                  
                 1. MySQL
                 2. PostgreSQL
                 : """))

while True:
    if choice == 1 or choice == 2:
        break
    else:
        choice = int(input("Veuillez entrer un chiffre valide. [1/2] ")) 

# Configuration de la connexion
DB_PASS = getpass("Quel est le mot de passe de votre SGBD? ")
DB_HOST = str(input("Quel est l'adresse IP de votre SGBD? "))

while True:

# MySQL    
    if choice == 1:
        # Import de la librairie
        import mysql.connector

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
        break

# PostgreSQL
    elif choice == 2:
        # Import de la librairie
        import psycopg

        # Connexion au SGBD
        conn = psycopg.connect(user="postgres",
            password=DB_PASS,
            host=DB_HOST,
            port="5432")
        
        # Création de la BDD Pokemon
        poke_bdd_choice_psql = input("Voulez-vous créer la BDD Pokemon? [y/n] ")
        while True:
            if poke_bdd_choice_psql == "y" and "Y":
                cur = conn.cursor()
                conn.autocommit = True
                cur.execute("CREATE DATABASE pokemon;")
                conn.commit()
                conn.close()
                break
            elif poke_bdd_choice_psql == "n" and "N":
                print("La BDD Pokemon n'a pas été créée")
                conn.commit()
                conn.close()
                break
            else:
                poke_bdd_choice_psql = input("Veuillez entrer une réponse valide. [y/n] ")

        # Création de la table liste_pokemon
        poke_table_choice = input("Voulez-vous créer la table liste_pokemon? [y/n] ")
        while True:
            if poke_table_choice == "y" and "Y":
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
                conn = psycopg.connect(dbname="pokemon",
                            user="postgres",
                            password=DB_PASS,
                            host=DB_HOST,
                            port="5432")
                cur = conn.cursor()
                #for name in generate_random_gen4_pokemon_names(poke_gen_number):
                for name in tqdm (generate_random_gen4_pokemon_names(poke_gen_number)):
                    poke_insert = "INSERT INTO liste_pokemon (nom) VALUES (%s)"
                    cur.execute(poke_insert, (name,))
                conn.commit()
                cur.close()
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
            elif see_pokemon == "n" and "N":
                print("La liste des Pokémon n'a pas été affichée")
                break
            else:
                see_pokemon = input("Veuillez entrer une réponse valide. [y/n] ")
        break
    else:
        choice = int(input("Veuillez entrer un chiffre valide. [1/2] "))
