LANGUAGE:   fr
TITLE:   Les traitements et les applications
MENUTITLE: Les traitements
AUTHOR:     Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

# Comprendre les traitements

Remarques de l'auteur :

* Motiver ce cours par un extrait de la page présentation : "les
étudiants ne comprennent pas ce qu’ils font, ne savent pas comment
fonctionnent les machines ultrapuissantes qui sont dans leurs poches,
et passent très souvent à côté des opportunités qu’offrent le
numérique. Les pratiques restent basiques, dirigées par les interfaces
et rendent les individus prisonniers d’applications ou de logiciels"
* L'exemple n'est pas simple. A voir si c'est compréhensible donc peut
  être le faire lire. Il doit pouvoir être illustré facilement pour
  aider la compréhension.

L'utilisation d'un objet numérique connecté passe par l'exécution
d'applications (ou logiciels ou programmes). L'utilisateur est souvent
dirigé par l'interface de l'application qu'il utilise et éprouve des
difficultés à comprendre "ce que fait l'application". Il faut même
plutôt parler de "ce que fait la machine et les applications" car
l'exécution d'une application va souvent déclencher le lancement d'un
grand nombre d'applications en interaction avec la machine et ses
périphériques. Nous allons donc découvrir l'univers des applications :
comment passe-t-on d'une machine "bête" manipulant des 0 et des 1 à
une machine "intelligente" réalisant des applications complexes. En
particulier, nous étudions comment composer des opérations pour
définir de nouvelles opérations, comment représenter des données
complexes, comment sont organisées les applications sur une
machine. Nous terminons par l'étude de quelques applications : comment
le navigateur affiche-t-il une page en partant d'un document `html`,
comment un traitement de texte calcule-t-il une table des matières et
comment une machine peut-elle jouer aux échecs.

Pour introduire ce cours, partons de l'exemple de calcul d'itinéraire
sur un site comme Mappy ou Google Maps.  Plaçons-nous du côté du site
de l'application. Celle-ci doit en premier lieu proposer un formulaire
de saisie dans lequel l'utilisateur (vous) peut saisir (a minima) un
lieu de départ, un lieu destination et un moyen de
transport. L'utilisation de l'application nécessite l'utilisation de
Internet et du Web et des applications associées étudiés dans d'autres
cours "Culture numérique" pour les interactions entre votre navigateur
et le site dédié à l'application. Nous supposons donc que
l'application itinéraire récupère vos saisies, c'est-à-dire une
adresse de départ, une adresse d'arrivée et un moyen de transport sous
forme de chaînes de caractères. Des programmes peuvent alors être
appliqués et extraire un numéro, un nom de rue et une ville pour le
départ, de même pour la destination.  Si le site dispose des adresses
valides, ces informations peuvent être validées ou des suggestions
proposées si l'adresse est incorrecte.

Pour simplifier la présentation nous supposons connaître une ville de
départ, une ville destination et nous supposons que le moyen de
transport choisi est la voiture et qu'un trajet va de ville en ville
et qu'on cherche le trajet le plus court. Quelles sont les
informations que doit posséder l'application ? La liste des villes et
connaître les distances directes (sans étape) entre deux villes. Une
première remarque importante s'impose : mémoriser tous les itinéraires
possibles entre toutes les villes dépasserait les capacités
mémoire. C'est donc un programme qui va calculer l'itinéraire. Le
programme ne peut pas non plus calculer tous les itinéraires possibles
car il y en a trop donc le temps de calcul serait trop long et vous
n'allez pas de Lille à Paris en passant par Marseille ! Donc le
programme doit être plus "intelligent".

L'idée du programme de calcul d'itinéraire est de représenter les
villes et routes comme un graphe où les noeuds sont les villes et les
arêtes sont les routes. Une distance, la distance entre deux villes,
peut être associée à chaque arête. Le problème est de trouver dans le
graphe le chemin avec le plus petit total des distances entre deux
villes. Les mathématiciens et informaticiens ont étudié ce problème et
conçus des algorithmes pour résoudre cette question. Ayant trouvé cet
itinéraire, il reste à l'application sur le serveur à mettre à jour la
page Web pour que cet itinéraire puisse être affiché dans votre
navigateur. Ce principe peut être étendu au problème initial entre
deux adresses, étendu à la recherche du chemin le plus rapide si on
connaît le temps de parcours pour tous les couples de ville, étendu au
cas "temps réel" si vous utilisez le programme d'itinéraire dans votre
voiture et que vous déviez de l'itinéraire proposé.

Cet exemple simplifié avait pour objectif de mettre en lumière
certains des points qui vont être abordés dans ce cours. Tout d'abord,
bien comprendre que le principe général de l'informatique est de
composer des applications pour créer une nouvelle
application. C'est ce principe qui permet de passer de la machine
"bête" manipulant des 0 et des 1 à une machine "intelligente"
calculant un itinéraire en passant par beaucoup de compétences
intermédiaires : savoir saisir un texte dans un formulaire, savoir
traiter un texte pour extraire un nom de ville, savoir faire des
calculs de distances, savoir représenter un graphe, ... Ensuite, il
faut remarquer que, malgré les capacités sans cesse croissantes des
machines, il faut être attentif à la taille des données mémorisées et
il faut être attentif au temps de calcul des programmes. Enfin, on
peut noter que l'intelligence supposée de la machine provient
essentiellement de l'intelligence des hommes et femmes ayant conçus
les applications.

