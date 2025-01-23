#!/usr/bin/python

from getpass import getpass

from fonctions.pokemon import welcome
from fonctions.mysql import mysql_connection
from fonctions.postgresql import postgresql_connection
#from fonctions.mongodb import mongodb_connection
 
welcome()

choice=int(input("""Quel SGBD comptez-vous utiliser?
                                  
                 1. MySQL / MariaDB
                 2. PostgreSQL
                 : """))

while True:
    if choice == 1 or choice == 2:
    #if choice == 1 and 2:
        break
    else:
        choice = int(input("Veuillez entrer un chiffre valide. [1/2] ")) 

while True:


    if choice == 1:
        DB_PASS = getpass("Quel est le mot de passe de votre SGBD? ")
        DB_HOST = str(input("Quel est l'adresse IP de votre SGBD? "))
        mysql_connection(DB_PASS, DB_HOST)
        break

    elif choice == 2:
        DB_PASS = getpass("Quel est le mot de passe de votre SGBD? ")
        DB_HOST = str(input("Quel est l'adresse IP de votre SGBD? "))
        postgresql_connection(DB_PASS, DB_HOST)
        break

    else:
        choice = int(input("Veuillez entrer un chiffre valide. [1/2] ")) 
        continue