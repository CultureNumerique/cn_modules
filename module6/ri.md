LANGUAGE:   fr
TITLE:   Recherche d'information et référencement Web
MENUTITLE: Recherche d'information Web
AUTHOR: Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

<!-- pandoc -t latex -V geometry:margin=3cm --toc ri.md -o ri.pdf -->

<!-- pandoc -F ext.py -t latex -V geometry:margin=3cm --toc ri.md -o ri.pdf -->

# Recherche d'information : contexte et application au Web

Avec l'avènement du numérique et, en particulier, du Web, nous vivons dans un monde de documents, de ressources numériques. Ces documents sont divers comme des sms, des tweets, des mails, des pages Web, des articles journalistiques ou scientifiques, des livres, ... Ils contiennent des informations textuelles mais aussi des dessins, des images et des vidéos. Ils proviennent de sources variées comme des administrations, des journaux, des entreprises commerciales mais aussi les réseaux sociaux et les objets connectés (caméras, compteurs intelligents, gps, ...). Ils sont en très grande quantité avec, par exemple, un nombre estimé de 60 000 milliards de documents Web en 2016. Cette masse de documents génère de nouvelles possibilités et des besoins comme pouvoir rechercher rapidement des documents concernant un sujet précis. 

C'est cette **recherche d'information** qui fait l'objet de ce cours. En particulier, nous allons étudier l'outil numérique utilisé quotidiennement par chacun d'entre nous : le **moteur de recherche d'information**. 

```activite
::popularité des moteurs de recherche:: 
[markdown]
L'exemple le plus connu et le plus utilisé dans le monde occidental est **Google**. Mais vous connaissez peut-être **Bing** ou **Yahoo**.  Notez également d'autres moteurs qui sont leaders dans leurs sphères d'influence. Lequel a la plus grande part de marché en France, en Russie, en Chine ? 
{####Google en france, Yandex en Russie et Baidu en Chine}

::Qwant::
Que promeut le moteur français **Qwant**? 
{####La préservation de la confidentialité et le respect de la vie privée}
```

La fonction première d'un moteur de recherche est de vous permettre de *poser une requête*  et recevoir en réponse une partie d'un ensemble de ressources (documents texte, images, vidéos,...).  L'ensemble des ressources sur lesquels les requêtes sont posées est accessible au moteur de recherche et organisé de façon à répondre efficacement. C'est la phase d'*indexation*, autrefois manuelle dans les bibliothèques et aujourd'hui largement automatisée qui est responsable de cette organisation. La réponse peut être exhaustive pour certaines requêtes simples et bien formalisées, mais le plus souvent le moteur  renvoie *une liste ordonnée de documents selon un score de pertinence*.

Nous nous intéressons exclusivement aux ressources textuelles et aux moteurs de recherche du web dans le cadre de ce cours. Nous décrivons les méthodes de recherche approximatives utilisées qui combinent d'une part, une mesure de la proximité entre une requête et le contenu d'une page, avec d'autre part, un **score de notoriété**.  Ce score de notoriété mesure l'importance d'une page dans le réseau constitué des pages Web reliées entre elles par des hyperliens. Il calculé par le fameux algorithme **PageRank** qui a contribué à l'essor de `Google` à la fin du vingtième siècle. 

Après un examen des tendances nouvelles, nous concluons par une discussion sur les problèmes éthiques et sociaux posés par les moteurs de recherche. En effet, chaque moteur utilise ses propres algorithmes pour répondre aux requêtes et beaucoup d'éléments du calcul de score ne sont pas connus des utilisateurs ce qui pose, en particulier, la question de la **loyauté des moteurs de recherche d'information**.


```compréhension
::Des moteurs de recherche::
[markdown]
Il existe différents moteurs de recherche d'information{T}

::Des moteurs sur le Web et en entreprise::
[markdown]
Il existe des moteurs de recherche spécifiques d'entreprises, accessibles uniquement par les employés et ne portant que sur leur propres documents d'entreprise.{T}

::Le coeur des moteurs::
[markdown]
Regardez [la page d'accueil de Google](http://www.google.fr) et [la page d'accueil de Qwant](http://www.qwant.com). Tout moteur de recherche
d'information permet la saisie d'une requête composée de plusieurs
mots dans une barre de saisie{T}

::Les réponses du moteur Google::
[markdown]
Lancer la requête `apprentissage machine`. Le moteur Google renvoie
{
= une liste ordonnée de réponses
~ trois listes ordonnées de réponses
#### Google a volontairement une interface simple pour ses réponses avec une seule liste de réponses. Nous verrons que d'autres éléments peuvent être ajoutés par la suite.}

::Les réponses du moteur Qwant::
[markdown]
Lancer la requête `apprentissage machine`. Le moteur Qwant renvoie
{
~ une liste ordonnée de réponses
= trois listes ordonnées de réponses
#### Qwant a une interface plus moderne pour ses réponses avec trois listes de réponses en trois rubriques Web, Actualités et Social.}

::Une première comparaison::
[markdown]
**pas clair**
En comparant les réponses de
Google et les réponses de Qwant dans la liste Web, on peut affirmer
que les réponses à une requête sont toujours les mêmes
et sont dans le même ordre.{T}
```

# Modes de recherche d'information

## Recherche exacte

De nombreux logiciels comme les traitements de texte, les éditeurs, les outils de messagerie vous proposent une fonction de recherche lorsque vous visionnez un document, un texte, un message,... En actionnant le menu *Rechercher* vous avez la possibilité de taper quelques caractères. Ces mots définiront une requête et dans le plus simple des cas, le logiciel vous dirigera vers (ou vous surlignera) chaque position ou ces quelques caractères apparaissent. 

Pour réaliser cela, un algorithme de recherche parcourt le document du début à la fin et  pour toutes les positions, il évalue si le texte commençant à cette position correspond exactement à la requête. On parle de *recherche séquentielle* car l'algorithme évalue séquentiellement (les unes après les autres) toutes les positions. Vous pouvez imaginer une petite fenêtre qui se déplace du début à la fin du document puis compare deux à deux les  caractères recherchés avec ceux dans la fenêtre. 

Des travaux maintenant anciens ont étendu la recherche séquentielle en définissant des langages de requêtes qui dépassent la simple comparaison deux à deux. Dans ces langages de requêtes certains caractères prennent un sens différent de leur usage habituel. Le `?` ne désigne plus le point d'interrogation mais une présence optionnelle, si bien que la requête `mal?in` permet de dire que le `l` est optionnel et trouvera donc les positions où se trouve  `main` ou `malin`.  Le `.` par exemple représente n'importe quel caractère (et non plus uniquement le point) et `*` n'est plus une étoile mais une répétition. La requête `le .* dort` fonctionne comme un texte à trous qui peut rechercher par exemple `le gros chat noir dort`. Un tel langage de requête étendu s'appelle le langage des *expressions régulières*.

