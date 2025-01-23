# Pokemon in DB

<p align='center'>
    <img src='https://mir-s3-cdn-cf.behance.net/projects/404/5f7d78149825051.62eeab127b743.jpg'/>
</p>


## 🤔 1. Qu'est-ce qu'il fait?

Ce script se connecte à un SGBD MySQL, MariaDB ou PostgreSQL. Il va créer une base de données Pokemon, une table et insérez une liste de Pokémons dedans. Il va insérer des Pokémons de la 4e génération.Pourquoi la 4e génération? Parce que c'est la meilleur.

## 🐍 2. Comment ça marche?

Ce script fait appelle à une API qui s'appelle [PokeAPI](https://pokeapi.co/) à l'aide du module [PyPokedex](https://github.com/arnavb/pypokedex). Il va ensuite les insérez dans la table par rapport au nombre demandé par l'utilisateur.

## ⬇️ 3. Installation

### 3.1. Poetry

Installer Poetry sur votre système. Référez vous à la documentation spécifique à votre machine.

```shell
git clone https://github.com/Gapoly/Pokemon-in-DB
cd Pokemon-in-DB/
poetry init
poetry add mysql-connector mysql-connector-python psycopg psycopg-binary pypokedex tqdm pymongo
poetry run python3 Pokemon_in_DB.py
```

### Notes

Si dans votre SGBD vous avez déjà une base de données ou table avec déjà le même nom, il ne faut pas en recréer une par dessus. Ce script ne fais pas ça.
