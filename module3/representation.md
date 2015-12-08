LANGUAGE:   FR
TITLE:   Représentation numérique de l'information : les documents
AUTHOR:     Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

# Représenter c'est choisir...

Pourquoi représenter l'information sous format numérique ? En premier
lieu, c'est un changement de support. Par exemple pour un roman, il
faut passer d'un support papier à un support numérique compréhensible
par une machine pour qu'elle puisse le stocker et l'afficher. Il faut
donc représenter le roman comme une suite de 0 et de 1 et inversement
passer de cette suite de 0 et 1 en un texte lisible.

Il faut aussi pouvoir échanger. Plutôt que de se prêter un roman sur
support papier, c'est sa représentation numérique qui sera copiée à
travers le réseau. Il est donc nécessaire que l'émetteur et le
récepteur (en l'occurrence les logiciels utilisés par chacun d'eux)
soient d'accord sur la façon de représenter l'ouvrage.

Retrouver le titre et l'auteur du roman est une tâche qui vous semble
évidente. Elle sera rendue plus facile et sûre pour une machine si la
représentation choisie contient explicitement la désignation du titre
et de l'auteur.
  
De même, considérons la classification du roman dans les catégories
policier, historique ou libertin.  Cette tâche est difficile pour une
machine sauf à spécifier dans la représentation la catégorie définie
par un expert humain. Terminons par l'exemple d'une vidéo. En tant
qu'humain, vous reconnaîtrez sans problème des personnages connus dans
les images. Ici encore, c'est une tâche très difficile pour une
machine sans une représentation adéquate et des informations
complémentaires. Par conséquent, la représentation numérique d'une
information peut être enrichie pour faciliter les traitements relatifs
à de telles tâches.

La numérisation ne se limite pas à un changement de support. En effet,
elle permet des traitements automatiques sur des grandes quantités de
documents. 

Par exemple comment faire en sorte que votre smartphone reconnaisse un
morceau de musique chantonné ? À l'aide d'un logiciel transformant
les sons en un codage astucieux, votre voix est numérisée, puis la
représentation numérique qui a été produite est envoyée à un service
possédant un très grand nombre de morceaux de musique représentés avec
le même codage, après comparaison le morceau le plus proche pourra
être envoyé vers votre smartphone.

Nous allons dans ce module, présenter les bases de la représentation
numérique de l'information. Ce domaine est vaste. Nous avons fait le
choix de nous restreindre à un message principal : la représentation
numérique d'une information est un processus conçu par l'homme,
reposant sur des choix conceptuels, organisationnels et scientifiques
et assurant la possibilité de traitements numériques.  Divers critères
vont gouverner le choix d'une telle représentation :

- la pertinence : modélise-t-elle bien l'information et permet-elle de
  réaliser les traitements souhaités ?
- l'économie : est-elle économe en taille pour permettre un stockage
  et des échanges rapides ?
- l'efficacité : les traitements envisagés pourront-ils se faire rapidement ?
- la sûreté ou la confidentialité : permet-elle de cacher
  l'information ou d'en contrôler les accès ?

Cette liste est non exhaustive.  Les concepteurs, informaticiens en
relation avec des experts métier, vont effectuer les choix de
représentation. C'est un processus créatif complexe car l'espace des
solutions possibles est immense, ce qui explique la très grande
diversité des représentations numériques.

Un choix de représentation aura un impact important sur les
traitements possibles. Ces traitements sont accessibles à
travers des logiciels et prendre conscience des choix de
représentation contribue à une compréhension plus profonde et une
utilisation bien plus efficace et réfléchie de ces logiciels.


Nous allons considérer, dans un premier temps, la représentation
numérique des documents textuels. Le cours devrait vous permettre de
transposer les notions présentées dans d'autres domaines. En
particulier, à la fin du cours, les questions liées à la parole,
l'image et la vidéo seront esquissées pour vous guider dans le monde
numérique multimédia.

```activité
::Il n'existe qu'une façon de représenter numériquement une image:: 
{F# représenter une information est le résultat de nombreux choix}

::Les traitements possibles sur des données numériques dépendent fortement des choix de représentation::{T}

::La représentation numérique d'un livre peut inclure des données qui ne se limitent pas au texte. Donnez quelques exemples::
{#### Le genre, la date de création, ...}

::Donnez quelques exemples de critères qui peuvent gouverner le choix d'une représentation numérique d'une information.::
{#### la concision, la pertinence (permettre des traitements voulus), l'efficacité (les traitements sont réalisés rapidement, la confidentialité (l'accès aux données  peut être contrôlé),...} 
```

```activité-avancée
::Représenter et normaliser est une tache complexe : l'exemple de HTML.::
[markdown]En vous rendant sur la page wikipedia de HTML répondez aux questions suivantes : 
- Qui développe le format `html`
- Depuis quand ce travail sur ce langage `html` existe-t-il ?
- Quels sont les objectifs de cette numérisation ?
- Approximativement combien de groupes et de participants participent à l'élaboration de cette norme ?
- Quelle est la version la plus récente de `html` ? 
{#### Le W3C développe le HTML, Le travail a commencé au début des années 1990, HTML est conçu pour l'interopérabilité et donner du sens aux parties de textes ; la version  récente est HTML5.}
``` 


# Analyse d'un document : plusieurs vues complémentaires
## Introduction
Dans cette section, nous analysons ce qu'est un document textuel pour
déterminer les critères amenant à une bonne représentation numérique.
Le cours sur le Web a déjà introduit un exemple de représentation
numérique de document dont une caractéristique essentielle est de
représenter contenu et structure d'un côté dans le langage `html` et
présentation d'un autre côté avec une feuille de style `CSS`. Cette
représentation facilite les traitements et la transmission à travers
les réseaux et permet l'affichage sur tout type d'écran. Cette
distinction entre structure, contenu et présentation est plus générale
et résulte de l'analyse de ce qu'est un document textuel.

L'analyse des documents textuels met en évidence *quatre vues
complémentaires* : les vues séquentielle, structurée, qualifiée et de
présentation.

```activité
::Installer des logiciels:: 
[markdown]Selon le système d'exploitation de votre ordinateur, vous utiliserez et installerez si nécessaire les logiciels suivants
- Un éditeur de textes : Nous vous recommandons :
  - Sous linux : `gedit`  (installé par défaut) ou `atom` (https://atom.io)
  - Sous Windows : `notepad` (installé par défaut) ou `atom` (https://atom.io)
  - Sous Mac : `textEdit` (installé par défaut) ou  `atom` (https://atom.io)
- Un traitement de textes. Les exemples seront donnés dans ce cours avec `libreoffice` 
{}
```


## Le contenu, une vue séquentielle

Le premier constat évident est qu'un document textuel est une suite de
symboles. C'est la *vue séquentielle* du document.  L'ordre est
important et le parcours naturel est de commencer par le début, passer
d'un symbole au symbole suivant jusqu'à la fin.

Grâce à cette organisation séquentielle, il est déjà possible
d'imaginer des traitements : rechercher, remplacer, couper, copier,
coller, identifier des mots et pourquoi pas en vérifier l'orthographe,
...

```activité
::Éditeur de textes:: 
[markdown]Lancer un éditeur de textes et en faire une capture
  d'écran à déposer en réponse à ce quizz.
{}

::Fonctionnalités d'un éditeur de textes:: 
[markdown]
Parmi les fonctionnalités suivantes, lesquelles sont possibles ?
{
~%25%copier/couper/coller #tous les éditeurs le permettent
~%25%rechercher et remplacer #très souvent disponible 
~%25%avancer de mots en mots #souvent par la conjonction CRTL-flèches 
~%25%corriger l'orthographe #certains le font 
~%-100% mettre en gras #l'éditeur ne permet pas d'enregistrer des mises en forme (il est possible toutefois d'écrire des commandes de mise en forme : un mot n'est pas en gras mais un texte dans un langage peut exprimer l'ordre de mettre en gras)
}
```

