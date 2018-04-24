LANGUAGE:   fr
TITLE:   Recherche d'information et référencement Web
MENUTITLE: Recherche d'information Web
AUTHOR: Culture numérique
CSS: http://culturenumerique.univ-lille3.fr/css/base.css

<!-- pandoc -t latex -V geometry:margin=3cm --toc ri.md -o ri.pdf -->

<!-- pandoc -F ext.py -t latex -V geometry:margin=3cm --toc ri.md -o ri.pdf -->

# La recherche d'information : contexte et application au Web

Avec l'avènement du numérique et, en particulier, du Web, nous vivons dans un monde de documents, de ressources numériques. Ces documents sont divers comme des sms, des tweets, des mails, des pages Web, des articles journalistiques ou scientifiques, des livres, ... Ils contiennent des informations textuelles mais aussi des dessins, des images et des vidéos. Ils proviennent de sources variées comme des administrations, des journaux, des entreprises commerciales mais aussi les réseaux sociaux et les objets connectés (caméras, compteurs intelligents, gps, ...). Ils sont en très grande quantité avec, par exemple, un nombre estimé de 60 000 milliards de documents Web en 2016. Cette masse de documents génère de nouvelles possibilités comme pouvoir retrouver des documents concernant un sujet précis, pouvoir proposer des suggestions d'articles de journaux ou encore pouvoir faire des recommandations de livres à lire ou de films à regarder.

Nous allons considérer la **recherche d'information** et, en particulier un outil numérique utilisé quotidiennement par chacun d'entre nous : le **moteur de recherche d'information**. La fonction première d'un moteur de recherche est de vous permettre de *poser une requête*  et recevoir en réponse une partie d'un ensemble de ressources (documents texte, images, vidéos,...). On s'intéresse exclusivement aux ressources textuelles dans le cadre de ce cours. L'ensemble des ressources sur lesquels les requêtes sont posées est accessible au moteur de recherche et organisé de façon à répondre efficacement. C'est la phase d'*indexation*, autrefois manuelle dans les bibliothèques et aujourd'hui largement automatisée qui est responsable de cette organisation. La réponse peut être exhaustive pour certaines requêtes simples et bien formalisées, mais le plus souvent le moteur  renvoie *une liste ordonnée de documents selon un score de pertinence*.

Dans cet objectif, nous commençons par présenter les méthodes exactes de recherche d'information comme la recherche d'un mot dans un texte. Nous décrivons ensuite les méthodes approximatives utilisées dans les moteurs de recherche du web qui combinent une mesure la proximité entre une requête et le contenu d'une page avec le **score de notoriété**.  C'est l'introduction de ce score de notoriété qui mesure l'importance de la page dans le réseau constitué des pages Web reliées entre elles par
des hyperliens qui est calculé par le fameux algorithme **PageRank**.

Après un examen des tendances nouvelles,  nous concluons par une discussion sur les problèmes éthiques et sociaux posés par les moteurs de recherche. En effet, chaque moteur utilise ses propres algorithmes pour répondre aux requêtes et beaucoup d'éléments du calcul de score ne sont pas connus des utilisateurs ce qui pose, en particulier, la question de la **loyauté des moteurs de recherche d'information**.


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

# Les modes de recherche d'information

## La recherche exacte

De nombreux logiciels comme les traitements de texte, les éditeurs, les outils de messagerie vous proposent une fonction de recherche lorsque vous visionnez un document, un texte, un message,... En actionnant le menu *Rechercher* voire un simple bouton, vous avez la possibilité de taper quelques caractères. Ces mots définiront une requête et dans le plus simple des cas, le logiciel vous dirigera vers (ou vous surlignera) chaque position ou ces quelques caractères apparaissent. 

Pour réaliser cela, un algorithme de recherche parcourt le document de début à la fin et  pour toutes les positions, il évalue si le texte commençant à cette position correspond exactement à la requête. On parle de *recherche séquentielle* car l'algorithme évalue séquentiellement toutes les positions. 
Vous pouvez imaginer une petite fenêtre qui se déplace séquentiellement puis compare deux à deux les  caractères recherchés avec ceux dans la fenêtre. 

Des travaux maintenant anciens ont étendu cette recherche séquentielle en définissant des langages de requêtes qui dépassent cette simple comparaison deux à deux. Dans ces langages de requêtes certains  caractères prennent un sens différent de leur usage habituel. Le `?` ne désigne plus le point d'interrogation mais une présence optionnelle, si bien que la requête `mal?in` permet de dire que le `l` est optionnel et trouvera donc les positions où se trouve  `main` ou `malin`.  Le `.` par exemple représente n'importe quel caractère plutôt que le point et `*` n'est plus une étoile mais une répétition. La requête `le .* dort` fonctionne comme un texte à trous qui peut rechercher par exemple `le gros chat noir dort`. Un tel langage de requête étendu s'appelle le langage des *expressions régulières*. 

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

## La recherche exacte rapide avec un index

