LANGUAGE:   fr
TITLE:   Savoir-faire autour du traitement de texte et du tableur
MENUTITLE: Traitement de texte et tableur
AUTHOR:     Culture numérique
CSS: http://culturenumerique.univ-lille.fr/css/base.css
<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [Introduction](#introduction)   
- [Traitements de texte](#traitements-de-texte)   
   - [Objectifs](#objectifs)   
   - [Saisie du contenu et structure de base](#saisie-du-contenu-et-structure-de-base)   
   - [Saisie et éléments de structure](#saisie-et-éléments-de-structure)   
   - [Styles et structure](#styles-et-structure)   
   - [Point d'étape : respecter des règles de base](#point-détape-respecter-des-règles-de-base)   
   - [Personnaliser les styles](#personnaliser-les-styles)   
   - [Numérotation et tables associées](#numérotation-et-tables-associées)   
   - [Métadonnées](#métadonnées)   
   - [Avec un autre logiciel](#avec-un-autre-logiciel)   
   - [Aller plus loin](#aller-plus-loin)   
      - [Travail collaboratif](#travail-collaboratif)   
      - [Comprendre la hiérarchie de styles](#comprendre-la-hiérarchie-de-styles)   
      - [Mise en forme des listes](#mise-en-forme-des-listes)   
      - [Autres fonctionnalités](#autres-fonctionnalités)   
- [Le tableur](#le-tableur)   
   - [Objectifs](#objectifs-1)   
   - [Découverte du tableur](#découverte-du-tableur)   
      - [Fonctionnalités](#fonctionnalités)   
      - [Organisation générale](#organisation-générale)   
      - [Dans une cellule](#dans-une-cellule)   
      - [Mise en forme](#mise-en-forme)   
   - [Traiter des données](#traiter-des-données)   
      - [Organiser ses données dans le tableur](#organiser-ses-données-dans-le-tableur)   
      - [Expliciter les calculs](#expliciter-les-calculs)   
      - [Autres références](#autres-références)   
   - [Construire des formules](#construire-des-formules)   
   - [Opérations sur les tables](#opérations-sur-les-tables)   
      - [Le tri](#le-tri)   
      - [La sélection ou filtre.](#la-sélection-ou-filtre)   
   - [Représentations graphiques](#représentations-graphiques)   

<!-- /MDTOC -->
# Introduction

## Présentation du cours  
Ce cours est dirigé vers les savoir-faire autour de deux types de
logiciels, le traitement de texte et le tableur. Ces savoir-faire sont
basés sur les modules liés à la gestion de données et la gestion des
documents. En effet, les bonnes pratiques reposent sur une bonne
compréhension des concepts pour une utilisation intelligente de ces
logiciels. Car, peut-être à cause d'une apparente facilité, ces
logiciels sont parfois très mal utilisés. Pourtant leur maîtrise est
une compétence essentielle pour la suite de vos études et votre future
entrée dans la vie professionnelle.

**Modalités :** le cours introduit ces savoir-faire par le moyen de
textes et vidéos qui n'ont pas la prétention d'être des tutoriaux
exhaustifs. Vous êtes fortement encouragés à utiliser le forum pour
poser des questions et répondre aux questions, à interpeller les
tuteurs au besoin, à chercher des réponses sur les forums ou sur des
tutoriaux existants car le web abonde de ressources. Le cours est
complété par des exercices simples non évalués et des exercices de
production (créer un document, créer un classeur) qui seront évalués
par les pairs, c'est-à-dire par vos collègues étudiants inscrits au
même cours.

**Note :** Les démonstrations sont réalisées avec LibreOffice Writer
  pour le traitement de texte et LibreOffice Calc pour le tableur car
  ils sont libres, gratuits, disponibles sur tous les ordinateurs et faciles à
  installer. Toutes les notions de ce cours sont transférables dans
  tout  traitement de texte ou tout tableur de votre choix
  modulo des changements de noms de menus, des changements de forme
  des raccourcis, c'est-à-dire des modifications superficielles des
  interfaces des logiciels.

**Installer libreOffice :**  Si vous voulez installer LibreOffice, ce que nous vous conseillons, il faut :

- aller sur [http://www.libreoffice.org/](http://www.libreoffice.org/)
- télécharger et installer le logiciel
- retourner sur [http://www.libreoffice.org/](http://www.libreoffice.org/)
- télécharger et **exécuter** la traduction française de l'interface (*Translated User interface*)
- quitter et relancer LibreOffice.
- le cas échéant, ne pas tenir compte des messages d'erreur concernant *JRE* (un composant facultatif de `libreoffice`).


# Traitements de texte

## Objectifs

L'étude des documents fait apparaître les vues séquentielle (la suite
de caractères), de structure (titre, section, sous-section, ...), de
présentation (couleurs, dimensions, ...) et de métadonnées (date de
création, auteur, ...). On parle aussi de contenu, structure, forme et
métadonnées. Nous allons voir que cette vision définit le socle
commun à tous les logiciels de traitement de textes. Comprendre ce
socle va nous permettre d'utiliser n'importe quel traitement de texte
au mieux de ses possibilités, de s'adapter à ses évolutions.

Le **premier objectif** est la découverte des fonctionnalités
générales, communes à tous les traitements de texte, pour la
définition du contenu et de la structure. Ceci est réalisé dans une
interface avec, au centre, une grande zone représentant une page, en
haut les menus et une zone de boutons-raccourcis. Les noms des
actions, la forme et la couleur des boutons, les icônes et
l'organisation des menus varient d'un logiciel à un autre, d'une
version à une autre, d'une machine à une autre mais les
fonctionnalités sont globalement les mêmes. La *structure du document*
sera définie par l'intermédiaire de *styles* grâce aux niveaux de
titre. Il faut noter l'ambiguïté du terme "style" car il sera
également utilisé pour la mise en forme du document. Cette double
fonction peut amener à de mauvais usages.

Le **second objectif** est d'apprendre à définir des *règles de mise
en forme* associées aux styles. Il est important de noter que les
boutons raccourcis et le menu format, faciles d'utilisation permettent
de réaliser des mises en forme directes et rapides. Mais ce sont des
mises en forme au cas par cas qui ne peuvent pas traiter de grands
documents (vos mémoires, vos rapports de stage et vos documents
professionnels). Les règles de mise en forme sont essentielles pour un
bon usage des traitements de texte, pour la manipulation de grands
documents et pour le travail en groupe. Elles permettent, en effet, de
modifier la mise en forme d'un document complet en une action, de
numéroter les sections et les pages d'un grand document, d'uniformiser
la présentation et d'appliquer des thèmes ou une charte
graphique. Ceci à condition d'avoir préalablement correctement défini
la structure de votre document.

## Saisie du contenu et structure de base

[la saisie](https://vimeo.com/182868003){: .cours_video}

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

[Vidéographie : La saisie](https://player.vimeo.com/video/183312871){: .lien_video }

La structure de base est définie avec les niveaux de titre : de niveau
1 pour les sections, de niveau 2 pour les sous-sections, ... Vous
pouvez faire une saisie complète du contenu puis définir la structure
de base ou vous pouvez définir cette structure au cours de la saisie
comme sur l'exemple de la vidéo.  Dans cet exemple, on a saisi le texte
du titre, puis on l'a déclaré comme `titre principal`.  On a saisi le
sous-titre, puis le premier titre de niveau 1, et les premières
phrases du premier paragraphe. Remarquez que le paragraphe suivant est
automatiquement dans le style `corps de texte`.

Remarquez aussi l'aide à la saisie qui a souligné un mot mal
orthographié ou qui a proposé le mot en cours de saisie. On remarque
également que les mots sont identifiés car ils sont automatiquement
sélectionnés lors de la correction orthographique. On a aussi la
possibilité de se déplacer de mot en mot avec `CTRL-droite` ou
`CTRL-gauche` et de supprimer un mot avec `CTRL-Retour arrière`.
L'assistance à la saisie effectue des remplacements automatiques :
elle a mis en majuscule la première lettre du mot juste après le
point, elle a inséré automatiquement une espace insécable
(c'est-à-dire qui force à afficher les symboles à sa droite et à sa
gauche sur une même ligne), elle a inséré un symbole spécifique pour
les points de suspension. Jusqu'ici, nous conservons la mise en forme
par défaut, c'est-à-dire qu'aucune règle de mise en forme n'a été
définie donc les règles par défaut (choisies par le concepteur du
logiciel) s'appliquent.

[Vidéographie : La saisie - un copier-coller](https://player.vimeo.com/video/183312874){: .lien_video }

[Vidéographie : L'aide à la saisie](https://player.vimeo.com/video/183312878){: .lien_video }

```compréhension
::Typographie Accents capitales::
[markdown]
Savoir composer un document selon les règles typographiques n'est pas
simple. Pour vous en convaincre, vous pouvez vous rendre en
bibliothèque consulter les (très beaux) ouvrages qui y sont
consacrés. Dans bien des cas, mieux vaut laisser l'ordinateur gérer
seul certains choix comme, par exemple, la taille des espaces. Dans
quelques logiciels professionnels des règles de typographie sont
implantées, des algorithmes sophistiqués permettent de sélectionner la
meilleure organisation des pages pour l'homogénéité, la lisibilité et
la cohérence.  Mais certaines règles comme l'accent sur les
majuscules, la forme des abréviations ne reposent que sur vous.  
\n
Lisez [les petites leçons de typographie](http://jacques-andre.fr/ed/index.html#lessons)
par Jacques André pour vous en convaincre et découvrir les fautes les plus
courantes, puis répondez aux questions suivantes :
\n
En français, on accentue les capitales (majuscules). {T}

::Majuscule en début de mot::
[markdown]
En français, dans un titre de premier niveau on met une majuscule à chaque début de mot. {F}

::Dates::
[markdown]
En français, quand on écrit une date, on met une majuscule aux jours et aux mois. {F}

::Espaces et deux-points::
[markdown]
En français, lorsqu'on utilise le `:`, on doit mettre :
{
~ une espace normale avant et une espace normale après,
~ une espace insécable avant et pas d'espace après,
= une espace insécable avant et une espace normale après,
~ pas d'espace avant et une espace insécable après,
~ pas d'espace avant et une espace normale après.
#### comme pour les autres signes de ponctuation double `: ; ! ?` la règle est : **espace insécable avant, espace normale après**.
}

::Espaces et virgule::
[markdown]
En français, lorsqu'on utilise une virgule (`,`), on doit mettre :
{
~ une espace normale avant et une espace normale après,
~ une espace insécable avant et pas d'espace après,
~ une espace insécable avant et une espace normale après,
~ pas d'espace avant et une espace insécable après,
= pas d'espace avant et une espace normale après.
#### les signes de ponctuation simple `, .` sont collés au mot qui précède et sont suivis d'une espace normale.
}

::Guillemets::
[markdown]
En français, pour les guillemets, on utilise :
{
= les chevrons : «  »
~ les doubles quotes : ''  ''
~ les simples quotes : '  '
}
```

## Saisie et éléments de structure

Pour manipuler correctement votre document comme mettre les retours à
la ligne au bon endroit ou faire les sauts de page correctement, le
traitement de texte doit pouvoir reconnaître les mots, les
paragraphes, les listes. nous expliquons ici quelques règles à
respecter pour ce faire.

**Les caractères**

La plupart, par exemple, lettres, chiffres et
symboles de ponctuation, sont visibles, mais certains sont invisibles,
en particulier, les espaces. Certains caractères sont aussi
interprétés par le logiciel comme une commande ou une déclaration,
c'est, par exemple, le caractère qui marque la fin de paragraphe,
ou ceux qui marquent la fin d'un mot (espace ou ponctuation),
celui qui ajoute une espace insécable. C'est là une première
difficulté, l'espace par exemple a plusieurs fonctions. Ajouter une
espace typographique entre deux mots est utile à la présentation du
document, mais cet ajout déclare également la séparation de deux mots. Dans
la première fonction, on pourrait vouloir augmenter cette séparation
dans le rendu visuel et donc se faire suivre deux espaces. Mais on
perd le sens de la deuxième fonction puisqu'il n'y a pas de mot entre
ces deux espaces. La convention choisie est de **ne jamais avoir deux
espaces consécutives** et de faire confiance au logiciel pour réaliser
la meilleure présentation. En effet, si deux ou plusieurs espaces se
suivent, le traitement de texte est mis en difficulté et la mise en
forme peut être insatisfaisante. Donc, *visualiser tous les
caractères*, y compris ceux qui sont invisibles, aide à bien
comprendre le contenu saisi.

**Les mots**

Le logiciel les reconnaît car ils sont séparés par des
espaces ou des signes de ponctuation. Des règles typographiques,
spécifiques à chaque langue, définissent les espaces et symboles de
ponctuation. Par exemple, en français une espace précède toujours le
signe `:` alors qu'il n'y pas d'espace avant le signe `:` en
anglais. Le respect de ces règles est impératif et souvent, le
logiciel aide à une saisie correcte en ajoutant les espaces requis.

**Les paragraphes**

Ce sont des ensembles de mots séparés par des
*fins de paragraphes* créés par l'appui sur la touche `Entrée`. La fin
de ligne dans le rendu du document (le retour à la ligne) est calculée
par le traitement de texte et donc la touche `Entrée` ne marque pas la
fin de ligne. Il est parfois nécessaire de forcer une fin de ligne
dans certains paragraphes comme les poèmes. C'est la combinaison de
`Majuscule-Entrée` qui permet de réaliser une fin de ligne tout en
gardant le même paragraphe. Puisque chaque appui sur la touche
`Entrée` crée un nouveau paragraphe, les titres et les sous-titres
sont donc techniquement des paragraphes comme les paragraphes de
texte. Comme pour les espaces et les mots, la convention choisie est
de **ne jamais avoir deux fins de paragraphe consécutives** et de
faire confiance au logiciel pour réaliser le meilleur rendu visuel.

**Les titres**

Ce sont bien des paragraphes, mais le logiciel de
traitement de texte permet de les déclarer comme titres en précisant
leur niveau. Le niveau est la profondeur dans une hiérarchie : titre
de niveau 1 pour une section, titre de niveau 2 pour une
sous-section, titre de niveau 3 pour une sous-sous-section.

**Les listes**

Ce sont des suites de paragraphes reliés entre eux
pour permettre une présentation cohérente. Pour assurer cette
cohérence, beaucoup de caractéristiques sont définies sous forme de
règles utilisées par le logiciel pour l'apparence des listes : le
symbole utilisé pour les items des listes à puce, les espacements, la
numérotation des éléments, ... La logique est, ici encore, de déclarer
la liste et de laisser le logiciel s'occuper de l'apparence quitte à
adapter les règles de mise en forme à vos besoins.

Chaque élément de liste est un paragraphe. On active la structure de
 liste par bouton qui est un raccourci du menu format/puces et
 numérotation.  On ajoute un nouvel élément en ajoutant un
 paragraphe. On peut avoir plusieurs paragraphes dans le même élément
 de liste en utilisant la touche `Retour arrière` une seule fois en
 début de paragraphe. Deux appuis de `retour arrière` quittent la
 structure de liste.

[Vidéographie : Déclarer une structure de liste](https://player.vimeo.com/video/183317268){: .lien_video }

```Activité

::Refaire la saisie::
[markdown]
Reproduire avec LibreOffice l'exemple décrit dans ces 2 vidéos: [La saisie](https://player.vimeo.com/video/183312871), [La saisie - un copier-coller](https://player.vimeo.com/video/183312874).
\n
Une partie du texte est disponible en suivant ce [lien](./media/MonPremierPas-Master.txt).
\n
Enregistrer votre travail dans un fichier que vous déposerez sur votre compte *Nextcloud*. Récupérez le lien de ce fichier et collez-le dans la zone de texte de cette activité.{}

```

## Styles et structure

[Les styles](https://vimeo.com/182868052){: .cours_video}

Les logiciels de traitement de texte offrent tous la possibilité
d'afficher la liste des styles disponibles (avec LibreOffice, on peut
utiliser la touche `F11`, le menu `Style/Style et formatage `ou encore le
tiroir de droite). Nous pouvons voir cette liste de styles comme la
liste des structures possibles. Se placer dans un paragraphe du texte
permet de voir quel style lui est associé. L'ensemble des styles
possibles est très grand et organisé selon une hiérarchie. On peut
restreindre cette liste à ceux qui sont appliqués dans le document ou
à ceux qui sont souvent utilisés (styles automatiques). Les styles
portent sur différents éléments de structure du document :
paragraphes, caractères, cadres (flottants), pages ou listes.

[Vidéographie : L'utilisation des styles](https://player.vimeo.com/video/183317278){: .lien_video }

On associe facilement un style à un élément, ici des caractères en les
sélectionnant et en cliquant deux fois sur le style voulu. Ici, au
lieu de mettre en gras et en italique, nous préférons déclarer des
textes plus ou moins accentués. Il faut bien comprendre la
différence. Même si les textes déclarés en accentuation forte
apparaissent en gras, ce n'est pas identique de presser le bouton
gras. En les déclarant de cette façon nous ajoutons du sens que les
logiciels pourront exploiter dans d'autres situations : rendu oral,
présentation sur un autre support comme un objet portable, ou
simplement pouvoir modifier facilement dans tout le texte la mise en
forme choisie pour les éléments déclarés en style accentuation forte.

[Vidéographie : Les style caractères. Accentuation ou Gras ?](https://player.vimeo.com/video/183312876){: .lien_video }

Comme nous l'avons dit ci-dessus, l'affichage des caractères
invisibles permet de savoir exactement ce qui a été saisi. On voit les
espaces et les fins de paragraphe, on peut déceler des répétitions de
ces symboles et les supprimer. On voit également la représentation des
fins de ligne qui ne sont pas des fins de paragraphes dans cette
partie de texte.

[Vidéographie : Affichage des caractères spéciaux dont le retour à la ligne](https://player.vimeo.com/video/183313474){: .lien_video }

Le logiciel réalise souvent des opérations pour vous aider à bien
écrire votre document, comme par exemple, l'insertion d'une note de
bas de page. Le numéro est inséré automatiquement et sera adapté si
d'autres notes sont ajoutées. Le style choisi pour la note sera adapté
automatiquement.

[Vidéographie : Un style adapté et une numérotation automatique des notes bas de page](https://player.vimeo.com/video/183312861){: .lien_video }

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

[Vidéographie : Insérer des renvois aux textes et illustrations](https://player.vimeo.com/video/183312867){: .lien_video }

Terminons par un examen de la structure arborescente de ce
document. La manipulation de cette structure permet de déplacer des
sections entières ou de réorganiser le plan.

[Vidéographie : Réorganiser le plan](https://player.vimeo.com/video/183312870){: .lien_video }

```Activité

::Copier-coller::
[markdown]
Récupérer un texte d'une source par un copier/coller est une opération que chacun réalise régulièrement. Cette opération récupère en général de nombreuses mises en forme et styles. Par exemple, rendez-vous sur la page [https://www.univ-lille.fr/vie-des-campus/centre-de-sante-des-etudiants/](https://www.univ-lille.fr/vie-des-campus/centre-de-sante-des-etudiants/). Copiez le texte de la page et collez-le dans Libreoffice.
{
~%33%Vous avez importé le contenu
~%33%Vous avez importé la structure
~%34%Vous avez importé des mises en forme au cas par cas }

::Collage spécial::
[markdown]
En continuant l'activité précédente, vous pouvez maintenant appliquer un `collage spécial, texte non formaté` (dans le menu `Édition`).  
{ ~%100%Vous avez importé le contenu
~%-33%Vous avez importé la structure
~%-34%Vous avez importé des mises en forme au cas par cas }

```

## Point d'étape : respecter des règles de base

L'auteur d'un document est en charge du contenu et de sa qualité, du
niveau de la langue et de l'orthographe, de la structure du
document. Le traitement de texte réalisera le travail de mise en forme
à la condition d'avoir correctement défini la structure en respectant
les règles fondamentales suivantes :

- espace et ponctuation séparent les mots. On ne doit
  donc **jamais avoir plusieurs espaces consécutifs**.
- L'appui sur la touche `Entrée` sépare les paragraphes. On ne doit
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



```Activité

[markdown]
Voici le [texte brut de la charte](./media/charte.txt) des utilisateurs du système d'inforamtion de Lille3. Ouvrez ce texte dans un document LibreOffice par la méthode de votre choix, et utilisez les règles de mises en forme vues dans le cours pour reproduire [l'exemple que vous nous fournissons](./media/Charte.pdf).

Vous noterez bien :
\n
- les deux niveaux de titre (le titre principal et les titres de niveau1) ;
\n
- l'accentuation simple passe les caractères et italique et en rouge ;
\n
- l'accentuation forte transforme les caractères en petites capitales ;
\n
- la justification de tous les paragraphes de texte à l'exception des titres ;
\n
- les espaces verticaux avant les titres ne sont pas des lignes vides mais des paramètres du style titre1 ;
\n
- le haut de page reprend le titre déclaré dans les métadonnées ;
\n
- les lignes horizontales ont été réalisées avec des bordures.
\n
N'hésitez pas à échanger sur le forum du cours si vous rencontrez des difficultés, ...
\n
À la fin, pour vérifier que vous avez correctement utilisé les styles et non la mise en forme directe, sélectionner l'ensemble de votre texte (ctrl-A), aller dans le menu `format` et sélectionner `effacer le formatage direct`. Votre mise en forme ne doit pas bouger.
\n

  Enregistrer votre travail dans un fichier que vous déposerez sur votre compte Nextcloud. Récupérez le lien de ce fichier et collez-le dans la zone de texte de cette activité.{}
```


## Personnaliser les styles

[La mise en forme](https://vimeo.com/182868165){: .cours_video}

Commençons par la mise en forme des paragraphes, en modifiant la
définition du style `corps de texte`, nous définissons une règle
générale qui va s'appliquer à tout le document, ou plutôt à tous les
paragraphes de style `corps de texte` de ce document. On choisit
souvent de *justifier*, c'est-à-dire de régler les espaces entre mots
pour avoir des marges correctement alignées des deux côtés. Dans ce
cas, une *césure* des mots est souvent appliquée pour éviter les
espacements trop grands ou trop petits.

[Vidéographie : Adapter les styles de paragraphes](https://player.vimeo.com/video/183313475){: .lien_video }

On peut également choisir des règles de mise en forme pour les
caractères comme pour les accentuations ou les accentuations
fortes. Si vous n'êtes pas satisfait de la règle choisie, vous la
modifierez pour changer l'apparence dans tout le document en une
seule opération.

[Vidéographie : Adapter les styles de caractères](https://player.vimeo.com/video/183317275){: .lien_video }

Parfois, certains éléments de structure sont propres à un certain type
de document. Par exemple ici, nous avons des noms de
logiciels. Déclarer ce nouvel élément de structure ajoute de la
sémantique, du sens au document qui pourra être exploité par d'autres
logiciels, mais facilitera également l'uniformisation de la
présentation de tous les noms de logiciel.

[Vidéographie : Nouveau style de caractère - logiciel](https://player.vimeo.com/video/183312863){: .lien_video }

Bien sûr, la définition de nouvelles structures, donc de nouveaux
styles, s'applique sur les caractères comme sur les paragraphes. Ici, notre
document contient un morceau de code qui ne doit pas être justifié. Il
peut être déclaré et mis en forme spécifiquement. Mais si votre
document contenait d'autres codes, vous associeriez une structure et
définiriez une mise en forme commune pour tous ces codes.

[Vidéographie : Nouveau style de paragraphe - code](https://player.vimeo.com/video/183317279){: .lien_video }

## Numérotation et tables associées

[Numérotation et tables](https://vimeo.com/182868191){: .cours_video}

La numérotation des chapitres ne doit jamais être faite manuellement
car elle est réalisée automatiquement par le traitement de textes à
partir de la structure.  Il suffit d'indiquer quels sont les noms des
styles (structures) identifiant les titres, en général, ce sont les
titre 1, titre 2, etc... Ensuite on choisit le style de numérotation
et si on doit faire apparaître la hiérarchie dans le numéro en
affichant les sous-niveaux. Amusez-vous à modifier tous les paramètres
pour comprendre les impacts sur la présentation de ces numéros.

[Vidéographie : Numérotation automatique des chapitres](https://player.vimeo.com/video/183312864){: .lien_video }

La structure d'un document, c'est aussi une structure en différentes
pages : une page de garde, des pages d'index ou de table des matières
ou d'illustrations, ... Différents styles de pages identifient cette
structure. On peut la déclarer en ajoutant des sauts de page manuels
et spéciaux, puis définir quel sera le style de la page suivante et le
début de sa numérotation et définir des mises en forme associées à ces pages.

[Vidéographie : Structuration en liste de pages de natures différentes](https://player.vimeo.com/video/183312879){: .lien_video }

Une fois la structure du document bien spécifiée, l'insertion d'une
table des matières, d'une table des illustrations,... est très simple,
et hautement paramétrable. Si la numérotation des chapitres a été
appliquée alors les numéros seront repris. Des efforts de mise en
forme peuvent être nécessaires selon les logiciels comme par exemple
ici. Par exemple, nous ajoutons une espace après chaque numéro.

[Vidéographie : Génération d'une table des matières](https://player.vimeo.com/video/183312877){: .lien_video }

```activité

::Exercice de styles::
[markdown]
Reproduire avec votre traitement de texte le document dont un pdf vous est donné [ici](./media/texte_final.pdf) à partir du texte brut fourni [là](./media/texte_final.txt). **Aucune mise en forme directe n'est tolérée !** (*i.e* les boutons de la barre d'outils ).
\n
Dans ce document, nous avons utilisé :
\n
- des styles spécifiques pour désigner les personnes et les œuvres,
\n
- le résumé et les citations,
\n
- 3 styles de page avec des numérotations en romain pour les pages d'index et de tables,
\n
- les guillemets et les listes françaises.
\n
La police de caractère est sans doute différente sur votre machine. Ici ce sont les polices Latin Modern Roman et Latin Modern Sans pour les versions avec et sans serif. **Vous pouvez prendre celles de votre choix**. Bien-sûr tous les principes expliqués dans ce cours ont été appliqués.
\n
Enregistrer votre travail dans un fichier que vous déposerez sur votre compte *Nextcloud*. Récupérez le lien de ce fichier et collez-le dans la zone de texte de cette activité. {}

```

## Métadonnées
[Métadonnées](https://vimeo.com/182868218){: .cours_video}

Les métadonnées sont des données à propos du document. Elles sont
calculées par le logiciel (par exemple le nombre de mots, la taille
etc...) ou déclarées par l'utilisateur (le titre, le sujet,
l'auteur...). Les métadonnées sont utiles pour le traitement de
corpus de documents. On les retrouve ici dans le menu des
propriétés. Il est aussi possible d'insérer les métadonnées comme
contenu textuel du document.

[Vidéographie : Utilisation des métadonnées](https://player.vimeo.com/video/183317406){: .lien_video }

## Avec un autre logiciel
[Avec d'autres logiciels](https://vimeo.com/182868251){: .cours_video}

Nous avons illustré les principes avec LibreOffice Writer et indiqué
que ceci est général à tout traitement de texte ce que nous illustrons
avec Microsoft Word. Nous retrouvons la possibilité d'afficher ou non
les caractères non imprimables, l'aide à la saisie, un styleur pour
structurer le document et le mettre en forme. On dispose, par exemple
du style `normal` pour le corps de texte qu'il est possible de
modifier.  La génération d'un index ou d'une table des matières suit
la même logique ainsi que l'insertion de marques, de repères ou de
renvois de notes.  Bien sûr, chaque logiciel a son interface propre et
le nom des menus ou des outils peut varier d'une version à une autre,
mais il est important de retenir que les **notions vues dans ce cours
sont communes à tous les traitements de texte**.

## Aller plus loin
[Pour aller plus loin](https://vimeo.com/182868392){: .cours_video}

### Travail collaboratif

Travailler en groupe c'est d'abord communiquer sur l'édition du
document. Dans ce cas, on veut commenter des parties. C'est aussi être
capable de suivre des modifications. Lisez le texte du document pour
mieux comprendre et regardez les différentes possibilités qui vous
sont offertes. En situation de travail collaboratif, les modifications
auront pu être apportées par différents auteurs et le coordinateur va
donc valider ou rejeter les modifications.

[Vidéographie : Commentaires et suivi des modifications](https://player.vimeo.com/video/183312857){: .lien_video }

Une autre fonctionnalité de suivi des versions est illustrée ici.

[Vidéographie : Suivi des versions](https://player.vimeo.com/video/183317276){: .lien_video }

### Comprendre la hiérarchie de styles

Les styles sont organisés dans une hiérarchie. Ce n'est pas qu'une
façon de les catégoriser pour les retrouver ou y accéder plus
rapidement. En effet, la raison principale tient à un concept qu'on
retrouve souvent en informatique : la notion d'*héritage*. Illustrons
cette notion par l'exemple. Si la couleur des caractères n'est pas
définie au niveau d'un style elle sera alors définie par celle de son
style juste au dessus de la hiérarchie. Par exemple en passant le
corps de texte en rose, les notes de bas de page le seront aussi, mais
pas les titres. Par contre définir cette couleur au style par défaut,
c'est-à-dire au sommet de la hiérarchie affectera tous les styles de
document (sauf bien sûr si cette propriété a été redéfinie pour un style
donné).

[Vidéographie : La hiérarchie de styles](https://player.vimeo.com/video/183313476){: .lien_video }

### Mise en forme des listes

Les listes en typographie française utilisent des tirets
demi-cadratins (Code unicode 2013,
[Tiret-moyen](https://fr.wikipedia.org/wiki/Tiret#Tiret_moyen)). On
peut définir une liste à la française respectant cette convention
typographique mais c'est un peu technique.

[Vidéographie : Listes à la française](https://player.vimeo.com/video/183312880){: .lien_video }

### Autres fonctionnalités

Ce n'est pas l'objectif du cours de parcourir toutes les possibilités
apportées par un traitement de textes mais vous disposez maintenant
des principes de base pour une bonne utilisation. Il est, par exemple,
possible de définir des tableaux organisés en lignes et en colonnes,
d'insérer des images dans des figures avec des légendes et des
numérotations. Il est également possible d'intégrer une
bibliographie. Cette opération est plus complexe mais vous trouverez
des tutoriaux sur le Web pour en réaliser. Enfin, dans un cadre
professionnel, vous serez amener à utiliser des modèles pour
respecter une charte graphique de votre employeur. Vous pourrez être
amenés à réaliser des mailings en insérant des références à des
fichiers de clients.
Voici quelques activités que nous vous proposons pour découvrir d'autres fonctionnalités plus avancées. Cherchez par vous-même et échangez sur le forum pour vous entraider.

[Vidéographie : Utiliser un modèle](https://player.vimeo.com/video/183313473){: .lien_video }

```Activité

::Ajouter des images::
[markdown]
À vous maintenant, ... Nous considérons que vous en savez suffisemment pour pouvoir aller découvrir par vous même d'autres fonctionnalités. Cette section a pour but de vous faire chercher d'autres fonctionnalités du traitement de texte. Encore une fois, n'hésitez pas à utiliser le forum pour échanger entre vous, ...
\n
Ajouter des images ([image1 "image styles"](./media/styles.png), [image2 "image style général"](./media/styleGeneral.png)) dans un cadre avec une légende pour construire les illustrations du cours.
\n
Enregistrer votre travail dans un fichier que vous déposerez sur votre compte *Nextcloud*. Récupérez le lien de ce fichier et collez-le dans la zone de texte de cette activité.{}

::Utiliser un modèle::
[markdown]
Reprendre le document de la charte graphique et appliquer le modèle donné [ici](./media/ModeleCN.ott).
\n
Enregistrer votre travail dans un fichier que vous déposerez sur votre compte *Nextcloud*. Récupérez le lien de ce fichier et collez-le dans la zone de texte de cette activité.{}

```

```Activité avancée

::Document maître::
[markdown]
Créer un document maître avec ce [modèle](./media/ModeleCN.ott). Inclure les différents chapitres de la charte comme autant de documents inclus dans le document maître. Le texte contenu dans le document MonPremierPas sur lequel vous avez déjà travaillé explique les principes, vous pouvez aussi lire [l'aide de LibreOffice](https://help.libreoffice.org/Writer/Working_with_Master_Documents_and_Subdocuments/fr) pour apprendre à maitriser de nouvelles notions en autodidacte.  Aidez-vous des forums et des ressources sur internet pour réaliser cet exercice.
\n
Enregistrer votre travail dans un fichier que vous déposerez sur votre compte *Nextcloud*. Récupérez le lien de ce fichier et collez-le dans la zone de texte de cette activité.{}

::Commentaires::
[markdown]
Faites circuler un document de votre choix entre 3 d'entre vous. Chacun ajoutera un commentaire, fera des modifications avec le suivi des modifications activé, et créera une version.
\n
Décrivez plusieurs situations ou les commentaires et le suivi des modifications peuvent être des outils très pratiques. {}

```

# Le tableur

## Objectifs

L'étude des données et de leur gestion fait apparaître différents
modes possibles d'organisation des données. Parmi celles-ci, la liste
est largement répandue car elle peut couvrir un grand nombre de
besoins dans des situations variées. Elle vous sera utile pour gérer
des élèves et des notes si vous êtes professeur, gérer des adhérents
d'une association, gérer des
listes d'objets dans des fouilles si vous êtes archéologue, ...  Le
tableur est un logiciel de base pour la gestion de données numériques
représentées par des listes.

Cette partie de cours est dédiée à l'étude du tableur.  Le **premier
objectif** est la découverte des fonctionnalités générales, communes à
tous les tableurs, pour faire des calculs et manipuler des listes. Le
**second objectif** est d'appréhender les questions liées au choix
d'organisation des données dans un tableur en réponse à des objectifs
bien établis.


## Découverte du tableur

[Le tableur](https://vimeo.com/183456909){: .cours_video}

### Fonctionnalités

Le tableur est un **outil pour représenter, traiter et interroger des
données**. Ce n'est pas un outil de présentation des tableaux car le
traitement de texte gère les tableaux et leur mise en forme. La
manipulation d'un tableur est donc une activité de traitement de
données, et donc un pas supplémentaire vers l'informatique en tant que
science du calcul.

Avec le tableur, on peut gérer  des données organisées
sous forme de **listes** : une liste d'élèves avec leurs notes, une
liste d'adhérents avec leurs adresses et leurs cotisations, une liste
d'objets avec une date de collecte et des informations de forme,
taille, poids,... Les listes, aussi appelées **relations** ou
**tables**, sont organisées en lignes et colonnes. Chaque ligne décrit
un élément (un élève, un membre, un objet). Chaque colonne décrit une
propriété de l'élément (un nom, un prénom, une note, une date de
naissance, une taille, un poids).

Les principales fonctionnalités d'un tableur sont :

- mémoriser des données et des listes,
- faire tous les calculs des plus simples aux plus compliqués,
- sélectionner des éléments dans des listes en fonction de critères,
  comme, par exemple, sélectionner les élèves garçons doublants,
- trier des listes d'éléments, comme, par exemple, trier les élèves par âge,
- analyser des listes et construire des diagrammes comme, par exemple,
  faire des moyennes de notes par âge d'élève et faire le graphique
  correspondant,
- produire des rapports mis en forme.

### Organisation générale

Un vocabulaire spécifique accompagne la manipulation du tableur. Avec
le tableur, on définit

- un *classeur* qui sera enregistré dans un fichier au format de
`Microsoft Excel` d'extension `xlsx` ou au format ouvert utilisé par `LibreOffice Calc` d'extension `ods`
- un classeur contient des *feuilles de calcul*, chaque feuille de
  calcul a un nom. Par défaut, en version française, `Feuille 1`,
  `Feuille 2`, ...
- chaque feuille de calcul est organisée en *lignes* numérotées 1, 2,
... et en *colonnes* numérotées A, B, ... L'intersection d'une ligne
et d'une colonne est une *cellule* qui va pouvoir contenir une donnée
élémentaire.

[Vidéographie : Petit tour d'horizon](https://player.vimeo.com/video/183320082){: .lien_video }

### Dans une cellule

La première chose à laquelle il **faut être très attentif** est la
distinction entre le contenu et ce qui apparaît dans la cellule. Ce
qui apparaît est une **valeur** mise en forme. La mise en forme
influence énormément l'apparence, notamment pour les valeurs
numériques. Par exemple une même valeur numérique peut être
interprétée comme un simple nombre, un pourcentage, une somme d'argent
ou même une date.

[Vidéographie : Valeur et apparence1](https://player.vimeo.com/video/183320080){: .lien_video }

La valeur affichée dans la cellule peut également être le résultat
d'un calcul exprimé par une *formule*. Une formule commence par le
signe `=` suivi d'une expression. On peut examiner la formule dans la
*ligne de saisie*. Le tableur recalcule automatiquement les valeurs
issues d'un calcul et permet facilement d'ajuster les calculs pour des
listes de valeurs.

En résumé, dans une cellule s'affiche une valeur, mais la cellule
contient bien plus d'informations : une valeur, un format, et
éventuellement une formule et même un commentaire.

[Vidéographie : Valeur et apparence2](https://player.vimeo.com/video/183320079){: .lien_video }

### Mise en forme

Comme pour le traitement de texte, on peut faire des mises en forme au
cas par cas ou utiliser des styles pour uniformiser la
présentation. **Attention** à ne pas mettre en péril les traitements
par des soucis de présentation. Par exemple, une liste est définie par
des lignes et colonnes contiguës et insérer des lignes (ou colonnes)
blanches ou avec un fond coloré pour faire des bordures rompt la
logique de liste. Les traitements de filtre, tri, etc... deviendraient
alors impossibles.

[Vidéographie : Styles](https://player.vimeo.com/video/183320077){: .lien_video }

[Vidéographie : Logique de table](https://player.vimeo.com/video/183320076){: .lien_video }

```Activité avancée

::Découverte d'un classeur simple::
[markdown]
Découvrez en autonomie les premières notions d'un classeur illustrant le calcul de résultats électoraux : [Classeur élections](./media/election.ods).
{}

::Découverte d'un classeur plus complet::
[markdown]
Un second exemple plus complet simule la gestion des cotisations des adhérents d'une association : [Classeur association](./media/association.ods).  {}

```

## Traiter des données

Faire un traitement de données, c'est

1. Disposer de données en entrée (des valeurs connues, acquises),
2. définir des opérations de calcul sur ces données,
3. produire et afficher les résultats.

La traduction dans le tableur posera les questions suivantes : Quelles
sont les cellules et les plages de cellules qui vont contenir des
valeurs en entrée ?  Quelles sont les cellules qui vont contenir des
résultats de calcul ?  Comment les organiser dans la feuille de calcul
? Comment écrire les calculs ?

### Organiser ses données dans le tableur

Nous considérons un exemple fictif simple. En vue d'un voyage de
classe à Londres, on souhaite mémoriser et analyser la monnaie
qu'emportent les enfants. On connaît le taux de conversion de la
livre, et un seuil maximal en euros qu'un enfant peut emporter a été
fixé par les organisateurs. Nous disposons pour chaque enfant de ses
nom et prénom, de sa classe et du montant en euros. Nous souhaitons
pouvoir disposer du montant en livres, pouvoir repérer les montants
supérieurs au seuil, calculer des montants moyen, minimal et maximal
de notre groupe d'élèves.

Certaines données vont être *saisies* : le taux, le seuil, les nom,
prénom, classe et montant en euros pour chacun des enfants. Les autres
données seront *calculées* : le montant en livres, le dépassement du
seuil, les montants moyen, minimal et maximal de notre groupe
d'élèves. Notre feuille de calcul contiendra : une cellule contenant
le taux de conversion, une cellule contenant le seuil ; une plage de
cellules rectangulaire avec en ligne les enfants et en colonne les
propriétés nom, prénom, classe, montant en euros, montant en livres et
dépassement ; des cellules avec les montants moyen, minimal et
maximal. Notez aussi qu'on ajoute des contenus textuels dans certaines
cellules pour expliquer le contenu de la cellule voisine ou pour
nommer les propriétés de notre liste d'enfants. Il nous reste à
expliquer comment, après avoir saisi les valeurs, on peut calculer les
valeurs utiles à notre application.

### Expliciter les calculs

Un calcul va utiliser des valeurs connues qui sont contenues dans des
cellules. Il faut dont pouvoir désigner une cellule et son
contenu. Dans le tableur on parle de **référence à une cellule**
désignée par numéro de ligne et de colonne dans la feuille comme, par
exemple `B7` pour la cellule en colonne B et ligne 7.

L'intérêt du tableur, par rapport à une calculatrice, est de pouvoir
généraliser des formules à une liste d'objets. Sur notre exemple, on
va écrire une formule pour un enfant et on va généraliser cette
formule à *tous les enfants* et ceci qu'on ait 10 élèves, 100 élèves
ou 1000 élèves. Sur notre exemple, on écrira une formule en `E8` pour
calculer le montant en euros à partir du montant figurant en `D8`. Puis
on généralisera, on étendra, la formule à toute la plage de `E8` jusque
`E108` si on a 100 enfants avec une *copie*. Le tableur va
automatiquement adapter les références et la formule en `E9` fera
référence à `D9` pour l'enfant en ligne 9, ... Ceci est réalisé avec la
notion de *référence relative* comme `D8`, `B7`, `E12`, `G2` qui permet de
traiter des listes, même de grande taille.

Mais parfois, la référence ne doit pas être modifiée lors de la
copie. C'est le cas de la référence au taux de conversion qui est dans
une seule cellule, `G2` sur notre exemple. Pour faire la distinction de
comportement, on utilisera dans notre formule une *référence absolue*
en utilisant le symbole $. Donc, par exemple, pour faire référence au
taux de conversion, on utilisera la référence absolue `$G$2`.

Le **mécanisme des références est donc essentiel pour traiter des
listes**. Vous devez, lorsque vous écrivez une formule, vous poser la
question suivante : est-ce que ma référence doit être adaptée lorsque
je copie ma formule. Si oui, vous utilisez une référence relative, si
non, vous utilisez une référence absolue. Sur notre exemple, la
formule à écrire en `E8` est donc `=D8*$G$2` qu'il suffit de copier
pour toute la liste d'enfants et en `E12`, nous aurons la formule
attendue `=D12*$G$2` qui est bien le montant en euros pour l'enfant en
ligne 12 multiplié par le taux de conversion situé en `G2`.

### Autres références

- On peut avoir besoin d'utiliser, dans certains cas, des *références
  mixtes* comme `B$2` ou `$A5` où une composante est relative et l'autre
  est absolue
- Les références peuvent désigner une *plage rectangulaire* de cellules
  en donnant les références des coins supérieur gauche
  et inférieur droit séparés par `:` comme `B3:D7` ou `$B$3:D7` ou `$B3:D$7`
- On peut faire référence à des cellules d'une *autre feuille* avec la
  syntaxe suivante : 'Nom de Feuille'.reference comme 'Feuille 1'.B7
- Les références peuvent désigner une *liste* de cellules en donnant
  les références séparées par des `;` comme `B3;D$7;$A1;E3`
- Mais on peut aussi attribuer des noms à des cellules ou plages de
  cellules. On peut alors y faire référence par le nom qui se comporte
  alors comme une référence absolue. On aurait, sur notre exemple, pu
  nommer la cellule `G2` avec le nom `tauxchange`, écrire en `E8` la
  formule `=D8*tauxchange`, puis copier cette formule dans la plage
  `E8:E108`.

[Vidéographie : Autres références](https://player.vimeo.com/video/183320068){: .lien_video }

[Vidéographie : Nommer des cellules](https://player.vimeo.com/video/183320074){: .lien_video }

```Activité avancée

::Jouer avec les références::
[markdown]
Le classeur [Jeu avec les références](./media/jeureferences.ods) contient deux feuilles de calcul. Suivez les instructions qui s'y trouvent. Quelle est la bonne formule à utiliser dans l'onglet Références2 ?  {
~ Celle en ligne 5
~ Celle en ligne 9
= Celle en ligne 13}

```


## Construire des formules

Pour construire des formules on suit un langage formel, informatique,
bien particulier. Le respect de la syntaxe est essentiel, sinon des
erreurs apparaissent. Chaque formule doit commencer par le signe
`=`. Derrière le signe `=` se trouve une expression utilisant des
valeurs, des références, des opérateurs comme `+,-,*,/`, et des
*fonctions* comme `ARRONDI`, `MOIS`, ... Le tableur contient un
*générateur de formules* qui peut vous assister dans la création de
formules. Voici des exemples de formule :

	= 10 / 2 + 3
	= D8 * $G$2
    = MOIS(AUJOURDHUI())

[Vidéographie : Les expressions](https://player.vimeo.com/video/183320072){: .lien_video }

Certaines fonctions, comme les fonctions `SOMME`, `MOYENNE`, `MAX` et
`NB`, portent sur des ensembles de valeurs pour vous permettre de
calculer (respectivement) la somme des valeurs, la moyenne des
valeurs, la valeur maximale, le nombre de valeurs d'une plage de
cellules.

Enfin, une fonction très importante permet de différencier les
traitements selon les cas. C'est *la fonction SI* qui s'écrit sous la
forme `SI(critere;valeurVrai;valeurFaux)`. Par exemple, si vous avez
une liste d'élèves avec une moyenne des notes en colonne `G` à partir
de `G8`, si vous souhaitez traiter différemment les élèves ayant une
note supérieure à 10, vous pourrez écrire en `H8` une formule de la
forme `=SI(G8>=10;"Reçu";"Recalé")`

puis étendre cette formule à tous les élèves. Si un élève a une
moyenne inférieure à 10, le message "Reçu" sera affiché pour cet élève
et sinon sera affiché le message "Recalé".

[Vidéographie : Le si](https://player.vimeo.com/video/183320069){: .lien_video }

Les *fonctions peuvent être composées* comme dans l'exemple `=
MOIS(AUJOURDHUI())` où on appelle la fonction `AUJOURDHUI()` qui
calcule la date du jour et au résultat on applique la fonction
`MOIS()` qui calcule le mois d'une date et donc on affichera le mois
du jour courant. La composition de fonctions est très utile, par
exemple, très intéressant pour composer des `SI` lorsqu'il y a plus de
deux cas possibles comme dans l'exemple suivant :
`=SI(G8<10;"Recalé";SI(G8<12;"Passable";"Mention"))`

Ceci est illustré sur l'exemple. **Notez bien** aussi sur la video
l'intérêt d'avoir des cellules contenant les seuils car il suffit de
modifier les contenus de ces cellules sans changer les formules pour que les résultats s'adaptent automatiquement à un changement des seuils.

[Vidéographie : Le si imbriqué](https://player.vimeo.com/video/183320078){: .lien_video }

```Activité avancée

::Premières formules::
[markdown]
Dans ce dans le classeur [Premières formules](./media/premieresformules.ods) qui contient deux feuilles de calculs, vous vous entraînerez à écrire des formules avec des additions, des multiplications et la fonction `SOMME()`.  {}

::Fonction SI::
Entraînez-vous maintenant avec la [fonction SI](./media/fonctionSI.ods).  {}
```

## Opérations sur les tables

Nous avons vu comment calculer des valeurs qui permettent de
construire de nouvelles colonnes comme résultats de calcul. On dispose
donc d'une liste ou table qui est définie par une zone rectangulaire
avec des objets en ligne et des propriétés en colonne. Il existe
différentes opérations sur les tables et nous nous limitons ici à deux
opérations : le tri et la sélection. Une autre opération, non
présentée ici, consiste à effectuer des synthèses avec des
tableaux.

### Le tri

Le tri *ordonne les lignes* d'une table selon des *critères de
tri*. Pour réaliser cette opération, on doit :

- *désigner la table* : soit en se plaçant dans une cellule quelconque
de la table (le tableur en déduit sur quelle table vous souhaitez
travailler) ou en la nommant
- *expliciter les critères de tri* en donnant les noms des colonnes sur
lesquelles vous voulez trier et en précisant si vous souhaitez un
ordre croissant ou décroissant.

[Vidéographie : Le tri](https://player.vimeo.com/video/183320075){: .lien_video }

### La sélection ou filtre.

Cette opération consiste à sélectionner des lignes de la table qui
vérifient des conditions sur les valeurs des colonnes. Par exemple, on
pourrait, sur notre exemple, souhaiter sélectionner les enfants de
classe 1A, les enfants de classe 1A ayant plus de 10 euros, ... Pour
réaliser une sélection, on doit :

- *désigner la table* comme pour le tri
- *expliciter les critères de filtre*.

[Vidéographie : Le filtre](https://player.vimeo.com/video/183320070){: .lien_video }

```Activité avancée

::Tri et filtres::
En utilisant le [classeur à propos des associations](./media/association.ods),  vous pourrez trier par ordre alphabétique des noms. Puis trier par ordre croissant des âges et noter que l'ordre alphabétique est perdu ! Puis trier par tranche d'âge en triant chaque tranche d'âge par âge croissant. Des exemples de filtres à réaliser sont :
\n
1. Sélectionner les juniors ;
2. Sélectionner les juniors femmes ;
3. Sélectionner les membres qui ne sont pas à jour de leur cotisation, ... {}

```

## Représentations graphiques

Un graphique ou diagramme est utilisé pour porter un message. Le type
de diagramme est important car il précise ce message :

- Pour une répartition : les camemberts et barres de pourcentage
- Pour  des valeurs qui peuvent s'ajouter : les empilements
- Pour les séries de valeurs continues : les courbes
- Pour les séries de valeurs non continues : les histogrammes
- Pour les données dans de nombreuses dimensions : les radars.

Rappelez-vous donc qu'on ne représente pas pour faire beau mais pour informer.
