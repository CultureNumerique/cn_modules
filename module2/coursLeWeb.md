LANGUAGE: fr
CSS: http://culturenumerique.univ-lille3.fr/css/base.css" />
TITLE: Le Web
AUTHOR: Culture Numérique

# Introduction

## Cours 1/2
[video]( https://player.vimeo.com/video/138623497 ){: .lien_video } 
Le web, c'est sans doute l'application informatique qui a rencontré le plus grand succès.

C'est une utilisation particulière  d'internet. Il a été inventé par Tim Berners Lee au début des années 90. C'est d'abord un moyen de communication entre personnes qui permet de s'échanger des informations décrites dans des documents . Il est fréquent de constater une confusion entre Internet et le Web. Or, si le web utilise Internet, il n'est pas la seule application à le faire, le mail par exemple est un autre service qui utilise Internet. Socialement, le web a pris une place considérable dans nos vies. Sur cette application au départ très simple se sont bâties d'autres applications dans tous les domaines d'activités : pour le commerce, le marketing, la recherche d'emploi, le travail à distance et la collaboration... C'est un vecteur important de développement économique aujourd'hui. C'est aussi par des applications web que l'état et les administrations offrent leurs services aux citoyens. C'est encore par les applications sociales du web que nous communiquons dans notre vie privée. Maîtriser les technologies du web est important pour comprendre les enjeux, saisir des opportunités, éviter des pièges... Naviguer sur le web fait aujourd'hui partie du quotidien de chacun d'entre nous. Ce chapitre propose d'en expliquer le fonctionnement pour nous permettre d'avoir des comportements responsables et de garder la maîtrise de ce que nous faisons.
 
# Clients et serveurs

## Le modèle client/serveur
[video](https://player.vimeo.com/video/138623558){: .lien_video}
Le Web, et bien d'autres applications d'internet, fonctionnent selon un modèle très simple : le modèle client/serveur.

Celui-ci peut s'illustrer par un petit exemple du quotidien. Dans la vie de tous les jours, si je me promène en ville et que j'ai envie d'un café ou d'une boisson rafraîchissante, j'entre dans une brasserie et j'interpelle un serveur. S'engagent alors des échanges, qui suivent un protocole assez convenu dans une langue commune.

Dès que je lui ai passé ma commande, il s'empresse de me faire savoir qu'il a compris et vient me servir à condition évidemment qu'il ait à sa disposition ce que je lui ai demandé. Si je demande un pneu de vélo ou les œuvres complètes de Karl Marx, ou simplement une marque de bière qu'il ne possède pas, il me répondra gentiment qu'il ne peut pas répondre à ma demande.Dans tous les autres cas, il va s'empresser de me servir et dès qu'il aura fini, il sera à nouveau disponible pour d'autres clients ou une nouvelle demande de ma part. En l'absence de clients, le serveur attend patiemment que quelqu'un l'interpelle.

Sur Internet, les clients et les serveurs sont toujours des programmes qui s'exécutent sur des ordinateurs. Nous avons décidé de représenter les serveurs par des tours et les clients par des ordinateurs portables afin d'être plus clairs, mais il va de soi que n'importe quel type d'ordinateur peut potentiellement jouer le rôle de client ou de serveur.

Dans le cadre du web, les clients sont les navigateurs qui nous permettent d'accéder à des sites constitués de ressources hébergées par des serveurs . Ils respectent pour leurs échanges un langage et des règles communes qu'on appelle le protocole `http` pour hypertext transfer protocol. Chaque ressource fait l'objet d'un échange demande/retour entre le client et le serveur. Certaines demandes n'aboutissent pas, quand  la ressource demandée n'existe pas par exemple. Ce sont les fameuses erreurs 404.

# Exemple et récapitulatif

## Cours
[video]( https://player.vimeo.com/video/138623678 ){: .lien_video } 

### Exemple

Commençons par un exemple très simple pour comprendre le mécanisme de base. Si à l'aide d'un client web tel que Firefox, je saisis l'adresse :

```
 http://culturenumerique.univ-lille3.fr/PageExemple
```

Que se passe -t-il ?

Mon client interprète ma saisie comme l'interrogation par le protocole `http` du serveur situé sur la machine `culturenumerique.univ-lille3.fr` pour lui demander la ressource `/PageExemple`

Comme nous l'avons vu précédemment, l'adresse `IP` de ma machine sera nécessaire pour communiquer avec le serveur. Mais mon navigateur va également réunir un certain nombre d'autres informations disponibles sur ma machine (informations que nous verrons plus loin) et les joindre à la requête envoyée au serveur qui héberge la ressource.
Le serveur reçoit cette requête, la comprend car elle est formulée selon les règles définies dans ce fameux protocole `http`, norme utilisée pour que les clients web et les serveurs web puissent communiquer.


Une part du succès du web repose sur le fait que `http` est utilisé par TOUS les serveurs web et TOUS les clients WEB, quels qu'ils soient et leur permet donc de dialoguer et de s 'échanger des informations.

Le serveur fait alors une copie de la ressource demandée et la renvoie au client, celui-ci n'a plus qu'à afficher le contenu de la ressource dans la fenêtre du navigateur.

Notons qu'une adresse du type : `http://culturenumerique.univ-lille3.fr/PageExemple`
s'appelle une URL pour Uniform Resource Locator, c'est-à-dire en français l'adresse d'une ressource. Le mot uniform suggère une convention d'écriture de ces adresses et une uniformisation de l'écriture de ces adresses. Il est important de noter que cette URL contient à la fois le nom du serveur (la machine `culturenumerique.univ-lille3.fr` dans notre exemple) qui héberge la ressource ET le nom de la ressource sur ce serveur (ici `/PageExemple`).

### Récapitulatif

Retenons dans un premier temps les notions suivantes :

- le web permet à des clients d'accéder à des copies de ressources hébergées sur des serveurs.
- les ressources sont toutes repérées par des URLs.
- les ressources de type texte sont décrites dans un langage normalisé, le `html` qui permet de créer des hyperliens pour faciliter notre navigation.
- les programmes appelés serveurs (on ne les « voit » pas) et clients (les navigateurs) parlent tous la même langue : le protocole `http`.
- comme pour beaucoup de communications sur internet, ces échanges entre client et serveurs ne sont pas confidentiels, et le protocole ne peut même pas garantir que les clients et les serveurs sont bien ceux qu'ils annoncent être.

Une évolution du protocole `http` remédie à ces problèmes en ajoutant le cryptage des communications pour assurer la confidentialité, et l'authentification des protagonistes dans ces échanges.C'est le protocole `https`.

En conclusion, dès que vous transmettez des données confidentielles veillez bien à la présence du petit verrou qui indique l'utilisation du protocole `https`.

# HTML

## HTML: contenu, structure, liens
[video]( https://player.vimeo.com/video/138623721 ){: .lien_video } 
Allons maintenant voir plus en détail le fonctionnement ; le langage `html` a plusieurs caractéristiques très intéressantes. Nous avons vu qu'il permettait d'introduire des hyperliens dans un document, mais il possède d'autres atouts.

C'est un langage de description de document , c'est à dire qu'il permet d'expliquer comment le document est construit et donc comment un logiciel comme un navigateur peut l'afficher. Concrètement, `html` permet d'ajouter au contenu texte des éléments de structure du type : ce paragraphe est un titre, celui-là est un sous-titre, cet autre est une légende, ce mot doit être mis en exergue...

Cette distinction contenu/structure est essentielle, elle est présente dans de nombreux domaines et nous y reviendrons souvent. La structure permet d'ajouter du sens aux parties de textes et à l'aide de règles de présentation de rendre une page `html` affichable sur de nombreux types d'écrans. Le navigateur calcule alors la présentation adaptée, par exemple pour une tablette, un smartphone ou un grand écran d'ordinateur.

En français la traduction de `html` est : langage de balisage pour documents hypertexte. Les balises vont indiquer la structure du document en titres, paragraphes etc ainsi que des liens vers d'autres ressources du Web. Les documents sont donc des textes décrivant des documents hypertexte. Mais que fait ensuite le client, le navigateur avec ce document hypertexte qu'il vient de recevoir ?

Grâce à la description faite du document et en fonction de ses capacités le navigateur va pouvoir recomposer le document et vous l'afficher. Les pages web que votre navigateur affiche sont des textes avec le plus souvent des images, formant un document complet. En fait ce document est réalisé par l'assemblage de nombreuses ressources. En effet, le langage `html` permet également de spécifier l'insertion d'images (ou d'autres ressources) à différents endroits d'un document. Les images ne sont pas à proprement parler insérées dans le document principal, mais un balisage indique qu'à cet endroit il faudra insérer une image.

# Les Cookies
## Cours
[video]( https://player.vimeo.com/video/138623890 ){: .lien_video } 
### Les cookies, une technique très utile...

Rappelons la conclusion importante du chapitre précédent.

Une page web telle que nous la voyons dans notre navigateur, notre client, est en fait la composition de plusieurs ressources.
Chacune d'elles fait l'objet d'une requête de la part de notre client vers un serveur. Plusieurs serveurs peuvent être sollicités pour obtenir l'ensemble des ressources présentes dans une page web unique. Mais le web est finalement un peu plus que la consultation de quelques ressources et pages web.

Aujourd'hui c'est un moyen pour réaliser de nombreuses démarches administratives, ou pour faire des achats, ou pour échanger sur des réseaux sociaux.
Ce sont des services aux usagers du web qui nécessitent pour les mettre en place, un grand nombre d'échanges de pages web, dans un ordre bien précis, avec des contenusspécifiques à chaque fois.

Prenons l'exemple de l'inscription à l'université. Dans un schéma très simplifié, vous devez tour à tour recevoir :

- étape 1 : la page qui permet de lire la marche à suivre
- étape 2 : la page qui permet d'indiquer à quelle formation vous vous inscrivez
- étape 3 : la page qui permet de payer votre inscription
- étape 4 : la page qui comprend un accusé de réception du paiement.

Ces étapes peuvent être abandonnées, recommencées... et le serveur de l'université qui prend en charge les inscriptions répond en même temps à toutes les demandes, quelles que soient les étapes et les étudiants. Il est donc nécessaire pour chacun des clients utilisés par les (futurs) étudiants, de communiquer à quelle étape ils sont arrivés.

Les cookies sont exactement conçus pour cela. Un cookie contient une donnée qui sera enregistrée par le client sur la machine du client à la demande du serveur. Dans notre exemple, le cookie pourrait contenir un nombre entre 1 et 4 pour signifier la dernière étape effectuée. Le cookie sera renvoyé aux prochaines requêtes du client vers ce même serveur.

Une autre image est celle d'une carte de fidélité de magasin, que nous avons dans notre poche et que nous montrons à notre commerçant lors de nos visites.Le cookie est la carte de fidélité et la donnée associée au cookie est notre numéro de client.

### Les cookies tiers

Parfois certains services proposés par un site sont délocalisés. C'est-à-dire qu'une partie des ressources d'une page sont en fait hébergées sur un autre serveur, un serveur tiers.

Ce peut être le cas par exemple, d'un serveur qui "compte" les points d'un joueur et se souvient entre 2 parties de son score. Ce type de service peut être utilisé par de nombreux sites de jeux, qui utilisent tous le même serveur partenaire. Ce qui leur évite de développer eux-mêmes le service.Celui-ci peut aussi utiliser des cookies.

Ce qui signifie qu'un serveur tiers, qui n'est pas celui qui héberge le site principal dont l'adresse est indiquée dans la barre d'URL, stocke des cookies sur notre machine. Son adresse n'est pas visible et le dépôt du cookie se fait donc à l'insu de l'utilisateur.Dans ce cas, on parle de cookie tiers.

### Utilisation des cookies

On voit bien que les techniques qui se sont développées et qui continuent d'évoluer sur le Web sont puissantes et nous rendent beaucoup de services. En revanche, leur utilisation dans certains cas peut poser de graves questions de citoyenneté. Bien souvent, la donnée associée au cookie est un numéro d'identification permettant au serveur de retrouver dans ses bases des données propres à l'utilisateur. Dans notre exemple de démarche d'inscription, ce pourrait être, l'étape à laquelle il est arrivé, son nom, ses choix de formation... Il est très important de comprendre qu'un tel numéro d'identification est un moyen très commun utilisé sur le web aussi bien que dans la vie non numérique.

C'est la technique utilisée par la sécurité sociale (avec le numéro de sécurité sociale), pour vous suivre toute notre vie dans nos démarches de couverture sociale.

C'est aussi ce qui se cache derrière les cartes d'achat ou promotionnelles des magasins, proposées avant tout pour nous suivre et assurer du marketing direct.

Donc bien des numéros nous identifient.

Mais dès lors que ces numéros d'identification sont rapprochés ou unifiés, la technique devient si puissante qu'on l'estime menaçante pour nos libertés.

Si bien que par exemple, le parlement a dû légiférer il y plus de 30 ans pour empêcher ou limiter l'usage du numéro de sécurité sociale dans les autres administrations de l'état. Naturellement, avec l'avènement du numérique ce rapprochement de numéros d'identification devient très facile techniquement. Il convient de redoubler de vigilance...


# Profils et réseaux sociaux
Votre âge, votre adresse,   vos achats
récents, vos goûts musicaux, vos films préférés, vos amis, etc,
toutes ces données peuvent intéresser de nombreuses sociétés et
organisations soit pour vous surveiller soit pour vous vendre quelque
chose. Rassemblées, elles contribuent à définir votre /profil/. 

## Profils et cookies

Grâce aux cookies contenant des numéros d'identification, des sites ou
 des jeux, sur PC, en ligne ou sur smartphone peuvent contribuer à
 créer et compléter nos profils. Souvent c'est même à notre insu, en
 mémorisant nos parcours sur le site, les pages visitées, etc.. Cette
 collecte peut même être assurée par le biais de sites partenaires grâce à la
 technique des cookies tiers.


## Les réseaux sociaux - pistage systématique

 Les réseaux sociaux sont parmi les plus grands adeptes de la création
 de profils. Bien évidemment de nombreuses informations personnelles
 s'y trouvent, directement données par l'utilisateur, vous-même. Mais la collecte
 s'étend même au delà des pages du  réseau social lui-même.

 Les petits boutons /j'aime/, /G+/ et autre /tweeter/ qui proposent de
 nous faciliter le partage sont en fait des mouchards très
 puissants. Présents sur une multitude de sites, ce sont des ressources
 tierces, provenant des serveurs des réseaux sociaux eux-mêmes. En
 effet, les boutons cachent souvent des petits programmes appelés
 scripts qui informent systématiquement Facebook ou Google de votre
 passage sur les sites où le bouton est présent, même si vous ne
 cliquez pas dessus, ...

 Dès que vous affichez sur votre navigateur une page n'ayant pourtant
 rien à voir avec Facebook ou Google mais contenant l'un de ces boutons
 de réseau social, le script associé envoie toutes les informations
 disponibles au serveur (l'ip, le type de navigateur, ...  et surtout
 le site consulté). En plus, même si vous n'êtes pas à ce moment là
 connecté à Facebook, ou même si vous n'êtes pas membre de ce réseau,
 toutes ces informations sont associées à votre profil. Ainsi même si
 vous ne /likez/ pas de pages, Facebook et Google savent
 beaucoup de choses sur votre navigation et vos habitudes. Votre profil
 prend alors de la valeur sur le marché publicitaire.

## Nos profils mis aux enchères

 Enfin, pour conclure, nous allons expliquer comment nous sommes mis
 aux enchères en permanence. La plupart des sites commerciaux qui
 affichent de la publicité travaillent avec des régies
 publicitaires. Ces régies publicitaires travaillent elles-mêmes avec
 une multitude d'annonceurs.

 À chaque fois qu'un espace de publicité est disponible dans une page, la
 régie soumet à ses  différents clients (les annonceurs donc) le profil
 de l'internaute. En fonction des caractéristiques du profil, les
 annonceurs sont prêts à payer plus ou moins cher cet espace. La
 régie organise donc une vente aux enchères de notre profil. Le plus
 généreux remporte le droit d'afficher sa publicité sur notre écran. 

 Tout cela se déroule de manière automatique grâce à des algorithmes
 sophistiqués en quelques fractions de seconde. Ainsi la page qui
 héberge la publicité est payée par un annonceur qui a choisi le
 meilleur prix pour son annonce et la régie prend son pourcentage au
 passage. Le web est envahi par ce système complexe mais très
 efficace. C'est ce qui explique que n'avons pas tous les mêmes
 publicités qui s'affichent pour une même page.

## La minute citoyenne
 Le web est une formidable source d'informations, un lieu d'échanges,
 qui regroupe un ensemble d'outils très performants et utiles. C'est
 aussi un facteur de développement économique. Mais nous l'avons
 illustré, c'est également un moyen de surveillance pour les états, les
 entreprises. C'est un facteur de dissémination de notre vie privée et
 de collecte d'information à notre sujet, parfois,... souvent, à notre
 insu. 

 Vous avez maintenant les clés pour comprendre ces questions. Vous
 pouvez en toute connaissance de cause, et c'est bien le droit de
 chacun, laisser faire les mouchards, les régies publicitaires et tous
 les collecteurs d'informations privées.

 En revanche, si vous considérez que vos données vous appartiennent et
 que vous n'avez pas envie d'être pisté ni ciblé, alors vous pouvez
 utiliser les connaissances vues dans ce cours pour paramétrer votre
 navigateur et avoir des stratégies qui visent à vous protéger. Vous
 pouvez interdire systématiquement tous les cookies sur votre
 navigateur, mais dans ce cas, très peu de sites continueront à
 fonctionner correctement, car les cookies sont aussi utiles. Mais
 votre navigateur permet un paramétrage plus fin. Vous pouvez étudier
 ces paramètres et  par exemple :

 - interdire les cookies tiers (ils sont souvent autorisés par
   défaut),
 - limiter la conservation des cookies et même les effacer
   régulièrement

 Vous pouvez également installer des modules complémentaires bloquant
 les publicités, les boutons de réseaux sociaux, ou les mouchards en
 tout genre, ...

 Enfin, si vous pensez que vos droits de citoyens sont bafoués sur le
 web, c'est sûrement sur le plan juridique que la bataille doit avoir
 lieu. Vous êtes maintenant mieux armés pour rejoindre les différentes
 associations d'utilisateurs, ou pour interpeller les élus, participer
 aux débats publics sur les questions de respect de la vie privée. 

# Moteurs de recherche
## Des ressources qui n'existent que quand on les demande...
 Prenons l'exemple de l'URL suivante :

 ```
 http://www.univ-lille3.fr/etudes/orientation-emploi/.
```

 Rappelons que la partie `etudes/orientation-emploi` désigne une
 ressource sur le serveur web `www.univ-lille3.fr`.  Il est possible
 que ce soit un document composé par une personne du service des études
 puis enregistré sur les disques durs de ce serveur web pour le mettre
 à disposition des internautes. Mais à vrai dire, c'est un processus de
 conception à la mise en ligne de ressources aujourd'hui de plus en
 plus rare.  Dans le web moderne, de plus en plus souvent, ces
 ressources sont composées par des programmes informatiques, à partir
 d'éléments pris dans de nombreuses sources de données. Ces programmes
 sont par exemple des outils de publication web, systèmes de gestion de
 contenu (CMS en anglais), des wiki, des moteurs de blogs...

 Mais un autre exemple évident de la génération automatique de
 ressources est celui des moteurs de recherche. Lorsque vous appuyez
 sur le bouton de recherche après avoir saisi vos mots clefs, le
 document qui apparaît dans votre navigateur a évidemment été construit
 juste pour vous, au moment de votre demande.

## Un annuaire de toutes les ressources 
 Le web est un immense ensemble de ressources reliées entre
 elles. On pouvait imaginer à ses débuts parcourir cet ensemble et
 trouver son chemin vers la ressource souhaitée. On a donc commencé à
 construire des annuaires et des répertoires à l'image de ce qui peut
 se faire dans des bibliothèques. Tim Berners Lee, inventeur du web, a
 même maintenu une liste de serveurs web à cette époque. Mais cet idéal
 a rapidement été abandonné.  La taille du web a grandi tellement vite
 qu'il est devenu impossible de consigner les adresses de toutes les
 ressources, ou même seulement les plus importantes. C'est alors que
 sont entrés en jeu les moteurs de recherche. 

##  Comment fonctionne un moteur de recherche aujourd'hui
 Comment fonctionne un moteur de recherche ? C'est à la fois simple
 dans certains principes généraux et complexe pour de nombreux détails
 importants. C'est à la fois connu dans sa généralité et bien caché
 dans ses détails. Nous nous contentons ici de simples généralités. 

 Les moteurs de recherche construisent constamment, car le web évolue
 sans cesse, un index. L'index, c'est comme dans un livre, un moyen
 d'aller directement à une page à partir d'un mot. Pour construire un
 tel index, il faut avoir lu toutes les pages du livre et consigné pour
 tous les mots, la liste des pages où ils se trouvent. Les moteurs de
 recherche téléchargent toutes les ressources du web en permanence pour
 extraire la liste des mots qu'on y trouve et garder l'énorme liste des
 URLs où ces mots se trouvent. Ce ne sont pas des hommes qui parcourent
 le web pour eux, mais des programmes, appelés des robots. Les robots
 sont les clients des serveurs web les plus nombreux et réguliers... et
 de loin!

 Mais afficher simplement la liste de ces ressources quand l'internaute
 saisit quelques mots dans le formulaire de recherche n'est pas
 satisfaisant. La liste est bien trop longue. Le deuxième ingrédient du
 moteur de recherche est le programme qui permet d'interroger cet
 index, simplement en lui donnant quelques mots, et qui construit une
 liste, présentée par ordre d'importance, d'URLs désignant les
 ressources où ces mots se trouvent.


 La magie des moteurs de recherche tient dans les détails qui
 permettent à l'ensemble de fonctionner tels que l'existence d'un index
 à jour, la forme de l'index qui permet d'y retrouver extrêmement
 rapidement les pages associées à un mot, ou encore l'ordre
 d'importance dans lequel les résultats de l'interrogation de l'index
 apparaissent.

 L'avance technologique des grands moteurs de recherche se cache dans
 les détails de la construction de l'index mais surtout du programme
 qui permet de l'interroger et de la détermination de l'ordre des URLs
 affichées en retour. Ces détails sont protégés par de nombreux secrets
 industriels. 

## Collecte de données d'usage

 Mais un avantage qui rend la mise en concurrence des grands moteurs de
 recherche actuels presque impossible tient à un dernier
 paramètre. C'est la disponibilité d'énormes quantités de données
 d'usage, parfois personnalisées. En effet le résultat (l'ordre
 d'apparition des ressources) des requêtes au moteur dépend aujourd'hui
 fortement de ce qu'ont fait leurs utilisateurs : sur quels liens
 ont-ils cliqué ? À l'inverse des ressources du Web derrière les URLs,
 ces données d'usage ne sont pas publiques, mais sont tout aussi
 cruciales pour générer des réponses aux requêtes dans un ordre pertinent.

 En conséquence, les moteurs de recherche collectent sans cesse des
 données à propos de vos recherche. La tendance actuelle est de rendre
 les réponses personnalisées, ce qui entraîne une collecte de données
 personnelles rendue possible à la fois par les techniques de cookies
 et l'utilisation de comptes chez ces opérateurs de recherche. 

## Modèle économique du moteur de recherche

 Pour une institution qui veut être visible sur internet, if faut
 assurer sa présence dans l'index. Mais cela n'est pas suffisant : il
 faut être en haut de la liste et donc apparaître important aux yeux du
 moteur de recherche. 

 De bonnes pratiques en matière de conception de pages web peut y
 contribuer. Puisque toute la chaîne de traitement est automatique, les
 ressources que le moteur analyse et indexe doivent être parfaitement
 intelligibles par la machine. Il est donc très important d'écrire
 correctement ses pages web dans ce but de traitement automatisé autant
 que dans le but de se faire comprendre de ses lecteurs
 humains. Parfois des conseillers un peu charlatans tentent de se faire
 passer pour des gourous qui vont propulser des sites en première page
 des résultats de recherche. 

 Il faut s'en méfier car pour le moteur de recherche, une des premières
 sources de revenu est de vendre ces places. Cela se traduit
 littéralement par des /ventes de mots/. Une deuxième source de revenu
 est liée à la collecte des données personnelles des
 utilisateurs. Tirer des informations à l'insu ou non de ses usagers
 n'est pas une pratique réservée aux moteurs de recherche. De nombreux
 autres acteurs du web fonctionnent sur ce même principe.


## Aller plus loin

 Cette petite introduction des moteurs de recherche est volontairement
 très succinte et parcellaire. Des éléments techniques essentiels ne
 sont pas mentionnés comme 
 - les pré-traitements des textes et la sélection du vocabulaire, le
   traitement des majuscules, des accents etc... 
 - le calcul du score de pertinence sur lequel repose cet ordre
   d'affichage des réponses, et bien-sûr
 - l'un des algorithmes les plus connus qu'est PageRank utilisé par
   Google. 

 Nous vous invitons à suivre les cours d'option transversale en
 licence, les options de master sur les humanités numériques, ou les
 prochains cours de culture numérique qui aborderont sans doute ces
 questions beaucoup plus précisément. 

# Autres informations sensibles et bilan
## Autres informations
[video]( https://player.vimeo.com/video/138623956 ){: .lien_video } 
On voit bien que les techniques qui se sont développées et qui continuent d'évoluer sur le Web sont puissantes et nous rendent beaucoup de services. En revanche, leur utilisation dans certains cas peut poser de graves questions de citoyenneté. Bien souvent, la donnée associée au cookie est un numéro d'identification permettant au serveur de retrouver dans ses bases des données propres à l'utilisateur.
Dans notre exemple de démarche d'inscription, ce pourrait être, l'étape à laquelle il est arrivé, son nom, ses choix de formation...  

Il est très important de comprendre qu'un tel numéro d'identification est un moyen très commun utilisé sur le web aussi bien que dans la vie non numérique. C'est la technique utilisée par la sécurité sociale (avec le numéro de sécurité sociale), pour vous suivre toute notre vie dans nos démarches de couverture sociale. C'est aussi ce qui se cache derrière les cartes d'achat ou promotionnelles des magasins, proposées avant tout pour nous suivre et assurer du marketing direct.
Donc bien des numéros nous identifient.

Mais dès lors que ces numéros d'identification sont rapprochés ou unifiés, la technique devient si puissante qu'on l'estime menaçante pour nos libertés.
Si bien que par exemple, le parlement a dû légiférer il y plus de 30 ans pour empêcher ou limiter l'usage du numéro de sécurité sociale dans les autres administrations de l'état.
Naturellement, avec l'avènement du numérique ce rapprochement de numéros d'identification devient très facile techniquement. Il convient de redoubler de vigilance...