Lorsque vous utilisez l'index d'un livre, d'un atlas ou d'une encyclopédie, vous utilisez la liste des mots indexés rangés alphabétiquement pour trouver les pages du livre où ces mots sont définis ou utilisés. L'ordre alphabétique permet également rechercher très rapidement dans cet index. Cette simple organisation est reproduite dans les moteurs de recherche d'information pour dépasser la simple recherche séquentielle qui peut prendre un temps de calcul trop grand. 

Pour construire cet index, il faut choisir une représentation des documents. Dans les bibliothèques, les ouvrages sont  décrits ou représentés par des notices contenant des méta-données comme le titre, les auteurs, les éditeurs, une liste de mots-clés. L'index est alors construit à partir de ces informations collectées le plus souvent "à la main". Mais aujourd'hui, l'automatisation de cette phase d'indexation s'est généralisée.  Elle s'applique également sur le texte complet et donne alors la possibilité de *recherche plein texte*, à l'instar de ce qui est fait par les moteurs de recherche pour les documents du web. 

Comment fonctionne cette indexation automatique ? Chaque texte est découpé en une séquence d'unités
élémentaires, appelés `tokens`, qui sont des suites de caractères sans espace et sans symbole de ponctuation. Un token correspond à un mot de la langue ou un nombre ou une date ou un sigle.  De nombreux choix, parfois dépendants de la langue conditionnent ce découpage en tokens. Par exemple, considère-t-on différemment les majuscules et les minuscules ? Considère-t-on les accents ? Un texte comme  `La Révolution française, 1789-1799 : Une histoire socio-politique` pourrait alors être transformé en une suite de tokens `la revolution francaise 1789 1799 une histoire socio
politique`. L'ensemble de tous les tokens possibles, ou plus précisément, rencontrés dans l'ensemble de tous les documents qui constituent la base documentaire à indexer forme le **vocabulaire**. Parfois, les mots très fréquents sont retirés du vocabulaire, par exemple en français le `et`, `le`, ...

L'étape suivante pour la réalisation de l'index est maintenant d'associer à chaque token du vocabulaire l'ensemble des documents dans lesquels ce token apparaît. Pour cela on affecte un numéro unique, appelé identifiant, à chaque document de la base documentaire. La structure de l'index est alors simplement une liste de tokens avec pour chacun la liste des identifiants des documents où se token se trouve. Par exemple, l'index  mémorise que le mot `rose` apparaît dans les
documents de numéro 125, 245, 567, ... ; que le mot `blanche` apparaît
dans les documents de numéro 117, 176, 245, 312, ...

L'index peut avoir une taille de plusieurs centaines de milliers de tokens. Il est lui même organisé de façon à ce qu'une recherche soit rapide. Parmi les techniques utilisées, on peut décrire la plus simple. Il s'agit de s'assurer que l'index soit organisé par ordre alphabétique des tokens. Dans ce cas un algorithme de  *recherche dichotomique* peut être utilisé. La recherche dichotomique est illustrée en cherchant par exemple le mot `rose` : on regarde le mot au milieu du dictionnaire, c'est `maman`, donc on cherche dans la seconde moitié ; on regarde le mot au milieu de la seconde moitié, c'est `savant`, donc on cherche entre `maman` et `savant` ; jusqu'à trouver le mot `rose`. On peut montrer qu'un tel algorithme est très efficace. Pour un dictionnaire de 500 000 mots, il suffit d'effectuer 19 accès, pour une dictionnaire de 1 million de mots, il suffit d'effectuer 20 accès. Notons que si la taille du dictionnaire double, on ne doit faire qu'un accès supplémentaire ! Ce
qui explique la rapidité de ce mode de recherche. Terminons en signalant que des méthodes dites de hachage permettent d'effectuer des recherches plus rapides encore. 

Nous avons présenté la phase d'indexation qui fournit comme résultat un index défini de la manière suivante :

> Un **index** est constitué d'un vocabulaire avec une méthode
> d'accès rapide à un token, et, pour chaque token, on dispose de la liste
> des identifiants des documents qui contiennent ce mot.

Comment l'index permet-il de répondre rapidement à des requêtes formulées dans un moteur de recherche exacte ?

- Si la requête ne contient qu'un seul mot, on cherche si ce mot est un token dans l'index et on renvoie la liste des documents donnés par leurs identifiants associée dans l'index.
- Si la requête est composée de deux mots, le moteur procède comme suit : chercher le premier mot dans l'index et renvoyer la liste des identifiants de documents ; faire de même pour le deuxième mot ;  construire la liste  des identifiants qui apparaissent dans les deux listes (c'est une simple intersection de listes) ; renvoyer cette  liste comme réponse à la requête. Ce principe peut être étendu pour des requêtes à  plusieurs mots clés
- Une requête à plusieurs mots clés est interprétée avec un opérateur `ET` implicite car on souhaite que tous les mots soient présents. On  peut aussi écrire des requêtes avec les opérateurs logiques `OU` et `NON` qui correspondront à d'autres opérations simples sur les listes (union ou différence).
- Les interfaces des moteurs documentaires proposent également des *requêtes par position*. La plus importante est la **requête par phrase** où on recherche les mots en respectant exactement les positions des mots de la requête. Une requête par phrase est souvent exprimée avec des guillemets. Par exemple, si on considère la requête par phrase `"rose blanche"`, le moteur doit renvoyer tous les documents contenant les deux mots `rose` et `blanche` à des positions consécutives. Ceci peut être réalisé grâce à un index plus complet  mémorisant également les positions auxquelles apparaissent les tokens. Il existe d'autres requêtes par position exprimant des conditions sur les positions relatives de mots. Par exemple, on pourrait écrire une requête demandant que les mots `rose` et `blanche` soient distants de moins de 3 mots.