```activité 
::Expressions régulières::
[markdown]
Dans Libreoffice, créez un nouveau document contenant le texte de ce cours. Avec le menu /Rechercher et remplacer/, regardez les options de recherche (/autres options/) et placez une coche devant /Expressions régulières/. Effectuez ensuite des recherches avec ces symboles spéciaux. Par exemple, recherchez `m????n`, `e.e` et `e.*e`, `e$`. Donnez quelques exemples représentatifs de ce que vous avez trouvé. Que signfie le `$` dans ce langage ?
{####le $ représente la fin de paragraphe.}
```

Évidemment tous ces langages  de requête plus ou moins expressifs sont facilement disponibles pour traiter non seulement un unique document mais des bases de données ou des corpus de documents. Ils sont par conséquent très utilisés en linguistique informatique, pour des textes en langue naturelle, les biologistes pour rechercher dans les séquences génétiques, entre autres. 

Mais une une telle méthode de recherche séquentielle est-elle envisageable pour un moteur de recherche Web ?  Certainement non, car parcourir les 60 000 milliards de documents du Web à chaque fois que l'on fait une recherche sur le Web prendrait un temps de calcul bien trop long alors que vous attendez une réponse immédiate !

```compréhension
::Critiques de la recherche séquentielle::
[markdown]
Cochez les affirmations qui sont vraies à propos de la recherche séquentielle :
{
= Elle est utilisée dans de nombreuses applications. 
= Le langage de requêtes est simple mais peut être enrichi et devenir très expressif. 
~ Elle est réservée aux informaticiens
}
```


```activité avancée 
::Dans libreoffice::
[markdown]
Ouvrez le menu rechercher remplacer et regardez les options. Il est possible de faire une recherche avec des expressions régulières {T}

::Des lignes vides::
[markdown]
Dans les expressions régulières, les caractères `^` et `$` représentent le début et la find d'une ligne. Avec quelles expression peut-on donc rechercher 
{
=une ligne vide -> ^$
=une ligne ne contenant que bonjour -> ^bonjour$
=une ligne ne contenant que des espaces ->^ *$
}
``` 

## Recherche exacte rapide avec un index

Lorsque vous utilisez l'index d'un livre, d'un atlas ou d'une encyclopédie, vous utilisez la liste des mots indexés rangés alphabétiquement pour trouver les pages du livre où ces mots sont définis ou utilisés. L'ordre alphabétique permet également de rechercher très rapidement dans cet index. Cette organisation est reproduite dans les moteurs de recherche pour dépasser la simple recherche séquentielle qui peut prendre un temps de calcul trop grand. Étudions comment construire automatiquement des index pour les grand ensembles de documents numériques et comment les utiliser. Considérons pour cela que nous avons un corpus de documents fixé.

### Construction d'un index

Pour construire cet index, il faut choisir quels mots seront indexés et quelle sera la représentation des documents, ou plus précisément, la représentation des textes dans ces documents. 

Chaque texte est représenté par une séquence d'unités élémentaires, appelés `tokens` ou unités lexicales, qui sont des suites de caractères sans espace et sans symbole de ponctuation. Un token correspond à un mot de la langue ou un nombre ou une date ou un sigle.  De nombreux choix, parfois dépendants de la langue conditionnent ce découpage en tokens. Par exemple, considère-t-on différemment les majuscules et les minuscules ? Considère-t-on les accents ? Un texte comme `La Révolution française, 1789-1799 : Une histoire socio-politique` pourrait alors être transformé en une suite de tokens `la revolution francaise 1789 1799 une histoire socio politique`. L'ensemble de tous les tokens possibles, ou plus précisément, rencontrés dans l'ensemble de tous les documents qui constituent la base documentaire à indexer forme le **vocabulaire**. Parfois, les tokens très fréquents sont retirés du vocabulaire, par exemple en français le `et`, `le`, ... Si le programme d'indexation automatique dispose de plus d'informations linguistiques, il est parfois possible d'inclure dans le vocabulaire, et donc dans l'index, des tokens qui sont composés comme `révolution française` ou `socio-politique`. 


L'étape suivante pour la réalisation de l'index est maintenant d'associer à chaque token du vocabulaire l'ensemble des documents dans lesquels ce token apparaît. Pour cela on associe un numéro unique, appelé identifiant, à chaque document de la base documentaire. La structure de l'index est alors simplement une liste de tokens avec pour chacun, la liste des identifiants des documents où ce token se trouve. Par exemple, l'index  mémorise que le mot `rose` apparaît dans les documents de numéro 125, 245, 567, ... ; que le mot `blanche` apparaît dans les documents de numéro 117, 176, 245, 312, ...

### Recherche à l'aide d'un index

La création d'un index est un processus assez long mais qui ne se fait qu'une seule fois quand l'ensemble des documents ne change pas. En revanche la recherche dans l'index doit être très rapide pour être opérationnelle. Mais l'index peut avoir une taille de plusieurs centaines de milliers de tokens. L'index est donc lui même organisé de façon à ce qu'une recherche soit rapide. Parmi les techniques utilisées, on peut décrire la plus simple. Il s'agit de s'assurer que l'index soit organisé par ordre alphabétique des tokens. Dans ce cas un algorithme de  *recherche dichotomique* peut être utilisé. La recherche dichotomique est illustrée en cherchant par exemple le mot `rose` : on regarde le mot au milieu du dictionnaire, c'est `maman`, donc on cherche dans la seconde moitié ; on regarde le mot au milieu de la seconde moitié, c'est `savant`, donc on cherche entre `maman` et `savant` ; jusqu'à trouver le mot `rose`. On peut montrer qu'un tel algorithme est très efficace. Pour un dictionnaire de 500 000 mots, il suffit d'effectuer 19 accès, pour une dictionnaire de 1 million de mots, il suffit d'effectuer 20 accès. Notons que si la taille du dictionnaire double, on ne doit faire qu'un accès supplémentaire ! Ce
qui explique la rapidité de ce mode de recherche. Terminons en signalant que des méthodes dites de hachage permettent d'effectuer des recherches plus rapides encore. 

Nous avons présenté la phase d'indexation qui fournit comme résultat un index défini de la manière suivante :

> Un **index** est constitué d'un vocabulaire avec une méthode
> d'accès rapide à un token, et, pour chaque token, on dispose de la liste
> des identifiants des documents qui contiennent ce token.

Comment l'index permet-il de répondre rapidement à des requêtes formulées dans un moteur de recherche exacte ?

