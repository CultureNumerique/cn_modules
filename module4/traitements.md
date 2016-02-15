LANGUAGE:   fr
TITLE:   Les traitements et les applications
MENUTITLE: Les traitements
AUTHOR:     Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

# Comprendre les traitements

Pour être un utilisateur averti des machines ultrapuissantes utilisées
dans le monde numérique, il est utile de comprendre comme "raisonnent"
ces machines. Nous allons donc dans ce cours étudier les applications
et voir comment elles sont construites et comment elles peuvent
manipuler des données complexes.

L'utilisation d'un objet numérique connecté passe par l'exécution
d'applications (ou logiciels ou programmes). L'utilisateur est souvent
dirigé par l'interface de l'application qu'il utilise et éprouve des
difficultés à comprendre "ce que fait l'application". Il faut même
plutôt parler de "ce que fait la machine et les applications" car
l'exécution d'une application va souvent déclencher le lancement d'un
grand nombre d'applications en interaction avec la machine (processeur
de calcul et mémoire) et ses périphériques (disques, écran, clavier,
réseau). Nous allons donc découvrir l'univers des applications :
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
possibles entre toutes les paires de villes dépasserait les capacités
mémoire. C'est donc un programme qui va calculer l'itinéraire. Le
programme ne peut pas non plus calculer tous les itinéraires possibles
entre deux villes choisies car il y en a trop donc le temps de calcul
serait trop long et vous n'allez pas de Lille à Paris en passant par
Marseille ! Donc le programme doit être plus "intelligent".

L'idée du programme de calcul d'itinéraire est de représenter les
villes et routes comme un graphe où les noeuds sont les villes et les
arêtes sont les routes directes. Une distance, la distance entre deux villes,
peut être associée à chaque arête. Le problème est de trouver dans le
graphe le chemin avec le plus petit total des distances entre deux
villes. Les mathématiciens et informaticiens ont étudié ce problème et
conçu des algorithmes pour le résoudre. Ayant trouvé cet
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
essentiellement de l'intelligence des hommes et femmes ayant conçu
les applications.

```compréhension
::Une application indépendante ?::
[markdown]
**Une application indépendante ?**
Lancer une application implique de lancer plusieurs traitements
{T}

::Application et machine::
[markdown]
**Application et machine**
L'exécution d'une application fait usage de ressources de la machine. Donner des exemples.
{#### a minima avec le processeur de calcul et les mémoires}

::Application et périphériques::
[markdown]
**Application et périphériques**
L'exécution d'une application peut faire appel à des interactions avec l'extérieur de la machine par des périphériques. Donner des exemples de périphériques.
{#### réseau, clavier, souris, écran, ...}
```

# Composer des actions pour enrichir les compétences


### Introduction

Dans cette section, nous étudions les principes généraux de
composition permettant de créer une nouvelle fonctionnalité en
utilisant des fonctionnalités déjà existantes. Nous montrons également
que ce principe est général et que les nouvelles fonctionnalités
peuvent, à leur tour, être composées selon ces principes jusqu'à
pouvoir concevoir les applications complexes que vous utilisez
quotidiennement sur un ordinateur, une tablette ou un smartphone et
même dans de très autres nombreux objets comme votre box ou une montre
connectée.

Pour introduire ces principes de composition, plaçons nous au plus
près du matériel, c'est-à-dire de la machine qui manipule des 0 et
des 1. Le modèle de calcul de base de toutes les machines suppose :
une *unité de calcul* qui sait faire des calculs avec des 0 et des 1 ;
des *mémoires* dans lesquelles la machine peut ranger des résultats et
aller chercher les valeurs mémorisées ; et une *unité de contrôle* qui
donne les ordres à l'unité de calcul et aux mémoires.

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
3. ajouter 32 au code
4. aller chercher le caractère correspondant dans
   la table des codes
5. renvoyer le caractère comme résultat

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
sait faire (nous lui avons appris). Si ce n'est pas une majuscule, on
ne fait rien, c'est-à-dire on prend le caractère sans le
modifier. Peut-on savoir si un caractère est une majuscule ? Oui car
il suffit de regarder si le code du caractère est compris entre 65 (le
code de A) et 91 (le code de Z) et nous supposons que la machine sait
comparer deux nombres entiers. Ce qui donne le programme

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
séquences de caractères. 

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
encore plus riches. On peut comprendre les machines actuelles qui
disposent de très nombreuses applications comme construites selon ce
principe en partant de fonctionnalités de base avec un empilement de
couches successives applicatives de plus en plus riches. Par
conséquent, aujourd'hui, la plupart des besoins, personnels ou
professionnels, des utilisateurs sont couverts par une ou plusieurs
applications ce qui fait dire, à tort, à certains qu'il est inutile de
comprendre comment on code des applications. Nous pensons a contrario
que bien comprendre le fonctionnement des machines et des applications
permet de se poser les bonnes questions, de comprendre le
fonctionnement des applications et de pouvoir choisir la meilleure
application en fonction des besoins et de critères sociaux,
financiers, d'usage ou autres. De plus, il se peut qu'un besoin ne
soit pas couvert et, dans ce cas, il sera nécessaire de développer ou
faire développer une nouvelle fonctionnalité adaptée.

