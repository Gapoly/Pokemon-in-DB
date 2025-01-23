#!/usr/bin/python

import pypokedex
import random

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