- Si la requête ne contient qu'un seul mot, on cherche si ce mot est un token dans l'index et on renvoie la liste des documents donnés par leurs identifiants associée dans l'index.
- Si la requête est composée de deux mots, le moteur procède comme suit : chercher le premier mot dans l'index et renvoyer la liste des identifiants de documents ; faire de même pour le deuxième mot ;  construire la liste  des identifiants qui apparaissent dans les deux listes (c'est une intersection de listes) ; renvoyer cette  liste comme réponse à la requête. Ce principe peut être étendu pour des requêtes à  plusieurs mots
- Une requête à plusieurs mots est interprétée avec un opérateur `ET` implicite car on souhaite que tous les mots soient présents. On  peut aussi écrire des requêtes avec les opérateurs logiques `OU` et `NON` qui correspondront à d'autres opérations sur les listes (union ou différence).
- Les moteurs de recherche proposent également des *requêtes par position*. La plus importante est la **requête par phrase** où on recherche les mots en respectant exactement les positions des mots de la requête. Une requête par phrase est souvent exprimée avec des guillemets. Par exemple, si on considère la requête par phrase `"rose blanche"`, le moteur doit renvoyer tous les documents contenant les deux mots `rose` et `blanche` à des positions consécutives. Ceci peut être réalisé grâce à un index plus complet  mémorisant également les positions auxquelles apparaissent les tokens. Il existe d'autres requêtes par position exprimant des conditions sur les positions relatives de mots. Par exemple, on pourrait écrire une requête demandant que les mots `rose` et `blanche` soient distants de moins de 3 mots.



## La recherche approximative avec un score de pertinence

Les systèmes étudiés jusqu'à présent renvoient la liste complète des documents qui satisfont la requête. Lorsque le corpus de documents sur lequel porte les requêtes est trop grand, cette recherche est bien souvent inutile. Trop de documents satisfont la requête et le résultat devient illisible.  Les moteurs de recherche du Web fonctionnent différemment et ordonnent la liste de résultats selon des scores attribués aux documents. Ceci permet d'effectuer des recherches approximatives mais aussi de faciliter la lecture du résultat. Il est donc alors nécessaire de définir et calculer **un score de pertinence relativement à une requête**.

À cause de cet ordonnancement des résultats, des questions éthiques d'accès à l'information se posent, et plus évidemment encore si la liste est tronquée aux quelques documents de plus haut score, ou même du premier document. Mais il faut remarquer que les mêmes questions éthiques se posent dans la recherche exacte suite aux choix réalisés dans la phase d'indexation, de collecte et de représentation des documents. 

### Représenter des documents par des tableaux de nombres

On suppose toujours qu'un grand ensemble de documents est à la disposition du moteur de recherche. Rappelons rapidement que dans le cas du web, ce sont les robots (ou crawlers en anglais) qui se chargent de collecter le plus grand nombre possible de documents disponibles sur internet. Ce grand corpus de documents est ensuite indexé selon des techniques similaires à celles expliquées précédemment. 

Pour calculer un score, la représentation numérique des documents est adaptée et plusieurs représentations ont été utilisées. Trouver une bonne représentation, adéquate pour la recherche d'information est toujours un sujet de recherche. Nous en présentons trois. 

Dans la plus simple, un document sera représenté par une suite de 0 et de 1 correspondant à la présence ou l'absence dans ce document de  chaque token du vocabulaire considéré dans la phase d'indexation. On appelle un **vecteur** une telle suite de valeurs qu'on prend l'habitude de représenter comme un tableau d'une seule colonne. Chaque valeur 0 ou 1 se trouve dans une cellule de ce tableau qu'on appelle **composante** du vecteur et qui est ici associée à un token du vocabulaire. 
Prenons l'exemple d'un vocabulaire contenant les mots de langue française et du document textuel `citoyennes tricoteuses - les femmes du peuple à paris pendant la révolution française`. Ce document sera représenté par un vecteur avec une composante par mot du vocabulaire et toutes les composantes valent 0 sauf les composantes pour les mots `à`, `citoyennes`, ..., `tricoteuses` qui valent 1.  Cette représentation qui ne représente un document que par la présence ou l'absence de certains tokens est appelée **Boolean frequency**. 

Plutôt que de mémoriser simplement la présence ou l'absence, une extension est de compter combien de fois chaque token apparaît. On obtient une seconde représentation, appelée **Term frequency**, pour
laquelle un document est représenté par un vecteur où chaque composante est le nombre de fois où un token apparaît dans le document. Par exemple, considérons le document `réflexions sur la révolution de france suivi d'un choix de textes de burke sur la révolution`.  Il sera représenté par un vecteur dont toutes les composantes valent 0 sauf les composantes pour les mots `réflexions`, `france`, ... qui valent 1 et les composantes pour les mots `de`, `la`, `révolution` et `sur` qui valent 2 car ils apparaissent deux fois.

Mais, lorsque vous écrivez des requêtes, vous savez que des mots trop fréquents vont vous retourner trop de réponses donc vous essayez d'exprimer votre requête avec *des mots ou termes plus
pertinents ou plus discriminants* dans le sens où vous savez qu'il y a moins de documents contenant ces mots. Une troisième représentation, appelée **term frequency -- inverse document frequency (tf-idf)**, pénalise les mots fréquents et favorise les mots rares.  Dans cette représentation,
on multiplie la fréquence d'apparition (*tf* pour term frequency) par un facteur (*idf* ou inverse document frequency). Nous ne donnons pas la définition mathématique de l'idf mais il suffit de retenir que l'idf d'un mot

- est *grand pour un mot rare* qui apparaît dans peu de documents
- est *petit pour un mot fréquent* qui apparaît dans beaucoup de
  documents

Par conséquent, la multiplication par l'idf va augmenter la valeur pour les mots rares de la collection et la diminuer pour les mots fréquents. Par exemple, considérons le très petit document `la révolution française`. Sa représentation tf avec les fréquences aurait 1 pour le mot `la`, 1 pour le mot `révolution` et 1 pour le mot `française` et 0 pour tous les autres mots du vocabulaire. Sa représentation tf-idf aurait une valeur très petite pour le mot `la` (car la est très fréquent) disons 0,01, moyenne pour le mot `française` disons 0,14 et plus grande pour le mot `révolution` disons 0,25 (révolution est le moins fréquent des 3 mots). La représentation tf-idf permet donc de renforcer la valeur pour les mots qui apparaissent dans peu de documents ce qui va aider à trouver les documents les plus pertinents.


### Score de pertinence entre un document et une requête

Comment obtenir un score de pertinence d'un document vis à vis d'une requête ? Plusieurs formules de calcul ont été proposées et traduisent la similarité entre la représentation du document et celle de la requête par des tableaux de nombre, c'est-à-dire représentés sous forme de vecteurs. Intuitivement, le score exprime à quel point les deux vecteurs, document et requête, sont proches. Le score de similarité le plus utilisé est obtenu  en multipliant les composantes des vecteurs deux à deux (correspondant à un même mot) et en sommant les résultats. Notez que comme le 0 représente l'absence d'un mot dans ces représentations à base de vecteurs, seuls les mots à la fois présents dans la requête et dans le document contribuent au score.

Un bon choix pour la représentation sous forme de vecteurs des requêtes et documents est donc essentiel. Intuitivement, un document est pertinent si il contient les mots de la requête et si ces mots apparaissent souvent dans le document. De plus, le score doit être renforcé pour les mots rares et diminué pour les mots fréquents. Pour cela, on représente, en général, un *document avec la représentation term-frequency et la requête avec la représentation tf-idf*. 

