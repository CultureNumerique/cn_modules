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
et les objets connectés (caméras, compteurs intelligents, gps,
...). Ils sont en très grande quantité avec, par exemple, un nombre
estimé de 60 000 milliards de documents Web en 2016. Cette masse de
documents génère de nouveaux besoins comme pouvoir retrouver des
documents concernant un sujet précis, pouvoir recevoir des suggestions
d'articles de journaux ou encore pouvoir recevoir des recommandations
de livres à lire ou de films à regarder.

Nous allons considérer la recherche de documents et, pour cela, nous
étudions un outil numérique utilisé quotidiennement par chacun d'entre
nous : le **moteur de recherche d'information** Web. L'exemple le plus
connu et le plus utilisé dans le monde occidental est **Google**, mais
vous pouvez également utiliser **Bing** ou **Yahoo**. Nous vous
signalons également un moteur français **Qwant** qui promet la
préservation de la confidentialité et le respect de la vie
privée. Notez également d'autres moteurs qui sont leaders dans leurs
sphères d'influence comme **Yandex** en Russie et **Baidu** en
Chine. La fonction première d'un moteur de recherche est de vous
permettre de *poser une requête* constituée d'un ou plusieurs mots
clés. En réponse, le moteur vous renvoie *une liste ordonnée de
documents Web* organisée par pages de 10 documents. Cet outil est
devenu essentiel dans vos activités personnelles comme
professionnelles. L'ordre dans lequel les documents vous sont proposés
est calculé par le moteur. Un utilisateur ne regarde souvent que les
premières réponses et, par conséquent, l'ordre choisi peut orienter
vos réflexions et vos activités. Cet ordre influe également sur
l'activité économique en orientant les choix d'achats des
utilisateurs. Il est donc important de comprendre comment est calculé
le score d'un document Web pour que vous soyez un utilisateur
intelligent et averti de ces moteurs de recherche d'information.

Dans cet objectif, nous allons présenter les algorithmes et structures
de données utilisés pour calculer le score Web d'un document
relativement à une requête composée de plusieurs mots. Nous commençons
par présenter les méthodes classiques de recherche d'information que
sont la recherche séquentielle (comme la recherche de mails dans votre
lecteur de mails) et la recherche Booléenne (comme la recherche de
livres dans une bibliothèque).  Nous présentons ensuite les deux
composantes essentielles du score Web : le **score de pertinence d'un
document pour une requête** qui mesure la proximité entre la requête
et le document et le **score de notoriété d'une page Web** qui mesure
l'importance de la page dans le réseau constitué des pages Web reliées
entre elles par des hyperliens. C'est l'introduction de ce score de
notoriété calculé par **l'algorithme PageRank** qui a contribué au
succès de Google dès la fin du vingtième siècle. Nous montrons comment
utiliser ces scores pour attribuer un score Web à un document Web
relativement à une requête. Nous terminons par une discussion sur les
problèmes éthiques et sociétaux posés par les moteurs de recherche et
par une présentation des évolutions en cours. En complément, nous
présentons succinctement les bonnes pratiques pour que vos documents
soient bien classés par les moteurs de recherche. On parle aussi de
documents bien référencés et le *référencement* étudie ces questions.

```compréhension
::Des moteurs de recherche::
[markdown]
Il existe différents moteurs de recherche d'information{T}

::Le coeur des moteurs::
[markdown]
Regardez [la page d'accueil de Google](http://www.google.fr) et [la page d'accueil de Qwant](http://www.qwant.com). Tout moteur de recherche
d'information permet la saisie d'une requête composée de plusieurs
mots dans une barre de saisie{T}

::Les réponses du moteur Google::
[markdown]
Lancer la requête `apprentissage machine`. Le moteur Google renvoie
{
= une liste ordonée de réponses
~ trois listes ordonnées de réponses
#### Google a volontairement une interface simple pour ses réponses avec une seule liste de réponses. Nous verrons que d'autres éléments peuvent être ajoutés par la suite.}

::Les réponses du moteur Qwant::
[markdown]
Lancer la requête `apprentissage machine`. Le moteur Qwant renvoie
{
~ une liste ordonée de réponses
= trois listes ordonnées de réponses
#### Qwant a une interface plus moderne pour ses réponses avec trois listes de réponses en trois rubriques Web, Actualités et Social.}

::Une première comparaison::
[markdown]
En regardant les réponses de Google et de Qwant, les réponses à une requête sont les mêmes et dans le même ordre.{T}
```

# Les modèles de recherche d'information

## La recherche séquentielle ou "Grep Through text"

On suppose disposer d'un ensemble de documents textuels, c'est-à-dire
de documents qui sont des suites de caractères. Cela peut être le
contenu d'un texte dans un éditeur ou un traitement de textes, le
contenu textuel d'une page Web affichée dans votre navigateur,
l'ensemble des sujets des mails ou l'ensemble des contenus textuels
des mails contenus dans votre lecteur de mails, des articles d'un site
journalistique, les noms des fichiers de votre ordinateur ou de votre
téléphone.

Une requête simple est constituée d'un mot, c'est-à-dire d'une suite
de caractères. On peut exécuter une telle requête souvent en passant
par un menu *Chercher* ou *Find* et en tapant la suite de caractères
cherchée dans une zone de saisie. Un tel menu existe dans un éditeur
ou traitement de textes pour chercher dans le contenu, dans votre
navigateur pour chercher dans une page web, dans votre lecteur de
mails pour chercher dans les adresses ou les sujets ou les contenus de
vos mails, dans un site de journaux pour chercher dans les articles,
dans votre système d'exploitation pour chercher dans les noms des
fichiers ou dans les contenus des fichiers. Le résultat de la requête
est de surligner toutes les occurrences de la chaîne cherchée ou de
donner la liste des objets contenant la chaîne. Pour réaliser cela, un
algorithme de recherche parcourt le ou les documents textes en
déplacant une fenêtre qui contient la chaîne cherchée et en gardant
comme réponses correctes toutes les positions où le texte correspond
exactement à la chaîne cherchée. C'est un *algorithme séquentiel* qui
parcourt complètement le(s) texte(s) où l'on cherche.

