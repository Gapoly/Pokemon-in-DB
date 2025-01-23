#!/usr/bin/python

import pypokedex
import random

# \033[93m \033[0m - Jaune pour Pokémon

def welcome():
    ascii = r"""
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
"""
    print("\033[93m" + ascii + "\033[0m")


#print("\033[93mTexte en jaune\033[0m")  # 93 = jaune

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