## La recherche approximative avec un score de pertinence

Les systèmes étudiés jusqu'à présent renvoient la liste complète des documents qui satisfont la requête. Lorsque le corpus de documents sur lequel porte les requêtes est trop grand, cette recherche est bien souvent inutile. Les moteurs de recherche du Web fonctionnent différemment et ordonnent la liste de résultats selon des scores attribués aux documents. Ceci permet d'effectuer des recherches approximatives mais aussi de faciliter la lecture du résultat. Il est donc alors nécessaire de définir et calculer **un score de pertinence relativement à une requête**.

### Représenter des documents par des tableaux de nombres

On suppose toujours un grand ensemble de documents textuels possèdant
un numéro (un identifiant), on suppose avoir défini un dictionnaire et
construit un index.  Pour calculer un score, il faut des valeurs
numériques. Pour cela on va représenter un document par un tableau de
nombres appelé *vecteur*. La plus simple des représentations consiste
à représenter un document par un (très grand) vecteur. Chaque élément
du vecteur, aussi appelé *composante*, correspond à un mot du
dictionnaire et sa valeur est 1 si le mot apparaît dans le document et
0 sinon. Prenons l'exemple d'un dictionnaire contenant les mots de
langue française et du document textuel `citoyennes tricoteuses - les
femmes du peuple à paris pendant la révolution française`. Ce document
sera représenté par un vecteur avec une composante par mot du
dictionnaire et toutes les composantes valent 0 sauf les composantes
pour les mots `à`, `citoyennes`, ..., `tricoteuses` qui valent 1. On
mémorise donc la *présence (valeur 1) ou l'absence (valeur 0)* d'un
mot du dictionnaire dans le document. Cette représentation est appelée
**Boolean frequency**,

Plutôt que de mémoriser simplement la présence ou l'absence, une
extension est de compter combien de fois chaque mot apparaît. On
obtient une seconde représentation, appelée **Term frequency**, pour
laquelle un document est représenté par un vecteur où chaque
composante correspond à un mot du dictionnaire et la valeur est le
nombre d'occurrences (d'apparitions) du mot dans le document. Par
exemple, considérons le document `réflexions sur la révolution de
france suivi d'un choix de textes de burke sur la révolution`.  Il
sera représenté par un vecteur dont toutes les composantes valent 0
sauf les composantes pour les mots `réflexions`, `france`, ... qui
valent 1 et les composantes pour les mots `de`, `la`, `révolution` et
`sur` qui valent 2 car ils apparaissent deux fois.

Mais, lorsque vous écrivez des requêtes sur le Web, vous savez que des
mots trop fréquents vont vous retourner trop de réponses donc vous
essayez d'exprimer votre requête avec *des mots ou termes plus
pertinents ou plus discriminants* dans le sens où vous savez qu'il y a
moins de documents contenant ces mots. Nous allons, par conséquent,
présenter une troisième représentation, appelée **term
frequency -- inverse document frequency (tf-idf)**, qui pénalise les
mots fréquents et favorise les mots rares.  Dans cette représentation,
on multiplie la fréquence d'apparition (*tf* pour term frequency) par
un facteur (*idf* ou inverse document frequency). Nous ne donnons pas
la définition mathématique de l'idf mais il suffit de retenir que
l'idf d'un mot

- est *grand pour un mot rare* qui apparaît dans peu de documents
- est *petit pour un mot fréquent* qui apparaît dans beaucoup de
  documents

Par conséquent, la multiplication par l'idf va augmenter la valeur
pour les mots rares de la collection et la diminuer pour les mots
fréquents. Par exemple, considérons le --très petit-- document `la
révolution française`. Sa représentation tf avec les fréquences aurait
1 pour le mot `la`, 1 pour le mot `révolution` et 1 pour le mot
`française` et 0 pour tous les autres mots du dictionnaire. Sa
représentation tf-idf aurait une valeur très petite pour le mot `la`
(car la est très fréquent) disons 0,01, moyenne pour le mot
`française` disons 0,14 et plus grande pour le mot `révolution` disons
0,25 (révolution est le moins fréquent des 3 mots). La représentation
tf-idf permet donc de renforcer la valeur pour les mots qui
apparaissent dans peu de documents ce qui va aider à trouver les
documents les plus pertinents.