Illustrons par des exemples ce calcul de score de pertinence :

- la requête `la révolution française` avec la représentation tf-idf
est représenté par le vecteur (0,01 ; 0,25 ; 0,14) où les composantes
correspondent dans l'ordre aux mots `la`, `révolution` et `française`
et 0 pour tous les autres mots du dictionnaire.
- le document `l'économie française dans la compétition internationale
au XXe siècle` avec la représentation tf est représenté par le vecteur
(1 ; 0 ; 1) où les composantes correspondent dans l'ordre aux mots
`la`, `révolution` et `française`. Notez que les autres composantes ne
vont pas intervenir dans le calcul car elles sont multipliées
par 0. Son score, relativement à la requête `la révolution française`
est donc : 1x0,01 + 0x0,25 + 1x0,14 = 0,15
- le document `citoyennes tricoteuses - les femmes du peuple à paris
pendant la révolution française` avec la représentation tf est
représenté par le vecteur (1 ; 1 ; 1). Son score est donc : 1x0,01 +
1x0,25 + 1x0,14 = 0,40
- le document `réflexions sur la révolution de france suivi d'un choix
de textes de burke sur la révolution` avec la représentation tf est
représenté par le vecteur (2 ; 2 ; 0). Son score est donc : 2x0,01 + 2x0,25 +
0x0,14 = 0,52

C'est ce dernier document qui l'emporte car, même si il ne contient
pas le mot `française`, il contient deux occurrences du mot
`révolution` qui est plus rare. Nous constatons bien, sur cet
exemple, que le score mesure bien la pertinence des documents
relativement à la requête. Le calcul est en réalité, un peu plus compliqué car il faut limiter l'influence de la
longueur des documents.  Le calcul de la pertinence fait donc
intervenir une normalisation qui revient à ramener tous les documents
à une même longueur.

<!-- Notons enfin que les notices sont structurées, que les documents sont -->
<!-- structurés avec titre, résumé, ... On peut calculer un score de -->
<!-- pertinence pour chacun de ces éléments et combiner ces scores. Nous -->
<!-- reparlons de ce point lorsque nous définirons le score de pertinence -->
<!-- Web dans la suite. -->


```compréhension

::Recherche séquentielle dans un texte::
[markdown]
Activer l'élément de menu **Rechercher** ou **Find** de votre navigateur préféré.
\n
- Décrire le résultat obtenu si vous entrez une suite de caractères
- Donner les actions possibles sur le résultat
{#### Selon le navigateur, on met en évidence par surbrillance ou par coloration soit la première occurrence de la chaîne cherchée, soit toutes les occurrences. On dispose toujours de suivant, précédent et parfois de premier, dernier, respecter la casse, mots entiers, ...}

::Recherche séquentielle dans un ensemble de textes::
[markdown]
Activer l'élément de menu **Rechercher** ou **Find** de votre lecteur de mail préféré.
\n
- Décrire le résultat obtenu si vous cherchez une suite de caractères
- Décrire les zones de texte dans lesquelles on peut chercher
{#### Si on recherche dans un mail, on a le même comportement que précédemment. Si on recherche dans un ensemble de mails, on a la liste de tous les mails dans lesquels le mot apparaît. On peut en général chercher dans le champ From, dans le champ to, dans le champ subject ou sujet, dans le corps du mail, et partout.}

::Recherche avancée dans un traitement de textes::
[markdown]
Ouvrir un document texte avec LibreOffice. Activer l'élément de menu **Rechercher** et cliquer sur les jumelles (ou activer l'élément de menu **Rechercher et Remplacer**. Cliquer sur "Autres Options". Le programme de recherche permet
{
~%33% de respecter les majuscules et minuscules
~ de trier par score de pertinence
~%33% d'utiliser des expressions régulières
~%34% de remplacer toutes les occurrences d'un mot par un autre
#### On cherche en respectant ou pas la casse donc selon le cas on peut demander au programme de tenir compte (ou pas) du fait que l'on ait écrit le mot avec des majuscules ou des minuscules. On fait une recherche exacte donc pas de score de pertinence. On peut utiliser des expressions régulières avec des jokers. On peut remplacer partout ce qui est utile lorsqu'on a fait une faute récurrente.}

::Recherche Booléenne dans un catalogue de bibliothèque::
[markdown]
Vous pourrez adapter cet exercice à votre centre de documentation ou votre bibliothèque universitaire. Nous pouvons, par exemple, chercher dans le [catalogue du centre de documentation de l'université de Lille](https://scd-catalogue.univ-lille3.fr/). Lancer la requête simple *culture numérique*. Regarder et comprendre la notice du premier résultat présenté en cliquant sur le titre. Quelles affirmations suivantes sont vraies
{
~%33% sans précision on cherche dans la notice
~ on peut faire des recherches plein texte dans le contenu de l'ouvrage
~ on peut trier par score de pertinence
~%33% on peut limiter la recherche au titre
~%34% on peut trier par titre
#### On cherche dans la notice et on ne peut pas faire de recherche plein texte. On retourne une liste de documents contenant les mots-clés sans calculer de score de pertinence. On peut chercher dans les titres uniquement. On peut trier par titre si le nombre de documents n'est pas trop grand.}

::Recherche Booléenne avancée::
[markdown]
Nous utilisons à titre d'exemple [catalogue du centre de documentation de l'université de Lille](https://scd-catalogue.univ-lille3.fr/). En utilisant recherche simple et recherche avancée, dites quelles affirmations suivantes sont vraies
{
~ la requête *culture numérique* et la requête par phrase *"culture numérique"* (ou expression exacte) donnent les mêmes réponses
~%100% la requête *culture numérique* et la requête avancée *culture* ET *numérique*  donnent les mêmes réponses
~ la requête *culture numérique* et la requête avancée *culture* OU *numérique*  donnent les mêmes réponses
#### Une requête par phrase retourne un document seulement si les mots sont à eux positions consécutives donc on a moins de réponses à la requête par phrase. Une requête à deux mots clés renvoie les documents dont la notice contient les deux mots et est donc équivalente à une requête avec un ET. Elle n'est donc pas équivalent à une requête avec un OU pour laquelle il suffit que la notice contienne un des deux mots (ou les deux).}

::Score de pertinence::
[markdown]
On suppose les documents en représentation tf et les requêtes en représentation tf-idf. Pour une requête à trois mots clé, le document avec le plus grand score de pertinence contient obligatoirement les trois mots clé ? {T}

::Recherche dans le modèle vectoriel::
[markdown]
Nous utilisons à titre d'exemple [le site Gallica lié à la bibliothèque nationale de France](http://www.gallica.bnf.f). En utilisant recherche simple (bouton loupe) et recherche avancée (bouton +) et un exemple de requête comme *révolution française*, dites quelles affirmations suivantes sont vraies
{
~%33% on peut trier par score de pertinence
~%33% on peut utiliser des opérations logiques avec des ET et des OU
~ on peut faire des requêtes par position
~%34% on peut faire des requêtes par phrase
~ les mots clé apparaissent dans la notice
#### Un score de pertinence est calculé donc on peut trier par pertinence mais on note que l'ordre obtenu n'est pas simple à interpréter. La requête avancée permet les expressions logiques. Elle ne permet pas de requête par position générale mais permet des requêtes par phrase en utilisant les guillemets. On voit des documents bien classés pour lesquels les mots clé n'apparaissent pas dans la notice.}

```

