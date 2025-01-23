#!/usr/bin/python

from getpass import getpass

from fonctions.pokemon import welcome
from fonctions.mysql import mysql_connection
from fonctions.postgresql import postgresql_connection
from fonctions.mongodb import mongodb_connection

welcome()

choice=int(input("""Quel SGBD comptez-vous utiliser?
                                  
                \033[94m1. MySQL / MariaDB\033[0m
                \033[32m2. PostgreSQL\033[0m
                \033[92m3. MongoDB\033[0m
                > """))

print() # Saut à la ligne

while True:
    if choice == 1 or choice == 2 or choice == 3:
        break
    else:
        choice = int(input("Veuillez entrer un chiffre valide. [1 - 2 - 3] ")) 

while True:

    if choice == 1:
        DB_PASS = getpass("\033[94mQuel est le mot de passe de votre SGBD?\033[0m ")
        DB_HOST = str(input("\033[94mQuel est l'adresse IP de votre SGBD?\033[0m "))
        mysql_connection(DB_PASS,DB_HOST)
        break

    elif choice == 2:
        DB_PASS = getpass("\033[32mQuel est le mot de passe de votre SGBD?\033[0m ")
        DB_HOST = str(input("\033[32mQuel est l'adresse IP de votre SGBD?\033[0m "))
        postgresql_connection(DB_PASS,DB_HOST)
        break
    elif choice == 3:
        DB_PASS = getpass("\033[92mQuel est le mot de passe de votre SGBD?\033[0m ")
        DB_HOST = str(input("\033[92mQuel est l'adresse IP de votre SGBD?\033[0m "))
        DB_USER = input("\033[92mQuel est le nom d'utilisateur de votre SGBD?\033[0m ")
        mongodb_connection(DB_PASS,DB_HOST,DB_USER)
        break

    else:
        choice = int(input("Veuillez entrer un chiffre valide. [1 - 2 - 3] ")) 
        continue