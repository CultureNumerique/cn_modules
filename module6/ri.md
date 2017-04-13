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
relativement à une requête composée de plusieurs mots. Nous commeçons
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
complexes. On peut introduire des jokers souvent notés `*`, + et ? où
le `*` représente une suite de caractères quelconque, le `+` une suite de
caractères non vide et le `?` n'importe quel caractère. Par exemple, la
requête `pa*on` est satisfaite par des mots comme `paon`, `pantalon`
ou `passion` ; ces deux derniers mots satisfont la requête `pa+on`
alors que `paon` ne la satisfait pas ; la requête `pap?` est
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

C'est le cas d'un recherche dans un fond documentaire comme une
bibliothèque. On dispose d'un grand nombre d'ouvrages et on recherche
un ouvrage par l'intermédiaire d'une requête dans un formulaire.  Les
ouvrages sont représentés par des notices écrites par des
documentalistes et contenant le titre, les auteurs, les éditeurs, des
mots-clés, un résumé, ... Parfois, les ouvrages ont été numérisés et
on dispose alors aussi de leur contenu textuel et on pourra aussi
rechercher dans ce contenu textuel (on parle parfois de recherche
plein texte). Chaque ouvrage possède un *identifiant*, c'est-à-dire un
numéro qui identifie le document. Nous considérons, dans un premier
temps, des requêtes à un ou plusieurs mots clé. Dans le modèle
Booléen, le système de recherche d'information doit renvoyer
**l'ensemble des ouvrages dont la notice ou le contenu contiennent ces
mots**. Parfois, on peut restreindre la requête à chercher seulement
dans les titres. 

Quelle que soit la description d'un ouvrage (titre, notice, contenu
textuel), c'est un texte. On suppose donc avoir un grand nombre de
contenus textuels, éventuellement longs, dans lesquels chercher.  Par
conséquent, une **recherche séquentielle est impossible** pour des
raisons de temps de calcul. Plutôt que de parcourir l'ensemble des
documents à chaque requête, l'idée est de le faire une fois pour
construire une nouvelle représentation de l'ensemble des textes qui
permette ensuite de répondre très rapidement aux requêtes. La phase de
prétraitement est appelée **indexation** et amène à la construction
d'une structure de données appelée **index** qui permettra de faire
ces recherches rapides.  Nous expliquons cette étape d'indexation qui
peut être décomposée en une phase de prétraitement des documents, la
constitution d'un dictionnaire et la construction d'un index. Nous
expliquons ensuite comment calculer des requêtes efficacement.

Chaque texte est découpé en une séquence d'unités élémentaires appelés
`tokens` en utilisant les espaces et les ponctuations. On peut penser
à un token comme étant un mot mais il peut y avoir aussi des nombres,
des dates, ... Enfin, différents traitements peuvent être considérés
comme : considère-t-on différemment les majuscules et les minuscules ?
considère-t-on les accents ? ... Selon les choix, on effectue les
traitements adéquats. Par exemple, si on ne tient pas compte de la
casse, on va transformer tous les mots comme des chaînes de
minuscules. Ces choix étant effectués, les textes sont désormais des
suites de mots. On considère alors l'ensemble des mots duquel on
enlève parfois les mots très fréquents de la langue utilisée comme
`et`, `le`, ... en français et ceci définit un **dictionnaire ou
vocabulaire** qui est l'ensemble des mots qui vont être considérés
dans les requêtes.

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
exemple, si on trie le dictionnaire dans l'ordre lexicographique alors
on peut accéder rapidement à un mot avec l'algorithme suivant illustré
en cherchant le mot `rose` : on regarde le mot au milieu du
dictionnaire, c'est `maman`, donc on cherche dans la seconde moitié ;
on regarde le mot au milieu de la seconde moitié, c'est `savant`, donc
on cherche entre `maman` et `savant` ; jusqu'à trouver le mot
`rose`. On peut montrer qu'un tel algorithme est très efficace. Pour
un dictionnaire de 500 000 mots, il suffit d'effectuer 19 accès, pour
une dictionnaire de 1 million de mots, il suffit d'effectuer 20
accès. On parle de *complexité logarithmique* car si la taille du
dictionnaire double, on ne doit faire qu'un accès supplémentaire !
Nous avons défini l'indexation et supposons avoir construit un index
défini comme suit :

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
- Les interfaces proposent souvent également des *requêtes par
position*. Les **requêtes par phrase** sont souvent exprimées avec des
guillemets comme la requête `"rose blanche"`. On recherche alors les
documents qui contiennent les mots à deux positions consécutives. Ceci
peut être réalisé en mémorisant dans l'index la position auxquelles
apparaissent les mots. Il existe également des requêtes par position
comme : les deux mots cherchés doivent être distants de moins de 3
mots.