## La structure, une vue arborescente

Les mots, phrases et paragraphes définissent une première
structuration du document. Cependant, tout document textuel contient
des niveaux plus abstraits de structuration : un livre contient une
page de titre, une page de garde, une préface, des chapitres ; un
rapport contient un titre, un résumé, une introduction, des sections
et sous-sections, des listes, etc... C'est la vue *structurée*. Elle
est souvent hiérarchique ou arborescente car il y a des relations
d'inclusion : un paragraphe dans une sous-section dans une section
dans le document.

Grâce à cette organisation structurelle, de nouveaux traitements sont
disponibles : extraire le résumé, numéroter les sections, construire
une table des matières, réordonner des sections avec mise à jour de la
table des matières, ...

```activité
::La structure d'un document:: 
[markdown] Téléchargez le document suivant sur votre machine et ouvrez-le avec `libreoffice` : http://culturenumerique.univ-lille3.fr/activitesWeb/textes/representation.odt
- Ouvrez le *navigateur* (touche F5), déplier tous les niveaux de titre pour faire apparaître la structure complète des titres du document.
- Rendre une capture de cette fenêtre de navigateur
{}

::La structure d'une page web::
-  à l'aide de firefox, rendez-vous sur la page http://culture-numerique.univ-lille3.fr/activitesWeb/html. 
- Pressez les touches `CTRL-MAJ-C`. La fenêtre de l'inspecteur de code `html` s'ouvre.
- Observez la structure du document `html`. Utilisez les petites
  flèches pour découvrir ou cacher les parties de code `html` incluses les unes dans les autres.
- Sur quelles petites flèches devez-vous cliquer pour arriver au texte *Vous pouvez changer la taille...* ? 
- La liste des balises associées à chacune de ces petites flèches apparaît dans la zone située juste au dessus du code `html`. Elle représente le chemin dans l'arbre associé au document, depuis sa racine jusqu'au texte sélectionné. Reproduisez ce chemin en réponse à ce quizz.
{####html/body/section/ul/li}
```

```activité-avancée
::Réorganiser la structure d'un document::
Avec le document http://culturenumerique.univ-lille3.fr/activitesWeb/textes/representation.odt, déplacez la partie 4.2 en la plaçant juste après la partie 2.2. Pour cela, n'utilisez pas de copier coller mais uniquement les fonctionnalités offertes par l'usage du *navigateur* (touche `F5`). Rendez une capture d'écran de la structure obtenue visible dans le *navigateur*.
{}
```

## Les méta-donnnées, une vue qualifiée

Une troisième vue découle de besoins que l'on peut illustrer par les
exemples suivants : un utilisateur peut souhaiter retrouver la date de
création d'un document, un bibliothécaire cherche des documents par
auteur, par titre, par mot-clef, par édition et numéro d'édition, ou
encore par date. Ces éléments ne figurent pas nécessairement dans le
document mais ils le qualifient. Ce sont des méta-informations (ou
méta-données), c'est-à-dire des informations à propos des
informations. Elles forment la **vue qualifiée**** du document. Très
souvent ces informations sont mémorisées sous la forme de propriétés
(ou attributs) ayant une valeur.  Par exemple, la propriété **titre**
de ce document vaut `Culture numérique`, la propriété **datecréation**
de ce document vaut `10 septembre 2015`, etc...

Grâce à cette vue qualifiée et ces méta-données, les traitements sur
des ensembles de documents sont facilités : on peut classer par
auteur, rechercher par titre, ordonner des versions par date, ...

```activité 
::La vue qualifiée:: 
[markdown]Dans le traitement de texte, regarder les propriétés du
document suivant : http://culturenumerique.univ-lille3.fr/activitesWeb/textes/representation.odt
- Quel est le titre, le sujet, les mots clef ? Faites une capture d'écran de la fenêtre où vous avez trouvé ces meta-données.
{}
```

```activité
::Uniquement des méta-données:: 
[markdown]
Pour certaines applications, un document textuel peut se
résumer uniquement à ses méta-données. C'est le cas des notices
bibliographiques où la plus grande partie des fonds n'est pas
numérisée et donc pour lesquelles le contenu des livres n'est pas
représenté numériquement.
- Rendez-vous sur le site de la
bibliothèque de l'université dans l'interface de recherche de
livres.
- Indiquez sur quels critères vous pouvez effectuer
une recherche.
{####Vous pouvez rechercher selon les méta-données comme les dates, les auteurs, etc. Vous ne pouvez pas faire de recherche plein texte dans l'ensemble du texte d'un livre, sauf éventuellement sur des résumés.}
```
## La présentation, une vue pas uniquement graphique

Enfin, les choix du dessin de chaque caractère, de leur taille, de la
couleur du titre, de la taille des marges, etc.  participent à **la
présentation ou forme** du document. Cette forme va s'appliquer au
contenu en s'aidant de la structure mais il est important de bien
distinguer la **présentation** et le **contenu structuré**. En effet,
comme vous l'avez vu dans le cours sur le Web, la séparation entre
contenu et structure dans un fichier `html` et présentation dans une
feuille de style css permet d'afficher un même contenu avec
différentes formes mais aussi de faciliter certains traitements.
Enfin, soyez vigilants car les traitements de textes entretiennent la
confusion entre contenu, structure et forme. Or, un document mis en
forme **n'est pas** un document structuré. Les interfaces proposées qui
semblent très intuitives entraînent souvent de mauvais apprentissages
et de mauvais usages.

Cette vue de présentation est néanmoins très importante pour des
questions de communication et de diffusion car il faut toujours
adapter la forme à la fonction du document. La forme d'un document
pour impression et lecture diffère de la forme d'un document pour
affichage sur écran. La forme peut dépendre de l'objectif de
communication visé.

```activité
::Le jardin zen:: 
[markdown] Pour illustrer à la fois la pertinence de séparer les informations de présentation des autres informations textuelles, mais aussi l'effort de la communauté dans cette direction notamment avec les feuilles de style (CSS ou de documents de traitement de textes), regardez ces différents liens
- Sur le web, la beauté des CSS
  - http://www.csszengarden.com/tr/francais/
  - http://www.csszengarden.com/tr/fr/221/
  - http://www.csszengarden.com/tr/fr/219/
  Entre ces différents designs, qu'est-ce qui change ?
{
~La structure#non, elle reste la même, vérifiez l'identité des codes HTML avec l'affichage du code (CTRL-U) 
~Le contenu#non, lisez bien, les textes sont les mêmes!
=La présentation#oui uniquement la CSS qui ne contient que des éléments de présentation est adaptée.
}
```

```activité
::Mise en forme et structure:: 
Examinez les deux fichiers suivants.
- http://culturenumerique.univ-lille3.fr/activitesWeb/textes/representation.odt
- http://culturenumerique.univ-lille3.fr/activitesWeb/textes/representation2.odt
Sont-ils identiques ? Qu'est-ce qui les différencie ? Illustrez votre propos en citant des opérations qui seraient plus facilement réalisables avec l'un plutôt qu'avec l'autre et pourquoi.
{####Les documents semblent identiques, mais les éléments de structure ne sont pas désignés dans le second. Vous ne pouvez pas réaliser de traitements comme : la réorganisation des sections, la génération des tables de matières, etc.}
```

## Un point d'étape 


>[Animation]
Peut-être une anim de rappel
1. Le contenu brut : la suite de caractères
2. La structure : identification des paragraphes, des titres, des
   sections, etc... et identification de l'organisation de ces
   éléments.