Le langage de requêtes peut être étendu avec des requêtes plus
complexes. On peut introduire des jokers souvent notés `*`, `+` et `?`
où le `*` représente une suite de caractères quelconque, le `+` une
suite de caractères non vide et le `?` n'importe quel caractère. Par
exemple, la requête `pa*on` est satisfaite par des mots comme `paon`,
`pantalon` ou `passion` ; ces deux derniers mots satisfont la requête
`pa+on` alors que `paon` ne la satisfait pas ; la requête `pap?` est
satisfaite par des mots comme `pape` ou `papa`mais pas par
`papillon`. On peut également étendre le langage de requêtes pour
préciser qu'un caractère doit être dans un ensemble (par exemple un
chiffre), ajouter des conditions comme `la ligne commence par` ou `se
termine par` un caractère précis. On peut enfin ajouter des opérateurs
logiques comme des `ET`, `OU`, `NON`. On obtient ainsi des langages de
requêtes expressifs, appelés **expressions régulières**, qui sont très
utilisés par les informaticiens pour traiter des fichiers textes, les
linguistes pour traiter des textes en langue naturelle, les
biologistes pour rechercher dans les séquences génétiques, entre
autres. Des algorithmes sophistiqués ont été proposés pour répondre
rapidement à ces requêtes.

**Critiques de la recherche séquentielle:** elle est utilisée dans de
nombreuses applications. Le langage de requêtes est simple mais peut
être enrichi et devenir très expressif. Les algorithmes de recherche
séquentielle sont efficaces pour des volumes "raisonnables" de
documents. En effet, pour chaque exécution d'une requête, il est
nécessaire de parcourir séquentiellement les textes dans lesquels on
cherche. Une telle méthode est-elle envisageable pour un moteur de
recherche Web ?  Certainement non, car parcourir les 60 000 milliards
de documents du Web lorsque vous écrivez une requête Google prendrait
un temps de calcul bien trop long alors que vous attendez une réponse
immédiate !

## Le modèle Booléen : les documents satisfaisant un critère

C'est le cas d'un recherche dans un fonds documentaire comme une
bibliothèque. On dispose d'un grand nombre d'ouvrages et on recherche
un ouvrage par l'intermédiaire d'une requête dans un formulaire.  Les
ouvrages sont, en général, représentés par des notices. Une notice
contient des méta-données sur le document comme le titre, les auteurs,
les éditeurs et un résumé. Une notice contient également des mots-clés
sur le document et son sujet qui sont renseignés par des
documentalistes. Parfois, les ouvrages ont été numérisés, on dispose
alors de leur contenu textuel dans lequel on peut chercher et on
parle, dans ce cas, de *recherche plein texte*. Nous supposons que
chaque ouvrage possède un *identifiant*, c'est-à-dire un numéro qui
identifie le document. Nous considérons, dans un premier temps, des
requêtes à un ou plusieurs mots clé. Dans le modèle Booléen, le
système de recherche d'information doit renvoyer **l'ensemble des
ouvrages dont la notice ou le contenu contiennent ces mots**.

Quelle que soit la description d'un ouvrage (titre, notice, contenu
textuel), c'est un texte. On suppose donc avoir un grand nombre de
contenus textuels, éventuellement longs, dans lesquels chercher.  Par
conséquent, une **recherche séquentielle peut prendre un temps de
calcul trop grand**. Plutôt que de parcourir l'ensemble des documents
à chaque requête, l'idée est de le faire une fois et de construire une
nouvelle représentation de l'ensemble des textes. Cette représentation
permet alors de répondre très rapidement aux requêtes. Cette phase de
prétraitement est appelée **indexation** et la représentation est une
structure de données appelée **index**.  Nous expliquons cette étape
d'indexation puis nous expliquons comment calculer des requêtes
efficacement.

Chaque texte est découpé en une séquence d'unités élémentaires appelés
`tokens` qui sont des suites de caractères sans espace et sans symbole
de ponctuation. Pour simplifier, on peut penser à un token comme étant
un mot mais il peut y avoir aussi des nombres, des dates, ... Par
exemple, un texte comme `La Révolution française, 1789-1799 : Une
histoire socio-politique` sera transformé en la séquence `La
Révolution française 1789 1799 Une histoire socio politique`. Enfin,
différents traitements peuvent être considérés comme : considère-t-on
différemment les majuscules et les minuscules ?  considère-t-on les
accents ? Sur notre exemple, si on ne prend pas en compte les
majuscules et si on conserve les accents, on arriverait au texte `la
Révolution française 1789 1799 une histoire socio politique`. Ces
choix étant effectués, les textes sont désormais des suites de
mots. On considère alors l'ensemble des tous les mots apparaissant
dans la base de textes ce qui définit un **dictionnaire ou
vocabulaire** qui est l'ensemble des mots qui vont être considérés
dans les requêtes. Parfois, les mots très fréquents de la langue
utilisée comme `et`, `le`, ... en français sont retirés du
dictionnaire.

