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
utilisant des fonctionnalités déjà existantes. 

analysons ce qu'est un document textuel pour
déterminer les critères amenant à une bonne représentation numérique.
Le cours sur le Web a déjà introduit un exemple de représentation
numérique de document dont une caractéristique essentielle est de
représenter contenu et structure d'un côté dans le langage `HTML` et
présentation d'un autre côté avec une feuille de style `CSS`. Cette
représentation facilite les traitements et la transmission à travers
les réseaux et permet l'affichage sur tout type d'écran. Cette
distinction entre structure, contenu et présentation est plus générale
et résulte de l'analyse de ce qu'est un document textuel.

L'analyse des documents textuels met en évidence *quatre vues
complémentaires* : les vues séquentielle, structurée, qualifiée et de
présentation.



### Le contenu, une vue séquentielle


### La structure, une vue arborescente


```activité
::Installer LibreOffice::
[markdown]
**Installer LibreOffice**
Les activités seront proposées avec le traitement de textes `LibreOffice`. Vous pouvez l'installer depuis le site [http://fr.libreoffice.org/](http://fr.libreoffice.org/). 
Rappelez-vous que vous devez installer des logiciels depuis les sites officiels uniquement. 
Les activités peuvent aussi être réalisées depuis les salles d'accès libre de l'université où tous les logiciels nécessaires sont disponibles.
{}
```

# Une représentation adaptée pour un traitement

### Types de données élémentaires

### Types de données structurées

### Choisir le type de données adapté au traitement

# Les applications et les machines

### Le système d'exploitation

### Les langages de programmation

### Les applications

# Des exemples d'application

### Le navigateur affiche une page Web

### Un traitement de textes calcule une table des matières

### Un jeu d'échec sur ordinateur