3. La présentation : l'apparence graphique.
4. Les méta-données : informations à propos du document, non
   nécessairement affichées ou imprimées mais utiles pour sa gestion,
   son traitement.

   
Chacune des vues contenu, structure, qualifiée et de présentation est
importante.  Elles contribuent toutes, à des degrés divers, à des
objectifs complémentaires : l'intelligibilité est essentiellement
portée par le contenu et la structure ; la lisibilité est
majoritairement une affaire de présentation ; la capacité à être
efficacement traité par une machine repose sur le contenu, la
structure et les méta-données.

# Documents numériques - formats et normes

Chacune des vues va contribuer à la représentation numérique d'un
document textuel, mais, selon le domaine d'application, elle sera plus
ou moins importante ou nécessaire. La première question est : **que
veut-on représenter en vue de quels usages ?** Des choix techniques
seront associés pour répondre à la question : **comment représenter ?**
Cette distinction entre le quoi et le comment est, en informatique
comme dans beaucoup d'autres sciences, une approche essentielle des
problèmes.

```Activité
::Que représenter (I) ?::
[markdown]Pour représenter des caractères, différentes propositions ont été faites. Que permettait de représenter le code Baudot?
{#### 32 caractères uniquement : les lettres, les chiffres, la ponctuation, et quelques autres  symboles (=, +, -, /, *, &, #...) ; }

::Que représenter (II) ?::
[markdown]Pourquoi aujourd'hui ce code Baudot n'est plus utilisé pour représenter les caractères?
{#### Les symboles des langues autres que l'américain ne peuvent être représentés.}

::Comment représenter ?::
[markdown]Trouver plusieurs moyens utilisés pour représenter un texte: un basé sur des sons, un autre basé sur des trous.
{###Le codage morse ou les cartes perforées sont deux réponses possibles à comment représenter des textes ou des caractères.}
```

## Différents formats pour différents usages

Les choix effectués pour répondre à la question **comment représenter
des documents textuels** aboutissent à des **formats** de
représentation. Vous connaissez sans doute certains de ces formats
précisés avec les abréviations suivantes :

- le format `txt` pour les textes,
- le format `doc` ou le format  `docx` du traitement de textes Word,
- le format `odt` des traitements de textes LibreOffice ou OpenOffice,
- le format `pdf` pour l'impression,
- le format `html` pour les hypertextes.

Vous noterez, que pour de mêmes usages, comme la composition de
documents textuels, il existe des formats différents comme `doc` et
`odt`. Vous noterez également que les formats évoluent avec les usages
et les technologies. Par exemple `html` a été défini dans des versions
successives depuis le début des années 90 jusque `html5`, paru
en 2014.


## Formats et logiciels

Nous avons expliqué la relation forte entre le choix de la
représentation et les traitements qui peuvent être faits sur une
donnée numérique. D'un point de vue très concret, cette relation se
traduit souvent par la liaison entre un format et une application
spécifique d'un éditeur logiciel. Par exemple, un document textuel au
format `doc` est associé au logiciel `Word` de Microsoft. Il aura
souvent été créé avec ce logiciel et pourra être lu et modifié avec ce
logiciel.

Un document dans un format pourra être stocké dans un fichier. Pour
des raisons historiques, le format d'un document est souvent précisé
dans l'extension du nom de fichier constituée de trois ou quatre
lettres après le point. On désigne même abusivement un format par
cette extension, comme nous l'avons fait précédemment en parlant de
format `doc` par exemple. Cette extension peut être vue comme une
méta-donnée qui dit : "le document dans ce fichier respecte le format
de représentation de documents utilisé par le logiciel `Word`".

Si nous avons un document textuel au format `odt`, il ne suffit pas de
le renommer avec l'extension `doc` pour le rendre lisible par Word. Il
faut réaliser une **conversion** d'un format dans l'autre, opération qui
peut être difficile voire impossible. Pourquoi ? Pour au moins deux
raisons :

1. Tout d'abord, les choix qui ont été opérés pour définir les formats
   ne sont pas toujours compatibles.  On peut donc perdre des
   informations lors de cette conversion.
2. Ensuite, les choix ne sont pas toujours rendus publics. On ne peut donc pas toujours écrire de programme de conversion.

Par ailleurs, un document textuel dans un format peut être parfois
manipulé avec des logiciels différents pour des besoins différents.
Par exemple, un fichier `html` peut être ouvert par un navigateur pour
le visualiser.  Le même fichier peut être ouvert avec un éditeur de
texte pour le modifier. Comme vous l'avez vu dans le cours du Web, il
sera également manipulé par les robots des moteurs de recherche qui
contribuent à indexer le web.


```Activité
::Extensions::
[markdown] Dans le nom de fichier `mondocument.txt`, quelle est l'extension ? 
{####txt}

::Conversions::
[markdown] Est-il toujours possible de convertir un document d'un format vers un autre format ?
{####Non, il faut qu'un tel programme de conversion existe et parfois les formats ne sont pas publics et la conversion est alors très difficile ou impossible. }
```
## Ouvert ou propriétaire

Le processus de choix de représentation et de définition d'un format
est complexe et coûteux. Il peut être aussi stratégique d'un point de
vue industriel ou commercial. Dès lors, les créateurs ont la
possibilité de le rendre disponible pour tous librement ou non, de le
cacher ou de le protéger par des brevets.

On parle de **format ouvert** si le format est diffusé publiquement. Par
exemple, vous pouvez accéder librement sur le Web à la définition du
format `html5`.  De plus, aucune entrave légale n'accompagne
l'utilisation d'un format ouvert et de ce fait, un format ouvert n'est
pas lié à un logiciel. En effet, plusieurs logiciels différents
peuvent librement lire ou écrire les informations représentées dans ce
format. On facilite ainsi l'interopérabilité. Par exemple, le format
`html` est utilisé par de nombreux logiciels et même au delà du Web.

On parle de **format fermé** ou propriétaire lorsque des restrictions
d'accès et/ou d'utilisation s'appliquent. Être propriétaire d'un
format très répandu donne une puissance économique très importante
dans notre monde numérique et une position dominante. En effet, la
conversion étant impossible, une mise en concurrence est rendue très
improbable et les utilisateurs sont alors contraints d'utiliser le
logiciel associé. Si `html` avait été un format fermé, sans doute le
web serait-il très différent de celui d'aujourd'hui ou n'existerait
peut-être même pas.



```activité
::Les fichiers d'extension Doc::
[markdown] Lisez la page Wikipedia suivante : https://en.wikipedia.org/wiki/Doc_%28computing%29 et répondez aux questions suivantes
{~ Est-ce que les fichiers avec l'extension `doc` désignent  une chose unique ? #Non, plusieurs logiciels distincts l'ont utilisé pour stocker la représentation de choses distinctes.
~ Est-ce que ce format est ouvert ? #Non, c'est un format propriétaire fermé.
= Est-ce que ce format est toujours développé ?#Oui
}

::Les documents au format PDF::
[markdown]Lisez la page Wikipedia suivante : https://wikipedia.org/wiki/Portable_Document_Format et répondez aux questions suivantes
- Est-ce un format ouvert ?
- Peut-on lire et écrire du `pdf` avec des logiciels différents ?
- Que signifie portable ?
- Les documents dans ce format peuvent-ils toujours être reconstitués à l'identique ? Pourquoi ?
{}
```

## Une minute citoyenne

Le numérique est aujourd'hui un facteur de développement économique
important. Ce développement repose en partie sur des infrastructures
comme les réseaux, le web, étudiés dans les semestres précédents. Les
organisations publiques mondiales, pour ne pas freiner ce
développement ont mis en place des normes et étudient des garanties
pour un accès neutre et de qualité à ces infrastructures. Les normes
du W3C sont un exemple. Le débat actuel sur la neutralité du net est
une autre illustration. Par le passé et encore aujourd'hui plusieurs
entreprises, par des moyens techniques ou commerciaux tentent
d'accaparer ce que beaucoup pensent être soit un bien public soit des
données personnelles. Mais ces infrastructures ne sont pas le seul
point d'accès au numérique. La question des formats de représentation
des données entre évidemment dans l'éventail des possibilités de
contrôler l'économie du numérique.