Le dictionnaire étant choisi, pour chaque mot du dictionnaire, on peut
construire la liste des documents qui contiennent ce mot. Cette liste
est ordonnée par identifiant de documents croissants. Par exemple, on
mémorise que le mot `rose` apparaît dans les documents de numéro 125,
245, 567, ... ; que le mot `blanche` apparaît dans les documents de
numéro 117, 176, 245, 312, ... Enfin, la dernière chose à considérer
est de pouvoir trouver rapidement un mot du dictionnaire avec la liste
des documents associée car la taille d'un dictionnaire est de l'ordre
de quelques centaines de milliers de mots. Pour cela, les
informaticiens ont défini différentes méthodes d'accès rapides. Par
exemple, on trie le dictionnaire dans l'ordre lexicographique (ordre
usuel des mots d'un dictionnaire). On peut alors accéder rapidement à
un mot avec l'algorithme suivant illustré en cherchant le mot `rose` :
on regarde le mot au milieu du dictionnaire, c'est `maman`, donc on
cherche dans la seconde moitié ; on regarde le mot au milieu de la
seconde moitié, c'est `savant`, donc on cherche entre `maman` et
`savant` ; jusqu'à trouver le mot `rose`. On peut montrer qu'un tel
algorithme est très efficace. Pour un dictionnaire de 500 000 mots, il
suffit d'effectuer 19 accès, pour une dictionnaire de 1 million de
mots, il suffit d'effectuer 20 accès. On parle de *complexité
logarithmique* car si la taille du dictionnaire double, on ne doit
faire qu'un accès supplémentaire !  Nous avons défini l'indexation et
supposons avoir construit un index défini comme suit :

> Un **index** est constitué d'un dictionnaire avec une méthode
> d'accès rapide à un mot, et, pour chaque mot, on dispose de la liste
> ordonnée par identifiant croissant des documents qui contiennent ce
> mot.

Rappelons que l'objectif est de trouver l'ensemble des textes
contenant les mots de la requête.

- Pour *une requête à un mot clé*, c'est très facile avec l'index :
chercher le mot dans le dictionnaire, renvoyer la liste des documents
associée dans l'index.
- Pour *une requête à deux mots clés*, on procède comme suit :
chercher le premier mot dans le dictionnaire, se mettre au début de la
liste des documents associée, chercher le deuxième mot dans le
dictionnaire, se mettre au début de la liste des documents associée,
parcourir les deux listes et mettre en résultat les documents dont les
numéros apparaissent dans les deux listes. Par exemple, considérons la
requête à deux mots clés `rose` et `blanche`, on trouve la liste 125,
245, 567, ... pour `rose`, on trouve la liste 117, 176, 245, 312,
... pour `blanche`, dans la liste résultat on trouvera 245 et
éventuellement d'autres documents.
- Ces principes peuvent être étendus pour des requêtes à plusieurs
mots clés et même avec des requêtes contenant des opérateurs logiques
`OU` et `NON`.
- Les interfaces proposent également des *requêtes par position*. Les
**requêtes par phrase** sont souvent exprimées avec des guillemets
comme la requête `"rose blanche"`. On recherche alors les documents
qui contiennent les mots à deux positions consécutives. Ceci peut être
réalisé en mémorisant dans l'index la position auxquelles apparaissent
les mots. Il existe également des requêtes par position comme : les
deux mots cherchés doivent être distants de moins de 3 mots.

Les systèmes étudiés jusqu'à présent dans ce module renvoient une
liste de documents qui satisfont une propriété. C'est pour cette
raison qu'on parle de modèle Booléen car la réponse est `VRAI` ou
`FAUX` selon que le document satisfait ou ne satisfait pas la requête.
Vous êtes habitués à la recherche sur le Web où on attribue des scores
aux documents. Nous introduisons donc la notion de score de pertinence
qui mesure la proximité entre un document et une requête.

## Le modèle vectoriel : attribuer un score de pertinence aux documents

On suppose toujours un grand ensemble de documents dont chacun d'eux
possède un identifiant. On suppose que chaque document est une suite
de mots d'un dictionnaire. On suppose avoir construit un index. On
considère une requête à plusieurs mots clé, nous allons expliquer
comment **renvoyer une liste de documents ordonnée par un score de
pertinence relativement à une requête**.  Pour cela, nous allons voir
comment on représente un document et une requête par des vecteurs et
comment un calul sur ces vecteurs définit un score de pertinence.

### Représenter des documents par des vecteurs

Un document est une suite de mots du dictionnaire. La plus simple des
représentations vectorielles, appelée **Boolean frequency**, consiste
à représenter un document par un (très grand) vecteur où chaque
composante du vecteur correspond à un mot du dictionnaire et la valeur
est 1 si le mot apparaît dans le document et 0 sinon. Prenons
l'exemple d'un dictionnaire contenant les mots de langue française et
du document textuel `citoyennes tricoteuses - les femmes du peuple à
paris pendant la révolution française`. Ce document sera représenté
par un vecteur avec une composante par mot du dictionnaire et toutes
les composantes valent 0 sauf les composantes pour les mots `à`,
`citoyennes`, ..., `tricoteuses` qui valent 1. On mémorise donc la
*présence ou l'absence* d'un mot du dictionnaire dans le document.