Le principe de la **conception descendante** est de construire une
application ou une nouvelle fonctionnalité en décomposant le problème
en des problèmes plus simples. La décomposition se base toujours sur
les modes de composition introduits précédemment. On arrête la
décomposition lorsque tous les sous-problèmes introduits correspondent
à des fonctionnalités de base de la machine dont on dispose. Il ne
reste plus alors qu'à écrire les nouvelles fonctionnalités pour notre
machine. Exemple ? compter les mots d'un texte ? un exemple avec le
robot ?

Concevoir une application est une tâche de conception donc une tâche
de haut niveau. En effet, un telle tâche comporte de nombreux choix
sur la façon d'organiser les données, d'organiser les traitements, de
répondre aux besoins de l'utilisateur, de répondre aux contraintes en
particulier légales. On parle d'*analyse informatique* ou de *génie
logiciel* pour désigner la science de concevoir des
applications. C'est une tâche souvent réalisée en équipe associant des
informaticiens, des utilisateurs et des experts métier. Il y a de
nombreuses méthodes de conception. Les méthodes les plus récentes sont
les *méthodes agiles* alternant phases de conception, phases de
développement, phases de mise en oeuvre et de retour des
utilisateurs. Ce domaine est toujours en expansion et les développeurs
d'applications sont toujours très recherchés avec actuellement une
forte demande pour les applications sur petits objets portables tels
que smartphones et tablettes qui ont des contraintes spécifiques.

```activité
::Modèle de machine::
[markdown]
**Modèle de machine**
Porposer une ressource simple et poser des questions sur modèle de Von Neuman
```


```activité
::Les minuscules en majuscules::
[markdown]
**Les minuscules en majuscules**
On souhaite apprendre à la machine à faire la transformation inverse, à savoir transformer les minuscules en majuscules. 
- Pour transformer un caractère minuscule en majuscule, quelle instruction faut-il changer dans `MAJ2MIN-CARA` ?
- Pensez-vous qu'on puisse apprendre à une machine à faire cette nouvelle instruction ?
- Expliquez ce qu'il faut changer dans `MAJ2MIN-CHAINE` pour obtenir un programme `MIN2MAJ-CHAINE` qui prend en entrée une séquence de caractères et qui transforme les minuscules en majuscules et laisse tous les autres caractères inchangés.
{#### retirer 32 au code au
lieu d'ajouter 32 ; oui, on doit pouvoir apprendre à notre machine à
faire une soustraction de deux entiers même si cela semble un petit
peu plus compliqué que l'addition ; tester si le code du caractère est entre 97 et 123 et appeler le programme qui transforme minuscule en majuscule.}
```


```activité
::Robot::
[markdown]
**Programmer un robot simpliste**
Activité sur le robot ?
```

```compréhension
::Exécution de programmes::
[markdown]
**Exécution de programmes**
Des exemples simples de programmes robot pour demander situation finale
```

# Une représentation adaptée pour un traitement

Nous avons introduit, dans la section précédente, les trois opérations
de composition , à savoir la suite d'instructions, l'alternative et
l'itérative, qui permettent de définir ce qui est calculable par une
machine. Mais notre machine avec ses applications doit être capable de
traiter des objets divers comme des nombres et des chaînes de
caractères mais aussi des documents, des images, des tableaux,
... Nous allons, dans cette section, étudier comment sont définis des
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
du programme utilise des varaibles pour expliquer à la machine ce
qu'elle doit faire. Par contre, l'utilisateur ne voit pas les
variables. Par exemple, l'utilisateur de notre programme saisit une
première valeur, par exemple 12, puis une seconde valeur, par exemple
14, et tout ce qu'il verra sont les résultats produits, soit sur notre
exemple, "la plus petite note est : 12", "la moyenne est : 13"

### Types de données élémentaires

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

### Types de données structurés

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

### Les objets

```compréhension
::Représenter et manipuler::
[markdown]
**Représenter et manipuler**
Les traitements possibles dépendent fortement des choix de représentation
{T}
```

# Les applications et les machines

### Le système d'exploitation

Le système d'exploitation est la première couche logicielle de tout
ordinateur qu'il soit fixe ou portable ou tablette ou smartphone. Il
cache toute la complexité des calculs en binaire au niveau matériel
(vous vous en moquez), la façon dont il range les données dans les
mémoires (il faut qu'il retrouve ce que vous lui demandez), la façon
dont il gère l'exécution des programmes que vous lancez (il faut que
mes applications fonctionnent, plusieurs en même temps) et la façon
dont il gère toutes les entrées-sorties, c'est-à-dire toutes les
communications avec les périphériques (il saisit ce que je tape au
clavier, il comprend mes clicks, il affiche sur l'écran, il envoie mes
impressions à l'imprimante, il échange mes données sur le réseau).

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