Il existe de nombreuses variantes de ces représentations vectorielles
qui ont été étudiées et dont on a comparé les performances en
recherche d'information. Trouver la représentation vectorielle d'un
texte la mieux adaptée à une tâche reste un sujet de recherche actuel.

### Score de pertinence entre un document et une requête

Il faut définir un score qui doit mesurer à quel point un document
correspond à une requête composée de plusieurs mots clé. Ce score sera
grand si le document est très pertinent pour la
requête. Intuitivement, un document est pertinent si il contient les
mots de la requête et si ces mots apparaissent souvent dans le
document. De plus, le score doit être renforcé pour les mots rares et
diminué pour les mots fréquents. Pour cela, on représente, en général,
un *document avec la représentation tf et la requête avec la
représentation tf-idf*. Plusieurs formules de calcul de score de
pertinence ont été proposées mais une des plus utilisées que nous
expliquons ici est la **similarité cosinus ("Cosine similarity" en
anglais)**. Le score exprime à quel point les deux représentations
vectorielles sont alignées en multipliant les composantes deux à deux
(correspondant à un même mot) et en sommant les résultats. Pour une
requête à plusieurs mots clés, sa représentation vectorielle est
constituée de 0 partout sauf pour les mots de la requête. Par
conséquent, seules les valeurs associées aux mots de la requête vont
être utilisées dans le calcul du score. Illustrons par des exemples ce
calcul de score de pertinence :

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
relativement à la requête. Le calcul de la Cosine similarity est, en
réalité, un peu plus compliqué car il faut limiter l'influence de la
longueur des documents.  Le calcul de la pertinence fait donc
intervenir une normalisation qui revient à ramener tous les documents
à une même longueur.

Notons enfin que les notices sont structurées, que les documents sont
structurés avec titre, résumé, ... On peut calculer un score de
pertinence pour chacun de ces éléments et combiner ces scores. Nous
reparlons de ce point lorsque nous définirons le score de pertinence
Web dans la suite.


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

Nous avons présenté l'indexation et la calcul de score de pertinence
d'un document textuel relativement à une requête. Nous allons voir
comment ce score est adapté aux documents du Web. Nous présentons
ensuite le score de notoriété qui mesure l'importance d'une page
Web. C'est ce score introduit par `Google` qui lui a donné un avantage
significatif sur ses concurrents dans les années 1990. La combinaison de ces
deux scores est la base du score d'un document Web relativement à une
requête quel que soit le moteur utilisé.

## Indexation du Web

Pour calculer un score de pertinence, il faut au préalable que les
documents du Web soient indexés. Nous présentons quelques points
essentiels :


- L'**indexation du Web** est réalisé par des **programmes appelés
robots** qui parcourent les sites Web et suivent les liens. Ces
programmes récupèrent le contenu des pages et la structure des sites
(les hyperliens et l'organisation).
- **Tous les documents du Web sont indexés** quel que soit leur format :
  pages Web au format `html`, documents imprimables au format `pdf`,
  documents au format `doc`, ... ce qui mène à un nombre de documents
  de l'ordre de 60 000 milliards en 2016.
- **Tous les mots qui apparaissent sur le Web sont indexés** quels que
  soient leur fréquence, la langue, ..., ce qui amène à un
  dictionnaire contenant plusieurs millions de mots.
- Ceci permet de construire un **index de très grande taille** qui est
  **mis à jour continûment** avec les informations récupérées par les robots
- L'index est réparti sur des fermes de calcul (un grand nombre
  d'ordinateurs de grande capacité en réseau) réparties dans le monde
  entier. On peut noter que cela implique une très grande consommation
  d'énergie et donc le Web n'est pas si écologique qu'on pourrait le
  croire.



## Score de pertinence

Considérons un document du Web -- une page Web -- au format `html`. Un
tel document a un contenu mais aussi une structure avec un titre
principal et des sections ayant des titres. L'apparition d'un mot de
la requête dans un titre est plus important que son apparition dans le
contenu. Ceci doit donc être pris en compte dans le calcul de
pertinence. Un deuxième élément qui est spécifique au Web concerne les
liens (ou hyperliens). En effet, lorsqu'un lien sur une page Web est
créé, il est associé à un texte qui contient de l'information sur la
page. Par exemple, un site Web qui souhaite mettre un lien sur ce
module culture numérique définira un texte cliquable comme `cours
d'introduction à la recherche information` qui est très informatif sur
le contenu de la page. Il est donc intéressant de le prendre en compte
dans le calcul du score de pertinence.

Par conséquent, le score de pertinence d'une page Web va prendre en
compte des scores de pertinence calculés sur **différentes vues sur la
page Web** dont les principales sont :

- le contenu textuel de la page
- les titres de la page
- les mots clé associés à la page définis dans son entête et plus
  généralement les méta données de la page Web
- l'adresse du document (un texte de la forme
  `https://culturenumerique.univ-lille3.fr/modulerechercheinformation.html`)
- les textes des liens qui pointent sur la page