La seconde, appelée **Term frequency**, représente, de le même façon,
un document par vecteur mais la valeur est le nombre d'occurrences
(d'apparitions) du mot dans le document. Par exemple, considérons le
document `réflexions sur la révolution de france suivi d'un choix de
textes de burke sur la révolution`.  Il sera représenté par un vecteur
avec une composante par mot du dictionnaire et toutes les composantes
valent 0 sauf les composantes pour les mots `réflexions`, `france` qui
valent 1 et les composantes pour les mots `la`, `révolution` et `sur`
qui valent 2 car ils apparaissent deux fois.

Mais, lorsque vous écrivez des requêtes sur le web, vous savez que des
mots trop fréquents vont vous retourner trop de réponses donc vous
essayez d'exprimer votre requête avec *des mots ou termes plus
pertinents ou plus discriminants* dans le sens où vous savez qu'il y a
moins de documents contenant ces mots. Pour tenir compte de ceci, on
peut intégrer dans la représentation vectorielle un facteur qui dépend
de la fréquence du mot dans la base de documents. C'est la
représentation **term frequency -- inverse document frequency
(tf-idf)**. Dans cette représentation, on multiplie la fréquence
d'apparition (le tf pour term frequency) par un facteur (l'idf ou
inverse document frequency). Nous ne donnons pas la définition
mathématique de l'idf mais il suffit de retenir que l'idf d'un mot

- est *grand pour un mot rare*, i.e. qui apparaît dans peu de documents
- est *petit pour un mot fréquent*, i.e. qui apparaît dans beaucoup de
  documents

Par conséquent, la multiplication par l'idf va augmenter la valeur
pour les mots rares de la collection et la diminuer pour les mots
fréquents. Par exemple, considérons le --très petit-- document `la
révolution française`. Sa représentation tf avec les fréquences aurait
1 pour le mot `la`, 1 pour le mot `révolution` et 1 pour le mot
`française`. Sa représentation tf-idf aurait une valeur très petite
pour le mot `la` (car la est très fréquent) disons 0,01, moyenne pour
le mot `française` disons 0,14 et plus grande pour le mot `révolution`
disons 0,25 (révolution est le moins fréquent des 3 mots). La
représentation tf-idf permet donc de renforcer la valeur pour les
mots qui apparaissent dans peu de documents ce qui va aider à trouver
les documents les plus pertinents.

Il existe de nombreuses variantes de ces représentations vectorielles
qui ont été étudiées et dont on a comparé les performances en
recherche d'information. 

### Score de pertinence entre un document et une requête

Il faut définir une similarité entre un document et une requête
composée de plusieurs mots clé. Intuitivement, un document sera
similaire à une requête si il contient les mots de la requête et si
ses mots apparaissent fréquemment. Un document contenant un mot de la
requête qui apparaît dans peu de documents doit aussi voir son score
renforcé. Pour cela, on représente, en général, un document
avec la représentation tf et la requête avec la représentation
tf-idf. Plusieurs mesures de pertinence ont été introduites mais une
des plus utilisées que nous expliquons ici est la **Cosine
similarity** qui consiste à calculer le cosinus de l'angle entre les
vecteurs représentant la requête et le document. Le calcul consiste à
multiplier les composantes deux à deux et à faire la somme. Comme la
requête est un petit document, toutes les composantes du vecteur
associé sont nulles sauf pour les mots de la requête donc seuls les
mots de la requête sont utiles pour le calcul ce que nous illustrons
par l'exemple suivant.

- la requête `la révolution française` avec la représentation tf-idf
est représenté par le vecteur (0,01 ; 0,25 ; 0,14) où les composantes
correspondent dans l'ordre aux mots `la`, `révolution` et `française`
et 0 pour tous les autres mots du dictionnaire.
- le document `l'économie française dans la compétition internationale
au XXe siècle` avec la représentation tf est représenté par le vecteur
(1 ; 0 ; 1) où les composantes correspondent dans l'ordre aux mots
`la`, `révolution` et `française`. Son score, relativement à la
requête `la révolution française` est donc : 1x0,01 + 0x0,25 + 1x0,14
= 0,15
- le document `citoyennes tricoteuses - les femmes du peuple à paris
pendant la révolution française` avec la représentation tf est
représenté par le vecteur (1 ; 1 ; 1). Son score est donc : 1x0,01 +
1x0,25 + 1x0,14 = 0,40
- le document `réflexions sur la révolution de france suivi d'un choix
de textes de burke sur la révolution` avec la représentation tf est
représenté par le vecteur (2 ; 2 ; 0). Son score est donc : 2x0,01 + 2x0,25 +
0x0,14 = 0,52

On voit sur cet exemple que le score mesure bien la pertinence des
documents relativement à la requête. On voit également que l'usage du
tf-idf permet de privilégier le mot `révolution` qui est celui qui
apparaît dans le moins de documents et de limiter l'influence du mot
`la` qui ne sert pas à discriminer les documents pertinents. Le calcul
de la Cosine similarity est, en réalité, un peu plus compliqué car il
faut prendre en compte la longueur des documents. En effet, il faut
interdire la tricherie qui consisterait à répéter beaucoup de fois
certains mots dans des documents avec pour seul objectif d'obtenir un
meilleur score. Le calcul de la pertinence fait donc intervenir une
normalisation qui revient à considérer une même longueur pour tous les
documents.


# Recherche d'information sur le Web

Nous avons présenté l'indexation et la calcul de score de pertinence
d'un document textuel relativement à une requête. Nous allons voir
comment ce score est adapté aux documents du Web. Nous présentons
ensuite le score de notoriété qui mesure l'importance d'une page
Web. C'est ce score introduit par Google qui a donné un avantage
significatif à `Google` dans les années 1990. La combinaison de ces
deux scores est la base du score d'un document Web relativement à une
requête.

## Indexation du web

Pour calculer un score de pertinence, il faut au préalable que les
documents du Web soient indexés. Nous présentons quelques points
essentiels :


