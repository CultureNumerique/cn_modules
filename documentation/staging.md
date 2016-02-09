Hébergement du site de staging sur GitHub.com
==========================================

Lorsque l'on se rend sur le lien:
http://culturenumerique.github.io/cn_modules/
c'est le contenu de la branche *gh-pages* qui est servi en mode "server web", et donc le index.html qui se trouve à la racine dans notre cas. Pour que le site complet soit servi, il faut générer les fichiers HTML pour chaque module (`moduleX.html` situé dans chaque dossier de module `module`). C'est ce que fait le script `toHTML.py` (cf [doc sur les scripts](scripts.md)). L'idée est donc pour générer un site de staging sur la branche gh-pages de commiter ces fichiers HTML de module *uniquement* sur la branche gh-pages (puis de faire un push naturellement). Nous détaillons ci-après la procédure de manière manuelle puis automatisable à chaque *commit*.

# Mise à jour manuelle
Si on veut mettre à jour le site, il faut donc mettre à jour la branche gh-pages. Le contenu des branches *gh-pages* et *dev* sont les mêmes sauf que l'on rajoute les fichiers `moduleX.html`. Donc les commandes à effectuer pour mettre à jour le site sont, après avoir commité des modifications sur la branche dev:  

```
$  git fetch origin
$ git checkout -B gh-pages origin/gh-pages
$ git merge dev
$ python3 toHTML.py
# pour chaque dossier de module moduleX:
# nous utilisons git add -f car ces fichiers sont ignorés par le versionning (cf .gitignore file)
$ git add -f moduleX/moduleX.html
$ git commit -m 'updated html files'
$ git checkout dev
```
**ET**, lors du push, ne pas oublier de faire soit:  

```
$ git push origin dev gh-pages
```
OU  
```
$ git push origin --all
```

# Git hook `post-commit`
Pour automatiser cette tâche, il est possible d'utiliser un "git hook" `post-commit` qui est disponible dans ce dépôt : `git_hook/post-commit`. Pour l'activer il suffit de le copier en local dans votre dossier:
```
$ cp git_hooks/post_commit .git/hooks/
```
et de lui donner les droits d'exécution nécessaires: 
```
$ chmod 775 .git/hooks/post_commit
```