Lorsque vous enregistrez un document dans un certain format, c'est un
peu comme si vous rangiez un objet dans une boite. Si le format est
propriétaire et protégé, alors cela signifie que lorsque vous voulez
retrouver votre objet vous devez vous adresser à un tiers qui lui seul
a l'autorisation d'ouvrir la boite. La question de savoir si l'objet
vous appartient toujours se pose donc, ou encore celle de la liberté
d'utiliser cet objet.

Transposée dans le monde numérique, cette image signifie que limiter
cet accès a de nombreuses conséquences. L'interopérabilité est rendue
plus difficile : un document dans un format propriétaire, ne peut être
librement utilisé dans un autre logiciel. La liberté des utilisateurs
est également atteinte : en échangeant avec un format propriétaire,
vous forcez vos interlocuteurs à utiliser un logiciel précis. Enfin,
lorsqu'il s'agit de données sensibles ou devant être archivées pour
une très longue durée, l'usage de formats propriétaires repose sur des
logiciels qui peuvent disparaître ou changer leur règles
d'utilisation...

Comme pour les infrastructures, l'état et bien d'autres organisations sont conscientes de ces difficultés. Elle produisent souvent des directives, circulaires  pour inciter à utiliser des formats ouverts et libres. Mais il est bien plus difficile de convaincre les utilisateurs souvent plus enclins à continuer selon leurs habitudes, résultant souvent de nombreux efforts d'apprentissage.

De votre côté, recevoir une formation indépendante des outils, donc
plus fondamentale peut contribuer à être moins dépendant et moins
servile dans ce monde numérique. Mais cela demande un effort
particulier, une attente moins centrée sur l'immédiat et l'utilitaire,
un peu moins personnelle car prenant conscience d'enjeux
communautaires.

# Documents numériques textuels

Nous avons analysé ce qu'est un document textuel.  Nous avons mis en
évidence les quatre vues de contenu, de structure, de forme et
qualifiée. Nous avons discuté des formats de document. Nous allons
maintenant étudier comment peuvent être saisis des documents
numériques textuels. Nous allons voir deux approches :

- l'une dans laquelle on décrit les différentes vues sur le document
  dans un texte structuré,
- l'autre qui repose sur une approche plus orientée vers le rendu
  souhaité.

Auparavant, nous traitons la question du codage des caractères.

## Représentation numérique des caractères

Un document textuel est construit avec des caractères et une séquence
 de caractères correspond souvent à un texte intelligible par l'homme.
 Nous présentons donc, dans un premier temps, comment sont représentés
 en machine les *caractères*.

Précisons d'abord la notion de caractère en prenant l'exemple de la
langue française. Les caractères sont les minuscules, les majuscules,
les lettres accentuées, les chiffres, l'espace et les symboles de
ponctuation.  On peut aussi considérer des caractères comme le
caractère "e dans l'o" ou les symboles monétaires...

Mais avec l'internationalisation et la numérisation de textes anciens,
il faut être également capable de représenter tous les caractères de
toutes les langues, vivantes ou mortes.

Ce travail d'inventaire est long et complexe. Fort heureusement, il
existe des groupes internationaux qui ont pour mission d'établir des
normes pour la représentation numérique des caractères. C'est le cas
du consortium international *Unicode* fondé il y a plus de 20
ans. Il définit en premier lieu le *quoi*, c'est-à-dire quels
caractères ou symboles faut-il coder. À l'heure actuelle, la plupart
des caractères et symboles de la très grande majorité des langues sont
codés. Mais le consortium introduit régulièrement des nouvelles
langues rares ou anciennes ou même des langages comme les Emoji.

Dans ces normes comme Unicode, ce ne sont pas les dessins qui sont
répertoriés mais les caractères eux-même. Cette distinction est
parfois assez subtile : majuscules et minuscules sont des caractères
différents mais un *a* minuscule en gras ou italique en écriture
attachée ou en script est toujours le même caractère. À ces
caractères, s'ajoutent des caractères particuliers, dits caractères de
contrôle souvent invisibles. C'est par exemple, le caractère qui
signifie la fin d'un fichier texte. D'autres proviennent même de
l'époque des machines à écrire comme la tabulation, le retour à la
ligne ou même le *retour chariot* qui permettait à la tête d'écriture
de revenir en début de ligne.

Le consortium unicode définit en second lieu le *comment*. Il s'agit
d'associer à tout caractère pris en charge par Unicode, un nom et un
numéro appelé *point de codage*.  Par exemple, A a pour nom "Latin
Capital Letter A" et pour numéro 65, * a pour nom "Asterisk" et pour
numéro 42. Ces choix ont une histoire et ont été faits de façon
astucieuse pour faciliter certains traitements. Par exemple, pour
passer d'une lettre majuscule de notre alphabet à la lettre minuscule
correspondante, il suffit d'ajouter 32 à son numéro. Avec Unicode,
tout caractère a donc un numéro, il reste à préciser comment ce numéro
est représenté comme une suite de 0 et de 1. Il existe
différents codages, le plus répandu et le plus économe en place est
`UTF-8`.

>[Animation]
bien montrer le double encodage : car vers nombre vers
binaire. On peut le faire avec des caractères divers français, arabe,
chinois, et même Emoji.


```activité
::Unicode::
[markdown]Qu'est-ce que Unicode ? 
{~une manière standardisée de dessiner des caractères d'une langue#Non!
=un standard qui attribue à chaque caractère dans de nombreuses langues,  un nom et un numéro.#Correct}

::Caractère informatique, caractère et glyphe::
[markdown]En informatique le caractère est un peu différent du caractère en typographie... 
{=Le caractère informatique est une notion abstraite pour désigner un symbole d'écriture# oui
=Le caractère informatique peut être invisible#oui
=Le caractère typographique ou glyphe est le dessin imprimé ou reproduit à l'écran#oui
~Le caractère informatique est une émoticône qui permet de représenter un sentiment.#non, même si les émoticônes (emoji) font partie des caractères unicode, ils ne se réduisent pas à cela.
}

::Caractères sans glyphe::
[markdown]Donner des exemples de caractères non imprimables
{####l'espace bien-sûr, mais aussi le retour à la ligne, la fin de fichier, la tabulation,...}

::Point de codage::
[markdown]Quel est le point de codage unicode du point d'exclamation et son nom ?
{####33, mais encore 0x0021 en notation hexadécimale, et son nom est EXCLAMATION MARK}

::Encodage d'une page Web::
[markdown]Dans votre navigateur, ouvrez le menu `affichage/encodage du texte`. Regardez la liste des propositions. Si vous passez de la valeur actuelle à d'autres propositions que constatez-vous ? (N'oubliez pas de repositionner la valeur initiale, sans doute unicode.)
{
=l'affichage du texte est transformé#Correct, sans pour autant que le document ait changé.
~l'interprétation du codage des caractères est resté le même#Non, c'est justement l'inverse qui se produit.
}

```