- L'**indexation du Web** est réalisé par des **programmes appelés
robots** qui parcourent les sites Web et suivent les liens. Ces
programmes récupèrent les informations utiles comme les mots qui
apparaissent, leur nombre d'apparitions, entre autres.
- **Tous les documents du Web sont indexés** quel que soit leur format :
  pages Web au format `html`, documents imprimables au format `pdf`,
  documents au format `doc`, ... ce qui mène à un nombre de documents
  de l'ordre de 60 000 milliards en 2016.
- **Tous les mots qui apparaissent sur le Web sont indexés** ce qui amène
  à un dictionnaire contenant plusieurs millions de mots.
- Ceci permet de construire un **index de très grande taille** qui est
  mis à jour régulièrement avec les informations récupérées par les robots
- L'index est réparti sur des fermes de calcul (un grand nombre
  d'ordinateurs de grande capacité en réesau) réparties dans le monde
  entier. On peut noter que celà implique une très grande consommation
  d'énergie et donc le Web n'est pas si écologique qu'on pourrait le
  croire.

## Score de pertinence

Considérons un document du Web -- une page web -- au format `html`. Un
tel document a un contenu mais aussi une structure avec un titre
principal et des sections ayant des titres. L'apparition d'un mot de
la requête dans un titre est plus important que son apparition dans le
contenu. Ceci doit donc être pris en compte dans le calcul de
pertinence. Un deuxième élément qui est spécifique au Web concerne les
liens (ou hyperliens). En effet, lorsqu'un lien sur une page web est
créé, il est associé à un texte qui contient de l'information sur la
page. Par exemple, un site Web qui souhaite mettre un lien sur ce
module définira un texte cliquable comme `cours d'introduction à la
recherche information` qui est très informatif sur le contenu de la
page et doit être pris en compte pour le calcul de pertinence.

Par conséquent, le score de pertinence d'une page web va prendre en
compte des scores de pertinence calculés sur **différentes vues sur la
page Web** dont les principales sont :

- le contenu textuel de la page
- les titres de la page
- les mots clé associés à la page et définis dans son entête
- l'adresse du document (un texte de la forme
  `https://culturenumerique.univ-lille3.fr/modulerechercheinformation.html`)
- les textes des liens qui pointent sur la page

Pour chacune de ces vues, un score de pertinence peut être calculé
avec la méthode introduite auparavant. Il reste à combiner ces scores
avec une formule de la forme : un pourcentage du score de contenu + un
pourcentage du score des titres + ... **La formule de combinaison est
secrète !**, c'est-à-dire que l'on ne connaît pas les pourcentages
utilisés dans la formule. On sait qu'elle existe et qu'elle
évolue. Par exemple, l'influence du score de pertinence des mots clés
a été nettement diminuée suite à de nombreux abus de concepteurs de
pages Web qui ajoutaient des mots clé fictifs sur leur page pour
essayer d'améliorer artificiellement leur score, et donc on sait que
le pourcentage pour le score de pertinence des mots clé a été diminué.

## Score de notoriété

Le Web a une structure de réseau ou de graphe avec des pages Web qui
pointent les unes vers les autres avec les hyperliens. L'idée est
d'utiliser cette structure pour mesurer la **notoriété** des pages. On
souhaite donc un **score de notoriété** qui va mesurer à quel point
une page est importante les internautes. Une première tentative de
définition de score de notoriété d'une page pourrait être le nombre de
pages qui pointent sur elle. Cette définition n'est pas robuste car on
peut tricher (cela a été fait) : pour renforcer le score de notoriété
de ma page, je crée des (beaucoup) de pages artificielles qui pointent
sur ma page. La définition doit donc être plus intelligente et la
bonne définition est la suivante :

> Une page a **une forte notoriété** si beaucoup de pages **ayant une
> forte notoriété** pointent sur elle

Définir la notoriété n'est pas si simple car on voit que pour définir
une page de forte notoriété il faut déjà savoir calculer la
notoriété. C'est un exemple de définition récursive où on définit la
notoriété à partir d'elle-même. Mais ceci est fréquent en mathématique
et en informatique. Il est donc possible de définir des objets
mathématiques, des calculs et des algorithmes qui vont permettre de
définir et de calculer la notoriété d'une page Web. Nous allons donner
une autre vision de la notoriété avec la notion de **surfeur
aléatoire**. L'idée est d'imaginer qu'un surfeur se promène sur le
Web. Pour cela,

- il peut choisir une page au hasard sur le Web ce qui correspond à
émettre une requête, choisir un lien pour arriver à une page
- lorsqu'il est sur une page Web, il peut choisir et suivre un des
  liens présents sur la page d'où le nom de surfeur car il surfe sur
  le web

Le surfeur aléatoire choisit donc une page au hasard, il suit des
liens en partant de cette page puis recommence en rechoisissant une
nouvelle page au hasard. Si on répète un très grand nombre de fois
cette opération, toutes les pages Web seront visitées et plus souvent
elles sont visitées plus elles sont importantes. Le score de notoriété
d'une page correspond donc à la fréquence de visite de cette page par
le surfeur alétaoire. Ceci peut être modélisé de façon mathématique et
calculé par des algorithmes. Un algorithme pour calculer le score de
notoriété, appelé **algorithme PageRank**, a été introduit par les
fondateurs de Google au milieu des années 1990. Cet algorithme permet
d'**attribuer à toute page web un score de notoriété**.

