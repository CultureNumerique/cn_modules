
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->


<!-- /TOC -->
# Introduction

Ce cours est dirigé vers les savoir-faire autour de deux types de
logiciels, le traitement de texte et le tableur, qui sont des
logiciels dont la maîtrise est essentielle dans la vie universitaire,
la vie associative et votre future vie professionnelle. Ces
savoir-faire sont basés sur les modules liés à la gestion de données
et la gestion des documents. En effet, les bonnes pratiques sont
basées sur une bonne compréhension des concepts pour une utilisation
intelligente des logiciels car ces logiciels, assez faciles à
appréhender, sont souvent très mal utilisés. Leur maîtrise est une
compétence valorisable pour la suite de vos études et votre future
entrée dans la vie professionnelle.

**Modalités :** le cours introduit les savoir-faire avec textes et
vidéos qui n'ont pas la prétention d'être des tutoriaux
exhaustifs. Vous êtes fortement encouragés à utiliser le forum pour
poser des questions et répondre aux questions, à interpeller les
tuteurs au besoin, à chercher des réponses sur les forums ou sur des
tutoriaux existants car le web abonde de ressources. Le cours est
complété par des exercices simples non évalués et des exercices de
production (créer un document, créer un classeur) qui seront évalués
par les pairs, c'est-à-dire par vos collègues étudiants inscrits au
même cours.

**Note :** Les démonstrations sont réalisées avec LibreOffice Writer
  pour le traitement de textes et LibreOffice Calc pour le tableur car
  ils sont gratuits, disponibles sur tous les ordinateurs et faciles à
  installer. Toutes les notions de ce cours sont transférables dans
  tout  traitement de texte ou tout tableur de votre choix
  modulo des changements de noms de menus, des changements de forme
  des raccourcis, c'est-à-dire des modifications superficielles des
  interaces des logiciels.

# Traitements de texte

## Objectifs

L'étude des documents fait apparaître les vues séquentielle (la suite
de caractères), de structure (titre, section, sous-section, ...), de
présentation et de méta-données (taille, date de création, auteur,
...). On parle aussi de contenu, structure, forme et
méta-données. Nous allons voir que cette vision va nous permettre
d'utiliser les traitements de texte au mieux de leurs possibilités.

Le **premier objectif** est la découverte des fonctionnalités
générales, communes à tous les traitements de texte, pour la
définition du contenu et de la structure. Ceci est réalisé dans une
interface avec, au centre, une grande zone représentant une page, en
haut les menus et une zone de boutons-raccourcis. Les noms des
actions, la forme et la couleur des boutons, les icones et
l'organisation des menus varient d'un logiciel à un autre, d'une
version à une autre, d'une machine à une autre mais les
fonctionnalités sont globalement les mêmes. La *structure du document*
sera définie par l'intermédiaire de *styles* grâce aux niveaux de
titre. Il faut noter l'ambiguité du terme "style" car il sera
également utilisé pour la mise en forme du document. Cette double
fonction peut amener à de mauvais usages.

Le **second objectif** est d'apprendre à définir des *règles de mise
en forme* associées aux styles. Il est important de noter que les
boutons raccourcis faciles d'utilisation permettent de réaliser des
mises en forme directes et rapides. Mais ce sont des mises en forme au
cas par cas qui ne peuvent pas traiter de grands documents (vos
mémoires, vos rapports de stage et vos documents professionnels). Les
règles de mise en forme sont essentielles pour un bon usage des
traitements de texte, pour la manipulation de grands documents et
pour le travail en groupe. Elles permettent, en effet, de modifier la
mise en forme d'un document complet en une action, de numéroter les
sections et les pages d'un grand document, d'uniformiser la
présentation et d'appliquer des thèmes ou une charte graphique. Ceci à
condition d'avoir préalablement correctement défini la structure de
votre document.  3'30"

## Vidéo 1 : saisie, contenu et structure

### Saisie du contenu et structure de base

La saisie est une fonctionnalité fondamentale. Elle dépend de nombreux
paramètres dont la langue, les dispositifs de saisie et les aides à la
saisie. La *langue* définit l'ordre d'écriture, les caractères, les
symboles graphiques utilisés, la nature des mots, les règles
typographiques, ... Certains documents peuvent être multilingues. Nous
nous focalisons ici sur le français. Le *dispositif de saisie* le plus
répandu reste le clavier mais des systèmes d'acquisition par la voix
se développent. L'*aide à la saisie*, fréquente sur des objets
portables, peut prédire la complétion d'un mot, souligner un mot mal
orthographié, suggérer un mot, ...

La structure de base est définie avec les niveaux de titre : de niveau
1 pour les sections, de niveau 2 pour les sous-sections, ... Vous
pouvez faire une saisie complète du contenu puis définir la structure
de base ou vous pouvez définir cette structure au cours de la saisie
comme sur l'exemple de la video.  Dans cet exemple, on a saisi le texte
du titre, puis on l'a déclaré comme `titre principal`.  On a saisi le
sous titre, puis le premier titre de niveau 1, et les premières
phrases du premier paragraphe. Remarquez que le paragraphe suivant est
automatiquement dans le style `corps de texte`.