```activité-avancée
::codage de points de codage::
[markdown]Quelle est la différence entre UTF-8, UTF-16, unicode ?
{####Une fois un numéro, le point de codage,  attribué à un caractère il faut décider comment représenter ce numéro en suite de 0 et de 1. C'est le rôle des normes UTF-8 et UTF-16.}

::Déclaration du codage des caractères dans les pages Web::
[markdown]Aujourd'hui plus de 80% des pages web sont écrites en UTF-8. Pour vérifier quel encodage des caractères a été choisi pour une page Web, quand la page est bien écrite, elle indique clairement ce choix. En observant le code source (utilisez la séquence de touches `CTRL-U` pour l'obtenir) de la page  http://culturenumerique.univ-lille3.fr/, recopiez la ligne qui déclare cet encodage du jeu de caractères.
{#### =<meta charset="utf-8">=. Ici =meta= signifie metadonnée, c'est-à-dire information à propos de ce document, =charset= est une contraction pour signifier jeu (ou ensemble) de caractères, et bien-sûr =UTF-8= spécifie l'encodage choisi.}
```

>[Idées activités]
- Représenter et normaliser est une tache complexe :
  l'exemple du codage des caractères. Le site montre bien qui est
  dans le consortium et que c'est une structure complexe mais organisée
  qui gère tout cela. A des relations avec W3C et ISO. 
- Montrer la ligne avec codage des caractères dans une source
  html. Sur le Web, 85% des docts sont en UTF-8
- Trouver le point de codage de caractères
  français, et de caractères de différentes langues.
- Les codages ont évolué au cours du temps. Une activité
  autour de ASCII et Latin1 ?
- Les codages sont nombreux. Vous avez déja vu des problèmes
  d'affichage dans des mails ou des pages web, ils sont souvent dus à
  des erreurs de codage. Montrer des exemples ?
- Envoyer sur des documents décrivant UTF8 et UTF16 et poser
  des questions sur ces codages. 
- *avancée* on peut faire réfléchir au
  décodage et demander un algorithme de décodage d'un texte en UTF 16,
  puis en UTF8
  
## Textes "simples"

Un document textuel peut être réduit à la seule vue séquentielle,
c'est-à-dire une simple séquence de caractères. Dans ce cas, le format
de représentation privilégié est celui communément appelé *texte
simple*, dont l'extension principale est `txt` et le logiciel
principal pour le manipuler est un *éditeur de textes*. Pour
l'utilisateur, il existe cependant un niveau implicite de structure :

- un *mot* est une suite de caractères séparés par des espaces ou des
  caractères de ponctuation ;
- une *phrase* est une suite de mots dont le premier commence par une
  lettre capitale et qui se termine par un point ;
- un *paragraphe* est une suite de mots séparés par des fins de
  paragraphes.

Ce niveau de structure n'est pas explicitement représenté. Par
exemple, il n'existe pas de codage de la notion de fin de mot. La
notion de mot est le résultat d'un traitement par la machine dépendant
des choix des concepteurs des logiciels qui peuvent reposer sur la
langue, de la définition des symboles de ponctuation. 

> attention sous `macos`, `texedit` est en double mode : éditeur txt et rtf, en interrupteur. ça peut donc être contre productif. Par ailleurs, il ne sait pas compter les mots, ... et oui c'est top les mac
  
```activité
::Compter les mots::
[markdown]Dans libreoffice, essayez de saisir les expressions suivantes :
- Bonjour l'ami.
- Soyez curieux bien-sûr ; essayez-donc !
Dans le bas de la fenêtre le logiciel de traitement de textes indique le nombre de mots du document ou d'une sélection. Qu'observez-vous dans ces deux cas ?
Recommencez cette tentative dans un éditeur de textes. Vous chercherez dans les différents menus comment obtenir les statistiques du texte qui indiquent le nombre de mots.
{####Notre version compte un mot supplémentaire pour le point virgule et le point d'exclamation, mais cela changera-t-il dans le futur ? C'est en tous cas un choix implicite reposant sur la présence d'une espace, car vous n'avez pas explicitement désigné les mots. Dans l'éditeur de texte `gedit` ce choix n'est pas le même.}
```

>[Idées activités]
- Activité ou demo sur éditeur de textes et ses fonctionnalités
- Méta-données sur textes simples. Notez que le compte de
  mots est souvent différent selon le logiciel (gedit vs linux)
- Montrer que la ligne d'affichage n'est pas un élément de
  structure. Par contre, la ligne ou paragraphe correspondant à un appui
  sur touche Entrée en est un.
- Sur la notion de mot. On peut montrer que deux logiciels
  différents vont compter les mots de façon différente. On peut envoyer
  sur la page wikipedia mot et montrer que selon le point de vue le mot
  peut être défini de façon différente.

  
## Des langages et des logiciels

Au delà de cette structure informelle ou naturelle (les mots, les
phrases et les paragraphes), nous avons vu qu'il était important de
structurer un document de manière plus explicite et plus précise en
déclarant des parties, sections, sous-sections, listes, etc.  La
définition de cette structure est exclusivement sous la responsabilité
humaine. C'est le concepteur du document qui sait quelle organisation,
quelle structure associer à son contenu.  Il existe 2 grandes méthodes
pour interagir avec la machine, soit utilisant un langage spécifique
qui à l'aide de mots et de symboles permet de décrire la structure
comme avec le langage `html` dont nous avons déjà parlé, soit en
utilisant les fonctions prédéfinies d'un traitement de texte.
Étudions ces deux options un peu plus en détail.

> Alors comment définir cette structure de façon explicite ?
> L'interaction, par le biais d'un langage commun entre l'homme et la
> machine joue alors un rôle essentiel. Ce langage d'interaction peut se
> traduire par un texte écrit et formel qui décrit un document comme par
> exemple le `html` dont nous avons déjà parlé.  Mais, ce langage peut
> prendre la forme d'une suite d'actions dans un logiciel de traitement
> de textes.

```activité-avancée
::Les paragraphes, structure explicite::
[markdown]Dans un traitement de textes, la notion de paragraphe est explicite. Il existe un caractère informatique signifiant fin de paragraphe et l'utilisateur l'insère explicitement dans un texte en appuyant sur la touche `Entrée`. L'appui sur la combinaison `MAJ-Entrée` insère elle une fin de ligne. À vous de constater cela dans votre traitement de textes :
- Dans un nouveau document saisissez un très long texte. N'utilisez qu'une seule fois la touche entrée pour signifier que ce long texte est composé de deux paragraphes.
- Dans les options de mise en forme des paragraphes centrez le premier. Vérifiez que le second n'est pas centré.
- Au milieu du second, appuyez sur`MAJ-Entrée` pour retourner à la ligne. Dans les options de mise en forme des paragraphes alignez le second paragraphe à droite. Vérifiez que la mise en forme s'applique, y compris après le retour à la ligne.
{}

::La ligne n'est pas vraiment un élément structurel::
[markdown]Même s'il est possible d'insérer des retours à la ligne, c'est une possibilité rarement utilisée (sauf dans des textes particuliers comme des poèmes par exemple).
- Continuez l'exercice précédent en modifiant par exemple la taille des caractères des paragraphes et en vérifiant l'impact sur les retours à la ligne. Que concluez-vous ?
- Essayez de trouver dans des options de mise en forme des lignes : pouvez-vous en trouver ?
{####Le traitement de texte gère seul le retour à la ligne en fonction de paramètres comme la longueur maximale des lignes, la taille de la feuille de papier et des marges, le choix de l'alignement,... Non, il n'existe pas d'outils de mise en forme de ligne, la ligne n'est pas un élément de structure sur lequel on peut facilement appliquer une mise en forme spécifique.}
```

## Textes structurés pour décrire des documents textuels

Pour définir un document textuel, on peut décrire les différentes vues
sur ce document. On parle alors de composition de document en mode
*WYSIWYM* pour "What You See Is What You Mean", en français *ce que
vous voyez est ce que vous vous représentez*. Pour cela, on va décrire
le document par un texte dans un langage de description.  Dans ce
langage certains caractères ou certaines suites de caractères ont un
sens particulier. Les éditeurs de texte servent à écrire directement
dans le langage de description, et des logiciels spécifiques sont
ensuite utilisés pour *calculer* une vue de présentation du document à
partir de sa description.