C'est, en réalité, une amélioration de cet algorithme qui est utilisé
pour lequel on distingue deux types de pages : les *"hubs"* et les
*"authorities"*. Un hub est une page qui contient beaucoup de liens
comme une page de synthèse sur un sujet qui renvoie à toutes les pages
sur ce sujet. Une authority est une page de référence sur laquelle
beaucoup de pages pointent. Un exemple typique, dans le domaine des
conaissances générales, est une page `Wikipedia`. On peut alors
calculer un score de hub et un score d'authority et combiner ces deux
scores pour obtenir un score de notoriété.

## Score Web

Une requête sur le Web dans un moteur de recherche d'information est
très souvent exprimée comme une suite de mots clés. Le **score Web
d'un document Web relativement à une requête** est calculé comme une
combinaison de la forme : un pourcentage du score de pertinence de la
page relativement à la requête + un pourcentage du score de notoriété
de la page. Ici encore la formule de combinaison n'est pas connue !
Ici encore, on sait qu'elle existe et qu'elle évolue. Par exemple, on
observe que le score de notoriété a pris ces dernières années une
importance de plus en plus grande car les pages les mieux classées ont
souvent une forte notoriété comme les pages Wikipedia, des pages de
sites de journaux et, plus généralement, des pages de sites de
référence.

Rappelons également qu'il existe différents moteurs de recherche
d'information comme, par exemple, `Qwant` et `Google`. Chaque moteur a
développé ses propres algorithmes et ses propres formules de calcul
basés sur la pertinence et la notoriété.  On peut penser à des
recettes de cuisine utilisant les mêmes ingrédients mais avec des
proportions et des modes de cuisson différents. Il est donc important
de retenir que **les réponses et leur ordre à une même requête
diffèrent selon le moteur choisi**.

Si les deux éléments essentiels sont le score de pertinence et le
score de notoriété, le score Web fait intervenir d'autres éléments
sans qu'on sache exactement comment ils interviennent dans le calcul
du score web. Les éléments principaux intervenant dans le calcul sont :

- la langue d'interrogation
- le pays du site du moteur
- le media d'interrogation (ordinateur ou téléphone portable)

D'autres éléments comme la localisation du media d'interrogation et
l'historique des recherches et des liens suivis peuvent être pris en
compte mais nous y reviendrons dans la conclusion. Retenez que **le
score Web est calculé à partir de la pertinence et de la notoriété et
de nombreux autres éléments**. Il faut également être conscient que
**les algorithmes de calcul de score évoluent continuellement** et
donc les réponses et leur ordre à une moment donné ne seront peut-être
pas identiques un mois plus tard.

La plupart des requêtes posées sur le Web sont des requêtes avec une
suite de mots clés mais un autre type de requête correspond aux
requêtes par phrase. Rappelons qu'une requête par phrase consiste à
rechercher les documents contenant exactement la phrase saisie. La
convention usuelle est de mettre la phrase entre guillemets dans la
barre de saisie. Par exemple, on peut considérer la requête par phrase
`"la révolution française"`. Pour cette requête, on va retourner par
ordre de pertinence les documents contenant les trois mots
consécutifs. Notez que cette requête donnera donc des résultats
différents de la requête à trois mots clé `la révolution française`
pour laquelle la position des mots n'intervient pas. Pour être capable
de répondre aux requêtes par phrase, l'index contient également les
positions des mots dans les documents où ils apparaissent. Souvent il
existe aussi des possibilités de requête avancée qui sont très peu
utilisées en pratique.

# Evolutions, conclusion et discussion

## Evolutions en cours

### Adaptation à l'utilisateur

Les langues naturelles sont ambigues et un mot peu avoir plusieurs
sens. Le mot `java` peut désigner une danse ou un langage de
programmation. Un internaute informaticien souhaiterait voir
apparaître des pages parlant du langage de programmation alors qu'un
autre utilisateur préférera des informations sur la danse. Même si un
mot n'est pas ambigue, un utilisateur préférera des sites
d'information, un autre des articles scientifiques, un autre encore
des blogs. Il semble pertinent d'adapter les réponses du moteur aux
préférences de l'utilisateur. Ceci peut être réalisé si l'historique
des recherches et des liens suivis est connu. Lorsque vous avez un
compte et que vous êtes identifiés, le moteur peut mémoriser cet
historique des recherches et des navigations et l'utiliser pour
adapter son calcul de score. Ceci est réalisé par certains moteurs
mais, ici encore, les formules et algorithmes utilisés ne sont pas
connus. Notes bien que cette **adaptation à l'utilisateur se fait avec
la contrepartie de la connaissance complète de votre historique de
navigation** par le moteur.

Un autre type d'adaptation est d'utiliser les **informations de
géolocalisation** lorsque vous utilisez un téléphone portable et que
vous avez activé la géolocalisation. Le score des pages portant sur
des objets proches de vous peut alors être renforcé. Ici encore, les
algorithmes sont spécifiques à chaque moteur et ne sont pas
connues. Notez également que toutes les informations de
géolocalisation sont connues et peuvent être historisées.

### Web des données