Pour chacune de ces vues, un score de pertinence peut être calculé
avec la méthode introduite auparavant. Il reste à combiner ces scores
avec une formule de la forme : un pourcentage du score de contenu + un
pourcentage du score des titres + ... **La formule de combinaison est
secrète !**. C'est-à-dire que l'on ne connaît pas les pourcentages
utilisés dans la formule. Par exemple, suite à de nombreux abus de
concepteurs de pages Web qui ajoutaient des mots clé fictifs (sans
rapport avec le contenu) pour essayer d'améliorer artificiellement
leur score, on a pu constater que l'influence du score de pertinence
des mots clés a été diminuée.

## Score de notoriété

Le Web a une structure de réseau ou de graphe avec des pages Web qui
pointent les unes vers les autres avec les hyperliens. L'idée est
d'utiliser cette structure pour mesurer *la notoriété* des pages. On
souhaite donc définir un *score de notoriété* qui va mesurer à quel
point une page est importante pour les internautes. Une première
tentative de définition de score de notoriété d'une page pourrait être
le nombre de pages qui pointent sur elle. Cette définition n'est pas
robuste car on peut tricher (cela a été fait). En effet, il suffirait
pour renforcer le score de notoriété d'une page de créer (en grand nombre)
des pages artificielles qui pointent sur cette page. La définition
doit donc être plus intelligente et une bonne définition est la
suivante :

> Une page a **une forte notoriété si beaucoup de pages ayant une
> forte notoriété** pointent sur elle

Définir la notoriété n'est pas si simple car on voit que pour définir
une page de forte notoriété il faut déjà savoir calculer la
notoriété. C'est un exemple de définition récursive où on définit la
notoriété à partir d'elle-même. Mais ceci est fréquent en mathématique
et en informatique. Il est donc possible de mettre cette définition en
équations et de définir des algorithmes qui vont permettre de calculer
la notoriété d'une page Web. Une autre vision de la notoriété peut
être définie avec la notion de **surfeur aléatoire**. L'idée est
d'imaginer qu'un surfeur navigue sur le Web en suivant des liens. Pour
cela,

- il peut choisir une page au hasard sur le Web -- ceci correspond à
émettre une requête et suivre un lien sur la page de réponse
- lorsqu'il est sur une page Web, il peut choisir au hasard un des
  liens présents sur la page et le suivre

Le surfeur aléatoire choisit donc une page au hasard, il suit des
liens en partant de cette page puis, après avoir suivi quelques liens,
il recommence en choisissant une nouvelle page au hasard. Si le
surfeur réalise ceci un très grand nombre de fois, toutes les pages
Web seront visitées et plus souvent elles sont visitées plus elles
sont importantes. Le score de notoriété d'une page correspond donc à
la fréquence de visite de cette page par le surfeur aléatoire. Cette
définition a été démontrée équivalente à la précédente. Un algorithme
pour calculer le score de notoriété, appelé **algorithme PageRank**, a
été introduit par les fondateurs de Google au milieu des années 1990
dans un moteur de recherche d'information. Si les principes de cet
algorithme étaient connus, c'était un challenge de l'appliquer à la
recherche d'information avec des tailles de données (dictionnaire et
nombre de documents) très grands. Cet algorithme permet donc
d'**attribuer à toute page Web un score de notoriété**.

## Score Web

Une requête sur le Web dans un moteur de recherche d'information est
très souvent exprimée comme une suite de mots clés. Le **score Web
d'un document Web relativement à une requête** est calculé comme une
combinaison de la forme : un pourcentage du score de pertinence de la
page relativement à la requête + un pourcentage du score de notoriété
de la page. Ici encore la formule de combinaison n'est pas connue !
Ici encore, on sait qu'elle existe et qu'elle évolue. Par exemple, on
observe chez `Google` que la part du score de notoriété est de plus en
plus grande. En effet, les pages les mieux classées ont souvent une
forte notoriété comme les pages Wikipedia, des pages de sites de
journaux et, plus généralement, des pages de sites de
référence. Retenez que **le score Web est calculé principalement à
partir de la pertinence et de la notoriété**.

Rappelons également qu'il existe différents moteurs de recherche
d'information comme, par exemple, `Qwant` et `Google`. Chaque moteur a
développé ses propres algorithmes et ses propres formules de calcul
basés sur la pertinence et la notoriété.  On peut penser à des
recettes de cuisine utilisant les mêmes ingrédients mais avec des
proportions et des modes de cuisson différents. Certains moteurs vont
privilégier la notoriété alors que d'autres vont essayer d'introduire
de la diversité dans les réponses. Il est donc important de retenir que
**les réponses et l'ordre des réponses à une requête diffèrent selon
le moteur choisi**.

Si les deux éléments essentiels sont le score de pertinence et le
score de notoriété, le score Web fait intervenir d'autres éléments
sans qu'on sache exactement comment ils interviennent dans le calcul
du score Web. Les éléments principaux intervenant dans le calcul sont :

- la langue d'interrogation
- le pays du site du moteur
- le média d'interrogation (ordinateur ou téléphone portable) et sa
  localisation
