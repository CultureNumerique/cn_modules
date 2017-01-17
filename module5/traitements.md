LANGUAGE:   fr
TITLE:   Les traitements numériques et les applications
MENUTITLE: Les traitements numériques
AUTHOR: Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

<!-- pandoc -t latex -V geometry:margin=3cm --toc traitements.md -o t.pdf -->

<!-- pandoc -F ext.py -t latex -V geometry:margin=3cm --toc traitements.md -o t.pdf -->

# Comprendre les traitements

Pourquoi les ordinateurs peuvent-ils nous apparaître plus précis et
plus efficaces que nous et pourquoi peuvent-ils même apparaître
"intelligents" ?  Une partie de l'explication est technologique. Elle
tient au fait que les ordinateurs peuvent calculer très vite et, par
conséquent, traiter rapidement de grandes quantités de données.  Mais
une autre partie de l'explication est plus fondamentale.  L'ordinateur
a la capacité de combiner des traitements pour en définir de nouveaux
plus complexes. Ce principe est général. Les traitements définis par
combinaison peuvent à leur tour être combinés pour définir de nouveaux
traitements, jusqu'à définir des applications très sophistiquées que
vous utilisez. Ces combinaisons sont appelées *algorithmes* et rien
n'est magique dans ce domaine.  L'intelligence apparente des machines
est le résultat de ces combinaisons répétées, mais surtout de
l'intelligence collective des femmes et des hommes qui ont conçu ces
algorithmes. Les algorithmes sont traduits dans des programmes
informatiques. Ces programmes, logiciels, ou applications réalisent
les traitements au sein de vos machines. Et chacun peut être capable
de comprendre et d'écrire des algorithmes et des programmes. Nous
allons étudier, dans ce module, les principes généraux des
algorithmes, des programmes informatiques et donc des traitements
informatiques.

