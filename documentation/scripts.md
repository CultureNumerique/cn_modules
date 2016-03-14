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

Ce scrit génère un fichier `module_folder.imscc.zip` qui peut être importé dans Moodle en tant que cours (cf [restauration d'un cours depuis une archive IMSCC sous Moodle](https://docs.moodle.org/28/en/IMS_Common_Cartridge_import_and_export)). 

Cette archive contient également toutes les activités avec les questions associées déjà intégrées.

#### Limitations à l'import d'archives IMS dans Moodle

Cette procédure d'import vers Moodle au format IMS Common Cartridge a quelques limitations :

- un bug affecte la version 3.0 de Moodle et **empêche l'import d'archive IMS si les quiz intégré (au format [XML/IMS-QTI](http://www.imsglobal.org/question/qtiv1p2/imsqti_asi_bindv1p2.html#1439623)) contiennent au moins une question Vrai/Faux**. [Ce bug a été signalé au groupe de developpement de Moodle](https://tracker.moodle.org/browse/MDL-53337); un contournement a été inclu dans le code actuel de toIMS.py qui déclare les questions Vrai/Faux comme des questions à choix multiples (toIMS.py ~l52).
- les **paramétrages d'achèvement et de revue des quiz ne sont pas conservés**. En effet ces paramètres spécifiques à Moodle ne sont pas capturés dans le format IMS. Le comportement limitant vient surtout de ce que **[les paramètres globaux](https://docs.moodle.org/29/en/Common_module_settings)**, qui normalement sont utilisés comme paramètres par défaut lors de la création d'un nouveau quiz **ne sont pas pris en compte lors de l'import IMSCC**. Ce comportement semble plutôt anormal et [a été signalé également](https://tracker.moodle.org/browse/MDL-53422)


### Export vers Open EDX (En cours)

Un script permettant la conversion d'une archive Moodle au format mbz vers le format XML OPenEDX a été démarré [mais n'est plus maintenu](https://github.com/mitocw/moodle2edx).

L'objectif dans ce projet est de produire une archive au format [Open Learning XML (OLX)](http://edx-open-learning-xml.readthedocs.org/en/latest). Ce format est basé sur une architecture modulaire dans laquelle les activités sont décrites dans des blocs de composants "XBlocks"; les types de composants que nous devons développer en priorité sont :

- [composants HTML](http://edx-open-learning-xml.readthedocs.org/en/latest/components/html-components.html#html-components)
- [composants "Problems"](http://edx-open-learning-xml.readthedocs.org/en/latest/problem-xml/index.html#problems)