- les données d'usage

Pour ce dernier point, les données d'usage consiste à connaître les
liens dans les pages de réponse sur lesquels les utilisateurs ont
souvent cliqués. Ces pages vont voir leur score renforcé ce qui
contribue à renforcer encore le score des pages souvent visitées. Le
score privilégie alors fortement la notoriété vue par la majorité des
utilisateurs au détriment de la diversité. Notez également que ces
données d'usage sont possédées par les grands acteurs du domaine ce
qui leur donne un avantage concurrentiel important. D'autres éléments
sont certainement pris en compte.  Retenez que **le score Web est basé
sur pertinence et notoriété mais il prend en compte de nombreux autres
éléments**.

Il faut également être conscient que le Web est dynamique et évolue
sans cesse ce qui va modifier les scores dans le temps. De même, les
algorithmes de calcul de score Web des différents moteurs évoluent
continuellement. Par conséquent, les réponses et l'ordre des réponses
à une requête à un moment donné ne seront peut-être pas identiques si
elles sont exécutées à un autre moment. Retenez que **le score Web
évolue dans le temps**.

Nous avons essentiellement discuté des requêtes à plusieurs mots clé
mais un autre type de requête important sur le Web (environ 15 pour
cent des requêtes) correspond aux requêtes par phrase. Rappelons
qu'une requête par phrase consiste à rechercher les documents
contenant exactement la phrase saisie. La convention usuelle est de
mettre la phrase entre guillemets dans la barre de saisie. Par
exemple, on peut considérer la requête par phrase `"la révolution
française"`. Pour cette requête, on va retourner par ordre de score
Web les documents contenant les trois mots consécutifs. Notez que
cette requête donnera donc des résultats différents de la requête à
trois mots clé `la révolution française` pour laquelle la position des
mots n'intervient pas et dont les résultats ne contiennent pas
nécessairement les trois mots.  Souvent les moteurs proposent des
requêtes avancées mais elles sont très peu utilisées en pratique.

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

# Évolutions, conclusion et discussion

## Évolutions en cours

### Adaptation à l'utilisateur