- *Les langages Wiki* ont été utilisés principalement pour composer
  des pages Web dans un langage simplifié. On utilise des conventions
  comme : une ligne qui commence par `*` est un titre, `**` pour un
  sous-titre. Une ligne vide sépare les paragraphes. Un programme
  de calcul peut construire une page Web à partir d'une description
  textuelle en langage Wiki.
- *Le langage LateX* utilisé pour la composition de documents dans le
  monde scientifique (articles, rapports, thèses, livres). Dans ce
  langage, le texte structuré décrit le contenu et la structure avec,
  par exemple, une section commence par la séquence de caractères
  `\section{titredesection}`. La forme est définie par les règles
  externes de l'édition scientifique. Un programme de calcul prend en
  entrée le document texte décrivant le document et produit en sortie
  un document lisible et imprimable au format `pdf` respectant ces
  règles d'édition.
- *Le langage html* utilise des caractères particuliers comme `<`, `>` et
  `/` pour définir des balises. Par exemple, les balises `<section>` et
  `</section>` permettent de définir une section. Le corps du document
  `html` contient le contenu et la structure. L'entête du document
  contient des méta données comme le codage des caractères utilisé par
  le navigateur pour un affichage correct de la page, mais aussi des
  mots clés à destination des robots pour une bonne indexation du
  document. Enfin, la forme est définie dans un fichier texte
  structuré (une feuille de style) dans *le langage css*.



>[Idées activité]
- Éditeur de texte et org. Coloration syntaxique. Comprendre. Voir dans    navigateur.
- Éditeur de texte et LateX. Coloration syntaxique. Comprendre et montrer le pdf correspondant. On peut montrer un site LateX en ligne.
- On peut refaire html et css. Par exemple sur html montrer corps et entête. Montrer les méta-données de l'entête.
- On doit respecter certaines règles typographiques lorsqu'on décrit un document. Cf document Marc.

## Traitement de textes

Quand la définition de la structure se traduit par une suite d'actions
dans un logiciel, on parle alors de composition *WYSIWYG* pour "What
You See Is What You Get" en français *ce que vous voyez est ce que
vous obtenez*. Dans ce mode de composition, vos actions définissant la
structure, le contenu ou la présentation sont immédiatement
interprétées par le logiciel. Vous voyez donc à l'écran une image
presque fidèle du document imprimé final.  Les logiciels de
*traitements de textes* comme `Word` ou `LibreOffice Writer` ou même
certains éditeurs de contenu Web fonctionnent selon ce principe.

Le mode WYSIWYG semble très facile d'accès car vous échappez à
l'apprentissage contraignant d'un langage de description très
formel. Mais vous ne devez pas oublier que l'interaction avec le
logiciel repose toujours sur les vues structure, contenu, forme et
méta-données lorsque vous composez un document textuel. En effet, si
vous les respectez, vous aurez alors facilement accès aux
fonctionnalités de haut niveau des traitements de texte : la
génération automatique de table des matières, de bibliographie,
d'index ; la réorganisation des sections ; la modification de la
présentation dans tout votre document ; ...

L'apprentissage de cette interaction est alors d'apprendre le sens de
certaines actions. Vous apprendrez par exemple que le rôle de la
touche `entrée` est d'indiquer une fin de paragraphe ; que la
déclaration des sections se fait en cliquant sur le texte du titre
puis dans une liste pour sélectionner le niveau de titre etc.

### Comment procéder ?

Une dernière caractéristique commune aux langages de description et
aux traitements de texte est qu'ils sont extensibles et permettent de
s'adapter à des domaines spécifiques. Par exemple, la structure d'un
manuel scolaire peut comprendre la notion d'exercice, d'activité, de
leçon etc. Être capable de traduire dans la composition de documents
chacun de ces éléments structurels est une plus-value qui permet des
traitements adaptés, que ce soit dans la présentation ou
l'interrogation. Donc une démarche d'analyse préalable à la création
d'un document s'avère nécessaire.

Réaliser cette analyse, c'est comprendre qu'un document a des
objectifs, qu'il doit parfois respecter des règles liées à ses
objectifs. Vous devez avoir réfléchi à ces objectifs, au contenu et à
la structure la mieux adaptée. La démarche de composition d'un
document suivra, en général, l'ordre suivant :

1. Saisir le contenu textuel ou importer ce contenu textuel. Votre
   texte doit respecter les règles de typographie de la langue du
   document. Votre texte doit être structuré en paragraphes.
2. Effectuer les déclarations de structure : sections et titres de
   sections, listes, ... Ces déclarations sont faites à l'aide de
   styles (par exemple titre de niveau 1). L'emploi du mot style est
   regrettable car il entraîne des confusions.
3. Effectuer les choix de présentation basés sur la structure. Par
   exemple, vous préciserez que le style titre de niveau 1 sera
   présenté en gras, police Times, 14 pt, avec un retrait à droite de
   1cm et un espacement avant de 0.5cm et un espacement après de 0.2
   cm.
4. (3-bis) Cela revient à dire qu'il est préférable de ne *jamais* utiliser
les boutons de mise en forme directe qui sont pourtant en bonne
position dans l'interface... Toute les *mises en forme* doivent être
associées aux éléments de structure, et pas à des portions de texte
que l'on aurait sélectionnées.

Dans la pratique, il peut être intéressant de réutiliser une mise en
forme pour plusieurs documents. Par exemple, tous les rapports d'une
même entreprise respectent la même présentation. Pour cela, on utilise
la notion de *modèle de document*.

Enfin, la plupart des méta-données comme auteur, date de création,
date de dernière modification sont ajoutées automatiquement par
l'outil s'il a été correctement paramétré au préalable mais vous
pouvez ajouter explicitement des méta-données.

### Erreurs communes
Les modes WYSIWYG induisent souvent de mauvaises
pratiques. En effet, un utilisateur a souvent tendance à se laisser
guider par le rendu sur l'écran en oubliant que 

- les règles typographiques utilisées par le logiciel vont venir
  modifier ce rendu. Par exemple, c'est le logiciel qui va calculer la
  largeur d'une espace.
- des modifications ultérieures de contenu vont changer la mise en
  page. Par exemple, l'ajout d'un paragraphe peut changer toute la
  mise en page du document complet.

Nous vous donnons donc les conseils suivants :

1. *Respecter les règles de typographie, en particulier de ponctuation*
2. *Ne pas aligner/décaler des parties de textes avec des espaces*
3. *Ne pas mettre en page en créant des paragraphes vides*
4. *Ne pas utiliser les boutons de mises en forme directe*


```activité
- installer grammalecte sur son LO et jouer avec, on peut
  donner un texte avec plein d'erreurs et demander combien ont été
  corrigées par l'outil (typo, grammaire, conjugaison, style).
- Marc a un texte sur la typographie
```

# Ouverture, interopérabilité, licences, ... et liberté 

À travers cette présentation, vous avez sans doute retenu la distinction entre
les vues de contenu, structure, présentation et les méta-données qui
qualifient un document numérique. Dans les autres types de données
manipulées par les ordinateurs, comme les images, le son par exemple
on retrouve également ces distinctions.

Une autre distinction que vous pouvez également retenir c'est celle
entre logiciel et donnée. Parfois très liés à cause de formats
propriétaires, on en arrive de temps à autres à les confondre, mais
bien-sûr la donnée doit pouvoir exister, suivre son cycle de
développement et d'utilisation en dehors du logiciel qui l'a créé.

