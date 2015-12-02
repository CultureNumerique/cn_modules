Comment utiliser les scripts de transformations Culture Numérique
=================================================================
## Installation des dépendences 

Les scripts proposés dépendent d'autres paquets listés dans le fichier requirements.txt. 
Pour installer automatiquement ces dépendences, saisissez, à la racine du dépôt:
```
$ pip3 install -r requirements.txt
```

## Modules de transformation 
Ce module de cours est livré avec une série de scripts permettant d'exporter les contenus
de cours dans différents formats:
1. `scripts/fromMD.py` premier parsing du MarkDown source vers l'arborescence de fichiers
2. `scripts/toHTML.py` export vers site vitrine
3. `scripts/toIMS.py` export vers une archive IMSCC compatible Moodle

Sont inclus également quelques autres utilitaires:
* hooks Git `git_hooks/post-commit` permettant de mettre à jour automatiquement
la branche gh-pages (cf page Site Vitrine)

# `fromMD`
# `toHTML`
# `toIMS`

