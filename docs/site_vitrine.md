Lorsque l'on se rend sur le lien:
http://culturenumerique.github.io/cn_modules/
c'est le contenu de la branche *gh-pages* qui est servi en mode "server web", et donc le index.html qui se trouve à la racine dans notre cas

Si on veut mettre à jour le site, il faut donc mettre à jour la branche gh-pages. Pour éviter des manips particulières (styles copies, renommage, etc)  le contenu des branches *gh-pages* et *master" sont les mêmes. Donc les commandes à effectuer pour mettre à jour le site sont, après avoir commité sur la branche master:  
```
$ git checkout gh-pages
$ git rebase master
$ git checkout master
```
ET, lors du push, ne pas oublier de faire soit:  
```
$ git push origin master gh-pages
```
OU  
```
$ git push origin --all
```