Une évolution, apparue en 2014, est que lorsque vous tapez le nom
d'une entité du monde que ce soit un groupe de musique (essayez `Led
Zeppelin`), un personnage célèbre (essayez `Larry Page`), un lieu
géographique (essayez `Middelburg`) ou encore un nom de fleur (essayez
`rose`), vous voyez apparaître en résultat à votre requête un cadre
présentant des informations factuelles sur l'entité. Par exemple, pour
`Led Zeppelin`, vous trouvez une description du groupe, sa
composition, le genre de musique, les principales chansons, les
principaux albums, ... Donc, contrairement au résultat qui fournit des
liens vers des pages, ici on **extrait des données sur
l'entité**. Ceci est rendu possible grace au *Web des données et
connaissances* encore appelé *"knowledge graph"*.

Le Web et les moteurs de recherche d'information étaient jusqu'alors
destinés à des utilisateurs humains qui posaient des requêtes et
allaient consulter les pages en fonction des résultats. Pour trouver
une réponse à une question factuelle comme `âge des candidats à la
présidence aux élections françaises en 2017`, il faut taper une
requête et chercher la réponse sur la bonne page. On a souhaité
enrichir les capacités des moteurs pour qu'ils soient capables de
répondre à une telle question factuelle. Il faut donc connaître l'âge
des candidats. Vous pouvez taper une requête comme `âge de X` où vous
remplacez X par votre candidat préféré ou détesté pour vérifier que la
réponse est connue et affichée. Un deuxième objectif que nous verrons
dans la section suivante est que si on souhaite résoudre des tâches
plus complexes sur le Web, il faut que les machines sachent extraire
les données, les comprennent et les utilisent. Pour cela, s'est
développé le Web des données et connaissances.

Ceci a été réalisé conjointement par des communautés spécialisées
comme en musique avec `MusicBrainz` ou en géographie avec `GeoNames`,
des communautés d'utilisateurs et de chercheurs pour des bases
généralistes avec `Wikidata` et `DBpedia`, des bases pour normaliser
la description des données avec `foaf`. L'idée est de construire des
bases de données de connaissances exploitables sur le Web. Les données
sont décrites sous forme de triplets de la forme **(sujet, propriété,
objet)** comme, par exemple, `(Led Zeppelin, IsA, MusicGroup` ou
`(Jimmy Page, IsMemberOf, Led Zeppelin)` qui peuvent être vues comme
des phrases de la forme verbe sujet complément énonçant des faits
comme `Led Zeppelin est un groupe de musique` et `Jimmy Page est
membre de Led Zeppelin`. Ces bases de données ont été construites par
des communautés et sont désormais utilisées voire possédées par les
grands acteurs du domaine comme `Google`. Des algorithmes sur ces
bases de données permettent de chercher des informations et on pourra,
par exemple, rechercher les informations factuelles sur `Led Zeppelin`
qui pourront être affichés dans l'encadré sur la page de réponses à la
requête.

Une autre source de données est issue des pages Web construites par
les utilisateurs du Web. Par exemple, un site web de restaurant va
ajouter sur sa page Web des données comme sa latitude et sa longitude
ou encore des heures et jours d'ouverture. Ces données doivent
respecter des conventions d'écriture  en `html`. Elles peuvent
alors être utilisées par des programmes (comme le navigateur) pour
calculer des distances et donc savoir si le restaurant est proche de
votre géoloalisation ou encore pour savoir si le restaurant est ouvert
pour vous le recommander.

### Moteurs intelligents

Si les moteurs de recherche d'information sont capables de vous
suggérer des pages Web en réponse à une requête et de récupérer des
données relatives à une question factuelle, ils sont encore**
incapables de raisonner**. Pour nous en convaincre, supposons que vous
souhaitiez aller passer en week-end à Paris. Vous allez utiliser un
moteur de recherche d'information pour rechercher des horaires et
tarifs de train ou d'avion ou de bus, éventuellement en utilisant des
comparateurs, ou encore voir sur un site de covoiturage. Vous allez
chercher une auberge de jeunesse, une chambre en résidence, un hôtel
pour la nuit. Vous allez, éventuellement, rechercher des expositions,
des spectacles, des musées pour vous occuper. Le moteur vous aide mais
*l'intelligence c'est vous !* Vous savez que pour vous rendre à Paris,
il faut utiliser un moyen de transport, vous savez que les moyens de
transport principaux sont le bus, le train, l'avion. Vous avez une
connaissance du monde que ne possède pas la machine. Le Web des
données a pour objectif d'apporter cette connaissance du monde eux
machines et aux programmes. Mais cette connaissance n'est pas
suffisante car il faut savoir l'utiliser et raisonner. Par exemple,
pour choisir les meilleures options en fonction du lieu où vous
résidez et de vos préférences. Raisonner pour, par exemple, être
capable de chosir et d'enchaîner les transports pour, par exemple, si
je choisis le train, se rendre à la gare avec un moyen de transport et
un timing adéquat. De même pour me rendre de la gare d'arrivée au site
de résidence choisi. Pour l'heure, les moteurs ne sont pas capables de
répondre à des requêtes comme `Organise moi un week end à Paris`.

Cependant, il devient possible d'interroger votre ordinateur par la
parole. Une première couche logicielle se charge de transformer les
signaux acoustiques en une suite de mots de la langue utilisée. Pour
un moteur de recherche d'information ceci amène à une requête
textuelle en langage naturel. Vous pouvez d'ailleurs taper directement
une telle requête dans la barre de saisie. Nous avons déja évoqué des
requêtes comme `Quel est l'âge de François Hollande ?`. Comment est
traité cette requête ? Tout d'abord, il y a des traitements pour
reconnaître que c'est une question, le verbe, le sujet, le
complément. Tous ces traitements ne sont pas connus et ils évoluent
constamment car le nombre de questions auxquelles le moteur peut
répondre grandit sans cesse. Lorsque ces traitements sont réalisés le
moteur interroge le Web des données et le graphe du Web pour apporter
réponse factuelle à la question et une liste de liens. Pour cette
liste de liens, il est difficile de savoir comment sont calculés les
scores de pertinence à cause des pré-traitements inconnus et du calcul
de score dont nous avons déja signalé que beaucoup de points étaient
secrets. Si on considère une requête comme `quels sont les cinémas
proches ?`, le problème est plus difficile car il faut comprendre la
sémantique du mot proche, en déduire qu'il faut calculer des distances
à partir d'un point à choisir et adapter les réponses en
conséquence. Le traitement des requêtes en langage naturel progresse
mais toutes les questions sont loin d'être résolues.

## Conclusion et discussion

### Les liens payants

La fenêtre de réponse contient une liste ordonnée par score de
partinence de l'ensemble des pages Web et éventuellement un cadre
contenant des données factuelles relatives à la requête dont nous
avons déja parlé dans ce cours. Vous avez également souvent une liste
ordonnée de **liens sponsorisés**. Pour ces liens, seules apparaissent
des entreprises qui rémunèrent l'entreprise associée au moteur de
recherche d'information. La rémunération peut être calculée sur le
nombre d'utilisateurs cliquant sur les liens proposés. Retenez donc
que **l'apparition dans une liste de liens sponsorisés est lié à une
rémunération**.

### Le secret des moteurs

Nous avons vu dans ce cours que les formules de calcul de score pour
un moteur de recherche d'information sont secrètes même si on en
connaît les éléments principaux. De plus, ces formules évoluent et
avec les évolutions comme le langage naturel, la compréhension du
calcul du score et donc de l'ordre des réponses devient de plus en
plus complexe. Retenez que **l'ordre des réponses est donné par un
algorithme secret écrit par une entreprise commerciale**.

Ceci pose des *questions éthiques* car les réponses proposées et leur
ordre peuvent influencer votre vision sur une question et peuvent
influencer vos achats. Certains militent pour que les formules de
calcul de score soient publiées pour que l'utilisateur sache pourquoi
certaines pages lui sont proposées plutôt que d'autres.  La réponse
est souvent de dire que la diffusion de ces formules permettraient de
tricher plus facilement. Il faut savoir que, même avec des formules
secrètes, il existe une forte concurrence entre les sites sur la
question du référencement, c'est-à-dire sur la question d'être bien
classé dans l'ordre des réponses. C'est le cas des entreprises
commerciales qui veulent apparaître pour vous vendre des
produits. C'est le cas de courants de pensée qui veulent imposer une
opinion comme, par exemple, les courants anti-avortement qui luttent
pour que les sites critiquant l'avortement apparaissent bien classés
lorsque vous faîtes une requête sur l'avortement. Retenez que **vous
devez toujours avoir un regard critique sur les réponses qui vous sont
proposées et leur ordre**. Ceci est vrai pour les moteurs de recherche
d'information mais aussi pour beaucoup d'applications Web vous
suggérant ou vous recommandant des produits, des contacts, des
informations, des restaurants et autres.

Enfin, beaucoup de logiciels sur le Web disent s'adapter à vos
besoins. Ils s'adaptent en réalité à votre profil qui est construit à
partir de toutes les données qui ont pu être récupérées par le
logiciel à votre inscription mais aussi auprès de logiciels
partenaires mais surtout de toutes vos données historiques
correspondant à toutes vos actions. Ces données sont donc mémorisées
par l'entreprise concevant le logiciel et peuvent même être revendues
à d'autres éditeurs de logiciel. De même, l'adaptation à votre
localisation nécessite que vos données de géolocalisation soient
utilisées et donc soient mémorisées. Retenez donc que **l'adaptation à
votre profil et à votre localisation implique la mémorisation de
données personnelles historiques**.

# Le référencement

Nous ne parlons ici que du **référencement naturel** qui correspond
aux liens non sponsorisés contrairement au **référencement payant**
qui correspond aux liens sponsorisés. Nous avons vu que, pour de
bonnes ou de mauvaises raisons, il est important d'apparaître bien
classé en réponse à des requêtes mais nous nous plaçons dans le cas de
bonnes raisons. La **lecture de cette section est
facultative**. Considérons que vous êtes responsable d'une association
et que vous souhaitez que son site Web soit bien classé, c'est-à-dire
bien référencé, c'est-à-dire encore qu'un utilisateur va pouvoir
trouver le site de votre association.

## Une bonne indexation des documents

Pour assurer celà, il faut que le site Web soit bien conçu et facilite
la visite des robots qui indexent le Web. Ceci est du ressort du
gestionnaire du site Web et correspond à un certain nombre de
préconisations techniques à respecter comme : nom unique du site, pas
de lien menant sur une page inexistante, respect des normes `html`,
fourniture d'un plan du site, pages simples à téléchargement rapide,
format des pages adaptés au media d'interrogation. 

## Un bon score de pertinence

Il faut préciser les mots importants pour lesquels vous souhaitez être
trouvés. Lorsque ces mots sont choisis, il est important de les faire
figurer au bon endroit : dans l'adresse de la page, dans le titre de
la page, dans les titres de section, dans les mots clé, dans le
contenu. Bien évidemment ceci doit être fait en gardant un document
bien structuré, clair et agréable à lire. Notez qu'un tel contenu va
inciter à mettre des liens sur vos pages avec les bons mots dans les
textes des liens.

## Un bon score de notoriété

Il faut pour cela que beaucoup de pages à forte notoriété pointent sur
vous. Ceci doit être réalisé sans tricher. Vous pouvez mettre des
liens internes à votre site qui peuvent renforcer le score de
notoriété de certaines pages. Vous pouvez suggérer à des associations
partenaires de mettre des liens vers vos pages. Mais l'essentiel est
d'avoir un contenu intéressant dans votre site qui incite d'autres
usagers du Web à créer des liens vers vos pages.

En conclusion, pour être bien référencé l'important est d'avoir **un
site bien conçu avec un contenu structuré clair et pertinent**.
