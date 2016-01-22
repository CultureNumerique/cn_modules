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
mémoires dans lesquelles la machine peut ranger des résultats et aller
chercher les valeurs mémorisées. 

Apprenons à notre machine à transformer un caractère majuscule en
caractère minuscule correspondant. Nous supposons que la machine peut
accéder à une table qui donne le codage des caractères usuels. Vous
pourrez vérifier dans le cours sur les documents que le caractère A a
pour nom "Latin Capital Letter A" et pour numéro 65 et que pour passer
d'une lettre majuscule de notre alphabet à la lettre minuscule
correspondante, il suffit d'ajouter 32 à son numéro. Nous pouvons déjà
écrire une suite d'instructions pour écrire notre programme de
transformation. 

`MAJ2MIN-CARA`

1. un caractère lettre majuscule en entrée
2. aller chercher le code du caractère dans la table des codes
3. ajouter 32 au code trouvé
4. aller chercher le caractère correspondant au résultat trouvé dans
   la table des codes
5. renvoyer comme résultat le caractère trouvé

Où sont nos 0 et nos 1 ? Allons les voir puis nous les
oublierons. Prenons le caractère A de code 65, le nombre 65 se code
sur un octet par 01000001. Le nombre 32 se code sur un octet
par 00100000. Il suffit d'ajouter les deux codes ce qui peut être fait
en ajoutant les deux octets. Il faut donc un programme d'addition de
deux octets. Le principe est celui de l'addition que vous avez appris
à l'école primaire. On additionne les chiffres de la droite vers la
gauche avec les règles de calcul suivante : 0+0 = 0, 0+1 = 1, 1+0 = 1,
1+1 = 0 avec une retenue de 1. Ces régles sont facilement calculables
par notre machine de base et on peut utiliser une mémoire pour
mémoriser la retenue. On peut donc apprendre à la machine un programme
d'addition

1. deux octets en entrée, une retenue qui vaut 0
2. pour tous les bits de droite a gauche
3. ajouter le bit courant du premier octet avec le bit courant du
   second octet et avec la retenue courante
4. donner une valeur au bit courant du résultat et mettre à jour la retenue
5. fin du pour
6. renvoyer l'octet résultat

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
entiers. Ce qui donne le programme

`MAJ2MIN-CHAINE`

1. Une séquence de caractères en entrée
2. le résultat est une séquence de caractères vide
3. pour tous les caractères de la séquence d'entrée
4. si le code du caractère courant est compris entre 65 et 91
5. appeler le programme qui transforme une majuscule en minuscule et
   l'ajouter à la séquence résultat
6. Sinon
7. ajouter le caractère courant (sans rien faire)
8. fin du si
9. fin du pour
10. renvoyer la séquence résultat

Et voilà ! Notre machine a une nouvelle fonctionnalité : elle sait
transformer une séquence de caractères en remplaçant toutes les
majuscules par des minuscules. Et vous pouvez déjà imaginer que l'on
puisse ainsi continuer à construire de nouvelles fonctionnalités à
notre machine pour qu'elle sache faire beaucoup de traitements sur des
séquences de caractères. Nous allons préciser ces notions dans la
section suivante.

### Les trois compositions de base

Nous avons fait émerger les opérations de composition dans notre
exemple sur la transformation de séquences de caractères.  La
première, la plus évidente, est de combiner les instructions en
définissant une **suite d'instructions** encore appelée séquence
d'instructions. Un exemple est `MAJ2MIN-CARA` qui est constitué d'une
suite d'instructions. L'exécution d'une suite d'instructions se fait
en exécutant la première instruction, puis la seconde, jusqu'à
épuisement de la suite d'instructions.

