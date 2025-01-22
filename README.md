# Pokemon in DB

![Pokemon](https://mir-s3-cdn-cf.behance.net/projects/404/5f7d78149825051.62eeab127b743.jpg)




## Installation

### 1. Poetry

Installer Poetry sur votre système. Référez vous à la documentation spécifique à votre machine.

```shell
poetry init
poetry add mysql-connector mysql-connector-python psycopg psycopg-binary pypokedex tqdm
poetry run python3 Pokemon_in_DB.py
```

### Notes

Si dans votre SGBD vous avez déjà une base de données ou table avec déjà le même nom, il ne faut pas en recréer une par dessus. Ce script ne fais pas ça.