Les systèmes étudiés jusqu'à présent dans ce module renvoient une
liste de documents qui satisfont une propriété. C'est pour cette
raison qu'on parle de modèle Booléen car la réponse est `VRAI` ou
`FAUX` selon que le document satisfait ou ne satisfait pas la requête.
Vous êtes habitués de la recherche sur le Web où on attribue des
scores aux documents et nous allons donc maintenant introduire la
notion de score de pertinence qui mesure la proximité entre un
document et une requête. 

## Le modèle vectoriel : attribuer un score de pertinence aux documents

On suppose toujours un grand ensemble de documents dont chacun d'eux
possède un identifiant. On suppose que chaque document est une suite
de mots d'un dictionnaire. On suppose avoir construit un index. On
considère une requête à plusieurs mots clé, nous allons expliquer
comment **renvoyer une liste de documents ordonnée par un score de
pertinence relativement à une requête**.  Pour cela, nous allons voir
comment on représente un document et une requête par des vecteurs et
comment on peut définir un score par un calcul sur ces vecteurs.

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
*présence ou l'absence* d'un mot du dictionnaire dans le document. La
seconde, appelée **Term frequency**, représente un document par
vecteur où chaque composante du vecteur correspond à un mot du
dictionnaire et la valeur est le nombre d'occurrences (d'apparitions)
du mot dans le document. Par exemple, le document `réflexions sur la
révolution de france suivi d'un choix de textes de burke sur la
révolution` aurait la valeur 2 pour les composante des mots `la` et
`révolution`.

Mais, lorsque vous écrivez des requêtes sur le web, vous savez que des
mots trop fréquents, vont vous retourner trop de réponses donc vous
essayez de trouver des mots ou termes plus pertinents pour écrire
votre requête, où pertinent est pris dans le sens où il y a moins de
documents contenant ce mot. Pour tenir compte de ceci, on peut
intégrer dans la représentation vectorielle un facteur qui dépend de
la fréquence du document dans la base de documents. C'est la
représentation **term frequency -- inverse document frequency
(tf-idf)**. dans cette représentation, on multiplie la fréquence
d'apparition (le tf) par un facteur (l'idf), dont nous ne donnons pas
l'expression mathématique, mais qui 

- est *grand pour un mot rare*, i.e. qui apparaît dans peu de documents
- est *petit pour un mot fréquent*, i.e. qui apparaît dans beaucoup de
  documents

Par exemple, considérons le --très petit-- document `la révolution
française`. Sa représentation tf avec les fréquences aurait 1 pour le
mot la, 1 pour le mot révolution et 1 pour le mot française. Sa
représentation tf-idf aurait une valeur très petite pour le mot la
(car la est très fréquent) disons 0,01, moyenne pour française disons
0,14 et plus grande pour le mot révolution disons 0,25 (révolution est
le plus rare des 3 mots). Cette représentation permet de renforcer la
valeur pour les mots qui apparaissent dans peu de documents car ces
mots vont aider à trouver les bons documents.

Il existe de nombreuses variantes de ces représentations vectorielles
qui ont été étudiées et dont on a comparé les performances en
recherche d'information. 

### Score de pertinence entre un document et une requête

Il faut définir une similarité entre un document et une requête
composée de plusieurs mots clé. Intuitivement, un document sera
similaire à une requête si il contient les mots de la requête et si
ses mots apparaissent fréquemment. Un document contenant un mot de la
requête qui apparaît dans peu de documents doit aussi voir son score
renforcé. Plusieurs mesures de pertinence ont été introduites mais une
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
correspondent dans l'ordre aux mots `la`, `révolution` et `française`.
- le document `l'économie française dans la compétition internationale
au XXe siècle` avec la représentation tf est représenté par le vecteur
(1 ; 0 ; 1). Son score est 1x0,01 + 0x0,25 + 1x0,14 = 0,15
- le document `citoyennes tricoteuses - les femmes du peuple à paris
pendant la révolution française` avec la représentation tf est
représenté par le vecteur (1 ; 1 ; 1). Son score est 1x0,01 + 1x0,25 +
1x0,14 = 0,40
- le document `réflexions sur la révolution de france suivi d'un choix
de textes de burke sur la révolution` avec la représentation tf est
représenté par le vecteur (2 ; 2 ; 0). Son score est 2x0,01 + 2x0,25 +
0x0,14 = 0,52