Remarquez aussi l'aide à la saisie qui a souligné un mot mal
orthographié ou qui a proposé le mot en cours de saisie. On remarque
également que les mots sont identifiés car ils sont automatiquement
sélectionnés lors de la correction orthographique. On a aussi la
possibilité de se déplacer de mot en mot avec CTRL-droite ou gauche et
de supprimer un mot avec CTRL-Retour arrière.  L'assistance à la
saisie effectue des remplacements automatiques : elle a mis en
majuscule la première lettre du mot juste après le point, elle a
inséré automatiquement une espace insécable (c'est-à-dire qui force à
afficher les symboles à sa droite et à sa gauche sur une même ligne),
elle a inséré un symbole spécifique pour les points de
suspension. Jusqu'ici, nous conservons la mise en forme par défaut,
c'est-à-dire qu'aucune règle de mise en forme n'a été définie donc les
règles par défaut s'appliquent.

[La saisie](https://owncloud.univ-lille3.fr/index.php/s/mI7DtCQqsFWhLqn){: .lien_video }


[La saisie - un copier-coller](https://owncloud.univ-lille3.fr/index.php/s/fXsFycEyKbTW9hx){: .lien_video }

### Saisie et éléments de structure

Pour manipuler correctement votre document comme mettre les retours à
la ligne au bon endroit ou faire les sauts de page correctement, le
traitement de texte doit pouvoir reconnaître les mots, les
paragraphes, les listes. nous expliquons ici quelques règles à
respecter pour ce faire.

Les **caractères**. La plupart, par exemple, lettres, chiffres et
symboles de ponctuation, sont visibles, mais certains sont invisibles
, en particulier, les espaces. Certains caractères sont aussi
interprétés par le logiciel comme une commande ou une déclaration,
c'est, par exemple, le caractère qui marque la la fin de paragraphe,
ou ceux qui marquent la fin d'un mot (espace[^2] ou ponctuation),
celui qui ajoute une espace insécable. C'est là une première
difficulté, l'espace par exemple a plusieurs fonctions. Ajouter une
espace typographique entre deux mots est utile à la présentation du
document, mais il déclare également la séparation de deux mots. Dans
la première fonction, on pourrait vouloir augmenter cette séparation
dans le rendu visuel et donc se faire suivre deux espaces. Mais on
perd le sens de la deuxième fonction puisqu'il n'y a pas de mot entre
ces deux espaces. La convention choisie est de **ne jamais avoir deux
espaces consécutifs** et de faire confiance au logiciel pour réaliser
la meilleure présentation. En effet, si deux ou plusieurs espaces se
suivent, le traitement de texte est mis en difficulté et la mise en
forme peut être insatisfaisante. Donc, *visualiser tous les
caractères*, y compris ceux qui sont invisibles, aide à bien
comprendre le contenu saisi.

Les **mots**. Le logiciel les reconnaît car ils sont séparés par des
espaces ou des signes de ponctuation. Des règles typographiques,
spécifiques à chaque langue, définissent les espaces et symboles de
ponctuation. Par exemple, en français une espace précède toujours le
signe `:` alors qu'il n'y pas d'espace avant le signe `:` en
anglais. Le respect de ces règles est impérative et, souvent, le
logiciel aide à une saisie correcte en ajoutant les espaces requis.

Les **paragraphes**.  Ce sont des ensembles de mots séparés par des
*fins de paragraphes* créés par l'appui sur la touche *Entrée*. La fin
de ligne dans le rendu du document est calculée par le traitement de
texte et donc la touche entrée ne marque pas la fin de ligne. Il est
parfois nécessaire de forcer une fin de ligne dans certains
paragraphes comme les poèmes. C'est la combinaison de
`Majuscule-Entrée` qui permet de réaliser une fin de ligne tout en
gardant le même paragraphe. Puisque chaque appui sur la touche
*Entrée* crée un nouveau paragraphe, les titres et les sous-titres
sont donc techniquement des paragraphes comme les paragraphes de
texte. Comme pour les espaces et les mots, la convention choisie est
de **ne jamais avoir deux fins de paragraphe consécutives** et de
faire confiance au logiciel pour réaliser la meilleure
présentation.

Les **titres**. Ce sont bien des paragraphes, mais le logiciel de
  traitement de texte permet de les déclarer comme titres en précisant
  leur niveau. Le niveau est la profondeur dans une hiérarchie : titre
  de niveau 1 pour une section, titre de niveau 2 pour une
  sous-section, titre de niveau 3 pour une sous-sous-section. 

Les **listes**.  Ce sont des suites de paragraphes reliés entre eux
pour permettre une présentation cohérente. Pour assurer cette
cohérence, beaucoup de caractéristiques sont définies sous forme de
règles utilisées par le logiciel pour l'apparence des listes. C'est
notamment les symboles utilisés pour les listes à puce, les
espacements, la numérotation des éléments, etc. La logique est donc de
déclarer la liste et de laisser le logiciel s'occuper de l'apparence
avec les règles de mise en forme que vous indiquez.

Repérer les composants du texte permet de comprendre la structure d'un
document, saisir à la fois le contenu et la structure d'un document et
se préparer pour une mise en forme efficace et uniforme du document.



7'

```activité
Reproduire l'exemple en vidéo.
{ }
```


## Vidéo 2 - Styles et structure

Nous avons déja vu comment utiliser les styles pour la structure de
 base. Nous voyons ici comment définir d'autres éléments de structure
 en commençant par les listes.

Chaque élément de liste est un paragraphe. On active la structure de
 liste par ce bouton qui est un raccourci du menu format/puces et
 numérotation.  On ajoute un nouvel élément en ajoutant un
 paragraphe. On peut avoir plusieurs paragraphes dans le même élément
 de liste en utilisant la touche `Retour arrière` une seule fois en
 début de paragraphe. Deux appuis de `retour arrière` quittent la
 structure de liste.

[Déclarer une structure de liste](https://owncloud.univ-lille3.fr/index.php/s/lr5jK0ryRY9iGZM){: .lien_video }

Les logiciels de traitement de texte offrent tous la possibilité
d'afficher la liste des styles disponibles (avec LibreOffice, on peut
utiliser la touche F11, le menu Style/Style et formatage ou encore le
tiroir de droite). Nous pouvons voir cette liste de styles comme la
liste des structures possibles. Se placer dans un paragraphe du texte
permet de voir quel style lui est associé. L'ensemble des styles
possibles est très grand et organisé selon une hiérarchie. On peut
restreindre cette liste à ceux qui sont appliqués dans le document ou
à ceux qui sont souvent utilisés (styles automatiques). Les styles
portent sur différents éléments de structure du document :
paragraphes, caractères, cadres (flottants), pages ou listes.
[L'utilisation des styles](https://owncloud.univ-lille3.fr/index.php/s/GagbfhWe2hzo5nN){:
.lien_video }

On associe facilement un style à un élément, ici des caractères en les
sélectionnant et en cliquant deux fois sur le style voulu. Ici, au
lieu de mettre en gras et en italique, nous préférons déclarer des
texte plus ou moins accentués. Il faut bien comprendre la
différence. Même si les textes déclarés en accentuation forte
apparaissent en gras, ce n'est pas identique de presser le bouton
gras. En les déclarant de cette façon nous ajoutons du sens que les
logiciels pourront exploiter dans d'autres situations : rendu oral,
présentation sur un autre support comme un objet portable, ou
simplement pouvoir modifier facilement dans tout le texte la mise en
forme choisie pour les éléments déclarés en style accentuation forte.
[Les style caractères. Accentuation ou Gras ?](https://owncloud.univ-lille3.fr/index.php/s/Oq5OK6UEECh9zaB){:
.lien_video }

Comme nous l'avons dit ci-dessus, l'affichage des caractères
invisibles permet de savoir exactement ce qui a été saisi. On voit les
espaces et les fins de paragraphe, on peut déceler des répétitions de
ces symboles et les supprimer. On voit également la représentation des
fins de ligne qui ne sont pas des fins de paragraphes dans cette
partie de texte.
[Affichage des caractères spéciaux dont le retour à la ligne](https://owncloud.univ-lille3.fr/index.php/s/RGeyNGslqj7Hh1C){:
.lien_video }

Le logiciel réalise souvent des opérations pour vous aider à bien
écrire votre document, comment, par exemple, l'insertion d'une note de
bas de page. Le numéro est inséré automatiquement et sera adapté si
d'autres notes sont ajoutées. Le style choisi pour la note sera adapté
automatiquement.
[Un style adapté et une numérotation automatique des notes bas de page](https://owncloud.univ-lille3.fr/index.php/s/XTMY5MPYZqpp5p2){:
.lien_video }

Un autre type de numéros ou textes gérés automatiquement par le
logiciel sont les renvois aux chapitres, illustrations, figures,
... Remarquez la liste des éléments auxquels on peut faire
référence. Vous commencez à comprendre en quoi la déclaration de
structures est vraiment intéressante et valorisante. Vous voyez les
titres, les éléments de liste, les figures, etc...  Cette technique de
déclaration et de renvois est utilisée dans tout langage de
description de documents. Par exemple, en HTML, on utilise des
(hyper-)liens qui peuvent être internes au document (renvoi vers une
partie du document) ou externes (renvoi vers un autre document).
[Insérer des renvois aux textes et illustrations](https://owncloud.univ-lille3.fr/index.php/s/TfxHkw38bFoXuXa){:
.lien_video }
[Renvoi selon un repère](https://owncloud.univ-lille3.fr/index.php/s/7xk3sKCv7AhP3wl){:
.lien_video }

Terminons par un examen de la structure arborescente de ce
document. La manipulation de cette structure permet de déplacer des
sections entières ou de réorganiser le plan.
[Réorganiser le plan](https://owncloud.univ-lille3.fr/index.php/s/kL4rzZKR6ehpVBF){:
.lien_video }


[L'autocorrection](https://owncloud.univ-lille3.fr/index.php/s/vPHjISuIO7DUx87){: .lien_video }

## Point d'étape : respecter des règles de base

L'auteur d'un document est en charge du contenu et de sa qualité, du
niveau de la langue et de l'orthographe, de la structure du
document. Le traitement de texte réalisera le travail de mise en forme
à la condition d'avoir correctement défini la structure en respectant
les règles fondamentales suivantes :

- espace et ponctuation séparent les mots. On ne doit
  donc **jamais avoir plusieurs espaces consécutifs**.
- L'appui sur la touche Entrée sépare les paragraphes. On ne doit
**jamais avoir plusieurs fins de paragraphes consécutives**.
- Éviter autant que possible la mise en forme directe au cas par cas,
  que ce soit par les menus (format) ou par les boutons-raccourcis.
- Ne pas saisir des valeurs qui sont susceptibles de varier et qui
  peuvent être générées par le traitement de textes : numérotation des
  éléments de liste, des chapitres, des pages ; références, table des
  matières, bibliographies, index.

Si vous respectez ces règles, alors le logiciel va pouvoir calculer la
 meilleure mise en forme possible : l'espacement entre les mots, la
 taille des interlignes, l'espacement entre paragraphes, l'espacement
 avant et après les titres, les marges, les décalages, les
 alignements, ...  Vous pourrez également numéroter automatiquement
 les sections, créer une table des matières, ... Vous allez pouvoir
 agir sur tous ces éléments pour **personnaliser la mise en forme en
 modifiant les styles**, c'est l'objet de la suite de notre cours.

## Vidéo 3 - Personnaliser les styles

Un document de qualité est justifié et une césure des mots est appliquée. En modifiant la définition du corps de texte, nous définissons une règle générale qui va s'appliquer à tout le document, ou plutôt à tous les paragraphes de style `corps de texte` de ce document.

[Une première règle de mise en forme](https://owncloud.univ-lille3.fr/index.php/s/B4odOArZ2nzOPjU){: .lien_video }

Des règles de mise en forme s'appliquent aussi sur les caractères comme pour les accentuations ou les accentuations fortes.

[Une autre règle de mise en forme](https://owncloud.univ-lille3.fr/index.php/s/uwVtUNEDijTHcHE){: .lien_video }

Parfois, certains éléments de structure sont propres à un certain type de document. Par exemple ici, nous avons des noms de logiciels. Déclarer ce nouvel élément de structure ajoute de la sémantique, du sens au document qui pourra être exploité par d'autres logiciels, mais facilitera également l'uniformisation de la présentation. 

[Nouveau style de caractère : logiciel](https://owncloud.univ-lille3.fr/index.php/s/X4vXqDW9P6eKmtk){: .lien_video }

Bien sûr, la définition de nouvelles structures, donc de nouveaux style,  s'applique sur les caractères comme les paragraphes. Ici, ce morceau de code ne doit pas être justifié. Il peut être déclaré et mis en forme spécifiquement. Si d'autres parties de code apparaissent dans le document, il seront aussi déclarés comme tels et donc auront la même apparence. 

[Nouveau style de paragraphe : code](https://owncloud.univ-lille3.fr/index.php/s/H6vMvhj1yldSk4q){: .lien_video }

```activité
Reproduire le document dont un pdf vous est donné ici. Aucune mise en forme directe n'est tolérée !
{}
```

## Vidéos 4 - Tables et numérotations 

La numérotation des chapitres est également une opération réalisée automatiquement par le traitement de textes. Il ne faut pas saisir soi-même ces numéros. L'outil de numérotation des chapitres le fait pour vous. Il faut indiquer quelles sont les noms des styles (structures) identifiant les titres. Bien sûr par défaut ce sont les titre 1, titre 2, etc... Ensuite on choisit le style de numérotation et si on doit faire apparaître la hiérarchie dans le numéro en affichant les sous-niveaux. Amusez-vous à modifier tous les paramètres pour comprendre les impacts sur la présentation de ces numéros.
[Numerotation automatique des chapitres](https://owncloud.univ-lille3.fr/index.php/s/orItAwe4RtExNOe){: .lien_video }

La structure d'un document c'est aussi une structure en différentes pages. Une page de garde, des pages d'index ou de table des matières ou d'illustrations, ... Différents styles de pages identifient cette structure. On peut la déclarer en ajoutant des sauts de page manuels et spéciaux, puis définir quel sera le style de la page suivante et le début de sa numérotation.
[Structuration en liste de pages de natures différentes](https://owncloud.univ-lille3.fr/index.php/s/NC34k8SnyGy85Ye){: .lien_video }

Une fois la structure du document déclarée, l'insertion d'une table des matières, une table des illustrations,... est très simple, puis hautement paramétrable. Si la numérotation des chapitres a été appliquée alors les numéros seront repris. Des efforts de mise en forme peuvent être nécessaires selon les logiciels comme par exemple ici. Nous ajoutons une espace après chaque numéro.
[Génération d'une table des matières](https://owncloud.univ-lille3.fr/index.php/s/ftcxiFP4X3MKIms){: .lien_video }

```activité
Reproduire le document dont un pdf vous est donné ici. Aucune saisie directe des numéros et tables n'est autorisée!
{}
```


## Video 5 - métadonnées
Les meta-données sont des données à propos du document. Elles sont soit calculées par le logiciel (par exemple le nombre de mots, la taille etc...) ou déclarées par l'utilisateur (le titre, le sujet, l'auteur...). Les meta-données sont utiles pour le traitement de grands corpus de documents. On les retrouve ici dans le menu des propriétés. Il est aussi possible d'insérer les métadonnées comme contenu textuel du document. 
[Utilisation des méta-données](https://owncloud.univ-lille3.fr/index.php/s/aNCsseInHQ7Gf2D){: .lien_video }

## Vidéos avancées

### Travail collaboratif
Travailler en groupe c'est d'abord communiquer sur l'édition du document. Dans ce cas, on veut commenter des parties. C'est aussi être capable de suivre des modifications. Lisez le texte du document pour mieux comprendre et regardez les différentes possibilités qui vous sont offertes. En situation de travail collaboratif, les modifications auront pu être apportées par différents auteurs et le coordinateur va donc valider ou rejeter les modifications. 
[Commentaires et suivi des modifications](https://owncloud.univ-lille3.fr/index.php/s/rCEsDhJnDCN44Mg){: .lien_video }


Une autre fonctionnalité de suivi des versions est illustrée ici. 
[Suivi des versions](https://owncloud.univ-lille3.fr/index.php/s/Oaec8mpdueuxlY7){: .lien_video }

### Comprendre la hiérarchie de styles

Les styles sont organisés dans une hiérarchie. Ce n'est pas qu'une façon de catégoriser pour les retrouver ou y accéder plus rapidement. La raison principale tient à un concept qu'on retrouve souvent en informatique, la notion d'*héritage*. Illustrons cette notion par l'exemple. Si la couleur des caractères n'est pas définie au niveau d'un style elle sera alors définie par celle de son style juste au dessus de la hiérarchie. Par exemple en passant le corps de texte en rose, les notes de bas de page le seront aussi, mais pas les titres. Par contre définir cette couleur au style par défaut, sommet de la hiérarchie affectera tous les styles de document (sauf bien sûr si cette propriété a été définie pour un style donné). 

[La hiérarchie de styles](https://owncloud.univ-lille3.fr/index.php/s/PkfPwBzS7OziFfi){: .lien_video }


### Mise en forme des listes

Les listes en typographie française utilisent des tirets demi-cadratins (Code unicode 2013, [Tiret-moyen](https://fr.wikipedia.org/wiki/Tiret#Tiret_moyen)). On peut définir donc une liste à la française. C'est un peu technique. 

[Listes à la française](https://owncloud.univ-lille3.fr/index.php/s/3FauhABN3VewRHd){: .lien_video }

### Parallèle avec Word
Nous avons expliqué pourquoi toutes nos démos ont été réalisées avec LibreOffice, mais nous avons égalmeent indiqué que tout ce qui a été décrit est également valable avec les autres logiciels de traitement de textes. Voici un petit exemple avec une version de Word. Nous retrouvons la possibilités d'afficher ou non les caractères non imprimables, un styleur qui permet de structurer les différents éléments du document, que ce soient les paragraphes ou les caractères, la définition de listes à puces ou ordonnées.
Il est bien sûr également possible de modifier la présentation prédéfinis des styles comme si pour le style `normal` qui sert pour le corps de texte.
Nous retrouvons aussi l'outil de correction automatique lors de la saisie, les correcteurs orthographique et toutes les aides à la saisie.
La génération  d'un index ou d'une table des matières suit la même logique, ainsi que l'insertion de marque, de repère ou de renvois de notes.
Bien sûr chaque logiciel a son interface propre et le nom des menus ou des outils peut varier d'une version à une autre, mais il est important de retenir que les notions vues dans ce cours ne sont pas spécifiques à un logiciel mais communes à tous les traitements de texte.
[petite démo Word](https://owncloud.univ-lille3.fr/index.php/s/bxlm4dW5ddCLCmS){: .lien_video }

### Autres points possibles à aborder
- présentation de la création de liste pendant la frappe
(* , - , 1), a), ...) Insister sur l'automatisation
- présenter le bouton de liste ((dés)activer puces)
- détailler puce + retrait
- un copier/coller colle le style (exemple coller du texte dans une note de bas de page : on perd souvent le style par défaut de note de bas de page).

- insertion d'image
- pied de page / entête
- numeros de page / champs
- tableaux

- bibliographie
> surement en plusieurs fois




# Le tableur

## Qu'est-ce qu'un tableur ? Ce qu'il n'est pas...

Le tableur est un outil pour *représenter*, pour *interroger* et *traiter* des données. Ce n'est *pas* pour présenter des tableaux, faire des fiches ou n'importe quelle liste, ... Le logiciel de traitement de textes sait gérer des tableaux. La manipulation d'un tableur est donc une activité de traitement de données, et donc un pas supplémentaire vers l'informatique en tant que science du calcul. 

Un vocabulaire spécifique accompagne la manipulation du tableur. 

Pour représenter ses données, le tableur mémorise des  **relations**. Ces relations sont présentées dans des **tables** qui sont structurées en **lignes** et  **colonnes** à l'intersection desquelles se trouvent les  **cellules**. Une ligne représente une *relation* entre des données stockées dans les colonnes. Et dans chaque colonne on trouve une uniformité des valeurs qui sont de même nature. Les tables sont stockées dans des *feuilles de calcul*.

Interroger et traiter des tables, c'est par exemple :
- Sélectionner ou filtrer certaines lignes.
- Rechercher, extraire des lignes.
- Agréger, regrouper des lignes.
- Trier les lignes.
- En tirer des diagrammes.

C'est aussi traiter des données par des calculs (sommes, moyennes, comptes,...) de façon automatique, programmée, et représentée par des *formules*. Les formules sont comme des règles de calcul.


## Dans une cellule 

Que trouve-t-on (simultanément) dans une cellule ? On y trouve des **valeurs** (du texte, des nombres, et même des messages d'erreur). C'est ce qui s'affiche dans une cellule. Mais on y trouve aussi des formules, (ce qui permet d'obtenir la valeur), et des formats (ce qui permet de présenter cette valeur) ou encore des commentaires qui peuvent expliquer/commenter une valeur.

On peut observer des différences entre ce qui est contenu dans la cellule et ce qui est affiché à cause du choix de format. Par exemple, on peut représenter une valeur sous forme de nombre, de pourcentage, ou même de date.

Les formules commencent par le signe `=`. C'est ce qui distingue une valeur d'une formule. 


[Petit tour d'horizon](https://owncloud.univ-lille3.fr/index.php/s/HiN3wyQzb5Hlgr1){: .lien_video }


## Mise en forme

Comme pour le traitement de textes, il existe des styles pour uniformiser la présentation. Attention à ne pas mettre en péril les traitements par des soucis de présentation. Par exemple insérer des lignes blanches ou avec un fond coloré pour faire des bordures dans une table rompt la logique de table et les traitement de filtre, tri, etc... deviennent impossibles.

[Styles](https://owncloud.univ-lille3.fr/index.php/s/wRHYkInBqUjrkD6){: .lien_video }
[Logique de table](https://owncloud.univ-lille3.fr/index.php/s/tcnC1F86vnrkWcQ){: .lien_video }

## Traiter des données 

Faire un traitement c'est
1. Disposer de données en entrée (des valeurs connues, acquises)
2. Réaliser des opérations 
3. Produire des résultats

La traduction dans le tableur posera les questions suivantes :  Quelles sont les cellules, les lignes ou les colonnes qui vont  contenir des valeurs en entrée ?  Quelles sont les cellules qui vont contenir des résultats de calcul ?  Comment les organiser ? Comment écrire ces calculs ?

### Analyser un problème 
L'exemple suivant est évidemment fictif. En vue d'un voyage de classe à Londres, on souhaite mémoriser et analyser la monnaie qu'emportent les enfants. On connaît le taux de conversion, et le seuil maximal en euros qu'un enfant peut emporter. La table que nous allons construire va mettre en relation les noms et prénoms des enfants avec l'argent emporté. Chaque ligne correspond à un enfant. Les colonnes spécifient les noms des données en relation. 

Parmi les données manipulées, certaines sont saisies et d'autres sont calculées à partir des données saisies. Ici connaissant le taux de conversion et le montant en euros, il est facile de calculer le montant en livres. Connaissant le montant en euros et le seuil, on peut savoir si le montant  dépasse ce seuil. On peut aussi calculer la moyenne, le minimum et le maximum des montants emportés. 


### Décrire les calculs

Le calcul va faire référence à des données en entrée : On utilise des *références* aux cellules. Les références des cellules sont composées par les numéros de ligne et de colonne. Exemple : B7 la cellule en colonne B et ligne 7. Les références peuvent être *relatives* ou *absolues*. Les notions relative/absolue  n'ont de sens que lorsqu'on *copie* une cellule contenant une formule dans une autre cellule. 

Lors de la copie d'une cellule, les références relatives s'ajustent. Par exemple si on copie la cellule contenant la référence B7 de 2 colonnes à droite et 3 lignes vers le bas, la référence devient D10. 

Lors de la copie d'une cellule, les références relatives restent fixes. On peut fixer la ligne ou la colonne ou les deux en faisant précéder le numéro de ligne ou de colonne par un $. Par exemple, si on copie une cellule contenant la référence B$7 de 2 colonnes à droite et 3 lignes vers le bas, la référence devient D$7.  Avec $B7 la référence devient $B10. Avec $B$7 la référence reste $B$7.

### Autres références
- On peut faire référence à des cellules d'une *autre feuille* avec la
  syntaxe suivante : 'Nom de Feuille'.reference. 
  - Exemple : 'Feuille 1'.B7
- Les références peuvent désigner une *liste* de cellules
  en donnant les références séparées par des `;`
  - Exemple : `B3;D$7;$A1;E3`
- Les références peuvent désigner une *plage rectangulaire* de cellules
  en donnant les références des coins supérieur gauche
  et inférieur droit séparés par `:`
  - Exemples : `B3:D7` ou `$B$3:D7` ou `$B3:D$7` etc.
- Mais les références peuvent aussi se désigner par des *noms*.
 
[Autres références](https://owncloud.univ-lille3.fr/index.php/s/OIPzU7hIZXlYa3s){: .lien_video }
[Nom](https://owncloud.univ-lille3.fr/index.php/s/rN4qu3qhYycb4Kl){: .lien_video }

## Opérations sur les tables

On se concentre principalement sur deux opérations

### Le tri 

Le tri réordonne les lignes d'une table. Pour réaliser cette opération, on doit désigner :
La table : il suffit de sélectionner une cellule de la table pour cela. Il faut désigner les critères de tri. C'est une liste de noms de colonnes. 

[Le tri](https://owncloud.univ-lille3.fr/index.php/s/5e5Euyl25PAmgml){: .lien_video }

### La sélection ou filtre. 

En entrée de cette opération on doit désigner la table comme pour le tri et les critères de filtre : les conditions à vérifier pour qu'une ligne soit sélectionnée ou non.

[Le filtre](https://owncloud.univ-lille3.fr/index.php/s/KOYB3fVqeIzI6R4){: .lien_video }


## Représentations graphiques

Un graphique ou diagramme est utilisé pour porter un message. Le type de diagramme est important car il précise ce message : 
- Pour une répartition : les camembert, et barres de pourcentage.
- Pour  des valeurs qui peuvent s'ajouter : les empilements 
- Pour les séries de valeurs continues : les courbes.
- Pour les séries de valeurs non continues, les histogrammes
- Pour les données dans de nombreuses dimensions : les radars.

Rappelez-vous donc qu'on ne représente pas pour faire beau mais pour informer.

> Ici placer des images seulement pour illustrer le discours. Tous les étudiants se démerderont pour savoir comment faire un diagramme. 

## Construire des formules

Pour construire des formules on suit un langage formel, informatique, bien particulier. Le respect de la syntaxe est essentiel, sinon des erreurs apparaissent. Chaque formule doit commencer par le signe `=`. Derrière le signe `=` se trouve une expression utilisant des valeurs,  des références, des *fonctions*, des opérateurs comme `+,-,*,/`, Dans les formules, les valeurs textuelles s'écrivent avec des guillemets. 

Par exemple voici 4 formules différentes: 

	=10
    ="Bonjour"
    =10*2+1
    =(A1*2+1)/$B$2

[Les expressions](https://owncloud.univ-lille3.fr/index.php/s/wRF50DNBzJ3d8GD){: .lien_video }

Parmi les fonctions principales, beaucoup portent sur des ensembles de valeurs : SOMME, MOYENNE, MAX, MIN, NB, NBVAL. La fonction SI est très importante. Elle permet de faire un calcul conditionnel. La forme est =SI(critere;valeurVrai;ValeurFaux)=. Exemple : 

	=SI(A1>=10;"Bravo";"Recalé")
 
Si la valeur en A1 est supérieure ou égale à 10, alors la formule affiche dans la cellule la valeur "Bravo" (le texte *Bravo*) sinon la formule renvoie la valeur "Recalé". 
[Le si](https://owncloud.univ-lille3.fr/index.php/s/hTSA04wTrwgCNhd){: .lien_video }

Les fonctions peuvent être imbriquées les unes dans les autres. C'est par exemple très intéressant pour faire un calcul avec plusieurs SI correspondant à plus de deux cas possibles. Remarquez également la mise à jour des calculs lorsque les paramètres de seuil évoluent.

[Le si imbriqué](https://owncloud.univ-lille3.fr/index.php/s/Zn49n6f0dOQ47BN){: .lien_video }


# Le logiciel de présentation

# Les restes... 

[Modifs de styles paragraphes et caractères](https://owncloud.univ-lille3.fr/index.php/s/i2lN6EzSCU4XK39){: .lien_video }

Notre document est maintenant entièrement structuré et stylé. Nous allons nous interessé à la mise en page et à la mise en forme afin d'améliorer la vue de présentation.
Par exemple, les paragraphes de corps de texte sont alignés à gauche, une présentation justifiée est plus propre dans les documents imprimés. Nous allons donc utilisés le styleur pour modifier les attributs de présentation du style "corps de texte". À l'aide du clic-droit je choisis "modifier le style". Sur cet écran de nombreuses possibilités sont offertes, nous vous laissons les explorer. Je vais simplement modifier l'alignement pour choisir "justifié".
Je valide et automatiquement TOUS les paragraphes de style "corps de texte" de mon document sont mis à jour.
Je vais maintenant faire la même chose avec un style de caractères. Choisissons le style "accentuation forte". Je vais cette fois modifier sa couleur. Après validation tous les caractères de ce style sont mis à jour dans l'ensemble de mon document.
Il ne reste plus qu'à faire la même chose pour chacun des styles que je veux personnaliser.




### Vidéo 1 - Saisie des éléments de base
- débuter un document, page blanche sans styleur
- saisir au kilomètre, uniquement les fins de paragraphes et quelques éléments de structure (titres etc.)
- énoncer (voix off) les niveaux de titre sans mise en forme
- faire des fautes, utiliser le correcteur
- titre, sous-titre, titre1, titre2, plusieurs parag de contenu, une liste SANS mise en forme
> Cette vue est essentiellement séquentielle, les seuls éléments de structure présents sont les paragraphes, mais nous avons déjà utilisé le correcteur orthographique.
> Les traitements de texte sont des outils puissants qui proposent beaucoup de fonctionalités pour nous aider dans la rédaction, la conception et la présentation de notre travail. Par exemple les correcteurs orthographiques nous alertent en nous signalant des erreurs probables que nous pouvons corriger. Mais d'autres outils existent et s'appliquent parfois automatiquement, ce qui peut être perturbant. En particulier, il existe des fonctionnalités d'auto-correction qui peuvent s'appliquer pendant la frappe. Ces outils sont puissants, il sont capables de corriger à la volée des erreurs de saisie telles que l'oubli d'une majuscule en début de phrase, ou encore l'insertion d'espace insécable devant les ponctuation double afin de respecter les règles typographiques.
Cet outil est précieux et nous fait gagner du temps tout en amenant de la rigueur. Néanmoins, il faut bien avoir conscience qu'il peut être (dés)activer.
Par exemple il corrige systématiquement les fautes courantes à partir d'une liste, ou insére une majuscule en début de phrase, tous ces comportements sont paramétrés et nous pouvons choisir de les utiliser ou pas, ils sont en général une aide mais peuvent s'avérer gênants dans certains cas particulier, il est alors imortant de savoir comment les désactiver. Nous vous invitons à regarder de près le paramétrage de cet outil afin d'en comprendre le fonctionnement.

- montrer
 - la correction des maj en début de phrase (après point et espace).
 - la correction DOuble majuscule
 - l'insertion espace insécable devant ; (avec affichage des car non imprim)
 - correction d'un mot mal orthographié
- le panneau de config des paramètres
- qu'on peut (dés)activer quand on le veut

- enrigistrer (dossier / fichier / extension-format)

### Avant de démarrer

Il existe de nombreux logiciels de traitement de textes et trois d'entre eux sont particulièrement répandus :
- `Microsoft Word` de la suite `Office`
- `Writer` de la suite `LibreOffice`
- `Writer` de la suite `OpenOffice`

Tous ces logiciels ont le même objectif et donc les mêmes capacités de traitement (appelées fonctionnalités). Ils présentent de petites différences d'interface en fonction des versions et des systèmes d'exploitation des ordinateurs. Notre objectif n'est pas de les présenter tous, ni même de présenter tout ce dont ils sont capables. Ce que nous voulons que vous reteniez et que vous maîtrisiez est très général et ne dépend pas d'un logiciel en particulier.

Chacun d'entre vous pourra faire les exercices avec le logiciel de son choix à condition de respecter un format de fichier interopérable.

En effet, le choix du logiciel est en fait beaucoup moins important que le format de fichier utilisé. Aujourd'hui 2 grands formats se font concurrence :
- le format `.odt`(*Open Document Text*) qui est un standard ouvert développé pour l'interopérabilité. Il n'est pas développé par une société particulière mais par un consortium international[^1].
- le format `.docx` qui est la réponse apportée par `Microsoft` au format `.odt`.
La plupart des logiciels récents savent manipuler (ouvrir et enregister) des fichiers dans les 2 formats.

Notons qu'il reste encore beaucoup de vielles versions de `Word` qui ne savent gérer que des fichiers au format `.doc`. Ce format est propriétaire, fermé, pas du tout interopérable et il est devenu obsolète, nous déconseillons vivement son utilisation.

Nous avons choisi d'utiliser :
- le format `.odt` pour l'enregistrement des fichiers
- le logiciel `LibreOffice` pour sa facilité d'utilisation et la possibilité pour chacun de l'installer gratuitement et librement sur sa machine.
1'45"

### Veuves, orphelines, enchaînements
Nous voici maintenant avec un document dont la présentation a été entièrement revisitée. Nous allons voir que les modifications de styles permettent d'obtenir beaucoup de rigueur dans la présentation.
Par exemple à la page 3 on constate qu'alors qu'il restait un peu de place en bas de la page, le paragraphe commence sur la page suivante ce qui évite des lignes seules en bas ou en haut de page que l'on appelle des veuves et des orphelines. Pour règler cela, j'ai modifié dans le style les paramètres d'enchaînement, en demandant au logiciel de ne pas autoriser lors du calcul de la mise en page de ligne seules pour les paragraphes "corps de texte".

Parallèlement on voit à la page 4 que le titre de niveau 2 aurait pu "tenir" en bas de la page précédente. Or, un titre en bas de page nuit à la lisibilité et il est préférable de ne jamais laisser un titre ou un sous-titre en bas de page. Pour cela, il suffit de choisir dans la section enchaînement "solidaire avec le paragraphe suivant".
Ces techniques appliquées à tous les niveaux de titre vous assure une mise en page de grande qualité sans avoir à vérifier chacun des titres.

[Modifs de styles enchaînements](https://owncloud.univ-lille3.fr/index.php/s/TPCCJtoBfHhMe85){: .lien_video }


[^1]: OASIS, dont font partie the Document Foundation qui développe LibreOffice, mais aussi de grands acteurs du logiciel comme Microsoft ou ORACLE, des universités, etc.
[^2]: l'espace en typographie est un nom féminin.
