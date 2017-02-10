LANGUAGE:   fr
TITLE:   Recherche d'information et référencement Web
MENUTITLE: Recherche d'information Web
AUTHOR: Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

<!-- pandoc -t latex -V geometry:margin=3cm --toc ri.md -o ri.pdf -->

<!-- pandoc -F ext.py -t latex -V geometry:margin=3cm --toc ri.md -o ri.pdf -->

# La recherche d'information : contexte et application au Web

Avec l'avénement du numérique et, en particulier, du Web, nous vivons
dans un monde de documents. Ces documents sont divers comme des sms,
des tweets, des mails, des pages Web, des articles journalistiques ou
scientifiques, des livres, ... Ils contiennent des informations
textuelles mais aussi des dessins, des images et des videos. Ils
proviennent de sources variées comme des administrations, des
journaux, des entreprises commerciales mais aussi les réseaux sociaux
et les capteurs. Ils sont en très grande quantité avec, par exemple,
un nombre estimé de 60 000 milliards de documents Web en 2016. Cette
masse de documents génère de nouveaux besoins comme pouvoir retrouver
des documents concernant un sujet précis, pouvoir recevoir des
suggestions d'articles de journaux ou encore pouvoir recevoir des
recommandations de livres à lire ou de films à regarder.

Nous allons considérer la recherche de documents et, pour cela, nous
étudions un outil numérique utilisé quotidiennement par chacun d'entre
nous : le **moteur de recherche d'information** Web. L'exemple le plus
connu et le plus utilisé dans le monde occidental est `Google`, mais
vous pouvez également utiliser `Bing` ou `Yahoo`. Nous vous signalons
également un moteur français `Qwant` qui promet la préservation de la
confidentialité et le respect de la vie privée. Notez également
d'autres moteurs qui sont leaders dans leurs sphères d'influence comme
`Yandex` en Russie et `Baidu` en Chine. La fonction première d'un
moteur de recherche est de vous permettre de *poser une requête*
constituée d'un ou plusieurs mots clés. En réponse, le moteur vous
renvoie *une liste ordonnée de documents Web* organisée par pages de
10 documents. Cet outil est devenu essentiel dans vos activités
personnelles comme professionnelles. L'ordre dans lequel les documents
vous sont proposés est calculé par le moteur. Un utilisateur ne
regarde souven que les premières réponses et, par conséquent, l'ordre
choisi peut orienter vos réflexions. Cet ordre influe également sur
l'activité économique en orientant les choix d'achats des
utilisateurs. Il nous semble donc important de comprendre les bases du
calcul des scores attribués aux documents pour que vous soyez un
utilisateur intelligent et averti de ces moteurs de recherche qui
orientent vos activités.

Dans cet objectif, nous allons présenter les algorithmes et structures
de données utilisés pour calculer le score Web d'un document
relativement à une requête composée de plusieurs mots. Dans un premier
temps, nous présentons les méthodes classiques de recherche
d'information que sont la recherche séquentielle (comme la recherche
de mails dans votre lecteur de mails) et la recherche Booléenne (comme
la recherche de livres dans une bibliothèque). Nous présentons
également le modèle vectoriel qui permet de calculer le score d'un
document textuel relativement à une requête. Dans un second temps,
nous présentons l'algorithme de calcul d'un score de notoriété d'un
document Web calculé en utilisant les liens (appelés aussi hyperliens)
existant entre les pages Web. C'est cet algorithme connu sous le nom
de *PageRank* qui a contribué au succès de Google dès la fin du
vingtième siècle. Nous montrons alors comment il est possible de
combiner ces deux scores pour attribuer un score Web à un document Web
relativement à une requête. Nous en déduisons de bonnes pratiques pour
que vos documents soient bien classés par les moteurs de recherche. On
parle aussi de documents bien référencés et le *référencement* étudie
ces bonnes pratiques. Nous terminons par une discussion sur les
problèmes éthiques et sociétaux posés par les moteurs de recherche et
par une présentation des évolutions en cours.

# Les modèles de recherche d'information