En introduction de ce cours, illustrons ces points sur l'exemple d'une
application de calcul d'itinéraire par un site Web, une application
mobile ou encore un petit ordinateur spécifique qu'on appelle
abusivement `GPS`
(le [GPS](https://en.wikipedia.org/wiki/Global_Positioning_System) pour
"Global positioning System' est un système qui permet de déterminer
les coordonnées d'une position exacte sur terre). Tout d'abord,
réfléchissons aux informations que doit posséder le programme en
pensant à quoi nous aurions besoin si nous devions réaliser cette
tâche nous même. Tout d'abord, il faut connaître le point de départ
qui peut être obtenu par un dispositif technique comme un `GPS` ou
être renseigné par vos soins. Il faut également renseigner la
destination et le moyen de transport choisi.  Supposons, pour
simplifier la présentation, que le logiciel dispose d'une ville de
départ, d'une ville destination, que le moyen de transport choisi est
la voiture et qu'on recherche l'itinéraire le plus court.  Qu'est-ce
qu'un itinéraire ?  C'est une suite de routes à emprunter pour
rejoindre la destination mais nous pouvons aussi représenter un
itinéraire par une suite de villes voisines, toujours par souci de
simplification.  Le programme peut-il disposer de tous les itinéraires
possibles entre deux villes quelconques ? La réponse est non car cela
nécessiterait bien trop de ressources de stockage.

C'est donc un programme qui va calculer l'itinéraire le plus court
entre les villes de départ et de destination à partir uniquement des
distances entre villes voisines (sans étape).  L'ensemble de ces
distances représente déjà un volume de données important mais peut
être stocké dans un petit équipement comme un smartphone ou un `GPS`.
Mais un programme ne peut pas non plus calculer tous les itinéraires
possibles car, même si une machine calcule vite, le temps de calcul
serait trop long et vous n'allez pas de Lille à Paris en passant par
Marseille !  Donc ce programme se doit d'être plus "intelligent". Pour
cela, il utilise un algorithme de recherche de plus court chemin comme
l'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra),
issu des travaux de recherche des mathématiciens et informaticiens
ayant étudié ce problème. Mais qu'est-ce-qu'un algorithme ? Nous y
reviendrons dans ce cours, mais, pour l'instant, considérons qu'un
algorithme est une explication très précise de *comment* résoudre un
problème. L'algorithme de Dijkstra est un algorithme ingénieux qui
décrit comment combiner un nombre raisonnable d'opérations
élémentaires (des additions, des comparaisons, des recherches dans
l'ensemble des distances) pour calculer le plus court chemin entre un
départ et une destination.

Le coeur de notre application de calcul d'itinéraire est donc basé sur
un algorithme de recherche de plus court chemin qui peut être adapté
pour calculer le chemin le plus rapide en remplaçant les distances par
des temps de parcours. Il peut également être appliqué avec d'autres
moyens de transports. Ces algorithmes vont pouvoir être intégrés dans
des applications en les combinant avec d'autres calculs pour la
reconnaissance vocale, la géolocalisation, etc On construira, par
exemple, ainsi une application qui analyse le son de votre voix, le
traduit vos paroles en mots et phrases, identifie des adresses de
départ ou de destination, repère votre position, interroge un service
web sur l'état du trafic routier pour vous indiquer, en temps réel, le
chemin le plus rapide. Grâce à ces combinaisons nous obtenons une
application qui résout des tâches complexes, qui peut paraître
intelligente car ses capacités sont souvent supérieures à celles d'un
passager uniquement accompagné de sa vision locale, de ses
connaissances et sa carte routière. Toutefois, ce logiciel, reposant
sur le génie de ses concepteurs, ne peut résoudre que des tâches pour
lesquelles il a été programmé et ne pourra pas gérer des situations
imprévues.

Pour conclure, cet exemple montre qu'une application moderne interagit
avec l'environnement (utilisateur, périphériques dont système `GPS`,
réseau). Il montre également qu'une application est construite en
composant d'autres applications.  C'est ce principe de composition qui
permet de définir des algorithmes pour résoudre des problèmes et qui
permet de passer d'une machine "bête" manipulant des 0 et des 1 à une
machine "intelligente" pouvant réaliser des tâches complexes.
L'exemple a également permis de montrer que malgré les capacités sans
cesse croissantes des machines, il faut être attentif à la taille des
données mémorisées et au temps de calcul des programmes. Enfin, nous
rappelons que l'intelligence supposée de la machine est due à
l'intelligence des femmes et des hommes ayant conçu les
applications. Mais l'exemple montre également que l'algorithme ou
l'application a besoin de données pour fonctionner : les distances
entre villes, l'état du trafic, ... L'intelligence apparente de la
machine est aussi le résultat de la conjonction de ces données avec
ces algorithmes. L'industrie moderne du numérique l'a parfaitement
compris et accorde aujourd'hui bien plus de prix aux données qu'elle
accumule et partage peu, qu'aux algorithmes qui pour la plupart sont
publics.

Dans la suite du cours, nous présentons comment composer des
opérations pour définir de nouvelles opérations et discutons des
algorithmes, nous présentons les langages de programmation et la
traduction des algorithmes en programmes. Nous terminons par l'étude
de quelques exemples : comment un correcteur orthographique peut-il
corriger vos fautes, comment des programmes peuvent classer des textes
dans des thèmes et comment une machine peut jouer aux échecs (et au
go) en battant les experts humains.



```compréhension
::Des combinaisons::
[markdown]
Un programme peut combiner plusieurs traitements pour définir des traitements plus complexes{T} 

::Algorithmes et programmes::
Un algorithme est:
{
~%50% l'expression d'une méthode pour résoudre automatiquement une tâche
~%50% implanté dans un ordinateur dans un programme informatique
~ une suite de 0 et de 1
#### Un algorithme peut éventuellement être traduit dans un programme lui même traduit en une suite de 0 et de 1,  quand il est implanté dans un ordinateur. }


::Une application indépendante ?::
[markdown]
Lancer une application implique de lancer plusieurs traitements
{T}


::Application et machine::
[markdown]
L'exécution d'une application fait usage de ressources de la machine. 
Donner des exemples de ressources.
{#### a minima avec le processeur de calcul et les mémoires}

::Application et périphériques::
[markdown]
L'exécution d'une application peut faire appel à des interactions avec
l'extérieur de la machine par des périphériques. Donner des exemples de
périphériques.
{#### réseau, clavier, souris, écran, ...}
```


# Les algorithmes

## Introduction

Bien que la notion soit très ancienne, le mot *algorithme* a récemment
fait irruption dans les médias, car nous mesurons aujourd'hui plus
sensiblement l'impact du numérique dans la société. Par exemple, les
moteurs de recherche posent la question sociétale de l'accès à la
connaissance : *quel algorithme choisit l'ordre des résultats à une
requête dans un moteur de recherche ?* Une autre question de société
concerne l'utilisation des traces de nos actions dans le monde
numérique : *que peut inférer un algorithme de masse de données (big
data) sur moi à partir de mes activités sur le Web ?* Un dernier
exemple concerne l'*intelligence artificielle* avec la victoire
récente (2016) d'un ordinateur contre le meilleur expert humain au jeu
de Go qui a soulevé la question suivante : *les algorithmes vont-ils
permettre l'avènement d'une intelligence artificielle ?*


Qu'est-ce qu'un algorithme ? Dans ce cours de culture numérique,
plutôt qu'une définition scientifique, nous allons introduire les
idées principales portées par ce mot. Un
[célèbre livre d'introduction à l'algorithmique](https://mitpress.mit.edu/books/introduction-algorithms)
commence par "Before there were computers, there were algorithms". En
effet, un algorithme est essentiellement *une explication de comment
on résout un problème* et nous, humains, nous résolvons des problèmes
dans toutes nos activités : pour faire la cuisine, pour organiser
notre journée, pour nous rendre à une adresse, ..., et nous sommes, en
général, capables d'expliquer notre façon de procéder, mais cela n'en
fait pas pour autant toujours un algorithme.  Un algorithme doit être
très précis et ne contenir aucune ambiguïté car il doit pouvoir être
exécuté, de façon automatique, sans juger ni réfléchir.  Comme le dit
[Gérard Berry](http://www.college-de-france.fr/site/gerard-berry/#course) :
*Le but est d’évacuer la pensée du calcul, afin de le rendre
exécutable par une machine numérique*.  Enlever la pensée, c'est se
comporter comme un automate et exécuter les instructions sans faire
appel à des connaissances extérieures.

Prenons l'exemple de la préparation du café matinal
dans une machine à café à filtres : prendre un filtre dans la boîte ;
placer le filtre dans la cafetière ; prendre le paquet de café ;
mettre autant de cuillères de café que de tasses souhaitées ; mettre
de l'eau tant que le niveau ne correspond pas au nombre de tasses
souhaitées ; démarrer la cafetière. Les instructions ne sont pas
suffisamment claires. Par exemple, l'instruction pour mettre le café
suppose que vous sachiez que le café doit être placé dans le filtre
déposé précédemment sinon il faudrait le préciser pour que
l'instruction soit non ambiguë. Quant à la réalisation, elle dépend de
vos connaissances.  Un ami invité chez vous qui ne sait pas où vous
rangez vos filtres et votre café ne pourra pas la réaliser.

Enlever la pensée, le jugement, c'est aussi s'exposer à des exécutions
inattendues.  Car un algorithme, bien que précis et non ambigu peut
pour autant être faux, incomplet ou incorrect. En continuant l'exemple
du café matinal, votre invité très bête (convenons-en) suit
scrupuleusement les instructions que vous avez données, quelles que
soient les conditions. Il n'a pas vu que le réservoir était à moitié
rempli et il ajoute de l'eau sans jamais pouvoir atteindre le niveau
"1 tasse" et déclenche une (mini-) inondation !  Dans le monde
numérique, ce serait un logiciel qui plante, un bug suite à une
condition initiale imprévue !

Nous allons approfondir la notion d'algorithme et étudier sa relation
avec les ordinateurs. En effet, la citation complète est : "Before
there were computers, there were algorithms. But now that there are
computers, there are even more algorithms, and algorithms lie at the
heart of computing" qui montre bien l'importance des algorithmes.


```compréhension 
::Algorithmes et ordinateurs:: 
[markdown]
Les premiers algorithmes ont été conçus 
{
~ sur un ordinateur de type PC
~ par Dijkstra
~ pendant la seconde guerre mondiale
= bien avant les ordinateurs
#### Vous avez vous-même appris de nombreux algorithmes bien antérieurs à l'ordinateur comme celui qu'on réalise en posant une addition... et bien d'autres de la vie courante.}

::Recettes de cuisine::
[markdown]
Un exemple classique d'algorithme utilisé dans la vie courante est une recette de
cuisine comme
[la recette d'une omelette](http://www.lesoeufs.ca/recettes/omelette-de-base).
Regardez
cette recette et répondez aux questions suivantes :
\n
- Décrire les actions de base qu'est supposé savoir faire l'utilisateur de cette recette
- Décrire les éléments utiles à l'exécution
{#### actions : fouetter, chauffer, verser, mesurer le temps, ... ; éléments : les ingrédients, une poêle, une plaque de cuisson, ...}
```

## Algorithmes et ordinateurs

Nous avons expliqué le principe général de composition permettant de
créer une nouvelle fonctionnalité en utilisant des fonctionnalités
déjà existantes. Rappelons également que ce principe est général et
que les nouvelles fonctionnalités peuvent, à leur tour, être composées
selon ces principes jusqu'à pouvoir concevoir les applications
complexes que vous utilisez sur un ordinateur, une tablette ou un
smartphone. Les règles de composition sont décrites par des
algorithmes, mais il est avant tout nécessaire de définir quelles
fonctionnalités sont déjà existantes de base dans un ordinateur.

### La machine


*Ordinateur* est un mot inventé par un linguiste dans les
années 50. Il fait référence à l'exécution d'ordres,
d'instructions. En anglais le mot *computer* fait plutôt référence au
calcul et les deux notions se retrouvent dans cette
machine. Essentiellement, la machine repose sur une *unité de calcul*
qui fonctionne avec des nombres représentés (ou codés) avec des 0 et
des 1. L'unité de calcul sait changer des 0 en 1, faire des calculs
simples comme des additions, comparer des nombres. Elle utilise des
*mémoires* pour ranger et retrouver ces nombres. La mémoire est
organisée avec des emplacements repérés par des numéros appelés
adresses. La machine peut alors ranger une valeur à une adresse donnée
et retrouver une valeur rangée connaissant son adresse. Enfin, une
*unité de contrôle* donne les ordres à l'unité de calcul et aux
mémoires. Ce modèle de machine n'a pas évolué depuis les années 40
même si les machines ont évolué. En effet, l'électronique et la
miniaturisation ont considérablement réduit la taille et augmenté les
capacités et la rapidité de la mémoire, de l'unité de calcul et
l'unité de contrôle. Ces progrès ont aussi rendu l'ordinateur plus
économe et plus résistant si bien qu'on le retrouve désormais dans
tous les milieux et toutes les situations.

```activité
::Modèle de l'ordinateur::
[markdown]
Le modèle décrit précédemment a été inventé par Von Neumann. 
En voici [une description schématique](https://fr.wikipedia.org/wiki/Architecture_de_von_Neumann). Les données et les programmes (instructions) sont-elles considérées de la même manière dans la mémoire ?
{T
#### oui et c'est un élément important qui a permis le développement de l'informatique}

::Rôle des linguistes::
[markdown]
Toute la communauté scientifique a participé au développement de l'informatique et, tout particulièrement, les mathématiciens, les logiciens et les physiciensmais aussi les linguistes. En voici trois exemples :
\n
- Qui a inventé le mot ordinateur ?
- Qui est Larry Wall ?
- Qui est Noam Chomsky ?
{#### Jacques Perret sur une demande d'IBM de trouver un terme 
français. Larry Wall est un linguiste qui a inventé un langage 
de programmation Perl toujours très utilisé pour traiter des 
(ensembles de) fichiers textes. Noam Chomsky est un linguiste 
qui a caractérisé les langages formels (utilisés par les machines) 
et naturels (les langues humaines).}
```

### La séquence

Apprenons à notre machine à transformer un caractère majuscule en
caractère minuscule correspondant. Rappelons d'abord que, dans les
codages standards comme `ASCII` et `UTF8`, le caractère `A` majuscule
a pour nom "Latin Capital Letter A" et pour numéro `65`. Le caractère
`a` minuscule a pour numéro `97`. Croyez-nous sur parole, `65` s'écrit
`01000001` et `97` s'écrit `01100001`. C'est remarquable car, pour
passer de l'un à l'autre, seul le 6ème chiffre partant de la droite,
un `0`, est transformé en `1`. Ceci est vrai pour toutes les lettres
de notre alphabet latin et le passage de majuscule à minuscule
consiste juste à changer un `0` par un `1` à la sixième position. Et
l'unité de calcul sait réaliser cette opération.  Notons le lien très
fort entre le codage, très astucieux, et les capacités de la
machine. Notons aussi que changer ce 6ème chiffre correspond également
à ajouter 32 (65+32 vaut 97). Nous sommes donc capables de décrire le
traitement que doit réaliser la machine pour transformer une
majuscule, dont le code binaire est stocké dans sa mémoire à une
adresse connue, en minuscule avec l'algorithme suivant :

    Accéder à l'adresse mémoire pour trouver le codage du numéro du symbole
	Ajouter 32 (changer le 6ème chiffre du codage binaire de 0 en 1)
	Ranger le résultat dans la mémoire à la même adresse

Nous retrouvons dans cet exemple l'organisation de la machine avec ses
adresses, sa mémoire, son unité de calcul (pour ajouter 32) et son
unité de contrôle. L'unité de contrôle doit juste assurer que ces 3
instructions soient réalisées successivement dans cet ordre, *en
séquence*. Nous sommes donc arrivés à définir sur notre ordinateur un
traitement ayant un sens pour nous (remplacer une majuscule par une
minuscule) à partir de la représentation numérique d'une information
et grâce à une combinaison d'instructions en séquence. *La séquence
est le premier mode de combinaison utile pour décrire des
algorithmes*.


```compréhension
::Une séquence::
[markdown]
Quelle est la dernière valeur lue dans l'algorithme suivant
\n 
  Ranger 4 dans la mémoire à l'adresse 12 
  Ranger 8 dans la mémoire à l'adresse 5
  Lire la valeur de la mémoire à l'adresse 12 
  Ajouter 1 à cette valeur et la ranger dans la mémoire à l'adresse 12
  Lire la valeur de la mémoire à l'adresse 12 
  Lire la valeur de la mémoire à cette valeur
{#8}
```

### L'alternative

L'ordinateur est une machine très obéissante qui exécute
scrupuleusement les ordres qu'on lui donne. Le traitement précédent
ajoutera `32` au numéro du caractère en mémoire même si celui-ci n'est
pas le numéro d'une lettre majuscule. Par exemple, le numéro `63`
représente le point d'interrogation `?` et, si on lui ajoutait `32`,
on obtiendrait le caractère tiret bas `_`, ce qui n'est pas le
résultat attendu, donc un bug ! On doit donc ne réaliser cette
opération que pour une majuscule. Pour cela, nous allons contrôler que
le contenu de la mémoire correspond bien à une lettre majuscule avec
l'algorithme suivant :

    Accéder à l'adresse mémoire pour trouver le codage du numéro du symbole
	Si le numéro est compris entre 65 et 90 Alors (si c'est une majuscule)
       Ajouter 32 
	   Ranger le résultat dans la mémoire a la même adresse
    Fin du Si (sinon rien à faire -- laisser le contenu inchangé)

Cet algorithme est une séquence de deux instructions. La seconde
instruction est un *si* qui est le représentant d'un deuxième mode de
combinaison appelé *alternative*. L'ordinateur est capable d'exécuter
cette alternative car l'unité de calcul sait faire des
comparaisons et l'unité de contrôle est capable de sélectionner la
prochaine instruction à exécuter selon la valeur de cette
comparaison. Cela fait partie des fonctionnalités existantes de la
machine.  Donc selon le résultat de la *condition du si*, la machine
exécutera différentes instructions. Sur notre algorithme, si le numéro
du caractère en mémoire est compris entre 65 et 90, c'est-à-dire si le
caractère est une majuscule, la machine exécutera les deux
instructions pour remplacer la majuscule par la minuscule
correspondante dans la mémoire. Dans le cas contraire, on ne fait rien
mais nous aurions pu en toute généralité réaliser une autre suite
d'instructions. *L'alternative est le deuxième mode de combinaison
utile pour décrire des algorithmes*
