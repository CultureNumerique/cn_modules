
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Traitements de texte](#traitements-de-texte)
	- [Vidéo 0 - Avant de démarrer](#vido-0-avant-de-dmarrer)
	- [Interface](#interface)
	- [La saisie](#la-saisie)
		- [Repérer les composants du texte](#reprer-les-composants-du-texte)
		- [Respecter des règles de base](#respecter-des-rgles-de-base)
	- [Vidéo 1 - Saisie des éléments de base](#vido-1-saisie-des-lments-de-base)
	- [Vidéo 2 - structurer son document](#vido-2-structurer-son-document)
	- [Vidéo 3 - Personnaliser les styles](#vido-3-personnaliser-les-styles)
	- [Vidéo 4 - insertions](#vido-4-insertions)
	- [Vidéos 5 - TOC](#vidos-5-toc)
	- [Video 6 - métadonnées](#video-6-mtadonnes)
	- [Vidéo 7 -](#vido-7-)

<!-- /TOC -->
# Traitements de texte

## Vidéo 0 - Avant de démarrer

Il existe de nombreux logiciels de traitement de textes et trois d'entre eux sont particulièrement répandus :
- `Microsoft Word` de la suite `Office`
- `Writer` de la suite `LibreOffice`
- `Writer` de la suite `OpenOffice`

Tous ces logiciels ont le même objectif et donc les mêmes capacités de traitement (appelées fonctionnalités). Ils présentent de petites différences d'interface en fonction des versions et des systèmes d'exploitation des ordinateurs. Notre objectif n'est pas de les présenter tous, ni même de présenter tout ce dont ils sont capables. Ce que nous voulons que vous reteniez et que vous maîtrisiez est très général et ne dépend pas d'un logiciel en particulier.

Chacun d'entre vous pourra faire les exercices avec le logiciel de son choix à condition de respecter un format de fichier interopérable.

En effet, le choix du logiciel est en fait beaucoup moins important que le format de fichier utilisé. Aujourd'hui 2 grands formats se font concurrence :
- le format `.odt`(*Open Document Text*) qui est un standard ouvert développé pour l'interopérabilité. Il n'est pas développé par une société particulière mais par un consortium international[^1]. 
- le format `.docx` qui est la réponse apportée par `Microsoft` au format `.odt`.
La plupart des logiciels récents savent manipuler (ouvrir et enregister) des fichiers dans les 2 formats.

Notons qu'il reste encore beaucoup de vielles versions de `Word` qui qui ne savent gérer que des fichiers au format `.doc`. Ce format est propriétaire, fermé, pas du tout interopérable et il est devenu obsolète, nous déconseillons vivement son utilisation.

Nous avons choisi d'utiliser :
- le format `.odt` pour l'enregistrement des fichiers
- le logiciel `LibreOffice` pour sa faciliter d'utilisation et la possibilité pour chacun de l'installer gratuitement et librement sur sa machine.

## Objectifs de ce cours
Toutes les interfaces de logiciels de traitement de texte se ressemblent. Nous trouvons au centre une grande zone représentant une page, en haut les menus et une zone de boutons-raccourcis. La forme, les dessins, les couleurs des boutons et des menus varient d'une version à une autre, d'une machine à une autre mais les fonctionnalités sont globalement les mêmes. Le **premier objectif** est la découverte de ces fonctionnalités générales, communes à tous les logiciels, mais qui permettent de comprendre ce qu'est un document numérique, et prendre le recul sur l'usage. 

Notons que tous les logiciels de ce type utilisent un abus de langage en parlant d'outils de styles car ce sont avant tout des outils qui permettent de structurer et de hiérarchiser le document. La mise en forme associée à ces styles introduit de la confusion dans les différentes vues. En premier lieu, les *styles* sont utilisés pour définir les niveaux de titres et de sous-titres pour déclarer la **structure** du document, les aspects de mise en forme liés à la vue de présentation seront également traités avec cet outil d'où la confusion.

Notons dès à présent que les boutons raccourcis qui sont en bonne place et prêts à être utilisés sont réservés à réaliser de la mise en forme directe. C'est une mise en forme au cas par cas et qui ne privilégie pas la définition de **règles de mise en forme** comme le permettent les définitions de style. Vous savez tous réaliser une mise en forme au cas par cas à l'aide ces boutons. Ce n'est donc pas l'objet de ce cours. Vous savez moins réaliser des règles et c'est précisément sur ce point que porte le **second objectif** de ce cours. Rappelez-vous que les règles de mise en forme sont essentielles pour la manipulation de grands documents et le travail en groupe. Elles permettre d'uniformiser la présentation et appliquer des thèmes ou une charte graphique. Mais puisqu'elles reposent sur la structuration du document, elles permettent d'initier de bonnes pratiques de déclaration de cette structure. Ainsi d'autres traitements permettant de *valoriser des corpus de documents* peuvent s'appliquer, comme par exemple la recherche et l'indexation d'information... 

## La saisie

La saisie est une fonctionnalité fondamentale. Elle dépend de nombreux paramètres dont la langue, des dispositifs techniques de saisie et des aides logicielles à la saisie. 

Dans certaines langues, l'ordre d'écriture est de gauche à droite dans d'autres de droite à gauche. La langue définit les caractères, symboles graphiques utilisés, la nature des mots, les règles typographiques, etc. Les documents peuvent être multilingues. Nous nous focalisons ici sur le français.

Les dispositifs techniques influencent la saisie. Le clavier reste le plus répandu, mais se développent aujourd'hui des acquisitions par la voix.  Sur de petits équipements, on pallie l'absence de clavier par des assistances logicielles qui complètent les mots, prévoient le prochain mot etc.

L'assistance logicielle, c'est justement l'ensemble de ces fonctionnalités qui permettent de corriger la frappe, les fautes d'orthographe, compléter ou suggérer les mots, remplacer des abréviations, etc.


### Repérer les composants du texte
- les **caractères** visibles et invisibles en particulier les espaces et les fins de paragraphes.
Il est important d'avoir conscience que les espaces et les retours à la ligne sont des caractères à part entière. Les visualiser peut être intéressant pour bien comprendre ce qui a été saisi.
> il existe plusieurs sortes d'espaces, retenons surtout les espaces *normales* et les *espaces insécables*.


- les **mots**, séparés par des espaces ou des signes de ponctuation
- les signes de ponctuation qui se combinent avec des espaces en respectant les règles typographiques.
`fournir une doc *règle de typo*`
> **règle simple**
> - les ponctuations simples : pas d'espace avant, une[^2]  espace après
> - les ponctuations doubles : espace insécable avant, espace normale après.

- les **paragraphes** qui sont des ensembles de mots séparés par des *fins de paragraphes* créés par l'appui sur la touche *Entrée*.
> Du point de vue technique, chaque appui sur la touche *Entrée* crée un nouveau paragraphe, les titres et les sous-titres sont donc techniquement des paragraphes comme les paragraphes de texte. On peut donc égalmeent avoir des paragraphes vides.

- les **listes** qui peuvent être numérotées ou à puce sont des objets particuliers. Tous les items d'une liste sont reliés entre eux pour permettre une présentation cohérente.
> **Erreur à ne pas commettre**
>
> les symboles de puces ou de numérotation ainsi que l'indentation (i.e. le décalage de début de ligne) sont pris en charge par le logiciel, il est est donc tout à fait déconseillé d'insérer des espaces ou une tabulation pour commencer à saisir une liste. La bonne méthode consiste à saisir le texte du premier item et à transformer le paragraphe en liste en utilisant le bouton dédié à cela ou en passant par le menu. Chaque logiciel propose également des raccourcis-clavier permettant d'aller plus vite pour faire la même chose.

### Respecter des règles de base
Lorsqu'on récupère un texte à mettre en forme ou qu'on commence à saisir un nouveau texte, il est important de respecter scrupuleusement quelques règles élémentaires qui vont nous permettre à la fois de gagner beaucoup de temps et par ailleurs d'avoir un gage de qualité du résultat pour la vue de présentation. En effet, si nous sommes les seuls responsables du contenu de notre texte, qualité du fond, de la structure, du niveau de langue et de l'orthographe, il vaut mieux laisser au logiciel le travail de mise en forme pour la vue de présentation. Les traitements automatiques sont en général de bien meilleure qualité qu'un travail *à la main*. Cela ne veut pas dire que nous ne pouvons pas choisir la forme du résultat, bien au contraire.
Voici 4 règles fondamentales :
- Ne jamais saisir 2 *espaces* l'une derrière l'autre, les enlever s'il en existe.
- ne jamais saisir 2 *fins de paragraphes* l'une derrière l'autre, c'est à dire aucune ligne vide. Les interlignes et l'aération du texte seront bien mieux gérées par la mise en forme automatique.
- ne pas utiliser la mise en forme directe, que ce soit par le menu ou par les boutons-raccourcis. Ces boutons peuvent d'ailleurs être désactivés de l'affichage, ils ne devraient jamais servir.
- ne pas saisir des valeurs qui sont susceptibles de varier : références, numéros de page, numéros de chapitre, table des matières, bibliographies. Tous ces éléments dépendent du contenu principal du document et seront créés automatiquement par le logiciel grâce à des commandes spécifiques.



## Vidéo 1 - Saisie des éléments de base
- débuter un document, page blanche sans styleur
- saisir au kilomètre, uniquement les fins de paragraphes
- énoncer (voix off) les niveaux de titre sans mise en forme
- faire des fautes, utiliser le correcteur
- titre, sous-titre, titre1, titre2, plusieurs parag de contenu, une liste SANS mise en forme

>Cette vue est essentiellement séquentielle, les seuls éléments de structure présents sont les paragraphes, mais nous avons déjà utilisé le correcteur orthographique.

- enrigistrer (dossier / fichier / extension-format)

## Vidéo 2 - structurer son document
- reprendre à la fin de vidéo 1
- "On veut maintenant structurer le document"
- repérer la liste déroulante des styles et faire apparaître le styleur
- commencer à styler
"il suffit que le curseur soit placé dans un paragraphe pour que le style s'applique"
- montrer l'équivalence entre les deux outils
- présenter le bouton de liste ((dés)activer puces)
- détailler puce + retrait
> attention placer le texte en "corps de texte" et ne pas laisser style par défaut car tous les styles héritent de style par défaut

- présentation de la création de liste pendant la frappe
(* , - , 1), a), ...) Insister sur l'automatisation  
- enregistrer

## Vidéo 3 - Personnaliser les styles
- reprendre à la fin de vidéo 2
- modifier *corps de texte* pour le justifier, montrer l'héritage et expliquer pourquoi il ne vaut mieux pas utiliser "style par défaut".
- modifier les autres styles, espaces avant/après, couleur, interligne, alignement, enchaînements (veuves/orphelines et solidaires avec suivants)
- enregistrer

## Vidéo 4 - insertions
- insertion d'image
- notes de bas de page
- insertion de lien
- pied de page / entête
- numeros de page / champs

## Vidéos 5 - TOC
- numerotation automatique des chapitres
- génération d'une TOC

## Video 6 - métadonnées
- trouver les stats
- saisir les métadonnées

## Vidéo 7 -
- bibliographie
> surement en plusieurs fois


```activité recherche
comparer les formats odt et docx

décompresser un fichier .odt
```

[^1]: OASIS, dont font partie the Document Foundation qui développe LibreOffice, mais aussi de grands acteurs du logiciel comme Microsoft ou ORACLE, des universités, etc.