Par les formats de données libres et ouverts ou propriétaires ou
fermés, vous voyez également une illustration de la rencontre entre le
numérique et le droit. Le droit ne s'applique pas qu'aux formats, mais
aux également aux contenus et aux logiciels. Le domaine du droit du
numérique sort du périmètre de ce cours mais vous devez toujours vous
poser la question du droit dès que vous utilisez une ressource pour la
publier.

Enfin, sachez que l'idée de la liberté ou de l'ouverture s'applique
aux contenus par le biais des licences *creative commons* et aux
logiciels par le biais des licences *GPL* et *CECILL* en précisant
comment vous pouvez utiliser ces contenus et ces logiciels. La
philosophie du libre dans le numérique est née dans les années 80 à
propos des logiciels. Elle s'est étendue depuis et devient un
mouvement qui impacte aujourd'hui toute la société numérique.

```activité
::Les personnages du libre::
[markdown] Qui est Richard Stallman ? Qui est Laurence Lessig ?
{#### Stallman est un informaticien du fameux MIT à l'origine du projet GNU qui fonde le logiciel libre et de la licence associée GPL. Lessig est un juriste à l'origine de la licence Creative Commons. (Voir les pages correspondantes dans Wikipedia)}

::Creative Commons::
[markdown]Quelles sont les différentes variantes de creative commons ?
{#### Six possibilités existent, combinaisons de quatre pôles définissant les différents usages : Attribution : signature de l'auteur initial (obligatoire en droit français) (sigle : BY) ; Non Commercial : interdiction de tirer un profit commercial de l'œuvre sans autorisation de l'auteur (sigle : NC) ; No derivative works : impossibilité d'intégrer tout ou partie dans une œuvre composite ; l'échantillonnage (sampling), par exemple, devenant impossible (sigle : ND) ; Share alike : partage de l'œuvre, avec obligation de rediffuser selon la même licence ou une licence similaire (version ultérieure ou localisée) (sigle : SA)
}

::Le logiciel libre::
[markdown]Quels sont les 4 principes du logiciel libre (voir le site de l'April : http://www.april.org) ?
{#### la liberté d'utiliser le logiciel, pour quelque usage que ce soit ;  la liberté d'étudier le fonctionnement du programme, et de l'adapter à vos propres besoins ; la liberté de redistribuer des copies de façon à pouvoir aider votre voisin ; la liberté d'améliorer le programme, et de diffuser vos améliorations au public, de façon à ce que l'ensemble de la communauté en tire avantage. (L'accès au code source est une condition pour tout ceci)
}
```
<!--À discuter
- Faire réfléchir sur les évolutions récentes de html ? Web
  des données, knowledge graph, réseaux sociaux ?  