On voit sur cet exemple que le score mesure bien la pertinence des
documents relativement à la requête. On voit également que l'usage du
tf-idf va privilégier les mots rares dans le calcul du score de
pertinence. Le calcul de la Cosine similarity est un peu plus
compliqué car il faut prendre en compte la longueur des documents. En
effet, il faut interdire la tricherie qui consisterait à répéter
beaucoup de fois certains mots dans des documents avec pour seul
objectif d'obtenir un meilleur score. Ceci est réalisé par une
normalisation que nous ne présentons pas.


# Recherche d'information sur le Web

Nous avons présenté l'indexation et la calcul de score de pertinence
d'un document textuel relativement à une requête. Nous allons voir
comment ceci est réalisé sur le Web. Nous présentons ensuite le score
de notoriété qui mesure l'importance d'un site Web. C'est ce score
introduit par Google qui a donné un avantage significatif à `Google`
dans les années 1990. Nous en déduirons les éléments principaux du
calcul du score d'un document Web relativement à une requête.

## Indexation du web

- l'**indexation du Web** est réalisé par des **programmes appelés
robots** qui parcourent les sites Web et suivent les liens. Ces
programmes récupèrent les informations utiles à la construction de
l'index comme les mots qui apparaissent, leur nombre d'apparitions,
...
- tous les documents du Web sont indexés quel que soit leur format :
  pages Web au format `html`, documents imprimables au format `pdf`,
  documents au format `doc`, ... ce qui mène à un **nombre de documents
  de l'ordre de 60 000 milliards** en 2016
- tous les mots qui apparaissent sur le Web sont indexés ce qui amène
  à un dictionnaire contenant **plusieurs millions de mots**
- l'index est réparti sur des fermes de calcul (un grand nombre
  d'ordinateurs de grande capacité) réparties dans le monde entier. On
  peut noter que celà implique une très grande consommation d'énergie
  et donc le Web n'est pas si écologique qu'on veut nous le faire
  croire.

## Score de pertinence

Considérons un document du Web -- une page web -- au format `html`. Un
tel document a un contenu mais aussi une structure définie un titre
principal et des sections ayant des titres. L'apparition d'un mot de
la requête dans un titre est plus important que son apparition dans le
contenu. Ceci doit donc être pris en compte dans le calcul de
pertinence. Un deuxième élément qui est spécifique au Web concerne les
liens (ou hyperliens). En effet, lorsqu'un lien sur une page web est
créé, il est associé à un texte qui contient de l'information sur la
page. Par exemple, un site Web qui souhaite mettre un lien sur ce
module définira un texte cliquable comme `cours introduction à la
recherche information` qui est très informatif sur le contenu de la
page. Par conséquent, le score de pertinence d'une page web va prendre
en compte des scores de pertinence calculés sur différentes vues sur
la page Web dont les principales sont :

- le contenu textuel de la page
- les titres de la page
- les mots clé associés à la page et définis dans son entête
- l'adresse du document (un texte de la forme
  `https://culturenumerique.univ-lille3.fr/modulerechercheinformation.html`)
- les textes des liens qui pointent sur la page

Pour chacune de ces vues un score de pertinence peut être calculé avec
la méthode introduite auparavant. Il reste à combiner ces scores avec
une formule de la forme : un pourcentage du score de contenu + un
pourcentage du score de titre + ... **La formule de combinaison est
secrète !**. On sait qu'elle évolue. Par exemple, l'influence du score
de pertinence des mots clés a été nettement diminué suite à de
nombreux abus de concepteurs de pages Web qui pouvaient mettre des
mots clé fictifs sur leur page pour essayer d'améliorer leur score.

## Score de notoriété

Le Web a une structure de réseau ou de graphe avec des pages Web qui
pointent les unes vers les autres avec les hyperliens. L'idée est
d'utiliser cette structure pour mesurer la **notoriété** des pages. On
souhaite donc un **score de notoriété** qui va mesurer à quel point
une page est souvent visitée par les internautes. Une première
tentative de définition de score de notoriété d'une page pourrait être
le nombre de pages qui pointent sur elle. Cette définition n'est pas
robuste car on peut tricher (cela a été fait) : pour renforcer le
score de notoriété de ma page, je crée des (beaucoup) de pages
artificielles qui pointent sur ma page. La définition doit donc être
plus intelligente et la bonne définition est la suivante :

> Une page a **une forte notoriété** si beaucoup de pages **ayant une
> forte notoriété** pointent sur elle

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