# Recherche d'information sur le Web

Dans les années 1990, des travaux de recherche ont proposé une modification dans le calcul du score de pertinence en combinant le score avec une valeur reflétant la notoriété d'un document du web. Ces travaux ont été implantés et ont conduit à la création de Google. Ils sont aujourd'hui utilisés par tous les moteurs de recherche du web. Cette valeur de notoriété exploite la particularité des documents HTML du Web : l'existence de liens hypertexte entre documents.

En résumé, le moteur de recherche du web doit indexer les documents du web, calculer un score web qui compose un score de pertinence et un score de notoriété. 

## Indexation du Web

L'**indexation du Web** est réalisé par des **programmes appelés robots** qui parcourent les sites Web et suivent les liens. Ces robots fonctionnent comme un navigateur automatique. Reportez-vous au cours sur le Web. À partir d'une URL, ils téléchargent un premier document HTML, extraient automatiquement toutes les URLs  qui s'y trouvent et recommencent ce même processus indéfiniment. De cette façon, ils  récupèrent le contenu des pages et la structure décrite par tous les liens. Le tout (donc une copie partielle du web) est stocké dans d'immenses serveurs. La constitution d'un index s'opère dans le même temps, et au bilan :

- **Les documents du Web sont indexés** quel que soit leur format : pages Web au format `html`, documents imprimables au format `pdf`, documents au format `doc`, ... ce qui mène à un nombre de documents de l'ordre de 60 000 milliards en 2016.  
- **Tous les mots qui apparaissent sur le Web sont indexés** quels que soient leur fréquence, la langue, ..., ce qui amène à un dictionnaire contenant plusieurs millions de mots.
- Ceci permet de construire un **index de très grande taille** qui est **mis à jour continûment** avec les informations récupérées par les robots
- L'index est réparti sur des fermes de calcul et de stockage (un grand nombre d'ordinateurs de grande capacité en réseau) réparties dans le monde entier. On peut noter que cela implique une très grande consommation d'énergie et donc le Web n'est pas si écologique qu'on pourrait le croire.

## Score de pertinence

Considérons un document du Web au format `html`. Un tel document a un contenu mais aussi des méta-données et une structure comme un titre principal et des titres de section. L'apparition d'un mot de la requête dans un titre est plus important que son apparition dans le contenu. Ceci doit donc être pris en compte dans le calcul de pertinence. Un deuxième élément qui est spécifique au Web concerne les liens composés par une URL et un texte de lien. Par exemple, un lien sur ce module culture numérique définira un texte cliquable comme `cours d'introduction à la recherche information` et l'URL reprendra peut être une partie de ces mots. Ces textes sont très informatifs sur le contenu de la page. Il est donc intéressant de les prendre en compte dans le calcul du score de pertinence.

Par conséquent, le score de pertinence d'une page Web va prendre en compte des scores de pertinence calculés sur **différentes vues sur la page Web** dont les principales sont :

- le contenu textuel de la page
- les titres de la page
- les mots clé associés à la page définis dans son entête et plus généralement les méta données de la page Web
- l'adresse du document (un texte de la forme  `https://culturenumerique.univ-lille3.fr/modulerechercheinformation.html`)
- les textes des liens qui pointent sur la page

Pour chacune de ces vues, un score de pertinence peut être calculé avec la méthode introduite auparavant. Il reste à combiner ces scores avec une formule de la forme : un pourcentage du score de contenu + un pourcentage du score des titres + ... **La formule de combinaison est secrète !**. C'est-à-dire que l'on ne connaît pas les pourcentages utilisés dans la formule. Par exemple, suite à de nombreux abus de concepteurs de pages Web qui ajoutaient des mots clé fictifs (sans rapport avec le contenu) pour essayer d'améliorer artificiellement leur score, on a pu constater que l'influence du score de pertinence des mots clés a été diminuée.

## Score de notoriété

Le score de notoriété peut être basé sur la réflexion suivante : 

> Une page a **une forte notoriété si beaucoup de pages ayant une
> forte notoriété** y font référence.

Puisque Le Web a une structure de réseau ou de graphe avec des pages Web qui pointent les unes vers les autres avec les hyperliens, l'idée est d'utiliser cette structure pour mesurer *la notoriété* des pages. Même cela peut paraître compliqué car la définition de notoriété utilise elle même la notoriété (on parle de définition récursive) il est possible de mettre cette définition en équations et de définir des algorithmes qui vont permettre de la calculer. L'idée est d'imaginer qu'un surfeur navigue sur le Web en suivant des liens au hasard. On définit en fait un **surfeur aléatoire** dans le graphe du web. Pour cela,

- il peut choisir une page au hasard sur le Web
- lorsqu'il est sur une page Web, il peut choisir au hasard un des liens présents sur la page et le suivre

Si le surfeur réalise ceci un très grand nombre de fois, toutes les pages Web seront visitées et plus souvent elles sont visitées plus elles sont importantes. Le score de notoriété d'une page correspond donc à la fréquence de visite de cette page par le surfeur aléatoire. Notez que pour qu'une page soit souvent visitée, il ne suffit pas qu'elle soit la cible de nombreux liens, mais que ces liens proviennent eux mêmes de pages fréquemment visitées. Sans se résumer à cela, l'algorithme appelé **PageRank**, introduit par les fondateurs de Google au milieu des années 1990, simule ce surfeur aléatoire pour calculer le score de notoriété. Si les principes de cet algorithme étaient connus, c'était un challenge de l'appliquer à la recherche d'information avec des tailles de données (dictionnaire et nombre de documents) très grands. 

## Score Web

Le **score Web d'un document Web relativement à une requête** est calculé comme une
combinaison qui utilise un score de pertinence de la page relativement à la requête et un score de notoriété de la page. Ici encore la combinaison exacte utilisée par les acteurs comme Google, Bing, Qwant, Baidu ou Yandex,... (la liste est longue) n'est pas connue et chacun a la sienne! Elle reste secrète et évolue pour des raisons de compétition entre moteurs de recherche et sans doute aussi pour éviter aux concepteurs de sites de mettre en oeuvre des techniques pour augmenter artificiellement leur score. Mais il semble que la part du score de notoriété est de plus en plus grande. En effet, les pages les mieux classées ont souvent une forte notoriété comme les pages Wikipedia, des pages de sites de journaux et, plus généralement, des pages de sites de référence. Retenez que **le score Web est calculé principalement à partir de la pertinence et de la notoriété**, que **les réponses et l'ordre des réponses à une requête diffèrent selon le moteur choisi** et que **le score Web évolue dans le temps**.