- éditeur de texte: la notion de paragraphe définie par la fin de
  ligne 8-). Montrer que la ligne (vue à l'écran) n'est pas un élément
  de structure en faisant varier la taille de la fenêtre éditeur. Le
  mot et les ponctuations ? 
- Montrer que une organisation hiérarchique se retrouve souvent. Montrer la structure d'un livre avec un docbook simplifié. Montrer la structure d'une BD xml de gestion d'une
bibliothèque.  
-->

# Les images

Nous avons détaillé le cas des documents textuels comme exemple
générique de représentation de l'information. Étudions maintenant le
cas des images pour se persuader que les même principes (de choix,
d'exigence, de besoins,...) ont conduit à de nombreux *formats*. Ici
aussi la notion de *norme* est essentielle pour les mêmes raisons de
compatibilité et d'interopérabilité.

## Deux approches principales

En premier lieu, il convient de différentier deux types d'images qui
dérivent de besoins différents, et qui prolonge la distinction entre
des images représentant une abstraction du réel, en général créés par
l'homme et des images qui sont des copies fidèles du monde réel.

Dans le premier cas on trouve par exemple des dessins techniques ou
des cartes. Dans l'autre cas on trouve des images photographiques ou
des images issues de capteurs, radars, d'imagerie en médecine etc,
provenant donc de signaux physiques ou ondulatoires.

Les correspondances dans le monde numérique sont les images
*vectorielles* et les images *matricielles*.

## Les images vectorielles

Les images vectorielles sont une représentation numérique d'images
basée sur des ensembles d'objets abstraits géométriques. Ce sont par
exemple des lignes, des points, des rectangles, des arcs de cercles,
etc.  L'idée est ici de *décrire* des formes complexes par combinaison
de formes simples. Les différents objets qui constituent l'image sont
décrits dans un langage informatique qui précise pour chacun d'eux, la
forme, la dimension, la couleur, la position, etc.  La puissance des
formalismes mathématiques sous-jacents peuvent conduire à produire des
images d'une grande complexité et même des animations.

Les images vectorielles sont utilisées pour produire des schémas, des
diagrammes, des cartes etc. Elles peuvent évidemment contenir du texte
et sont particulièrement adaptées pour représenter des visuels tels
que des logos. On retrouve ces images et les outils qui permettent de
les créer dans de nombreuses applications, par exemple dans les
tableurs, les traitements de textes. Mais elles sont aussi créées à
partir de logiciels spécialisés : les *logiciels de dessin vectoriels*.

Les logiciels qui affichent et manipulent ces images *comprennent* et
*interprêtent* les descriptions, c'est-à-dire calculent le résultat
visuel à partir de la description.  Un avantage très important des
images vectorielle réside alors en leur capacité à les afficher à
n'importe quelle échelle sans aucune perte de qualité. L'affichage est
*recalculé* quel que soit le niveau de zoom. Il est également très
facile de modifier un élément de l'image indépendamment des autres.

Notons également que le même type de représentation est également
utilisée pour représenter des objets en 3 dimensions, autrement dit en
3D.

```activité
::Pierre Bézier::
- Qui est **Pierre Bézier** ?
{}
```

<!--
Ce type d'image n'est pas adapté à la représentation de photo, la
complexité de la réalité ne peut pas facilement être représentée par
des formules mathématiques.
-->

```activité-avancée 
::manipulations images svg::
http://www.w3schools.com/svg/svg_text.asp{}
```

## Les images matricielles

À l'inverse, les images matricielles sont représentées comme un
ensemble de points de couleur, juxtaposés, et souvent minuscules. Si
les points sont suffisamment petits et nombreux, notre oeil ne
parvient pas à les distinguer. Ce principe est largement utilisé
depuis bien longtemps et dans d'autres domaines que le numérique comme
la photographie, les écrans de télévision, l'imprimerie.

Aujourd'hui dans notre monde numérique, les images matricielles sont
particulièrement bien adaptées pour représenter les photos.  Les
appareils photo numériques ainsi que les scanners utilisent ces représentations. 

Dans les images matricielles, les points sont appelés *pixels*. Ils
sont ordonnés en ligne et en colonne dans une grande grille
rectangulaire, qu'on appelle matrice (d'où le nom d'image
matricielle). Simplement, toutes les lignes et toutes les colonnes ont
le même nombre de points.

<!--
Chaque pixel est associé à une couleur. Le codage des valeurs de
couleur fait une nouvelle fois l'objet de normes car il existe de très
nombreuses façons de la  représenter.
-->

## Échantillonner 

Nous pouvons donc considérer que chaque pixel est une observation
d'une très petite partie d'une image réelle, comme un tout petit
échantillon de l'image pris à un endroit précis. Pour ce petit
échantillon, on mesure et mémorise la couleur. Plus les échantillons sont
nombreux et petits, plus l'image sera fidèle à la réalité, à condition
que la mesure de la couleur soit également précise.

Ce processus d'échantillonnage est bien connu des physiciens auquel
nous empruntons le terme. Nous le retrouvons dans toutes les
représentations de signaux physiques, ici l'image, mais également pour
les sons, la musique.

Pour l'image l'échantillonnage découpe l'espace en petites
unités. Pour la musique, l'échantillonnage découpe le temps en petites
unités. Dans le cas d'une image on mesure une valeur de couleur pour
chaque échantillon. Dans le cas d'un son on mesure une valeur de note
(de fréquence sonore) pour chaque échantillon.




```activité-avancée
::Échantillonner la musique::
[markdown]Un CD contient une représentation numérique standardisée de la musique. Dans ce cas,  on prend une mesure de la valeur du son plusieurs milliers de fois par seconde. Les milliers de fois par seconde se disent  *kilo hertz* (Khz). Quelle est la valeur de l'échantillonnage utilisée dans le format des CD audio ?
{#### 44,1Khz, c'est-à-dire qu'on mesure le son 44 100 fois par seconde.}

::Échantillonner les images::
[markdown]Plusieurs  appareils photo sont équipés d'une cellule qui permet de capturer les image sur une grille de 4000 par 3000. Dans les notices, il est indiqué alors combien de mégapixels (millions de pixels) ?
{####12 Mégapixels. Voyez le tableau https://fr.wikipedia.org/wiki/Capteur_photographique#Capteurs_utilis.C3.A9s_dans_les_appareils_photographiques_num.C3.A9riques}

::La qualité de l'image::
[markdown]La qualité d'une image imprimée va dépendre du nombre de pixels, mais aussi de la taille de ces pixels. Vous avez sans doute remarqué que la qualité d'un agrandissement photo peut être parfois dégradé par rapport à un original de taille plus réduite. Des unités mesurent cette finesse des images, appelée encore la résolution. Cherchez sur internet les unités utilisées pour indiquer la résolution des images. *Aide* : l'influence anglo-saxonne est bien présente, le pouce (inch) est utilisé.
{####ppp (ppi) pour point par pouce (point per inch) ou dpi (dot per inch) }
```

## La couleur

Comment représenter cette valeur de couleur mesurée ? 

Depuis longtemps les peintres ont créé des nuances en
mélangeant des couleurs dites primaires. Ce procédé est comparable à
celui utilisé pour coder les couleurs des pixels d'une image
vectorielle ou matricielle. 

### les images RVB

Le modèle de couleurs le plus répandu est le modèle RVB pour Rouge
Vert Bleu. Chaque pixel est décrit par 3 valeurs représentant
respectivement la proportion de rouge, de vert et de bleu.  La couleur
finale est la combinaison de ces trois valeurs.  Le modèle RVB est
directement issu de contraintes technologiques.  En effet, les écrans
(télévision, ordinateur, tablettes, ainsi que les capteurs des
appareils photos numériques ou les scanners utilisent tous ce mode de
représentation de la couleur.  Dans le modèle RVB, la couleur (O, O,
O) correspond au noir, alors que lorsque les 3 composantes sont au
maximum, cela donne du blanc.

```activité-avancée
::Les valeurs de R de G ou de B::
[markdown]Pour chaque pixel, échantillon spacial de l'image, une valeur de couleur est mémorisée. La qualité de l'image dépend à la fois du nombre et la taille des pixels, mais également de la précision de cette mesure de couleur. Très souvent, chaque proportion de rouge, vert et bleu est stockée sur un octet. Mais combien de valeurs possibles peut-on représenter avec un octet ?
{####256, Voir https://fr.wikipedia.org/wiki/Octet. Avec un bit, deux valeurs (0 et 1) peuvent être codées ; avec 2 bits, 4 valeurs (00,01,10,11) ; avec 3 bits, 8 valeurs (000,001,010,011, 100,101,110,111),... avec 8 bits, on obtient 256 valeurs possibles.}

::Les valeurs RGB::
[markdown]Avec 1 octet par couleur, combien d'octets et combien de couleurs possibles peuvent être codées ?
{####1 octet par couleur, 3 couleurs, donc 3 octets, donc 256*256*256=16 777 216 valeurs possibles. Soit environ 16 millions.}

::Les images CMJN::
[markdown] Un autre modèle de couleur
est utilisé dans le monde de l'édition, il s'agit du modèle `CMJN`. Le
principe est similaire au modèle RVB, il s'agit de décrire une couleur
par combinaison de plusieurs couleurs primaires. Mais alors que le RVB
correspond aux technologies des écrans, le CMJN est adapté au monde de
l'impression. Que signifient les initiales CMJN ?
{#### Cyan Magenta Jaune et Noir}
```
## Les formats

Comme pour le cas des documents, les formats d'images sont très variés et la grande distinction entre image matricielle et vectorielle n'entraîne pas que deux formats.  Évidemment le langage de description des formes géométriques dans les images vectorielles entraîne de nombreux choix. Aujourd'hui la communauté semble toutefois s'accorder de plus en plus sur le standard `SVG`. Pour les images matricielles, la variabilité des formats est vraiment très grande. De nombreuses caractéristiques issues des besoins de manipulation sont à considérer mais également les progrès technologiques liés aux dispositifs d'acquisition comme simplement les appareils photos. À titre d'exemple, citons la possibilité comme la manière de stocker les méta-données comme par exemple la date, l'auteur, etc ; la volonté de les échanger sur internet rapidement et donc de limiter l'espace stockage ; la possibilité de gérer des images composées de plusieurs couches superposées, ou de gérer de la transparence.


```activité-avancée
::meta-données de photos::
[markdown] La plupart des appareils photos
numériques ajoutent des méta-données à chaque prise de vue. Elles
peuvent décrire les caractéristiques techniques de la prise de vue
(valeur de la focale, vitesse d'obturation, ouverture du
diaphragme,...) mais aussi des informations plus personnelles comme
les coordonnées GPS quand elles sont disponibles, le modèle d'appareil
utilisé, ainsi que l'heure et la date de la prise de vue.
Mais aussi les personnages ou les étiquettes associées à la photo ...
{}
```

<!--  ### la taille des images
Ce vocabulaire de taille peut recouvrir 3 notions bien distinctes :

- la taille du fichier contenant la représentation numérique de
  l'image
- la *résolution* (on dit aussi la *définition*) de l'image,
  c'est-à-dire le nombre de pixels qui la constituent.
- les dimensions en cm de l'image affichée sur un écran ou imprimée
  sur un support.

Les deux premières notions sont évidemment liées et proportionnelles,
chaque couleur (chaque pixel) étant codée avec un certains nombre de
bits, une image découpées en 50 000 pixels prendra une place 50 fois
supérieure à une image de 1 000 pixels (ou prendra 50 fois plus de
temps à être télécharger sur le réseau).

La troisième notion est plus délicate et les liens avec la résolution
des images sont souvent mal compris. Il faut d'abord comprendre qu'un
pixel n'a pas de taille fixe, 

Les écrans peuvent être vus comme des images numériques matricielles,
ils sont eux aussi découpés en pixels organisés en ligne et
colonne. D'ailleurs, lorsqu'on fait une *copie d'écran*, cela génère
une image matricielle contenant exactement le même nombre de pixels
que l'écran.

Les images matricielle affichée à l'écran peuvent être affichées en
faisant correspondre un pixel de l'image avec un pixel de
l'écran. Les dimensions (en cm) de l'image affichée dépendent alors du
paramétrage de l'écran (un même écran peut être configurée selon
plusieurs résolutions) et de la taille physique de l'écran. 
Certains smartphones ont des résolutions identiques aux
grands écrans de bureau, les pixels sont alors beaucoup plus petits.

Lors de l'impression, on retrouve les mêmes caractéristiques, les
images peuvent être imprimées en *serrant* beaucoup les pixels c'est à
dire en mettant beaucoup de pixel par unité de longueur soit en
imprimant de plus gros pixels, ce qui 

Mais on peut aussi effectuer une opération de zoom qui 

Une même image peut donc avoir plusieurs
représentations dans des modèles différents, le choix du codage
dépendra de l'utilisation désirée.
-->
