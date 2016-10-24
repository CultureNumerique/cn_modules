LANGUAGE:   fr
TITLE:   Les traitements numériques et les applications
MENUTITLE: Les traitements Numériques
AUTHOR: Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

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
::Une application indépendante ?::
[markdown]
Lancer une application implique de lancer plusieurs traitements
{T}

::Application et machine::
[markdown]
L'exécution d'une application fait usage de ressources de la machine. Donner des exemples de ressources.
{#### a minima avec le processeur de calcul et les mémoires}

::Application et périphériques::
[markdown]
**Application et périphériques**
L'exécution d'une application peut faire appel à des interactions avec l'extérieur de la machine par des périphériques. Donner des exemples de périphériques.
{#### réseau, clavier, souris, écran, ...}
```

# Les algorithmes

## Introduction

Bien que la notion soit très ancienne, le mot *algorithme* a récemment
fait irruption dans les médias, car nous mesurons aujourd'hui plus
sensiblement l'impact du numérique dans la société. Par exemple, les
moteurs de recherche posent la question sociétale de l'accès à la
connaissance : *quel algorithme choisit l'ordre des résultats à une
requête dans un moteur de recherche ?* Une autre question sociétale
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
appel à connaissances extérieures.

Prenons l'exemple de l'explication de la réalisation du café matinal
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

## Algorithmes et ordinateurs

Nous avons expliqué le principe général de composition permettant de
créer une nouvelle fonctionnalité en utilisant des fonctionnalités
déjà existantes. Rappelons également que ce principe est général et
que les nouvelles fonctionnalités peuvent, à leur tour, être composées
selon ces principes jusqu'à pouvoir concevoir les applications
complexes que vous utilisez sur un ordinateur, une tablette ou un
smartphone. Les règles de composition sont décrites par des
algorithmes, mais il est avant tout nécessaire de définir quelles
fonctionnalités dont déjà existantes de base dans un ordinateur.


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
Le modèle décrit précédemment a été inventé par Von Neumann. Trouver une description schématique de ce modèle appelé architecture de Von Neumann
{}

::Rôle des linguistes::
[markdown]
Qui a inventé le mot ordinateur ? Qui est Larry Wall ? Qui est Noam Chomsky ?
{#### Jacques Perret sur une demande d'IBM de trouver un terme français. Larry Wall est un linguiste qui a inventé un langage de programmation Perl toujours très utilisé pour traiter des (ensembles de) fichiers textes. Noam Chomsky est un linguiste qui a caractérisé les langages formels (utilisés par les machines) et naturels (les langues humaines).}
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

### La répétition

Nous souhaitons appliquer la transformation à tous les caractères d'un
texte. Il faut d'abord choisir une représentation du texte. Nous
supposons que notre texte est une suite de caractères. Tous les
caractères de ce texte sont stockés dans la mémoire de l'ordinateur
les uns à la suite des autres, à des adresses consécutives à partir
d'un adresse connue.  Pour être capable de repérer la fin du texte, on
choisit d'ajouter après le dernier caractère du texte un symbole
spécial choisi ici comme ayant pour code `0`. Notre
algorithme peut s'écrire :

    Accéder à la mémoire à l'adresse du premier caractère du texte
	Répéter tant que la valeur n'est pas 0
  	   Si la valeur est comprise entre 65 et 90 Alors
          Ajouter 32
	      Ranger le résultat dans la mémoire à l'adresse actuelle
	   Fin du Si
       Ajouter 1 à l'adresse actuelle (pour passer au caractère suivant)
       Accéder à la mémoire à la nouvelle adresse actuelle
    Fin de la répétition

Dans cet algorithme, nous utilisons, pour parcourir tous les
caractères du texte, une *répétition* appelée aussi par les
informaticiens une *boucle* ou une *itération*.  L'ordinateur est
capable d'exécuter cet algorithme uniquement à l'aide de ses
fonctionnalités existantes.  Sur notre algorithme, lorsque l'unité de
contrôle demande à exécuter la répétition, l'unité de calcul
effectuera la comparaison avec la valeur `0`. Si tel est le cas
l'unité de contrôle fera exécuter les ordres jusqu'à la fin de
répétition puis sélectionnera à nouveau l'instruction de comparaison
au début l'unité de contrôle, créant ainsi une répétition. Si la
comparaison est fausse alors l'unité de contrôle fera exécuter
l'instruction juste *apres* la fin de répétition, terminant alors la
répétition.

Ce mode de combinaison par une répétition est essentiel car il permet
d'appliquer un même traitement un grand nombre de fois, par exemple
comme ici à une suite de caractères. Notez bien qu'il est important de
s'assurer que l'algorithme s'arrête. Sur notre exemple, il faut être
sûr de rencontrer le code `0` à la fin du texte pour que l'algorithme
s'arrête à la fin du texte sinon il ferait des opérations inattendues
dans la mémoire et donc un bug. De plus, il risquerait de "planter la
machine" car si il ne trouve jamais de 0, notre algorithme tournerait
sans fin ! *La répétition est le troisième mode de combinaison utile
pour décrire des algorithmes*.

## Les trois combinaisons de base

Faisons un point d'étape. Les algorithmes permettent de
définir des traitements à partir de traitements de base et trois modes
de combinaison à savoir la *séquence* qui fait passer à l'instruction
suivante, l'*alternative* qui permet de choisir les instructions à
exécuter selon la valeur d'un test et la *répétition* qui répète des
instructions tant qu'un test est satisfait. La machine qui
peut exécuter les traitements ainsi définis grace à une unité de
calcul, de la mémoire et une unité de contrôle. 

Notre exemple nous a permis d'expliquer comment construire une
nouvelle fonctionnalité à en combinant des opérations simples. Mais,
une grande force de ces combinaisons, et donc des algorithmes, est
qu'elles peuvent s'appliquer sur des instructions plus évoluées. Nous
pourrions, par exemple, réutiliser l'algorithme de transformation des
majuscules dans un nouvel algorithme. Et c'est un vrai jeu de
construction ! À la manière des Legos où, partant de briques de bases,
on construit par assemblages successifs des maisons puis des villes,
on se trouve devant un univers infini de possibilités où toute votre
créativité peut s'exprimer. En informatique, au fur et à mesure des
constructions algorithmiques, les traitements deviennent de plus en
plus sophistiqués.  Par exemple, dans le cas de notre application
d'assistance routière, on compose en séquence la reconnaissance vocale
des directions, le calcul d'itinéraire et son affichage. L'alternative
permet, si le lieu d'arrivée n'est pas connu ou est imprécis,
d'afficher un message plutôt que l'itinéraire. L'itération permet de
poursuivre l'exécution de l'assistant tant que vous n'êtes pas arrivé.

## Calculer et calculable

Est-ce que ces trois modes de composition que sont la séquence,
l'alternative et l'itérative sont suffisants ? Oui car il existe un
**théorème** qui affirme que tout ce qui est calculable avec une
machine peut être défini par quelques opérations élémentaires et ces
trois opérations de composition. Ce théorème a été démontré au milieu
du vingtième siècle par des mathématiciens et des logiciens.

Ceci soulève immédiatement la question : *une machine peut-elle tout
calculer ?* La réponse, démontrée à la même époque, est négative : il
existe des problèmes que ne peut pas résoudre une machine. Par
exemple, il est démontré qu'*il n'existe pas d'algorithme* qui est
capable de dire si une suite d'instructions contenant des alternatives
et des itératives va s'arrêter lorsqu'on l'exécutera. Ces sujets
soulèvent des problèmes importants étudiés par les mathématiciens, les
informaticiens, les logiciens et les philosophes autour des notions de
calcul et d'intelligence.

Mais, savoir qu'un problème est calculable ne suffit pas. En effet, il
faut alors proposer des représentations des données du problème et des
algorithmes pour le résoudre. Et, comme nous l'avons signalé dans
notre exemple de calcul d'itinéraire, il faut que la mémoire
nécessaire pour représenter les données soit dans les limites des
capacités des machines car leur mémoire n'est pas infinie. Il faut
également que le temps de calcul de l'algorithme soit raisonnable et
adapté au problème : de moins d'une seconde de temps de réponse pour
une application interactive à quelques heures pour une application
scientifique complexe comme la prédiction météorologique. Ces deux
questions posent des challenges scientifiques majeurs aux chercheurs
pour déterminer les problèmes qui sont *calculables en un temps
raisonnable*. Pour ces problèmes, on étudie alors la *complexité des
algorithmes* pour trouver les algorithmes les plus efficaces en temps
de calcul et en mémoire

```activité
::Les minuscules en majuscules::
[markdown]
On souhaite apprendre à la machine à faire la transformation inverse, à savoir transformer les minuscules en majuscules.
- Pour transformer un caractère minuscule en majuscule, quelle instruction faut-il changer dans l'algorithme présenté ci-avant ?
- Pensez-vous qu'on puisse apprendre à une machine à faire cette nouvelle instruction ?
- Expliquez ce qu'il faut changer  pour obtenir un algorithme qui prend en entrée une séquence de caractères et qui transforme les minuscules en majuscules et laisse tous les autres caractères inchangés ?
{#### retirer 32 au code au
lieu d'ajouter 32 ; oui, on doit pouvoir apprendre à notre machine à
faire une soustraction de deux entiers même si cela semble un petit
peu plus compliqué que l'addition ; tester si le code du caractère est entre 97 et 123 et appeler le programme qui transforme minuscule en majuscule.}
```


```activité
::La répétition par Mark Zuckerberg (Facebook)::
dans Hour of Code : https://www.youtube.com/watch?v=mgooqyWMTxk  {}

::Autres formes de répétition::
Nous avons vu la répétition de la forme tant que. Comme vous l'avez entendu dans la présentation précédente, une autre forme de répétition est le pour. Donnez deux algos simples avec pour et tant que et montrer qu'ils font la même chose {}

::Faut-il apprendre à coder ?::
L'avis d'un président des Etats-Unis : https://www.youtube.com/watch?v=6XvmhE1J9PY {}

::Apprendre les bases de l'algorithmique::
Parmi les nombreux sites disponibles, pourquoi pas "Hour of Code" : https://code.org/learn

::Algorithme et programme::
en une minute par Gérard Berry : https://www.youtube.com/watch?v=u9XEsJypSdc {}
```

```compréhension
::Conception des algorithmes::
[markdown]
- Pour résoudre un problème il existe un seul algorithme{F}
- Pour résoudre un problème il existe des algorithmes plus efficaces que d'autres{T}
- Tout problème peut être résolu par un algorithme{F}
```


# Algorithmes, programmes et applications

## Machines, algorithmes et langages

Rappelons que machines, langages et algorithmes sont intimement liés
et comprendre l'une de ces notions ne peut se faire indépendamment des
autres. Nous avons introduit les algorithmes sur une machine de base
très simple travaillant avec des opérations élémentaires, des
mémoires, une unité de calcul et un langage de codage des
caractères. Nous avons signalé que l'informatique s'apparentait à un
grand jeu de construction. Celui-ci s'applique à la fois pour les
données et pour les programmes grace à des langages informatiques.

En effet, si la machine de base travaille avec des 0 et des 1, les
*langages de description* permettent de décrire, dans ce jeu de
construction, avec un niveau d'abstraction toujours croissant, les
caractères et les nombres, les images, les textes et les tableaux de
nombres, les documents structurés, les documents multimedia. Par
exemple, le navigateur manipule des documents `html`, des images, des
videos.

Le jeu de construction porte donc sur les objets manipulés mais aussi
sur les algorithmes et les programmes. En effet, à partir d'opérations
de base sur ces objets complexes, on va pouvoir les composer dans des
algorithmes avec les trois compositions de base. Mais, si un
algorithme est conçu et lu par des humains, il doit ensuite être
traduit pour pouvoir être exécuté par une machine. Pour cela, il faut
traduire l'algorithme dans un langage compréhensible par la
machine. Il faut donc disposer d'un langage commun entre l'humain et
la machine avec la contrainte forte d'être compréhensible par les
humains tout en étant suffisamment formel et précis pour ne pas
laisser d'ambiguïté à la machine. C'est le rôle des langages
informatiques pour les traitements.

Il existe, en réalité, de nombreux langages dépendant du mode
d'interaction entre l'humain et la machine. Vous pouvez, par exemple,
interagir avec une application par un langage graphique à base de
menus ou par des clics de souris ou par l'action de frapper sur des
touches de clavier. Pour apprendre à vous servir d'une application,
vous allez apprendre ce langage : quelle est l'action réalisée par le
choix de cet élément de menu, quelle est l'effet d'un clic de souris
sur cet élément, quel est l'effet de l'appui sur cette combinaison de
touches. Mais, il est difficile d'automatiser ces actions dans des
programmes. On préfère alors utiliser un langage écrit.  Lorsqu'il
s'agit de traduire un algorithme, c'est-à-dire expliquer à la machine
une combinaison d'instructions, on utilise des langages écrits appelés
*langages de programmation*. Il en existe de nombreux, le choix va
dépendre des fonctionnalités de base du langage, des besoins de
l'application, des performances souhaitées, ... Les textes écrits dans
ces langages sont des *programmes* qui sont la traduction
d'algorithmes dans le langage choisi. Ces langages et les programmes
se doivent d'être compréhensibles par l'informaticien(ne) mais comme
ils sont destinés à être exécutés par la machine, ils respectent des
règles très strictes de syntaxe. Ceci explique qu'une machine va
refuser une commande mal écrite alors qu'un humain acceptera une
phrase mal formée dès qu'il en comprend le sens. Cette rigueur
nécessaire et la difficulté d'apprendre un langage de programmation
effraient beaucoup de monde. 

```activité
::Algorithmes et programmes::
[markdown]
**Algorithmes et programmes**
Un algo qui affiche 5 fois "Hello World" traduit dans différents langages
```

## Coder ou programmer

Ces deux termes désignent l'activité de *concevoir des algorithmes et
des programmes*. Si cette activité est principalement le fait des
informaticiens, il est important de connaître les notions essentielles
de la programmation pour être un acteur du monde numérique (voir, par
exemple, le discours, donné en activité, d'un récent président des
Etats Unis).

Nous supposons disposer d'une machine avec des fonctionnalités de
base. Cela peut être une machine très proche du matériel sachant faire
des opérations sur des 0 et des 1 ; cela peut être une machine qui
sait manipuler des nombres, des caractères et des textes ; cela peut
être un robot qui sait avancer, tourner et repérer des obstacles ;
cela peut être un logiciel de dessin vectoriel qui sait se repérer sur
une grille, tracer des segments, des cercles, des courbes et colorier
; cela peut être un tableur qui sait traiter des listes de données ;
cela peut être un navigateur qui sait gérer des documents du Web. On
suppose disposer d'un langage de programmation qui connaît ces
fonctionnalités de base et qui dispose d'instructions pour la
séquence, l'alternative et la répétition.

On souhaite ajouter une nouvelle fonctionnalité. Il faut donc la coder
(ou la programmer) ce qui va se faire en deux étapes : concevoir un
algorithme puis écrire le programme correspondant. Nous allons décrire
deux principes de conception en rappelant qu'on conçoit d'abord des
algorithmes avant de traduire les algorithmes dans le langage
choisi. Il est important de remarquer que le plus difficile est de
concevoir un bon algorithme alors que programmer n'est que traduire
cet algorithme dans le langage choisi.

La démarche la plus souvent utilisée est celle de la **conception
descendante** qui consiste à décomposer le problème en des problèmes
de plus en plus simples. Notons que c'est une démarche courante. En
effet, si je dois me rendre de mon domicile à Lille à l'hôtel Arosfat
à Londres par le train, je vais décomposer le problème en problèmes
plus simples : aller de mon domicile à la gare TGV, prendre le TGV,
aller de la gare St Pancras à l'hôtel. On peut alors continuer le
processus de décomposition. Par exemple, aller de la gare St Pancras à
l'hôtel peut se décomposer en : se rendre au terminus des navettes, si
une navette est disponible rapidement, prendre la navette, sinon se
rendre au métro, ... On arrête la décomposition lorsque tous les
sous-problèmes introduits correspondent à des fonctionnalités de base
de notre langage. On peut alors expliciter un algorithme (ou des
algorithmes) pour définir la fonctionnalité attendue puis les traduire
dans des programmes.

On observe que les environnements de programmation sont de plus en
plus riches et disposent de très nombreuses fonctionnalités parfois
rangées dans des bibliothèques. C'est le principe de la **conception
ascendante** de créer de nouvelles fonctionnalités qui peuvent, à
leur tour, être considérées commes des fonctionnalités de base ce qui
permet de recommencer le processus pour créer de nouvelles
fonctionnalités encore plus riches. On peut comprendre les machines
actuelles, qui disposent de très nombreuses applications, comme
construites selon ce principe en partant de fonctionnalités de base
avec un empilement de couches applicatives de plus en plus
riches. Par conséquent, aujourd'hui, la plupart des besoins,
personnels ou professionnels, des utilisateurs sont couverts par une
ou plusieurs applications.

Ceci fait dire à certains qu'il est inutile de savoir coder ou
programmer. Nous pensons, a contrario, que bien comprendre les notions
de base sur les algorithmes et les programmes permet de bien
comprendre le fonctionnement des machines et des applications. Et même
de faire preuve de créativité, car nous pouvons définir de nouvelles
fonctionnalités si nous savons programmer. Par exemple, la
*programmation créative* vous permet de définir de nouvelles formes
d'expressions artistiques sonores ou visuelles.

```activité
::Langages de programmation::
[markdown]
Il existe de nombreux langages de programmation. En voici quelques exemples

* pour apprendre en s'amusant : lien sur scratch
* pour la conception artistique : lien vers processing
* pour le Web : lien vers javascript
```


```compréhension
::Algorithmique et programmation::
[markdown]
Le plus difficile est-il de concevoir l'algorithme ou de traduire l'algorithme en programme ? {####concevoir algo}
```

## Les applications

Une application est constituée d'un ensemble de programmes qui
interagissent. Un programme est la traduction dans un langage
compréhensible par la machine d'algorithmes très précis. Ceci explique
que l'application fonctionne correctement pour des situations prévues
à l'avance. Par contre, une application peut s'arrêter, avoir un
comportement inattendu ou calculer un mauvais résultat dès qu'elle
rencontrera des conditions imprévues.

Le jeu de construction informatique fait que les applications
actuelles ont des fonctionnalités très riches et manipulent des
données de toute nature. Les solutions étant diverses et les acteurs
du monde numérique très nombreux, nous disposons d'un nombre
impressionnant d'applications disponibles dans le monde numérique :
pour communiquer, pour chercher de l'information, pour écouter de la
musique, pour regarder des vidéos, pour composer de la musique, pour
dessiner, pour composer des textes ou des pages Web, pour faire des
statistiques, etc

Pour un même besoin, plusieurs applications sont souvent
disponibles. Comme utilisateur, dans votre vie personnelle, vous êtes
amenés à choisir une application pour votre ordinateur ou téléphone
portable. Dans votre vie professionnelle, vous serez amenés à choisir
ou à participer au choix d'une application. Ce peut être, par exemple,
le choix d'un logiciel de production de documents écrits, le choix
d'un logiciel de dessin, le choix d'un logiciel de conception de sites
Web, le choix d'un langage de programmation, ... Nous présentons
quelques critères principaux participant au choix d'une
application répondant à un besoin applicatif :

* **contraintes techniques :** environnement matériel et
  logiciel 
* **critères d'usage :** compétences des utilisateurs
* **fonctionnalités :** correspondance entre les besoins et les
  possibilités du logiciel. 
* **type de logiciel :** nature de la licence, support, maintenance, évolutivité
* **prix :**

Cette liste de critères ne prétend pas être exhaustive. Les critères
ne sont pas indépendants et le choix correspondra en la recherche du
meilleur compromis entre les besoins et les possibilités fournies par
l'application.

# Exemples de programmes

Dans cette section, nous présentons le fonctionnement de trois
programmes. Pour chacun d'eux, un premier objectif est de vous faire
comprendre les algorithmes qui sont derrière ces applications, de vous
montrer que cette compréhension vous permet de savoir ce que vous
pouvez attendre de l'application, c'est-à-dire comprendre ce qu'elle
peut faire et ne peut pas faire. Un second objectif est de vous
montrer les choix du concepteur de l'application et leur influence sur
les possibilités de traitements et leur efficacité. Le dernier exemple
introduit, par l'exemple d'un jeu, un algorithme plus sophistiqué issu
du domaine de l'intelligence artificielle.

## Un correcteur orthographique en français

Certains traitements de texte incluent une fonctionnalité de
correction orthographique. Dans sa forme la plus simple, le correcteur
vérifie que tout mot du texte est une forme correcte d'un mot de la
langue française. Pour décrire cet algorithme, nous allons commencer
par préciser nos hypothèses sur le langage et la machine. La première
hypothèse porte sur le choix de représentation du texte. Nous allons
considérer ici que le texte est une suite de mots. Sachant que le
texte est une suite de 0 et de 1 représentant des nombres qui sont les
codes des caractères constitutifs du texte, cette hypothèse suppose
que des algorithmes sont capables d'identifier des mots à partir de
cette suite. Notez que ces algorithmes sont complexes car un mot ne se
définit pas simplement comme une suite de lettres délimitées par des
symboles qui ne sont pas des lettres (pensez à des mots comme aujourd'hui ou
grand-père). La seconde hypothèse est que nous disposons d'un certain
nombre d'instructions de base comme : lire le premier mot, lire le mot
suivant, repérer la fin du texte, mémoriser un mot, tester si deux
mots sont égaux et souligner un mot.

Avec ces hypothèses, un algorithme de correction orthographique va
pouvoir parcourir chaque mot du texte. Mais pour vérifier
l'orthographe, il est également indispensable de posséder un
dictionnaire des mots corrects. C'est, pour le Français, une ressource
constituée d'une liste de tous les mots français avec leurs formes
conjuguées et accordées. Elle peut aussi inclure des noms propres, des
abréviations, des sigles, ... Avec cette ressource à disposition, nous
pouvons proposer l'algorithme suivant :

`Correcteur orthographique`

     1. **en entrée** : un texte
     2. lire le premier mot et le mémoriser comme mot courant
     3. **tant que** ce n'est pas la fin du texte
     4.   chercher le mot courant dans le dictionnaire
     5.   **si** il n'existe pas **alors**
     6.     souligner le mot courant
     7.   **fin du si**
     8.   lire le mot suivant et le mémoriser comme mot courant
     9. **fin du tant que**
    10. **en sortie** : le texte avec des mots soulignés qui
                        sont considérés comme mal orthographiés


L'instruction *chercher le mot courant dans le dictionnaire* ne fait
pas partie de nos instructions de base. Il est donc nécessaire
d'expliquer à notre machine comment réaliser cette opération. On
suppose qu'on dispose d'instructions élémentaires pour lire le premier
mot du dictionnaire, lire le mot suivant et repérer la fin du
dictionnaire. Nous pouvons alors proposer un algorithme qui recherche
le mot à chercher en parcourant le dictionnaire un mot après
l'autre. Si le mot est dans le dictionnaire, l'algorithme renvoie une
valeur vraie ou fausse selon que le mot à chercher est dans le
dictionnaire ou pas. Ce qui donne l'algorithme naïf suivant :

     1. **En entrée**  : un mot à chercher
     2. lire le premier mot du dictionnaire et le mémoriser comme mot courant
     3. **tant que** le mot courant n'est pas le mot cherché et qu'on n'a pas atteint la fin du dictionnaire
     4.   lire le mot suivant du dictionnaire et le mémoriser comme mot courant
     5. **fin du tant que**
	 6. **en sortie** : **si** le mot courant est le mot cherché **alors** existe **sinon** n'existe pas

En combinant ces deux algorithmes, nous avons un algorithme de
correction orthographique.  Cet algorithme est-il efficace en temps de
calcul ? Le parcours de tous les mots du texte est obligatoire. Pour
chaque mot du texte, il faut faire une recherche dans le dictionnaire,
ce qui, avec notre algorithme naïf peut amener à parcourir tous les
mots du dictionnaire. Ceci peut amener à un temps de calcul assez long
car un dictionnaire contient de l'ordre de plusieurs centaines de
milliers de mots et il faut le parcourir pour chaque mot du
texte. Peut-on faire mieux ? Oui si vous pensez à la façon dont vous
cherchez dans un dictionnaire qui est rangé dans un ordre
alphabétique. Il existe des algorithmes rapides de recherche dans un
dictionnaire et ces algorithmes sont souvent disponibles dans les
langages de programmation. Vous pourrez en savoir plus en suivant le
module qui introduit les méthodes de recherche d'information.

Cet algorithme met-il en évidence toutes les fautes d'orthographe ?
Il souligne et donc considère comme mal orthographiés tous les mots du
texte qui n'apparaissent pas dans le dictionnaire. Quelles sont les
erreurs possibles de cet algorithme ? Une erreur possible est de
souligner à tort un mot parce que les listes sont incomplètes. Des
listes de mots les plus complètes et les plus actuelles possibles
corrigent ce type d'erreur. Il est par contre incapable de souligner
les fautes d'accord ou de conjugaison comme "la vache bleu" ou "je
montres". La méthode pour réaliser ce type de correction et bien
différente et nécessite d'autres algorithmes.  Une première
possibilité serait de doter le correcteur de la capacité d'analyser
votre phrase pour répondre aux questions telles que : quel est le
sujet du verbe ? Avec qui s'accorde cet adjectif ? Ceci afin de lui
permettre de vérifier des règles grammaticales.  La difficulté est de
réaliser ces analyses car ils nécessitent une grammaire numérisée de
la langue et des programmes d'analyse. Souvent ces règles de grammaire
numérisées sont incomplètes car c'est encore un sujet de recherche
actif en (informatique) linguistique d'être capable d'exprimer toutes
les règles grammaticales et d'analyser correctement toutes les
phrases. Une seconde possibilité serait d'utiliser des méthodes dites
"force brute" qui étendent l'approche par dictionnaire utilisée pour
l'orthographe. Au lieu de mémoriser des listes de mots, le
dictionnaire mémorise des listes de couples de mots, de triplets de
mots voire de phrases complètes. La difficulté, dans ce cas, est
d'avoir des listes exhaustives, de mémoriser ces listes, de les mettre
à jour et de les interroger très rapidement.

Ceci explique que les correcteurs disponibles dans les applications
sont des correcteurs orthographiques simples à base de dictionnaires
de mots. Parfois, ils font des corrections liées à des règles
grammaticales mais il est difficile de savoir exactement quelles
corrections ils sont capables de faire. Par conséquent, **en
pratique**, lorsque vous avez rédigé un texte et souhaitez en vérifier
l'orthographe, vous procéderez de la façon suivante :

1. vous *faites passer un correcteur orthographique*
2. vous corrigez les erreurs repérées par le correcteur
3. vous *vérifiez vous-même l'orthographe* en vous concentrant sur les
*possibles fautes grammaticales restantes*.

## Classer et apprendre à classer des textes

Nous poursuivons avec un second algorithme utilisé en traitement
automatique du langage naturel qui est un domaine à la frontière entre
linguistique et informatique. En effet, les ordinateurs sont,
aujourd'hui, capables, d'identifier dans un grand corpus de textes
ceux dont le sujet porte sur un thème (on parle aussi de catégorie ou
de classe) précis. Il peut s'agir de classer des nouvelles dans des
thèmes pour pouvoir les classer sur un site Web. Il peut s'agir de
diriger automatiquement des mails de réclamation vers le bon service
pour une entreprise. Il peut s'agir d'attribuer des textes à des
auteurs ce qui est une question considérée en stylistique. Il est
intéressant de noter que, si on dispose de corpus de textes de
différents auteurs, on peut apprendre à classer les textes et qu'un
tel programme a des résultats étonnamment bons (du niveau d'un expert
humain) même si, comme nous allons le voir, il ne fait pas une étude
de style mais se base simplement sur des fréquences d'apparition de
mots.

Explorons les idées permettant à un algorithme de classer des textes
en considérant la question de trouver les textes parlant de politique.
 Une méthode naïve, voire idiote, est de dire qu'un texte est dans le
thème "politique" si et seulement si le mot politique s'y trouve. On
pourrait écrire un algorithme comme

     1. **en entrée** : une suite de mots
     2. lire le premier mot et le mémoriser comme mot courant
     3. **tant que** ce n'est pas la fin du texte
     4.   **si** le mot courant est "politique" **alors**
     6.     mémoriser que j'ai vu le mot politique
     7.   **fin du si**
     8.   lire le mot suivant et le mémoriser comme mot courant
     9. **fin du tant que**
    10. **en sortie** : le texte est politique si j'ai mémorisé que j'ai vu
                        le mot politique

Cet algorithme naïf n'est pas satisfaisant car un texte peut être
considéré comme politique sans contenir le mot politique et un texte
contenant le mot politique ne parle pas forcément de politique ! On
peut l'améliorer en constituant un dictionnaire des mots parlant de
politique (droite, gauche, parlement, assemblée, ...)  et s'inspirer
de l'algorithme réalisant la correction orthographique. On peut
poursuivre cette idée sensiblement en constatant que la décision de
l'appartenance à ce thème politique peut dépendre aussi bien de la
présence que de l'absence de certains mots, ou mieux encore de combien
de fois chaque mot est employé. Nous avons l'idée de base qui est que
*l'appartenance d'un texte à un thème va dépendre de la fréquence
d'apparition de certains mots*.

C'est cette idée qui est souvent employée. Pour cela, un dictionnaire
ayant été choisi, on va représenter un texte par le nombre de fois où
chaque mot du dictionnaire apparaît dans le texte. Au vu des
algorithmes vus dans ce module, vous êtes capables de comprendre qu'il
est possible d'écrire un algorithme qui, avec un texte et un
dictionnaire, construit une telle représentation. À partir de cette
représentation, il faut trouver des seuils en dessous ou au delà
desquels on dira que le mot parle d'un thème précis. Par exemple, un
texte parle de politique si le mot politique apparaît au moins une
fois, le mot gauche au moins deux fois, le mot droite au moins deux
fois et le mot chat n'apparaît pas. Mais, comment trouver ces seuils ?

C'est ici qu'interviennent des développements récents autour de
l'apprentissage artificiel ("Machine Learning") amplifiés par le
phénomène des masses de données ("Big Data"). En effet, on dispose
désormais de grands corpus de textes. Les textes peuvent être annotés
par des experts comme parlant d'un thème. Avec ces corpus de textes,
on peut représenter chacun d'eux par les fréquences des mots. On peut
alors écrire un programme qui apprenne quels sont les seuils pour
chacun des thèmes et, avec ces seuils, on peut maintenant classer un
nouveau texte dans un thème. Les détails d'un tel algorithme
d'apprentissage (ou de fouille de textes) sortent du contenu de ce
cours. Nous espérons cependant vous avoir fait comprendre comment une
machine pouvait classer des textes avec des résultats souvent
comparables à celles d'un expert humain.

## Un jeu d'échec sur ordinateur

Le jeu d'échecs est un jeu ancien datant du 10ème siècle
environ. C'est un jeu de plateau, c'est-à-dire un jeu qui se joue avec
des pièces positionnées sur un plateau découpé en cases. Le plateau du
jeu d'échecs est un plateau de 64 cases de forme carrée avec des cases
blanches et des cases noires. C'est un jeu à deux joueurs. Chacun des
joueurs dispose de 16 pièces de différente nature : les pions, les
tours, ..., le roi et la reine. Chacune des pièces a des possibilités
de déplacement et des possibilités de prise de pièce adverse. Le jeu
est défini par un ensemble de règles très précises pour les
déplacements, les prises, le calcul du gagnant.

Nous nous intéressons à la question de faire jouer un ordinateur au
jeu d'échecs. La réalisation d'un programme de jeu capable de gagner
contre les humains a été un sujet important de l'intelligence
artificielle sur toute la seconde moitié du 20ème siècle. Il a fallu
plus d'un demi-siècle pour qu'un ordinateur puisse gagner contre le meilleur
joueur humain, en l'occurence le programme "Deep Blue" qui gagne
contre Kasparov en `1997`. Désormais, des programmes, qui peuvent être
exécutés sur un ordinateur personnel, sont plus forts que tout expert
humain. Nous allons expliquer les principes algorithmiques qui font
"l'intelligence" de ces programmes.

Nous laissons complètement de côté toutes les questions liées au
graphisme, aux interactions entre le joueur humain et le
programme. Nous supposons que le programme dispose d'une
représentation numérique du plateau et des pièces, qu'il existe des
programmes permettant de vérifier qu'un déplacement est autorisé,
permettant de calculer, pour un état du jeu, tous les déplacements
possibles du joueur qui doit jouer, permettant de voir si la partie
est finie et de déclarer le match nul ou le gagnant. Nous nous
intéressons donc simplement à la question suivante (la plus
difficile) : la partie étant dans un certain état après plusieurs
coups de chacun des deux joueurs, *comment le programme peut-il choisir
le meilleur coup à jouer ?*

Si vous avez déja joué à un jeu de plateau, vous raisonnez très
certainement de la façon suivante : quels sont les coups possibles ?
Pour chacun d'eux, voir leur effet, réfléchir à la réponse potentielle
de mon adversaire, de penser à ce que je pourrais jouer ensuite,
... Après avoir examiné un certain nombre de coups possibles, je fais
un choix. Un algorithme va avoir une approche similaire mais très
systématique. Il va considérer tous les coups possibles de sa part,
tous les coups possibles de l'adversaire, tous les coups possibles de
sa part en réponse, ... On peut ainsi construire une structure,
appelée arbre en informatique, qui possède une racine pour l'état
courant du jeu, des fils pour les états du jeu pour chaque coup
possible, etc. Une première idée est alors de construire cet arbre de
toutes les suites possibles du jeu à partir de l'état courant, puis de
calculer le coup qui va me mener à la victoire quoi que fasse
l'adversaire. 

Le problème est-il résolu ? Malheureusement non ! Nous avons signalé,
dans l'introduction de ce module, la notion d'être calculable par une
machine. Mais il ne suffit pas qu'un problème soit calculable. Il faut
qu'il le soit avec une mémoire et un temps de calcul raisonnables. Sur
notre exemple, imaginez qu'il y ait environ 10 coups possibles et
qu'on souhaite regarder les états possible pour 10 tours de jeu, soit
pour 20 coups. Il y aurait 10 puissance 20 états possibles, soit
encore 1 suivi de 20 zéros, soit encore 100 milliards de milliards
d'états possibles. Il est **impossible** à toute machine de mémoriser
ces états ou de faire des calculs sur tous ces états. C'est ici qu'il
faut donc être "intelligent" pour notre programme.

Vu que le programme ne peut pas explorer le jeu pour voir si un coup
mène sur une position gagnante, nous allons doter le programme d'une
fonction d'évaluation d'un état du jeu. Dans sa forme la plus simple,
une valeur est attribuée à chacune des pièces et l'évaluation d'un
état du jeu consiste à sommer la valeur des pièces dont le joueur
dispose dans cet état. Cette fonction peut être améliorée par des
bonus ou malus dépendant de la position de la pièce. Par exemple, on
va bonifier un pion qui est près du camp adverse car il peut se
transformer en reine, on va pénaliser un pion isolé car il peut être
pris facilement. Nous supposons qu'une fonction d'évaluation a été
choisie.

Faisons le point. Le jeu est dans un certain état (une configuration
du jeu après plusieurs coups), le programme doit choisir un meilleur
coup à jouer. La succession des coups que chacun des joueurs peut
jouer définit un arbre de tous les états possibles. Nous savons qu'il
est impossible d'explorer cet arbre complètement. L'idée de base de
l'algorithme est de l'explorer incomplètement mais
intelligemment. Pour cela, on utilise la fonction d'évaluation pour
attribuer un score à un état de l'arbre. En effet, on va explorer
l'arbre en éliminant complètement des sous-arbres lorsqu'on estime que
les scores dans ce sous-arbre ne seront pas assez bons.  C'est un peu
ce qu'un joueur humain fait : si je joue ce coup, je perd ma reine et,
sauf cas particulier, ce coup n'est pas intéressant donc je ne vais
pas explorer plus loin ce qui peut se passer. C'est ce principe qui a
été formalisé bien plus précisémment en utilisant les scores sous
forme d'un algorithme célèbre appelé *algorithme alpha-beta*.

Vous connaissez maintenant les principes du fonctionnement de
l'algorithme. Pour avoir un algorithme performant on examinera le plus
grand nombre d'états possibles dans l'arbre simplifié grace à la
méthode alpha-beta. Pour avoir un algorithme très performant, on
ajoute d'autres éléments comme, par exemple, une bibliothèque des
débuts de partie. C'est-à-dire que le programme pourra mimer des
débuts de partie classiques des meilleurs joueurs qui sont connues sur
quelques coups en début de partie. Mais avoir le jeu le plus fort ne
sera pas le seul critère car un joueur standard n'a pas le niveau du
champion du monde et ne prendra pas plaisir à perdre toutes les
parties qu'il joue ! Avoir un jeu qui s'adapte à l'utilisateur est une
question importante qui est toujours étudiée par les concepteurs de
jeux.

Il est difficile de ne pas parler du jeu de Go qui défraie la
chronique au moment de la rédaction de ce cours en 2016. En effet,
pour la première fois, un programme a gagné contre le champion du
monde humain du Go. On croyait le Go hors de portée des machines car
le nombre de configurations possibles est encore plus gigantesque que
pour les échecs et les stratégies des joueurs humains utilisent une
vue spatiale de l'état du jeu. Le programme de Go n'utilise pas les
stratégies développées par les humains mais utilise des techniques
d'apprentissage automatique ("machine learning" en anglais) avec un
programme de jeu qui s'améliore avec l'expérience, c'est-à-dire qu'il
"apprend" à partir de parties jouées (contre un humain ou contre
lui-même). Un petit cocorico Lillois (les rédacteurs de ce cours sont
Lillois) car c'est notre collègue Rémi Coulom qui a initié ces
recherches sur le Go avec un programme champion du monde dans les
années 2010, battant même des experts humains mais avec handicap.

```compréhension
::Représenter et manipuler::
[markdown]
**Représenter et manipuler**
Les traitements possibles dépendent fortement des choix de représentation
{T}
```
# Conclusion

Nous avons étudié les principes des applications informatiques et de
leur construction comme un vaste jeu de construction avec des données
complexes construites à partir de données de base et des programmes
construits avec des algorithmes qui peuvent être composés et
recomposés.  Nous avons présenté des exemples d'application comme la
recherche d'itinéraire, la correction orthographique, le classement de
textes et le jeu de Go. Ces exemples montrent comment une machine
simple peut grace à sa puissance de calcul et à l'inventivité des
humains se transformer en une machine capable de résoudre des tâches
de haut niveau. Ils montrent également que l'intelligence supposée des
machines est obtenue par la capacité de traiter de grands jeux de
données comme des grands corpus de textes ou des corpus de parties de
Go. Ceci ouvre des perspectives nouvelles avec le phénomène "Big
Data". Posséder les données est désormais un enjeu essentiel et les
grandes entreprises du Web l'ont bien compris car ces données leur
permettent de développer des applications de prédiction : prédire vos
goûts musicaux, prédire vos achats et recommander des produits en
conséquence, suggérer des informations à lire, ... Ce qui amène des
questions éthiques sur la possession des données souvent personnelles
et l'utilisateur, trop souvent consentant, doit désormais se poser la
question de la communication de ses données personnelles.

# Données et objets (optionnel)

Nous avons introduit des notions d'algorithmique et de conception
d'applications mais ceux-ci doivent manipuler des données. Il faut donc
également considérer les données manipulées et les choix de
représentation de ces données. En effet, si nous avons signalé les
contraintes d'efficacité, nous ne les avons pas prises en
compte. L'efficacité d'un programme est lié au choix de l'algorithme
mais aussi au choix de la représentation des données. Nos applications
doivent traiter des objets divers comme des nombres et des chaînes de
caractères mais aussi des documents, des images, des tableaux,
... Nous allons, dans cette section, étudier comment sont définies des
données complexes à partir de données élémentaires et voir que les
choix d'organisation peuvent être nombreux et influent sur les
performances d'une application. Avant cela, une parenthèse sur la
façon dont on mémorise les données dans les applications avec la
notion de **variable informatique**.

Les applications manipulent des caractères, des nombres, des listes,
des documents, des images. Ces objets doivent pouvoir être mémorisés
dans la mémoire de la machine et on doit pouvoir les retrouver au
besoin. La gestion de la mémoire étant complexe, on utilise un
mécanisme de **nommage avec des variables**. Supposons que
l'application ait besoin de manipuler un caractère, on peut utiliser
une variable `caracourant` dans laquelle on va pouvoir mémoriser un
caractère et avec laquelle je pourrais retrouver le caractère
mémorisé. On peut, de même, utiliser une variable `note` pour un
nombre entre 0 et 20, ou encore une variable `montexte` pour une suite
de caractères. On peut aussi considérer une variable `listenotes` pour
gérer une liste de notes. Le principe est que, lorsqu'une variable est
définie, la machine range la valeur (qui peut être complexe) à une
adresse dans la mémoire et que la machine saura retrouver la valeur
car elle mémorise l'association entre le nom de la variable et
l'adresse mémoire. Illustrons ceci sur un exemple de programme simple

`TRAIT2NOTES`

1. `nbnotes` <- 2
2. saisir une note au clavier et ranger la valeur dans `note1`
3. saisir une note au clavier et ranger la valeur dans `note2`
4. afficher le message "la plus petite note est : ", afficher le
   résultat du calcul `MIN(note1,note2)`
5. afficher le message "la moyenne est : ", afficher le résultat du
   calcul `(note1 + note2)/nbnotes`

La première instruction est une *affectation* : on range la valeur 2
dans la variable `nbnotes`. Les instructions 2 et 3 sont une
affectation à partir d'une interaction avec l'utilisateur du programme
qui choisit une première valeur rangée dans `note1` puis une seconde
valeur rangée dans `note1`. L'instruction 4 correspond à l'affichage
d'un message et du résultat du calcul du minimum des 2 valeurs qui
viennent d'être rangées dans `note1` et `note2`. Les variables
permettent donc de désigner des objets par un nom pour ranger et
retrouver des valeurs sans que l'utilisateur ait à gérer la complexité
des accès à la mémoire de la machine. Il faut noter que le concepteur
du programme utilise des variables pour expliquer à la machine ce
qu'elle doit faire. Par contre, l'utilisateur ne voit pas les
variables. Par exemple, l'utilisateur de notre programme saisit une
première valeur, par exemple 12, puis une seconde valeur, par exemple
14, et tout ce qu'il verra sont les résultats produits, soit sur notre
exemple, "la plus petite note est : 12", "la moyenne est : 13"

## Types de données élémentaires

Nous avons auparavant introduit que nous pouvions étendre les
capacités de notre machine. En particulier, nous avons vu qu'à partir
de simples 0 et 1, on pouvait définir des nombres entiers et on
pouvait définir des caractères en utilisant des codages adéquats. Ceci
peut être généralisé et nous allons étudier les données élémentaires
que peut utiliser une machine.

On peut utiliser des **nombres ou valeurs
numériques**. Les choix sont divers et diffèrent selon les
environnements. On distingue souvent les nombres entiers avec le type
`entier` ou `integer`. Ils peuvent être codés sur 1, 2, 4, ou un
nombre quelconque d'octets ce qui permet de représenter des ensembles
plus ou moins grands d'entiers. Par exemple, sur 1 octet on peut coder
256 valeurs soit les entiers de 0 à 255 si on se limite à utiliser des
entiers positifs, soit les entiers de -128 à +127 sinon. Sur 2 octets,
on peut coder 65 536 entiers. Pour les nombres avec une partie
décimale, on définit le type `décimal` ou `réel`. On peut ici encore
avoir des codages plus ou moins longs qui donnent une précision plus
ou moins importante. Pour des calculs scientifiques ou des calculs
financiers, on utilise des nombres avec une très grande précision. Que
ce soit pour les entiers ou les réels, on dispose de beaucoup de
fonctions permettant de mettre en oeuvre de nombreux calculs.

Ensuite, il existe un type pour manipuler les valeurs de vérité que sont
`VRAI` et `FAUX`, c'est le type **Booléen** ou **Boolean**. Il est
très utilisé en informatique car il correspond aux valeurs que peut
prendre une condition et ces conditions sont utilisées dans
l'alternative (le si alors sinon) et l'itérative (le tant que). On
dispose d'opérations comme le `NON`, le `ET` et le `OU`. On notera que
le `OU` logique est dit inclusif, c'est à dire qu'il vaut `VRAI` si l'un
des deux ou les deux valent `VRAI`. Par exemple, `être-grand OU
être-blond` vaut `VRAI` si je suis grand ou blond ou un grand
blond. Dans la langue française, on utilise le ou comme conjonction de
coordination avec un sens qui peut être inclusif ou exclusif selon les
expressions. Les valeurs de vérité et la logique sont utiles également
pour modéliser le raisonnement comme en intelligence artificielle mais
nous en parlerons dans un autre cours.

## Types de données structurés

On peut assembler des données élémentaires pour construire des données
structurées. Par exemple, on peut construire des tableaux de
nombres. Un tableau de nombres à une dimension contient des nombres et
on peut accéder à chaque nombre du tableau par son indice. On aura le
premier nombre du tableau, le second, le dernier, ... Un tableau à
deux dimensions sera organisé en lignes et en colonnes, il y aura deux
indices et on pourra accéder au nombre situé en ligne `i` et en
colonne `j` du tableau. Ces structures de données sont très utiles dès
que l'on fait des calculs qu'ils soient scientifiques, économiques ou
financiers. Il existe bien d'autres structures de données qui se
distinguent les une des autres par la façon d'organiser les données,
de pouvoir accéder aux données, de pouvoir les parcourir. Chacune des
structures peut être mieux adaptée qu'une autre en fonction des
besoins et des performances attendues. Plutôt que de parcourir toutes
ces structures, nous allons considérer les documents textuels et voir
l'importance de la structure pour les traitements à réaliser.

Un document peut être représenté par une **chaîne de caractères**. En
règle générale, une chaîne de caractères est une suite de caractères
indicée de 1 à un indice qui est la longueur de la chaîne (parfois on
commence à compter à 0) ce qui permet de parler du premier caractère,
du second caractère, du dernier caractère. Nous avons vu dans une
précédente section comment on pouvait définir des fonctionnalités sur
les chaînes de caractères. On dispose souvent d'un grand nombre de
fonctions comme transformer en majuscules, extraire les premiers
caractères, compter le nombre d'apparitions d'un caractère, parcourir
tous les caractères. Cette représentation correspond à une *structure
séquentielle* dont nous allons voir les possibilités.

Considérons une application comme un éditeur de textes ou un
traitement de textes déja considérée dans le cours sur les
documents. Regardons comment peut-on chercher un mot dans un
texte. Par exemple, cherchons le mot `taille` dans le texte du cours
de la section 3 du cours sur les traitements. Un programme de
recherche va, en gnéral, fonctionner comme suit : il prend une fenêtre
de longueur 6 (le mot cherché est de longueur 6) se positionne sur le
premier caractère du texte, teste si la fenêtre contient le mot
`taille`, si oui il positionne un curseur ou met en couleur le mot
trouvé, si non il passe à la deuxième position et recommence jusqu'à
avoir trouvé le mot ou être arrivé à la fin du document. C'est un
*traitement séquentiel* et le programme doit parcourir tout le
document. Peut-on faire mieux ? Nous verrons une réponse positive à
cette question dans le cours sur la recherche d'information.

Considérons maintenant le cas où le document possède une
structure. C'est, par exemple, le cas pour un document `html` qui est
un document textuel avec une structure définie à l'aide de
balises. Une application, comme le navigateur, peut alors représenter
le document avec une *structure arborescente* : la racine du document
qui contient une entête ("head") et un corps ("body"), le corps
contient un titre et des sections, les sections peuvent contenir des
sections contenant des paragraphes et des listes. Quel avantage
apporte cette structure en forme d'arbre ? Par exemple, l'application
peut accéder directement au titre sans parcourir le document,
l'application peut numéroter facilement les sections ou construire une
table de navigation sans parcourir tout le document. Le navigateur
peut appliquer les styles en fonction de cette structure : il applique
le style de la page (fond, marges, retraits), puis les styles de
section, puis les styles des titres de section, ... Qu'en est-il de
notre programme de recherche d'un mot dans la page Web ? On utilise le
même programme que précédemment pour les contenus textuels aux
feuilles de l'arbre. La structure arborescente facilite et accélère
les traitements pour le navigateur. La conscience de cette structure
pour un utilisateur permet de bien comprendre ce qu'est une page Web
et permet de définir des styles appropriés si vous êtes amenés à
modifier l'apparence de pages Web.

## Les objets

La définition d'*objet* est issue du monde réel dans lequel nous avons
une définition plus ou moins précise d'un objet du monde réel. Une
voiture possède des propriétés comme avoir 4 roues (souvent), une
couleur, une marque, un identifiant (le numéro d'immatriculation),
..., peut réaliser des actions comme démarrer, rouler, freiner, et
interagit avec d'autres objets comme rouler sur une route, suivre une
autre voiture, réagit à l'action du chauffeur sur le volant, ... Les
objets au sens informatique sont des abstractions des objets du monde
réel mais aussi de tout concept qu'on doit manipuler de façon
informatique comme un client ou même un sentiment.

Cette abstraction va correspondre à la notion de *classe* qui va définir
les *propriétés* ou attributs que peut prendre un objet, les *méthodes*
qui sont les actions possibles et les relations possibles avec
d'autres classes. Un objet ou instance est une réalisation
particulière de la classe. On définit la classe des voitures et on
considérera, par exemple, l'objet voiture de couleur rouge, de marque
peugeot, immatriculée 235HGR34 qui roule à 55km/h sur la
départementale 455.

Les objets interagissent les uns avec les autres par des *échanges de
messages* avec un émetteur, un destinataire et un contenu qui permet de
transmettre une information pour modifier une propriété ou de demander
un traitement. Par exemple, l'objet chauffeur demande à l'objet
voiture de freiner en lui envoyant un message, l'objet voiture peut
alors modifier sa propriété vitesse.

Un autre point conceptuel important à comprendre est la notion
d'*encapsulation*. L'idée est de protéger les données et de cacher le
fonctionnement interne de l'objet. Les attributs et méthodes sont
contenus dans l'objet et seul l'objet pourra modifier les valeurs. Il
le fera en réponse à un message. Par exemple, la vitesse est une
propriété encapsulée, elle ne sera modifiée qu'en réponse à un message
demandant de freiner ou d'accélérer et les valeurs de la propriété
vitesse peuvent être contrôlées. Un autre aspect de l'encapsulation
est de "cacher" comment sont réalisées effectivement les méthodes. Si
vous avez un objet de classe voiture et que vous savez disposer d'une
méthode pour freiner, vous pouvez utiliser cette méthode sans vous
préoccuper de la façon dont est exécuté le freinage.

Une dernière notion utile est de savoir que les classes peuvent
posséder des relations entre elles. On peut avoir une classe étudiant
et une classe personnel qui sont des cas particuliers d'une classe
générale membre université qui elle-même peut être cas particulier
d'une classe personne. Pour ce type de relation, on peut définir une
notion d'*héritage*. Par exemple, la classe étudiant peut hériter de la
classe membre université des propriétés comme accèsENT. Comprendre les
formes diverses de l'héritage et les autres relations entre classes
sort du propos de cette introduction.

La *programmation objet* est un mode de programmation basé sur les
objets. Au premier niveau, on utilise un langage de programmation qui
va contenir des classes d'objets prédéfinies et on écrit des
programmes utilisant ces objets. Au second niveau, on définit de
nouveaux objets avec leurs propriétés et leurs méthodes en vu de
définir une nouvelle application.