Mais on est vite confronté à des situations où l'instruction à
réaliser peut dépendre de conditions. Par exemple, dans
`MAJ2MIN-CHAINE` on ne souhaite transformer le caractère que si c'est
une lettre majuscule. Un autre exemple peut être celui d'un robot qui
avance si il n'y a pas d'obstacle devant lui et qui tourne
sinon. Cette opération de composition est appelée **alternative** ou
**si alors sinon**. Elle s'écrit de façon générale sous la forme `SI
condition ALORS SuiteInstructionsSi SINON SuiteInstructionsSinon
FINSI` où condition peut prendre une des deux valeurs `VRAI` ou `FAUX`
et `SuiteInstructionsSi` et `SuiteInstructionsSinon` sont des suites
d'instructions. L'exécution d'une alternative se fait en estimant la
valeur de `condition`, puis si cette valeur est `VRAI` on exécute les
instructions dans `SuiteInstructionsSi`, si cette valeur est `FAUX` on
exécute les instructions dans `SuiteInstructionsSinon`.

La suite d'instructions permet de définir une suite d'instructions
mais il faut écrire chaque instruction et il faut donc connaître à
l'avance le nombre d'instructions à exécuter ce qui n'est pas toujours
le cas. Reprenons l'exemple de `MAJ2MIN-CHAINE`, on ne connait pas la
longueur de la séquence à l'avance et nous avons utilisé une
composition de la forme "pour tous les caractères de la séquence
d'entrée" pour dire que l'on devait appliquer une transformation à
tous les caractères de la séquence. Un second exemple est le cas du
robot qu'on souhaite faire avancer dans un environnement inconnu. On
souhaite qu'il répète l'action d'avancer tant qu'il ne rencontre pas
d'obstacle. Ces deux exemples ont introduit la troisième et dernière
opération de composition appelée **itérative** ou **répétition** ou
**tant que**. Elle s'écrit de façon générale sous la forme `TANTQUE
condition FAIRE SuiteInstructions FINTANTQUE`. L'exécution se fait en
estimant la valeur de `condition`, puis si cette valeur est `VRAI`, on
exécute les instructions dans `SuiteInstructions`, et on revient
estimer la valeur de `condition`, et on réitère. Dans le cas où la
valeur de `condition` est `FAUX` on passe à la suite, on dit que "on
sort du tant que". Ce mode de composition permet de réitérer un même
traitement un nombre quelconque de fois. Notez bien que il faut
s'assurer que la condition prenne au bout d'un certain temps la valeur
`FAUX` pour que l'exécution s'arrête ! Cette opération de composition
peut aussi s'écrire avec une opération `REPETER` ou avec une opération
`POURTOUT`.

Voilà, vous savez tout ! ou plus exactement vous connaissez les trois
modes de composition qui permettent d'écrire toutes les
applications. En effet, il existe un **théorème** qui affirme que tout
ce qui est calculable avec une machine peut être défini par quelques
opérations élémentaires et les opérations de composition que sont la
suite (ou la séquence), l'alternative et l'itérative. Ce théorème a
été démontré au milieu du vingtième siècle par des mathématiciens et
des logiciens. Ceci soulève immédiatement la question : une machine
peut-elle tout calculer ? La réponse, démontrée à la même époque est
négative : il existe des problèmes que ne peut pas résoudre une
machine. Par exemple, il est montré qu'il n'existe pas de machine qui
prend en entrée une suite d'instructions contenant des alternatives et
des itératives et qui répond en sortie cette suite d'instructions va
s'arrêter en un temps fini lorsqu'on l'exécutera. Ces sujets soulèvent
des problèmes importants qui ont été et sont encore étudiés par les
mathématiciens, les informaticiens, les logiciens et les
philosophes. Notons enfin, que savoir qu'un problème est calculable ne
suffit pas à savoir le traiter car le temps de calcul peut être
prohibitif.

Question : parler de Variables en lien avec les mémoires données en
exemple introductif ? 


### Créer de nouvelles applications

Nous supposons disposer d'une machine avec des fonctionnalités de
base. Cela peut être une machine très proche du matériel sachant faire
des opérations sur des 0 et des 1 ; cela peut être une machine qui
sait manipuler des nombres, des caractères et des textes ; cela peut
être un robot qui sait avancer, tourner et repérer des obstacles ;
cela peut être un logiciel de dessin vectoriel qui sait se repérer sur
une grille, tracer des segments, des cercles, des courbes et
colorier. Les exemples sont nombreux, mais, pour tous ces exemples,
notre objectif est d'ajouter de nouvelles fonctionnalités à notre
machine. Nous allons décrire deux principes de conception.

Le principe de la **conception ascendante** est de créer de nouvelles
fonctionnalités en utilisant les modes de composition introduits dans
la section précédente. Ces nouvelles fonctionnalités peuvent, à leur
tour, être considérées commes des fonctionnalités de base et on peut
recommencer le processus de conception de nouvelles fonctionnalités
encore plus riches. Ceci fait que vous disposez sur les machines
actuelles d'environnements très riches avec de très nombreuses
applications. Par conséquent, la plupart des besoins, personnels ou
professionnels, des utilisateurs sont couverts par une ou plusieurs
applications. Bien comprendre le fonctionnement des machines et des
applications permet de se poser les bonnes questions et de choisir la
meilleure application en fonction des besoins et de critères sociaux,
financiers, d'usage ou autres. Néanmoins, il se peut qu'un besoin ne
soit pas couvert, dans ce cas, il sera nécessaire de développer ou
faire développer une nouvelle fonctionnalité adaptée.

Le principe de la **conception descendante** est

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