## La recherche séquentielle ou "Grep Through text"

On suppose disposer d'un ensemble de documents textuels, c'est-à-dire
de documents qui sont des suites de caractères. Cela peut être le
contenu d'un texte dans un éditeur ou un traitement de textes, une
page Web de votre navigateur, l'ensemble des sujets des mails ou
l'ensemble des contenus textuels des mails contenus dans votre lecteur
de mails, des articles d'un site journalistique, les noms des fichiers
de votre ordinateur ou de votre téléphone.

Une requête simple est constituée d'un mot, c'est-à-dire d'une suite
de caractères. On peut exécuter une telle requête souvent en passant
par un menu *Chercher* ou *Find* et en tapant la suite de caractères
dans une zone de saisie. Un tel menu existe dans un éditeur ou
traitement de textes pour chercher dans le contenu, dans votre
navigateur pour chercher dans une page web, dans votre lecteur de
mails pour chercher dans les adresses ou les sujets ou les contenus de
vos mails, dans un site de journaux pour chercher dans les articles,
dans votre système d'exploitation pour chercher dans les noms des
fichiers ou dans les contenus des fichiers. Le résultat de la requête
est de surligner toutes les occurrences de la chaîne cherchée ou de
donner la liste des objets contenant la chaîne.

L'algorithme de recherche va parcourir le ou les documents textes en
déplacant une fenêtre qui contient la chaîne cherchée et en gardant
comme réponses correctes toutes les positions où le texte correspond
exactement à la chaîne cherchée. C'est un *algorithme séquentiel* très
simple qui parcourt complètement le(s) texte(s) où l'on cherche.

Le langage de requêtes peut être étendu avec des requêtes plus
complexes. On peut introduire des jokers souvent notés *, + et ? où
le * représente une suite de caractères quelconque, le + une suite de
caractères non vide et le ? n'importe quel caractère. Par exemple, la
requête `pa*on` est satisfaite par des mots comme `paon`, `pantalon`
ou `passion` ; ces deux derniers mots satisfont la requête `pa+on`
alors que `paon` ne la satisfait pas ; la requête `pap?` est
satisfaite par des mots comme `pape` ou `papa`mais pas par
`papillon`. On peut également introduire des notations pour préciser
des plages de caractères comme les chiffres, on peut ajouter des
conditions comme la ligne commence par ou se termine par. On peut
enfin ajouter des opérateurs logiques comme des `ET`, `OU`, `NON`. On
peut obtenir des langages de requêtes sophistiqués qui sont très
utilisés par les informaticiens pour traiter des fichiers textes, les
linguistes pour traiter des textes en langue naturelle, les
biologistes pour rechercher dans les séquences génétiques. Il faut
alors développer des algorithmes adaptés.

La recherche séquentielle est utilisée dans de nombreuses
applications. Le langage de requêtes est simple mais peut être enrichi
et devenir très expressif. Les algorithmes de recherche séquentielle
sont efficaces pour des volumes "raisonnables" de documents. En effet,
pour chaque exécution d'une requête, il est nécessaire de parcourir
séquentiellement les textes dans lesquels on cherche. Une telle
méthode est-elle envisageable pour un moteur de recherche Web ?
Certainement non, car il n'est pas pensable de devoir parcourir les 60
000 milliards de documents du Web à chaque requête posée !

## Le modèle Booléen : les documents satisfaisant un critère

On suppose donc un grand ensemble de documents textuels comme des
articles de journaux, des articles scientifiques, des livres
numérisés. On suppose également que chaque document possède un
*identifiant*, c'est-à-dire un numéro qui identifie le document. Nous
considérons des requêtes à un mot et l'objectif est de trouver tous
les documents contenant ce mot.