Si les deux éléments essentiels sont le score de pertinence et le score de notoriété, le score Web fait intervenir d'autres éléments sans qu'on sache exactement comment ils interviennent dans le calcul
du score Web. Parmi les éléments principaux intervenant dans le calcul, on trouve :

- des données d'usage
- des données personnelles 

Les données d'usage consistent à connaître par exemple le nombre de fois où les utilisateurs, considérés globalement et non individuellement, ont cliqué sur chaque lien fourni sur la page de résultat du moteur de recherche. Ces pages vont voir leur score renforcé ce qui contribue à renforcer encore le score des pages souvent visitées. Le score privilégie alors fortement la notoriété vue par la majorité des utilisateurs au détriment de la diversité. Notez également que ces données d'usage sont possédées par les grands acteurs du domaine ce qui leur donne un avantage concurrentiel important. 


Les données personnelles sont attachées aux utilisateurs du moteur de recherche. Il peut s'agir de la langue d'interrogation, de la localisation de l'utilisateur, du média d'interrogation, autant d'informations qui accompagnent ou peuvent se déduire d'une requête HTTP (voir le cours sur le web). Mais grâce aux cookies et autres techniques de tracking, d'autres informations définissant un profil de l'utilisateur sont collectées par la plupart des moteurs de recherche. Il peut s'agir des requêtes passées, mais aussi d'informations bien plus personnelles comme le sexe ou l'âge ou les goût. 
Elles peuvent alors être utilisées et modifier cette fois individuellement les résultats proposés par le moteur de recherche. Certains moteur comme *Qwant* ou *DuckDuckGo* s'engagent à ne pas user de cette pratique. Retenez donc que **le score Web est basé sur pertinence et notoriété mais il prend en compte de nombreux autres éléments**.


<!-- Nous avons essentiellement discuté des requêtes à plusieurs mots clé mais un autre type de requête important sur le Web (environ 15 pour cent des requêtes) correspond aux requêtes par phrase. Rappelons qu'une requête par phrase consiste à rechercher les documents contenant exactement la phrase saisie. La convention usuelle est de mettre la phrase entre guillemets dans la barre de saisie. Par exemple, on peut considérer la requête par phrase `"la révolution française"`. Pour cette requête, on va retourner par ordre de score Web les documents contenant les trois mots consécutifs. Notez que cette requête donnera donc des résultats différents de la requête à trois mots clé `la révolution française` pour laquelle la position des mots n'intervient pas et dont les résultats ne contiennent pas nécessairement les trois mots.  Souvent les moteurs proposent des requêtes avancées mais elles sont très peu utilisées en pratique. --> 

```compréhension

::Tout est indexé::
[markdown]
Utilisez, par exemple, le moteur Google.fr. Pour se faire une intuition que tout est indexé, vous pouvez tester une requête avec un mot très fréquent comme `le` et vérifier qu'il est bien indexé car on retrouve tous les documents contenant ce mot. Aussi, nous allons regarder si on trouve des pages pour des mots hétéroclites. Par exemple, lancer
une requête comme *afggd* puis ajouter des lettres au mot clé.
Quelles affirmations suivantes sont vraies
{
~%33% il existe des requêtes avec plusieurs millions de réponses
~%33% il existe des requêtes à 1 mot clé avec moins de 10 réponses
~%34% il existe des requêtes à 1 mot clé avec 0 réponse
#### Une requête avec un mot courant comme *le*, *la*, *et* ou encore *and*  donne plusieurs millions de réponse. Sur mon ordinateur à un moment donné, la requête afggdfk donne 7 réponses et la requête afggdfkr donne 0 réponse.}

::La casse et les accents::
[markdown]
Utiliser, par exemple, le moteur Google.fr pour tester. Pour les majuscules, vous pouvez prendre des mots ayant un sens différent selon qu'on les écrive avec ou sans majuscule, avec ou sans accent comme *Manche* (département) ou *manche*, comme *côté* et *cote* ou comme *jeûne* et *jeune* et d'autres exemples de votre choix. Comme il est impossible de regarder toutes les réponses, nous supposons que les réponses sont les mêmes si les nombres de réponses sont les mêmes et que les réponses en première page sont identiques. Dire quelles affirmations suivantes sont vraies
{
~ la casse (majuscule ou minuscule) influe  sur les réponses du moteur
~ deux requêtes avec ou sans accent donnent toujours les mêmes réponses
#### La casse ne semble pas influer sur les réponses même si les nombres de réponse peuvent être légèrement différents. Les accents changent les réponses. Le Web français évolue vers une prise en compte de plus en plus importante des accents.}

::Requêtes par phrase et plagiat:: [markdown] La plagiat consiste à
copier une oeuvre en omettant de citer son auteur. Le numérique
facilite le plagiat car la copie est aisée. Mais les moteurs
permettent de retrouver des parties de textes copiées et donc de
retrouver les plagieurs. Ceci montre également que **tout est indexé**
car le moteur retrouve des phrases complètes où qu'elles soient sur le
Web. Par exemple, nous avons copié une phrase du module
traitements numériques de notre cours culture numérique. Effectuez la
requête par phrase *"Rappelons que machines, langages et algorithmes
sont intimement liés et comprendre l'une de ces notions ne peut se
faire indépendamment des autres"*.  Le moteur permet de retrouver le
site (ou les sites) contenant cette phrase{T}

::Les pages bien classées::
[markdown]
Utiliser, par exemple, le moteur Google.fr. Lancer
une requête comme *culture numérique*, regarder la première page de réponses et dites quelles affirmations suivantes sont vraies
{
~%33% les titres des pages contiennent souvent les deux mots
~%33% l'adresse http des réponses contient souvent les deux mots
~%34% les sites ont souvent une forte notoriété
~ certains sites ne contiennent qu'un des deux mots
#### tous les titres contiennent les deux mots, l'adresse http contient souvent les deux mots comme https://www.culture-numerique.fr, les sites ont une forte notoriété avec Wikipedia et eduscol mais aussi des sites de journaux et d'université. Toutes les réponses contiennent les deux mots.}

::Tous les mots sont-ils présents dans les pages de réponse ?::
[markdown]
Rechercher une requête à trois mots pour laquelle des réponses en première page ne contiennent que deux des trois mots. Peut-on affirmer qu'une requête à plusieurs mots donne des réponses contenant tous les mots de la requête ?
{F}

::Requêtes par phrase sur le Web::
[markdown]

La requête *culture numérique* et la requête par phrase *"culture numérique"* donnent les mêmes réponses
{T}

::Notoriété versus diversité::
[markdown]
Vous pouvez comparer les moteurs Google et Qwant en effectuant quelques recherches dans les deux moteurs. Dites quelles affirmations suivantes sont vraies
{
~%33% Les réponses de Google et les réponses Web de Qwant sont souvent très proches
~%33% Google valorise davantage la notoriété
~%34% Qwant encourage la diversité
#### les réponses en tête de classement sont très souvent les mêmes avec, parfois, un ordre légèrement différent et des réponses apparaissant dans l'un et pas dans l'autre. Google privilégie fortement la notoriété jusqu'à parfois oublier des mots de votre requête. Qwant essaie d'apporter de la diversité dans ses réponses Web mais aussi avec les deux listes Actualités et Social.}

::Score Web::
[markdown]
On considère une requête à plusieurs mots clé. Dites quelles affirmations suivantes sont vraies
{
~%33% Les réponses et leur ordre peuvent être différents selon le moteur
~ Les réponses et leur ordre sont les mêmes quel que soit le média (ordinateur ou téléphone)
~%33% Les réponses et leur ordre peuvent être différents à 1 mois d'intervalle
~%34% Les réponses et leur ordre peuvent être différents selon que je sois identifié ou pas
~ Les réponses et leur ordre sont les mêmes quel que soit le lieu où je saisis ma requête
#### les réponses différent selon le moteur, le média, le moment et le lieu.}

```