Les langues naturelles sont ambiguës et un mot peu avoir plusieurs
sens. Par exemple, le mot `java` peut désigner un langage de
programmation ou une danse ou une île. Un internaute informaticien
souhaiterait voir apparaître des pages parlant du langage de
programmation alors qu'un autre utilisateur préférera des informations
sur la danse. Même si un mot n'est pas ambigu, un utilisateur
préférera des sites d'information, un autre des articles
scientifiques, un autre encore des blogs. Il semble pertinent
d'adapter les réponses du moteur aux préférences de
l'utilisateur. Ceci peut être réalisé si l'historique des recherches
et des liens suivis est connu. Lorsque vous avez un compte et que vous
êtes identifiés, le moteur peut mémoriser cet historique des
recherches et des navigations, en déduire un profil et l'utiliser pour
adapter son calcul de score. Ceci est réalisé par certains moteurs
mais, ici encore, les formules et algorithmes utilisés ne sont pas
connus. Notez bien que cette **adaptation à l'utilisateur se fait avec
la contrepartie de la connaissance complète de votre historique de
navigation** par le moteur. Rappelons que
[Qwant affirme ne pas mémoriser les traces de navigation et ne pas créer de profil](https://about.qwant.com/fr/legal/confidentialite/à)
de ses utilisateurs.

Un autre type d'adaptation est d'utiliser les **informations de
localisation** obtenues à partir d'un gps si vous êtes géolocalisés ou
à partir d'informations sur l'ordinateur sur lequel vous faites cotre
requête. Le score des pages portant sur des objets proches de vous
peut alors être renforcé. Ici encore, les algorithmes sont spécifiques
à chaque moteur et ne sont pas connus. Notez également, lorsque vous
activez la géolocalisation, que les informations de géolocalisation
sont connues et peuvent être historisées. Ici encore, l'adaptation se
fait au détriment du respect de votre vie privée.

### Web des données

Une évolution, apparue en 2014, est que, lorsque vous tapez le nom
d'une entité du monde, que ce soit un groupe de musique (essayez `Led
Zeppelin`), un personnage célèbre (essayez `Larry Page`), un lieu
géographique (essayez `Middelburg`) ou encore un nom de fleur (essayez
`rose`), vous voyez apparaître en résultat à votre requête un cadre
présentant des informations factuelles sur l'entité. Par exemple, pour
`Led Zeppelin`, vous trouvez une description du groupe, sa
composition, le genre de musique, les principales chansons, les
principaux albums, et des images associées. Plutôt que de donner des
liens vers des pages associées à la requête, pages que vous devez
aller lire, ici on **extrait des données sur l'entité**. Ceci est
rendu possible grâce au *Web des données et connaissances* encore
appelé *"knowledge graph"*.

Le Web et les moteurs de recherche d'information étaient jusqu'alors
destinés à des utilisateurs humains qui posaient des requêtes et
allaient consulter les pages en fonction des résultats. Pour trouver
une réponse à une question factuelle comme `âge des candidats à la
présidence aux élections françaises en 2017`, il fallait taper une
requête puis aller lire la réponse sur la bonne page. Les moteurs ont
souhaité pouvoir répondre à ces questions factuelles. Pour cela, il
faut connaître les réponses. Sur notre exemple, il faut connaître
l'âge des candidats. Vous pouvez taper une requête comme `âge de X` où
vous remplacez X par votre candidat préféré ou détesté pour vérifier
que la réponse est connue et affichée. Un deuxième objectif des
moteurs, que nous verrons dans la section suivante, est de résoudre
des tâches plus complexes. Il faut alors connaître les réponses mais
aussi les comprendre et les utiliser. C'est avec ces objectifs que
s'est développé le Web des données et connaissances.

Ceci a été réalisé conjointement par des communautés spécialisées
comme en musique avec `MusicBrainz` ou en géographie avec `GeoNames`,
des communautés d'utilisateurs et de chercheurs pour des bases
généralistes avec `Wikidata` et `DBpedia`, des bases pour normaliser
la description des données avec `foaf`. L'idée est de construire des
bases de données de connaissances exploitables sur le Web. Les données
sont décrites sous forme de triplets de la forme **(sujet, propriété,
objet)** comme, par exemple, `(Led Zeppelin, IsA, MusicGroup)` ou
`(Jimmy Page, IsMemberOf, Led Zeppelin)` qui peuvent être vues comme
des phrases de la forme sujet verbe complément énonçant des faits
comme `Led Zeppelin est un groupe de musique` et `Jimmy Page est
membre de Led Zeppelin`. Ces bases de données ont été construites par
ces communautés et sont désormais utilisées voire possédées par les
grands acteurs du domaine. Des algorithmes sur ces
bases de données permettent de chercher des informations et on pourra,
par exemple, rechercher les informations factuelles sur `Led Zeppelin`
qui pourront être affichés dans l'encadré sur la page de réponses à la
requête.

Une autre source de données est issue des pages Web construites par
les utilisateurs du Web. Par exemple, un site Web de restaurant va
ajouter sur sa page Web des données comme sa latitude et sa longitude
ou encore des heures et jours d'ouverture. Ces données doivent
respecter des conventions d'écriture en `html`. Elles peuvent alors
être utilisées par des programmes (comme le navigateur) pour calculer
des distances et donc savoir si le restaurant est proche de votre
localisation ou encore pour savoir si le restaurant est ouvert afin de
vous le proposer en réponse à une requête.

### Parole et langage naturel

Il devient possible d'interroger votre ordinateur par la parole. Une
première couche logicielle se charge de transformer les signaux
acoustiques en une suite de mots de la langue utilisée. Les logiciels
de reconnaissance de la parole ont progressé très nettement ces
dernières années avec l'utilisation de méthodes basées sur des réseaux
de neurones profonds. Ce traitement étant réalisé, le moteur de
recherche d'information doit alors traiter une requête en langage
naturel.

Il est d'ailleurs possible de taper directement une requête en langage
naturel dans la barre de saisie. Nous avons déjà évoqué des requêtes
comme `Quel est l'âge de François Hollande ?`. Comment est traitée
cette requête ? Tout d'abord, il y a des traitements pour reconnaître
que c'est une question, en déterminer le verbe, le sujet, le
complément. Le traitement de la langue comprend beaucoup de problèmes
difficiles pour les machines. Seules certaines formes simples de
question sont prises en compte par les moteurs. Cependant, les
recherches progressent et les moteurs augmentent toujours leurs
possibilités.

Lorsque qu'une requête en langage naturel est posée, elle est traitée
par le moteur, puis le moteur interroge le Web des données pour
afficher une réponse factuelle à la question (si possible), il calcule
également un score Web pour afficher une liste ordonnée de pages. Il
est très difficile de savoir comment sont calculés ces scores à cause
des nombreux pré-traitements inconnus sur la requête et du calcul de
score Web dont nous avons déjà signalé que beaucoup de points étaient
secrets.

Enfin, si on considère une requête comme `Quel est le plus âgé des
candidats aux élections présidentielles de 2017 ?`, en plus des
difficultés précédentes, il faut comprendre la sémantique de la
question et faire un raisonnement : trouver l'âge des candidats,
comprendre que l'on cherche l'âge le plus élevé, comparer les âges et
retourner le nom et l'âge du candidat trouvé. Ceci ouvre la question
de l'intelligence des moteurs que nous discutons maintenant.

### Moteurs intelligents

Si les moteurs de recherche d'information sont capables de vous
suggérer des pages Web en réponse à une requête et de récupérer des
données relatives à une question factuelle, ils sont encore
**incapables de raisonner**. Pour nous en convaincre, supposons que
vous souhaitiez aller passer en week-end à Paris. Vous allez utiliser
un moteur de recherche d'information pour rechercher des horaires et
tarifs de train ou d'avion ou de bus, éventuellement en utilisant des
comparateurs, ou encore voir sur un site de covoiturage. Vous allez
chercher une auberge de jeunesse, une chambre en résidence, un hôtel
pour la nuit. Vous allez, éventuellement, rechercher des expositions,
des spectacles, des musées pour vous occuper. Le moteur vous aide mais
*l'intelligence c'est vous !* Vous savez que pour vous rendre à Paris,
il faut utiliser un moyen de transport, vous savez que les moyens de
transport principaux sont le bus, le train, l'avion. Vous avez une
connaissance du monde que ne possède pas la machine. Le Web des
données apporte cette connaissance aux machines et aux
programmes. Mais cette connaissance n'est pas suffisante car il faut
savoir l'utiliser et raisonner. Par exemple, pour choisir les
meilleures options en fonction du lieu où vous résidez et de vos
préférences. Raisonner pour être capable de choisir et d'enchaîner les
transports pour, par exemple, si je choisis le train, se rendre à la
gare avec un moyen de transport et un timing adéquat. De même pour me
rendre de la gare d'arrivée au site de résidence choisi. Actuellement,
les moteurs ne sont pas capables de répondre à des requêtes comme
`Organise moi un week-end à Paris` mais la question est étudiée et des
progrès sont attendus.

## Conclusion et discussion

### Les liens payants

La fenêtre de réponse contient une liste ordonnée par score de
pertinence de l'ensemble des pages Web et éventuellement un cadre
contenant des données factuelles relatives à la requête dont nous
avons déjà parlé dans ce cours. Vous avez également souvent une liste
ordonnée de **liens sponsorisés**. Pour ces liens, seules apparaissent
des entreprises qui rémunèrent l'entreprise associée au moteur de
recherche d'information. La rémunération peut être calculée sur le
nombre d'utilisateurs cliquant sur les liens proposés. Retenez donc
que **l'apparition dans une liste de liens sponsorisés est lié à une
rémunération**.

### La loyauté des moteurs

Nous avons vu dans ce cours que les formules de calcul de score pour
un moteur de recherche d'information sont secrètes même si on en
connaît les éléments principaux. De plus, ces formules évoluent et
avec les évolutions comme le langage naturel, la compréhension du
calcul du score et donc de l'ordre des réponses devient de plus en
plus complexe. Retenez que **l'ordre des réponses est donné par un
algorithme secret écrit par une entreprise commerciale**.

Ceci pose des *questions éthiques* car les réponses proposées et leur
ordre peuvent influencer votre vision sur une question et peuvent
influencer vos achats. Comment peut-on être sur que l'algorithme est
loyal, c'est-à-dire qu'il respecte l'égalité de traitement entre les
sites Web ?  C'est une question très sensible actuellement et les lois
évoluent pour que les algorithmes puissent expliquer leurs
décisions. Pour les moteurs, cela signifie expliquer le calcul des
scores pour vérifier sa loyauté. Certains militent donc pour que les
formules de calcul de score soient publiées pour que l'utilisateur
sache pourquoi certaines pages lui sont proposées plutôt que d'autres.
La réponse des entreprises liées aux moteurs est souvent de dire que
la diffusion de ces formules permettraient de tricher plus
facilement. Mais, on peut noter que `Qwant` s'est engagé à diffuser
ses formules de calcul de score.

Il faut savoir que, même avec des formules secrètes, il
existe une forte concurrence entre les sites sur la question du
référencement, c'est-à-dire sur la question d'être bien classé dans
l'ordre des réponses. C'est le cas des entreprises commerciales qui
veulent apparaître pour vous vendre des produits. C'est le cas de
courants de pensée qui veulent imposer une opinion comme, par exemple,
les courants anti-avortement qui agissent pour que les sites
critiquant l'avortement apparaissent bien classés lorsque vous faîtes
une requête sur l'avortement. Retenez que **vous devez toujours avoir
un regard critique sur les réponses qui vous sont proposées et leur
ordre**. Ceci est vrai pour les moteurs de recherche d'information
mais aussi pour beaucoup d'applications Web vous suggérant ou vous
recommandant des produits, des contacts, des informations, des
restaurants et autres. C'est vrai également dans tout le monde
numérique où on utilise des algorithmes pour vous affecter dans un
établissement scolaire ou dans une filière de l'enseignement
supérieur.

### L'adaptation à l'utilisateur

Enfin, beaucoup de logiciels sur le Web disent s'adapter à vos
besoins. Ils s'adaptent en réalité à votre profil qui est construit à
partir de toutes les données qui ont pu être récupérées par le
logiciel à votre inscription mais aussi auprès d'entreprises
partenaires mais surtout de toutes vos données historiques
correspondant à toutes vos actions. Ces données sont donc mémorisées
par l'entreprise concevant le logiciel et peuvent même être revendues
à d'autres éditeurs de logiciel. De même, l'adaptation à votre
localisation nécessite que vos données de géolocalisation soient
utilisées et donc soient mémorisées. Retenez donc que **l'adaptation à
votre profil et à votre localisation implique la mémorisation de
données personnelles historiques**.

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