Nous venons de voir que la recherche séquentielle est impossible pour
des raisons de temps de calcul. Il faut donc procéder autrement ! Bien
évidemment, il faut avoir parcouru au moins l'ensemble des textes pour
chercher dans leur contenu, l'idée est donc de le faire une fois pour
construire une nouvelle représentation de l'ensemble des textes qui
permet ensuite de répondre très rapidement aux requêtes. La phase de
prétraitement est appelée **indexation** et amène à la construction
d'une structure de données appelée **index** qui permettra de faire
ces recherches rapides.  Nous expliquons cette étape d'indexation qui
peut être décomposée en une phase de prétraitement des documents, la
constitution d'un dictionnaire et la construction d'un index. Nous
expliquons ensuite comment calculer des requêtes.

La première opération est de transformer les documents en des textes
qui sont des simples suites de caractères. Ceci est nécessaire car les
documents peuvent avoir des formats divers comme `doc`, `docx`, `pdf`
ou encore `html`. Cecie est réalisé avec des logiciels spécialisés
pour chacun des formats existants. Dans une seconde étape, chaque
document est découpé en une séquence d'unités élémentaires appelés
`tokens` en utilisant les espaces et les ponctuations. On peut penser
à un token comme étant un mot mais il peut y a voir aussi des nombres,
des dates, ... Enfin, différents traitements peuvent être considérés
comme : considère-t-on différemment les majuscules et les minuscules ?
considère-t-on les accents ? ... Selon les choix, on effectue les
traitements adéquats. Par exemple, si on ne tient pas compte de la
casse, on va transformer tous les mots comme des chaînes de
minuscules. Parfois, on considère des traitements linguistiques comme
*lemmatiser* qui consiste à ramener toutes les formes d'un mot à son
lemme : ramener toutes les formes d'un verbe à sa forme à
l'infinitif. Les choix sont nombreux et dépendent du contexte.

Les documents sont désormais des suites de mots. L'ensemble des mots
qui apparaissent définissent un **dictionnaire** ou vocabulaire qui
est l'ensemble des mots qui vont être considérés dans les
requêtes. Pour chaque mot du dictionnaire, on peut construire la liste
des documents qui contiennent ce mot. Cette liste est ordonnée par
identifiant de documents croissants. Par exemple, on mémorise que le mot
`rose` apparaît dans les documents de numéro 125, 245, 567, ...

Enfin, la dernière chose à considérer est de pouvoir trouver
rapidement un mot dans le dictionnaire car la taille d'un dictionnaire
peut aller de quelques centaines de milliers de mots dans des bases de
documents à plusieurs millions dans le cas du Web. Pour cela, les
informaticiens ont défini différentes méthodes d'accès rapides. Pour
notre propos, il suffit d'imaginer que si on trie le dictionnaire
alors on peut accéder rapidement à un mot. **trouver presentation**

> Un **index** est constitué d'un dictionnaire avec une méthode d'accès
> rapide à un mot, et pour chaque mot de la liste ordonnée par numéro
> croissant des documents qui contiennent ce mot.

Dans le modèle
Booléen, l'objectif est de trouver l'ensemble des documants qui
satisfont une requête. Pour une requête à un mot clé, c'est l'ensemble
des documents qui contiennent de mot, pour une requête à plusieurs
mots clés, c'est l'ensemble des documents qui contiennent tous les
mots clés. La base de documents ayant été prétraitée de façon à
construire un index,


principes de la recherche
séquentielle. Matrices. Introduction des index. Principes des
algorithmes. Extension aux phrases. Analyse critique.

## Le modèle vectoriel : attribuer un score de pertinence aux documents

représentation vectorielle de documents (tf et tf-idf), score de
similarité entre deux documents avec Cosinus, score de pertinence d
wrt q, algorithme, extension aux phrases.

# Recherche d'information sur le Web

## Score de pertinence

combinaison de scores de pertinence de différentes parties du document.

## Score de notoriété

introduction de PageRank. Hubs et Authorities.

## Score Web

combinaison score de pertinence et de notoriété. Autres éléments.

# Le référencement

objrctifs et principes

## Une bonne indexation des documents

au niveau du site et de la page

## Un bon score de pertinence

bons mots aux bonxs endroits

## Un bon score de notoriété

bon contenu pour attirer les liens

# Conclusion

formules cachées, formules qui évoluent, évolutions vers le langage
naturel, le Web des données

