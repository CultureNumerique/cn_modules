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
1. HTML sous forme d'un site vitrine proposant une navigation entre les différents modules (décrits dans le fichier de configuration [`toHTMLglobal.config.json`](../toHTMLglobal.config.json)) et pour chaque module, une navigation entre les sous-sections de différents types (cf [la documentation sur la chaine éditoriale](chaine_editoriale.md))
2. IMSCC permettant d'importer le cours notamment dans Moodle.

Sont inclus également quelques autres utilitaires:
* hooks Git `git_hooks/post-commit` permettant de mettre à jour automatiquement
la branche gh-pages (cf [page Site Vitrine](staging))

### Export vers HTML

Ce script prend un argument, le chemin vers le fichier de configuration qui suit le même modèle que dans le fichier  [`toHTMLglobal.config.json`](../toHTMLglobal.config.json). 

Une fois à la racine du dépôt, éxécuter le script comme suit:

```
$ python3 toHTML.py [config_file]
```

**Option** Si on ne spécifie pas de fichier de configuration, alors le script utilise le fichier [`toHTMLglobal.config.json`](../toHTMLglobal.config.json)

Ce script génère pour chaque module `moduleX` un fichier `moduleX.html` placé dans le dossier de module (par convention nommé `moduleX` également). Ces fichiers sont appelés par le fichier `index.html`, situé à la racine du dépôt et  servant de point d'entrée au site vitrine, à travers le menu de navigation entre modules.

### Export vers IMSCC/Moodle

Ce script prend comme argument le chemin vers le dossier où se trouvent les sources du cours, à savoir le fichier markdown et les médias (stockés par convention dans un dossier nommé `media`). 

Une fois à la racine du dépôt, éxécuter le script comme suit:
```
$ python3 toIMS.py module_folder
```

Ce scrit génère un fichier `module_folder.imscc.zip` qui peut être importé dans Moodle en tant que cours (cf [restauration d'un cours depuis une archive IMSCC sous Moodle](https://docs.moodle.org/28/en/IMS_Common_Cartridge_import_and_export))