```compréhension
::Représenter et manipuler::
[markdown]
**Représenter et manipuler**
Les traitements possibles dépendent fortement des choix de représentation
{T}
```

# Composer des actions pour enrichir les compétences


### Introduction

Dans cette section, nous étudions les principes généraux de
composition permettant de créer une nouvelle fonctionnalité en
utilisant des fonctionnalités déjà existantes. Nous montrons également
que ce principe est général et que les nouvelles fonctionnalités
peuvent être à leur tour être composées selon ces principes jusqu'à
pouvoir concevoir les applications complexes que vous utilisez
quotidiennement sur un ordinateur, une tablette ou un smartphone et
même dans de très autres nombreux objets comme votre box ou une montre
connectée.

Pour introduire ces principes de composition, plaçons nous au plus
près du matériel, c'est-à-dire de la machine qui manipule des 0 et
des 1. Le modèle de calcul de base de toutes les machines suppose une
unité de calcul qui sait faire des calculs avec des 0 et des 1 et des
mémoires dans lesquelles la machine peut ranger des résultats dans
lesquelles la machine peut aller chercher les valeurs mémorisées. Nous
supposons que la machine peut ainsi accéder à une table qui donne le
codage des caractères usuels sur un octet (un octet est constitué de 8
bits).

Apprenons à notre machine à transformer un caractère majuscule en
caractère minuscule correspondant. Vous pourrez vérifier dans le cours
sur les documents que le caractère A a pour nom "Latin Capital Letter
A" et pour numéro 65 et que pour passer d'une lettre majuscule de
notre alphabet à la lettre minuscule correspondante, il suffit
d'ajouter 32 à son numéro. Nous pouvons déjà écrire une suite
d'instructions pour écrire notre programme de transformation : avec un
caractère lettre majuscule en entrée,

1. aller chercher le code du caractère dans la table des codes
2. ajouter 32 au code trouvé
3. aller chercher le caractère correspondant au résultat trouvé dans
   la table des codes
4. renvoyer comme résultat le caractère trouvé

Où sont nos 0 et nos 1 ? Allons les voir puis nous les
oublierons. Prenons le caractère A de code 65, le nombre 65 se code
sur un octet par 01000001. Le nombre 32 se code sur un octet
par 00100000. Il suffit d'ajouter ces deux octets avec un programme
qui va se comporter comme l'addition que vous avez appris à l'école
primaire. On additionne les chiffres de la droite vers la gauche avec
les règles de calcul suivante : 0+0 = 0, 0+1 = 1, 1+0 = 1, 1+1 = 0
avec une retenue de 1. Ces régles sont facilement calculables par
notre machine de base et on peut utiliser une mémoire pour mémoriser
la retenue. On peut donc apprendre à la machine un programme
d'addition : avec deux octets en entrée

1. pour tous les bits de droite a gauche
2. ajouter le bit courant du premier octet avec le bit courant du
   second octet et avec la retenue courante
3. donner une valeur au bit courant du résultat et mettre à jour la retenue
4. fin du pour
4. renvoyer l'octet résultat

Et, par conséquent, on peut utiliser ce programme d'addition pour
ajouter 32 au code de notre lettre majuscule ! Le tour est joué !
Notre machine a une nouvelle fonctionnalité : elle sait transformer
une lettre majuscule en lettre minuscule ! Encore plus fort !
Apprenons à la machine un programme qui prend en entrée une séquence
de caractères et qui transforme les majuscules en minuscules et laisse
tous les autres caractères inchangés. L'idée est de traiter chacun des
caractères, regarder si c'est une majuscule. Si c'est une majuscule,
le transformer en la minuscule correspondante ce que notre machine
sait faire. Si ce n'est pas une majuscule, on ne fait rien,
c'est-à-dire on prend le caractère sans le modifier. Peut-on savoir si
un caractère est une majuscule ? Oui car il suffit de regarder si le
code du caractère est compris entre 65 (le code de A) et 91 (le code
de Z) et nous supposons que la machine sait comparer deux nombres
entiers. Ce qui donne le programme suivant : avec en entrée une
séquence de caractères,

1. le résultat est une séquence de caractères vide
2. pour tous les caractères de la séquence
3. si le code du caractère courant est compris entre 65 et 91
4. appeler le programme qui transforme une majuscule en minuscule et
   l'ajouter à la séquence résultat
5. Sinon
6. ajouter le caractère courant (sans rien faire)
7. fin du si
8. fin du pour
9. renvoyer la séquence résultat

Et voilà ! Notre machine a une nouvelle fonctionnalité : elle sait
transformer une séquence de caractères en remplaçant toutes les
majuscules par des minuscules. Et vous pouvez déjà imaginer que l'on
puisse ainsi continuer à construire de nouvelles fonctionnalités à
notre machine pour qu'elle sache faire beaucoup de traitements sur des
séquences de caractères. Nous allons préciser ces notions dans la
section suivante.

