# Pokemon in DB

<p align='center'>
    <img src='https://mir-s3-cdn-cf.behance.net/projects/404/5f7d78149825051.62eeab127b743.jpg'/>
</p>


## 🤔 1. Qu'est-ce qu'il fait?

Ce script se connecte à un SGBD MySQL, MariaDB, PostgreSQL ou MongoDB. Il va créer une base de données Pokemon, une table et insérez une liste de Pokémons dedans. Il va insérer des Pokémons de la 4e génération.Pourquoi la 4e génération? Parce que c'est la meilleur.

## 🐍 2. Comment ça marche?

Ce script fait appelle à une API qui s'appelle [PokeAPI](https://pokeapi.co/) à l'aide du module [PyPokedex](https://github.com/arnavb/pypokedex). Il va ensuite les insérez dans la table par rapport au nombre demandé par l'utilisateur.

## ️💡 3. Pourquoi ce projet?

J'ai toujours était habitué à faire du MariaDB, soit du SQL. J'ai décidé de pousser mes limites en essayant de manipuler d'autres type de SGBD que je n'avais jamais touché avant, comme du PostgreSQL et MongoDB. J'ai voulu rester sur le thème Pokémon et j'ai eu l'idée de générer une liste Pokémon automatiquement avec le script présenté en classe.

## 📟️ 4. L'IA dans tout ça?

Bien sur, j'ai dû m'aider de l'IA pour faire ce script. Même ci je maîtrise la base du Python et comprends son principe, il y a des choses pour lequelle je n'avais pas les connaissances pour. Dans le script, il ma soit aidé à réparer des erreurs ou générer des bouts de code que je n'aurais pas pu faire, tel que:

- Les fonctions faisant appelle à l'API pour générer une liste de Pokémon de manière aléatoire
- Quelques corrections de bug de manières général

Même ci les chatbots sont outils des très utiles pour ce genre de travail. J'essaye de les utiliser le moins possible pour ne pas en être dépendant.

## ⬇️ 5. Installation

Pour l'utilisation de ce script, il est nécessaire d'avoir au moins un SGBD fonctionnel avec ces paramètres ci-joint :

- MySQL / MariaDB :
    - Utilisateur : root
    - Port : 3306

- PostgreSQL :
    - Utilisateur : postgres
    - Port : 5432

- MongoDB :
    - Port : 27017

Pour l'éxécution du script, je recommande l'utilisation de Poetry pour tester le script dans un environement isoler.

### Notes

Si dans votre SGBD vous avez déjà une base de données ou table avec déjà le même nom, il ne faut pas en recréer une par dessus. Ce script ne fais pas ça. Sauf pour MongoDB.

### Poetry

Installer Poetry sur votre système. Référez vous à la documentation spécifique à votre machine.

```shell
git clone https://github.com/Gapoly/Pokemon-in-DB
cd Pokemon-in-DB/
poetry init
poetry add mysql-connector mysql-connector-python psycopg psycopg-binary pypokedex tqdm pymongo
poetry run python3 Pokemon_in_DB.py
```

