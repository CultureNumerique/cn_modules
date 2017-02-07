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
également un moteur français `Qwant` qui axe son travail sur la
préservation de la confidentialité. Notez également d'autres moteurs
qui sont leaders dans leurs sphères d'influence comme `Yandex` en
Russie et `Baidu` en Chine. La fonction première d'un moteur de
recherche est de vous permettre de *poser une requête* constituée d'un
ou plusieurs mots clés. En réponse, le moteur vous renvoie *une liste
de documents Web ordonnée* par scores décroissants et organisée par
page de 10 documents. Cet outil est devenu essentiel dans vos
activités personnelles comme professionnelles. Mais l'ordre choisi
pour les réponses peut orienter vos réflexions et vos choix. Cet ordre
influe également sur l'activité économique en orientant vos choix
d'achats. Il nous semble donc important de comprendre les bases du
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
relativement à une requête. Nous terminons par une discussion sur les
problèmes éthiques et sociétaux posés par les moteurs de recherche
et sur une présentation des évolutions en cours.

# Les modèles de recherche d'information

chapeau sur les 3 modèles

## La recherche séquentielle "Grep Through text"

principes de la recherche séquentielle. Analyse critique.

## Le modèle Booléen : les documents satisfaisant un critère

principes de la recherche séquentielle. Matrices. Introduction des
index. Principes des algorithmes. Extension aux phrases. Analyse critique.

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