### Les trois compositions de base

suite, sialorssinon, boucle ou itération. Theoreme. note sur
calculabilité. pointeurs historique et philosophique

### Composer : la vision ascendante

composer de couche en couche

### Composer : la vision descendante

résoudre un problème : décomposer

```compréhension
::Représenter et manipuler::
[markdown]
**Représenter et manipuler**
Les traitements possibles dépendent fortement des choix de représentation
{T}
```
# Une représentation adaptée pour un traitement

### Types de données élémentaires

nombres, textes et Booléens

### Types de données structurées

listes, tableaux, arbres

### Choisir le type de données adapté au traitement

structure adaptée, introduire les questions de mémoire et d'accès rapide

```compréhension
::Représenter et manipuler::
[markdown]
**Représenter et manipuler**
Les traitements possibles dépendent fortement des choix de représentation
{T}
```

# Les applications et les machines

### Le système d'exploitation

Le système d'exploitation est la première couche logicielle de tout ordinateur qu'il soit fixe ou portable ou tablette ou smartphone. Il cache toute la complexité des calculs en binaire au niveau matériel (vous vous en moquez), la façon dont il range les données dans les mémoires (il faut qu'il retrouve ce que vous lui demandez), la façon dont il gère l'exécution des programmes que vous lancez (il faut que mes applications fonctionnent, plusieurs en même temps) et la façon dont il gère toutes les entrées-sorties, c'est-à-dire toutes les communications avec les périphériques (il saisit ce que je tape au clavier, il comprend mes clicks, il affiche sur l'écran, il envoie mes impressions à l'imprimante, il échange mes données sur le réseau).

Vous vous moquez de la façon dont il travaille mais vous l'utilisez souvent pour lancer vos applications, pour sauvegarder vos fichiers de travail, pour vous connecter au réseau, pour installer un nouveau périphérique. Il se présente comme une interface graphique (depuis les années 90) avec principalement : un gestionnaire d'applications, un gestionnaire de configuration du système, un gestionnaire de fichiers et souvent une console (ou terminal ou fenêtre de commande) permettant de donner des instructions au système. Pour être un utilisateur averti, il est utile de comprendre les principes du système de gestion de fichiers et de savoir manipuler et donc désigner des fichiers dans le système de gestion de fichiers.

En effet, en informatique les données et les applications sont rangées dans des fichiers. Malgré certaines tentatives, on n'a pas encore trouvé mieux que de ranger les fichiers dans des boîtes qui sont elles-mêmes contenues dans des boîtes qui ... Ces boîtes sont appelées dossiers ou répertoires. Donc, les fichiers sont organisés dans une hiérarchie de répertoires, chaque répertoire contenant des fichiers et/ou des répertoires. Il faut comprendre que l'on peut se déplacer dans cette hiérarchie avec des commandes ou en ouvrant le répertoire en mode graphique par un double clic. Le répertoire dans lequel on est à un instant donné s'appelle le répertoire courant. Le sommet de la hiérarchie s'appelle la racine.

Les fichiers sont désignés par un nom souvent de la forme préfixe.suffixe. Nous avons vu dans d'autres cours que le suffixe pour un fichier est souvent lié à une application. Dans une utilisation courante, il est conseillé de nommer vos fichiers (et répertoires) avec des noms qui ont un sens (une sémantique), d'utiliser le bon suffixe (il est parfois ajouté automatiquement par le logiciel), d'éviter les espaces et les accents dans les noms et de ranger vos fichiers dans un répertoire où vous saurez le retrouver. Pour désigner un fichier, il faut préciser son nom et où il est rangé. Pour préciser où il est rangé on utilise un chemin permettant de le trouver. Le chemin peut etre relatif (le chemin pour accéder au
fichier en partant du répertoire courant) ou absolu (en partant de la racine).

### Les langages de programmation

principes généraux, illustrer ce qui précède avec packages, langage
adapté selon type d'application à développer

### Les applications

la superposition des couches logicielles, fonctionnalités d'une
application, choisir la bonne application
```compréhension
::Représenter et manipuler::
[markdown]
**Représenter et manipuler**
Les traitements possibles dépendent fortement des choix de représentation
{T}
```

# Des exemples d'application

### Le navigateur affiche une page Web

lecture du document texte structuré entête et corps, reprendre
Internet et Web pour aller chercher les ressources, avec toutes les
ressources comment construire la page, avec la css la mettre en forme

### Un traitement de textes calcule une table des matières

montrer l'importance d'avoir un document structuré, avec la structure
comment calculer les numéros de section, les numéros de page, ...

### Un jeu d'échec sur ordinateur

représenter le plateau, les pièces, une configuration de jeu. Comment
choisir un coup étant donné une configuration.

```compréhension
::Représenter et manipuler::
[markdown]
**Représenter et manipuler**
Les traitements possibles dépendent fortement des choix de représentation
{T}
```