# Évolutions en cours

## Web des données

Bien que depuis sa création le web ait été conçu comme un outil collaboratif de partage d'information, cet aspect s'est renforcé au fil des années. Des évolutions technologiques, l'extension d'internet et des ordinateurs domestiques ont permis la production de contenu web par tout un chacun, amplifiant le caractère participatif. C'est le Web 2.0 avec les wikis, blogs et forums. Dans certains domaines très organisés, avec parfois des règles de contribution strictes et des automatismes permettant d'en contrôler le sens et la forme, le web s'est transformé en énorme base de données. C'est le **web des données** avec Wikipedia comme illustration majeure, ou d'autres bien moins connus mais tout aussi importants dans des domaine spécifiques comme `MusicBrainz` (musique), `GeoNames` (géographie), `OpenStreetMap` (cartographie),... 

Pour rendre ces données maintenant accessibles à des traitements automatiques et donc des applications, plusieurs initiatives de chercheurs et de communautés d'utilisateur ont vu le jour pour rassembler ces données dans des bases de données bien plus structurées.  L'idée est donc de construire des **bases de connaissances** en phase avec l'ambition d'un **Web sémantique**. Les bases `Wikidata` ou `DBpedia` ont ainsi été initiées.  Les données sont décrites sous forme de triplets de la forme **(sujet, propriété, objet)** comme, par exemple, `(Led Zeppelin, IsA, MusicGroup)` ou `(Jimmy Page, IsMemberOf, Led Zeppelin)` qui peuvent être vues comme des phrases de la forme sujet verbe complément énonçant des faits comme `Led Zeppelin est un groupe de musique` et `Jimmy Page est membre de Led Zeppelin`. 


Des recherches d'informations factuelles comme savoir quels sont les membres de `Led Zeppelin` deviennent alors possibles grâce à de simples requêtes dans ces bases de données. Cette évolution est en fait apparue en 2014 en premier lieu dans les résultats du moteur de recherche de Google. C'est le fameux cadre en colonne de droite présentant des informations factuelles sur l'entité. Par exemple, pour`Led Zeppelin`, vous trouvez une description du groupe, sa composition, le genre de musique, les principales chansons, les principaux albums, et des images associées. 

Les données issues de `Wikidata` ou `DBpedia` sont libres et ouvertes. De ce fait, chacun peut les utiliser et les exploiter et la plupart des moteurs de recherche le font. Toutefois, les données peuvent être enrichies et complétées seulement en interne de certains grands groupes (comme Google avec son Knowledge Graph).




## Langage naturel et raisonnement

