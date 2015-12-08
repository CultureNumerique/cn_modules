Hébergement du site de staging sur GitHub.com
==========================================

Lorsque l'on se rend sur le lien:
http://culturenumerique.github.io/cn_modules/
c'est le contenu de la branche *gh-pages* qui est servi en mode "server web", et donc le index.html qui se trouve à la racine dans notre cas.

# Mise à jour manuelle
Si on veut mettre à jour le site, il faut donc mettre à jour la branche gh-pages. Pour éviter des manips particulières (styles copies, renommage, etc)  le contenu des branches *gh-pages* et *dev" sont les mêmes. Donc les commandes à effectuer pour mettre à jour le site sont, après avoir commité sur la branche master:  
```
$ git checkout gh-pages
$ git merge dev
$ git checkout dev
```
ET, lors du push, ne pas oublier de faire soit:  
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