L'interrogation du moteur à l'aide mots clefs est une évidente limitation. De nombreux travaux portent sur la possibilité d'écrire des requêtes en langage naturel, comme `Quel est l'âge de Robert Plant ?` ou `Quel temps fera-t-il demain ?` . À certains types simples de questions factuelles comme celles-ci, des moteurs de recherche sont capables de répondre.   Comment est traitée cette requête ? Tout d'abord, il y a des traitements pour reconnaître que c'est une question, en déterminer le verbe, le sujet, le complément. Le traitement de la langue comprend beaucoup de problèmes difficiles pour les machines. Mais avec une requête comme `Quel est le membre le plus âgé de Led Zeppelin ?`, en plus des difficultés précédentes, il faut comprendre la sémantique de la question et faire un raisonnement : trouver les membres, l'âge de chacun, comprendre que l'on cherche l'âge le plus élevé et comparer les âges. Même si ces requêtes ne donnent pas la réponse attendue aujourd'hui, les recherches progressent et les moteurs augmentent toujours leurs possibilités. Des avancées dans le traitement automatique des langues et dans la constitution de plus grands web des données contribuent à cette évolution. Mais, des requêtes plus complexes encore nécessitent d'enchaîner des recherches de faits, des raisonnements ou des traitements, et aujourd'hui et pour encore longtemps, c'est  inaccessible à la machine. 



# Questions éthiques
## La loyauté des moteurs

Nous avons vu dans ce cours que les formules de calcul de score pour un moteur de recherche d'information évoluent et la compréhension du calcul du score et donc de l'ordre des réponses devient de plus en plus complexe. Ces formules, à l'exception de très peu de moteurs de recherche, parfois libres, sont secrètes même si on en connaît les éléments principaux.  Retenez que **l'ordre des réponses est donné par un algorithme secret écrit par une entreprise commerciale**.

Ceci pose des *questions éthiques* car les réponses proposées et leur ordre peuvent manipuler l'opinion. Elles peuvent influencer votre vision sur une question et peuvent influencer vos achats.  Il existe une forte concurrence entre les sites sur la question du référencement, c'est-à-dire sur la question d'être bien classé dans 'ordre des réponses. C'est le cas des entreprises commerciales qui veulent apparaître pour vous vendre des produits. C'est le cas de courants de pensée qui veulent imposer une opinion comme, par exemple, les courants anti-avortement qui agissent pour que les sites critiquant l'avortement apparaissent bien classés lorsque vous faîtes une requête sur l'avortement. 
Comment peut-on être sûr que l'algorithme est loyal, que l'entreprise qui propose le moteur de recherche ne favorise pas certains produits ou certaines idées ?  C'est-à-dire comment savoir qu'elle respecte l'égalité de traitement entre les sites Web ?

Retenez que **vous devez toujours avoir un regard critique sur les réponses qui vous sont proposées et leur ordre**. Ceci est vrai pour les moteurs de recherche d'information mais aussi pour beaucoup d'applications Web vous suggérant ou vous recommandant des produits, des contacts, des informations, des restaurants et autres. C'est vrai également dans tout le monde numérique où on utilise des algorithmes pour vous affecter dans un établissement scolaire ou dans une filière de l'enseignement supérieur.

## Assistants personnels 

La reconnaissance automatique de la parole qui consiste à transformer les signaux acoustiques en une suite de mots fonctionne aujourd'hui assez bien dans les langues les plus parlées. Il en est de même pour l'opération inverse de synthèse de la parole à partir de texte. Ces progrès assez fulgurants ont été réalisés grâce aux technique d'apprentissage machine et notamment aux réseaux profonds (Deep Learning). Les moteurs de recherche sont donc accessibles depuis des petits ordinateurs sans clavier (ou presque) tels que les assistants domestiques ou les smartphones. Mais dans ce cas la réponse se limite souvent à une liste très courte, voire même une seule réponse. L'impact du calcul du score, la question de la loyauté sont alors encore plus forts et peut devenir très conditionnant. 


## Respect de la vie privée

Les moteurs de recherche comme désormais beaucoup de logiciels sur le Web disent s'adapter à vos besoins. Les langues naturelles sont ambiguës et un mot peut avoir plusieurs sens. Par exemple, le mot `java` peut désigner un langage de programmation ou une danse ou une île. Un internaute informaticien souhaiterait voir apparaître des pages parlant du langage de programmation alors qu'un autre utilisateur préférera des informations sur la danse. Ceci peut être réalisé si l'historique des recherches et des liens suivis est connu. À l'aide de cookies et plus facilement encore lorsque vous avez un compte et que vous êtes identifiés, le moteur peut mémoriser cet **historique des recherches et des navigations**, en déduire un profil et l'utiliser pour adapter son calcul de score. Un autre type d'adaptation est d'utiliser les **informations de localisation** obtenues à partir d'un gps si vous êtes géolocalisés ou à partir d'informations sur l'ordinateur sur lequel vous faites votre requête. Le score des pages portant sur des objets proches de vous peut alors être renforcé. Mais ces informations historiques et de géolocalisation disent beaucoup de choses à votre sujet, de façon directe ou indirecte. Ce sont des **données personnelles**.  Retenez donc que **l'adaptation à vos besoins implique la mémorisation de données personnelles**.

Mais même si l'objet n'est pas de personnaliser les réponses d'un moteur de recherche ou d'un service web, la collecte des données personnelles a bien lieu. Car en effet, ces données ont de la valeur, elles peuvent être un outil pour être plus compétitif vis à vis de la concurrence, elles peuvent être revendues à des tiers,... Le modèle dominant est alors de collecter toutes ces données personnelles et de les  mémoriser par l'entreprise concevant le logiciel.

Le nouveau règlement général sur la protection des données personnelles qui s'applique désormais en Europe (le RGPD) définit des limites et des contraintes sur cette collecte et gestion des données personnelles. C'est un excellent outil de sensibilisation. Mais ce n'est pas la réponse définitive à cette question importante du respect de la vie privée car il ménage à la fois les intérêts commerciaux et ceux des utilisateurs et laisse une grande place à l'interprétation. 



## Des réponses possibles ?
### Les liens payants

La fenêtre de réponse des moteurs de recherche contient une liste ordonnée par score de pertinence de l'ensemble des pages Web et éventuellement un cadre contenant des données factuelles relatives à la requête dont nous avons déjà parlé dans ce cours. Vous avez également souvent une liste ordonnée de **liens sponsorisés**. Pour ces liens, seules apparaissent des entreprises qui rémunèrent l'entreprise associée au moteur de recherche d'information. La rémunération peut être calculée sur le nombre d'utilisateurs cliquant sur les liens proposés. Retenez donc que **l'apparition dans une liste de liens sponsorisés est lié à une rémunération**.

Ces liens commerciaux sont donc une source de revenus pour le moteur de recherche. Ce n'est pas forcément un mal en soi, car le service coûte cher. Une formule doit être trouvée soit par des financements participatifs, par l'impôt ou par le commerce. Si ces liens commerciaux sont bien séparés et annoncés comme tels, ils peuvent contribuer à ne pas (ou modérer) les problèmes de loyauté et de respect de la vie privée. C'est par exemple la solution choisie par [Qwant qui affirme ne pas mémoriser les traces de navigation et ne pas créer de profil](https://about.qwant.com/fr/legal/confidentialite/à)
de ses utilisateurs.

### Code source ouvert!

C'est une question très sensible actuellement et les lois évoluent pour que les algorithmes puissent expliquer leurs décisions. Pour les moteurs, cela signifie expliquer le calcul des scores pour vérifier sa loyauté. Certains militent donc pour que les formules de calcul de score soient publiées pour que l'utilisateur sache pourquoi certaines pages lui sont proposées plutôt que d'autres. La réponse des entreprises liées aux moteurs est souvent de dire que la diffusion de ces formules permettraient de tricher plus facilement. Mais, on peut noter que `Qwant` s'est engagé à diffuser
ses formules de calcul de score.


### Éducation 

Mais nous sommes convaincus qu'une réponse pérenne passe par l'éducation des citoyens, qu'ils soient responsables politiques, juristes, journalistes ou simplement usagers. Pour que ces questions soient abordées dans les lois, dans les médias et dans les esprits. 



```compréhension

::S'identifier sur le Web::
[markdown]
Les réponses et l'ordre des réponses sont les mêmes en tant qu'utilisateur anonyme ou utilisateur connecté à 1 compte{F}

::Web des données::
[markdown]
Tentez de deviner le personnage qui sera affiché dans l'encadré Web
des données pour la requête *et*. *Première aide* : c'est un personnage
cinématographique célèbre mais daté. *Deuxième aide* : pensez que le moteur ne tient pas compte de la casse et des symboles de ponctuation. *Troisième aide* : ce film daté est un film de science fiction.


::Requêtes et (géo)localisation::
[markdown]
les suggestions de restaurants dépendent du lieu où la requête est posée{T}

::Algorithmes et recherche d'information::
[markdown]
Serge Abiteboul est membre de l'académie des sciences et parmi les brillants chercheurs français en informatique. Lisez [son interview](https://www.fabernovel.com/insights/cultures/il-a-assiste-a-la-premiere-demo-de-google-par-brin-et-page) sur la création de Google et sur les problèmes éthiques liés aux algorithmes comme les algorithmes utilisés dans un moteur de recherche d'information. Quelles sont les  affirmations suivantes qui sont vraies
{
~ Google a été crée dans les années 1980
~%33% Google est issu de chercheurs universitaires
~%33% Google était à l'origine sans liens payants et sans publicité
~ Les algorithmes actuels de Google sont transparents
~%34% Il faut être attentif et responsable devant les réponses d'un algorithme comme un moteur de recherche d'information.
#### Google a été créé à la fin des années 90 par des universitaires et il était à l'origine transparent et sans publicité. Ce qui n'est plus le cas aujourd'hui. C'est un algorithme secret, même si on en connaît les principes, et écrit par une entreprise privée qui classe les réponses à vos requêtes et donc vous devez toujours regarder ces réponses en pensant que certaines réponses ont pu être oubliées car mal classées.}

```

