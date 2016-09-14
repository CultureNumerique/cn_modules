LANGUAGE: fr
CSS: http://culturenumerique.univ-lille3.fr/css/base.css" />
TITLE: Le Web
MENUTITLE: Le Web
AUTHOR: Culture Numérique

# Introduction

## Cours 1/2
[video]( https://vimeo.com/138623497 ){: .cours_video }
Le web, c'est sans doute l'application informatique qui a rencontré le plus grand succès.

C'est une utilisation particulière  d'internet. Il a été inventé par Tim Berners Lee au début des années 90. C'est d'abord un moyen de communication entre personnes qui permet de s'échanger des informations décrites dans des documents . Il est fréquent de constater une confusion entre Internet et le Web. Or, si le web utilise Internet, il n'est pas la seule application à le faire, le mail par exemple est un autre service qui utilise Internet. Socialement, le web a pris une place considérable dans nos vies. Sur cette application au départ très simple se sont bâties d'autres applications dans tous les domaines d'activités : pour le commerce, le marketing, la recherche d'emploi, le travail à distance et la collaboration... C'est un vecteur important de développement économique aujourd'hui. C'est aussi par des applications web que l'état et les administrations offrent leurs services aux citoyens. C'est encore par les applications sociales du web que nous communiquons dans notre vie privée. Maîtriser les technologies du web est important pour comprendre les enjeux, saisir des opportunités, éviter des pièges... Naviguer sur le web fait aujourd'hui partie du quotidien de chacun d'entre nous. Ce chapitre propose d'en expliquer le fonctionnement pour nous permettre d'avoir des comportements responsables et de garder la maîtrise de ce que nous faisons.

## Cours 2/2
[video]( https://vimeo.com/138623515 ){: .cours_video }

Alors, qu'est-ce réellement  que le web ? Le Web est avant tout un service qui permet de s'échanger des ressources. Celles-ci peuvent être très variées et prendre de nombreuses formes. Dans un premier temps, nous considérerons pour simplifier que ce sont uniquement des documents qui contiennent soit du texte soit des images.
Le succès du web est sans doute lié à la notion de document hypertexte. C'est à dire la possibilité d'intégrer à l'intérieur d'un document des liens, qui sont des parties de texte cliquables permettant d'accéder à d'autres ressources.
Cela a été rendu possible grâce à l'utilisation du fameux langage HTML - Hyper Text Markup Language - inventé par Tim Berners Lee en 1991.
L'ensemble des documents ainsi que les liens qui les relient forment alors un réseau de documents. Cette multitude de liens a fait naître l'image bien connue de la toile d'araignée. En anglais : le web

```compréhension// question: 159977  name: La toile et ses fils
::La toile et ses fils::[html]<p>Dans l'image du web représentée par une toile d'araignée, les fils sont \:</p>{
	=<p>des liens</p>
	~<p><strong id\="docs-internal-guid-566566e9-d108-1f1b-8d6f-529e33dacd53" style\="font-weight\: normal;"><span style\="font-size\: 14.666666666666666px; font-family\: Arial; color\: \#434343; background-color\: transparent; font-weight\: 400; font-style\: normal; font-variant\: normal; text-decoration\: none; vertical-align\: baseline; white-space\: pre-wrap;">des câbles du réseau internet</span></strong></p>
}


::La toile et ses noeuds::[html]<p>Dans l'image du web représentée par une toile d'araignée, les nœuds sont \:</p>{
// question: 159978  name: La toile et ses noeuds
	=<p>des ressources</p>
	~<p><span style\="font-weight\: normal;"><span style\="font-size\: 14.666666666666666px; font-family\: Arial; color\: \#434343; background-color\: transparent; font-weight\: 400; font-style\: normal; font-variant\: normal; text-decoration\: none; vertical-align\: baseline; white-space\: pre-wrap;">des ordinateurs</span></span></p>
}

// question: 159983  name: Les échanges sur le web
::Les échanges sur le web::[html]<p>Que s'échangent les ordinateurs sur le Web ?</p>{
	~%33.33333%<p>Des ressources</p>
	~%33.33333%<p>Des images</p>
	~%33.33333%<p>Des textes</p>
	####<p>Les trois !</p><p>Dans ce contexte du web, le mot ressource désigne à la fois des textes, des images, des sons, ... C'est ce mot qu'on retrouve dans la signification de l'acronyme URL \: Uniform Resource Locator</p>
}
```

```activité-avancée
::Tim Berners-Lee::[html]<div>
	<p>En vous aidant par exemple de cette ressource : </p>
	<p>
	<a target="_blank" href="http://home.web.cern.ch/fr/topics/birth-web">http://home.web.cern.ch/fr/topics/birth-web</a>
	</p>
	<p>Faites quelques recherches sur <b>Tim Berners-Lee</b> et l'origine du web et répondez aux questions suivantes :
</p>
      <ol>
        <li>Quelle était la spécialité professionnelle de Tim Berners-Lee ?</li>
        <li>Que contenait le premier site web ?</li>
        <li>En quelle année a-t-il été créé ?</li>
      </ol>
    </div>
{####<p>Contrairement à ce qu'on pourrait imaginer, Tim Berners-Lee n'était pas informaticien mais <b>physicien</b>. Il était chercheur en physique nucléaire au CERN dans les années 80. Son objectif était de faciliter le transfert de connaissance dans la communauté scientifique internationale.</p><p>Le premier site réellement opérationnel décrivait les principales caractéristiques du web et expliquait comment accéder aux documents d'autres personnes et comment configurer son propre serveur.</p><p>Les travaux ont démarré en 1989, le premier site a été mis en ligne en <b>1991</b> mais c'est en 1993 que le premier navigateur au sens ou nous les manipulons aujourd'hui est apparu.</p>}


::Qui dirige le Web ?::[html]
<p>Le 30 avril 1993, le CERN annonce que le « World Wide Web » sera <b>libre d'utilisation</b> pour tout le monde.</p>
<div class="editor-indent" style="margin-left: 30px;"><i>Ressources :<br /></i></div>
<ul>
<li><a target="_blank" href="http://fr.wikipedia.org/wiki/Site_web">http://fr.wikipedia.org/wiki/Site_web</a>,</li>
<li><a target="_blank" href="http://home.web.cern.ch/fr/topics/birth-web/licensing-web">http://home.web.cern.ch/fr/topics/birth-web/licensing-web</a></li>
</ul>
<p>Le web n'appartient à personne, en revanche chaque site est sous la responsabilité d'un auteur (le rédacteur des pages) et d'un hébergeur (le propriétaire du serveur). Les seules lois qui le régissent sont les lois sur la diffusion de contenu dans des média, comme par exemple dans la presse ou l'audiovisuel. <br />Si des contenus inappropriés, insultants, diffamants, ... font l'objet d'une plainte, l'auteur est responsable et l'hébergeur est tenu de les effacer. Aucun contenu ne se retrouve donc <i>a priori</i> sans responsable, il se trouve toujours hébergé sur un serveur avec un numéro IP officiel et donc une identité physique répertoriée. <br />Évidemment, dans la pratique, certains serveurs peuvent être physiquement dans des pays où les autorités sont très laxistes, et les contenus s'en trouvent quasi intouchables. Le web n'a pas de frontière, la localisation géographique d'un serveur n'a aucune conséquence sur son accessibilité, les internautes que nous sommes n'avons en général pas conscience du lieu où est hébergé le site que nous consultons, pourtant les lois en vigueur ne sont pas les mêmes dans tous les pays. <br />Par exemple <b>Wikileaks</b> est interdit d'hébergement sur des serveurs américains, mais a trouvé des pays qui acceptent de l'héberger.</p>
<div class="editor-indent" style="margin-left: 30px;"><i><b>Questions</b></i></div>
<ol>
<li>Qu'est-ce que Wikileaks ?</li>
<li>Qui en est le fondateur ?</li>
<li>Exprimez-vous en quelques lignes sur votre position citoyenne (intérêt, légalité, ...) de ce genre de sites.</li>
</ol>
{####<p id="docs-internal-guid-3fe28ae3-d61d-dc88-8eea-c34984c1d971"><b>WikiLeaks</b> (wikileaks.org) est une<a href="https://fr.wikipedia.org/wiki/Association_%C3%A0_but_non_lucratif"> </a><span>association à but non lucratif</span> dont le<span> site web</span><span> lanceur d'alertes</span> publie des documents ainsi que des analyses politiques et sociales. Sa raison d'être est de donner une audience aux<span> fuites d'information</span>, tout en protégeant ses sources.</p>
<p dir="ltr">( ref : <a target="_blank" href="https://fr.wikipedia.org/wiki/WikiLeaks">https://fr.wikipedia.org/wiki/WikiLeaks</a>)</p>
<p dir="ltr"></p>
<p dir="ltr">Le fondateur est <b>Julian Assange.</b></p>
  </body>}

```

# Clients et serveurs

## Le modèle client/serveur

[video](https://vimeo.com/138623558){: .cours_video}
Le Web, et bien d'autres applications d'internet, fonctionnent selon un modèle très simple : le modèle client/serveur.

Celui-ci peut s'illustrer par un petit exemple du quotidien. Dans la vie de tous les jours, si je me promène en ville et que j'ai envie d'un café ou d'une boisson rafraîchissante, j'entre dans une brasserie et j'interpelle un serveur. S'engagent alors des échanges, qui suivent un protocole assez convenu dans une langue commune.

Dès que je lui ai passé ma commande, il s'empresse de me faire savoir qu'il a compris et vient me servir à condition évidemment qu'il ait à sa disposition ce que je lui ai demandé. Si je demande un pneu de vélo ou les œuvres complètes de Karl Marx, ou simplement une marque de bière qu'il ne possède pas, il me répondra gentiment qu'il ne peut pas répondre à ma demande.Dans tous les autres cas, il va s'empresser de me servir et dès qu'il aura fini, il sera à nouveau disponible pour d'autres clients ou une nouvelle demande de ma part. En l'absence de clients, le serveur attend patiemment que quelqu'un l'interpelle.

Sur Internet, les clients et les serveurs sont toujours des programmes qui s'exécutent sur des ordinateurs. Nous avons décidé de représenter les serveurs par des tours et les clients par des ordinateurs portables afin d'être plus clairs, mais il va de soi que n'importe quel type d'ordinateur peut potentiellement jouer le rôle de client ou de serveur.

Dans le cadre du web, les clients sont les navigateurs qui nous permettent d'accéder à des sites constitués de ressources hébergées par des serveurs . Ils respectent pour leurs échanges un langage et des règles communes qu'on appelle le protocole `http` pour hypertext transfer protocol. Chaque ressource fait l'objet d'un échange demande/retour entre le client et le serveur. Certaines demandes n'aboutissent pas, quand  la ressource demandée n'existe pas par exemple. Ce sont les fameuses erreurs 404.

## Les clients
[video](https://vimeo.com/138623609){: .cours_video}

**Les clients**
**Le client quant à lui, émet les requêtes vers le serveur et réceptionne les ressources qui sont envoyées en réponse. Les clients que nous utilisons sont les navigateurs web.Ce sont donc des logiciels qui s'exécutent sur nos propres machines sous notre contrôle.**

Il en existe des centaines mais les plus connus du grand public sont Firefox, Chrome, Safari, Opera ou Internet Explorer.

**D'autres clients moins connus sont pourtant les plus actifs sur le web. Il s'agit des programmes robots des moteurs de recherche, sorte de mini navigateurs automatiques.**

Une remarque importante doit être signalée. Le terme naviguer peut prêter à confusion. **Si vous nous avez bien entendu, les clients ne se déplacent pas chez le serveur. Ce sont plutôt les ressources qui sont copiées du serveur vers le client** à travers le réseau.
**Cela signifie donc que lorsque vous visitez un site web, le serveur envoie une copie des pages que vous demandez et votre navigateur vous les présente.**

## Les serveurs

**Les serveurs**
[video](https://vimeo.com/138623583){: .cours_video}

Un serveur est un logiciel (un programme) qui s'exécute sur une machine le plus souvent 24/24 et 7/7 et attend qu'un client l'interpelle, par exemple c'est le cas du serveur web www.univ-lille.fr qui distribue les ressources du site de l'université de Lille. Dans ces journaux, de nombreuses informations à propos des clients sont mémorisées : leur adresse IP, des dates de visites, la ressource demandée... Notons que, l'envoi d'une ressource, est en fait l' envoi d'une copie de la ressource, l'original restant disponible pour d'autres requêtes identiques. En plus de ce service de distribution, le serveur garde l' historique de toutes les requêtes qui lui ont été adressées dans des journaux d'activité : les logs en anglais. Ces journaux sont autant de traces que nous laissons et qui peuvent être analysées et exploitées.
Son rôle est de distribuer les ressources dont il dispose, c'est-à-dire qui sont stockées sur ses disques, aux clients qui les demandent .

```compréhension

// question: 268  name: Erreur 404!
::Erreur 404!::[html]<p>Que signifie le code d'erreur 404 dans le protocole HTTP</p>{
	~<p>La ressource a été déplacée sur un autre serveur</p>
	=<p>La ressource n’existe pas sur le serveur</p>#<p>Votre réponse est correcte.</p>
	~<p>Le client de peut pas communiquer avec le serveur</p>
	####<p>L'erreur 404 apparaît lorsque la ressource demandée n'existe pas sur le serveur. Cela se produit en général lorsqu'il y a une 'faute' dans l'url ou lorsque le gestionnaire du site a déplacé, supprimé ou renommé une ressource. L'url devient alors invalide.</p>
}


// question: 270  name: le meilleur Navigateur
::le meilleur Navigateur::[html]<p>Avec quel navigateur peut-on accéder au plus grand nombre de sites ?</p>{
	~<p>Firefox</p>
	~<p>Internet Explorer</p>
	~<p>Chrome</p>
	~<p>Safari</p>
	=<p>Tous</p>#<p>Votre réponse est correcte.</p>
	####<p>Tous les navigateurs sont équivalents de ce point de vue, seuls leur rapidité, leurs fonctionnalités avancées ou leur ergonomie les différencient.</p>
}


// question: 273  name: Les clients
::Les clients::[html]<p>Qu'est-ce qu'un client web ?</p>{
	~%33.33333%<p>Tout logiciel qui demande des ressources à un serveur web</p>
	~%33.33333%<p>un navigateur</p>
	~%33.33333%<p>un robot de moteur de recherche</p>
	~<p>une page HTML</p>
}


// question: 271  name: Les logs c'est quoi ?
::Les logs c'est quoi ?::[html]<p>Qu'est-ce qu'un fichier de logs d'un serveur web ?</p>{
	~la liste des noms des gens qui ont consulté le site hébergé sur le serveur#non, sur la plupart des sites nous n'envoyons pas nos noms, les logs conservent les traces des requêtes effectuées par les clients repérés par leur adresse IP ainsi que toutes les activités du serveur dans un journal
	=un journal des activités du serveur#Oui, bravo
	~la liste de toutes les ressources stockées sur ce serveur#Non, les logs conservent le journal des activités du serveur
	####<p>Voici ci dessous quelques lignes extraites d'un journal (log) d'un serveur Web. Chaque ligne correspond à une requête d'un client. Les lignes ont été "anonymisées" \: nous avons remplacé les adresses IP des clients par 127.0.0.1.  </p><p> </p><p>Sur cette ligne vous avez l'adresse IP (anonymisée) du client, suivi de la date et l'heure de la requête et entre guillemets la requête adressée ("GET /polys/...") qui signifie " donne-moi la ressource "/poly/...etc". On voit également le code 200 signalant que la requête a bien été traitée sans erreur et aussi les caractéristiques du client \:  C'est ici le robot du moteur de recherche bing.</p><p><br /><code>127.0.0.1 - - [22/Sep/2015\:08\:22\:48 +0200] "GET /polys/access-1997/node66.html HTTP/1.1" 200 2257 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http\://www.bing.com/bingbot.htm)"</code></p><p> </p><p>L'exemple suivant est intéressant car il montre une suite de 5 requêtes. La première est un celle d'un document contenant des liens vers d'autres ressources (feuilles de style CSS et images au format PNG). Les 5 requêtes sont enchaînées car le navigateur (ici Safari) a immédiatement demandé au serveur les ressources nécessaires pour afficher une page web complète.</p><p>    <br /><code>127.0.0.1 - - [22/Sep/2015\:08\:19\:57 +0200] "GET /\~torre/Football/Confrontations/Ajaccio-Clermont.php HTTP/1.1" 200 4836 "https\://www.google.fr/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240" </code><br /><code>127.0.0.1 - - [22/Sep/2015\:08\:19\:57 +0200] "GET /\~torre/include/css/ft-v3.css HTTP/1.1" 200 6692 "http\://www.grappa.univ-lille3.fr/\~torre/Football/Confrontations/Ajaccio-Clermont.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"</code><br /><code>127.0.0.1 - - [22/Sep/2015\:08\:19\:57 +0200] "GET /\~torre/include/css/ft-print-v3.css HTTP/1.1" 200 2231 "http\://www.grappa.univ-lille3.fr/\~torre/Football/Confrontations/Ajaccio-Clermont.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"</code><br /><code>127.0.0.1 - - [22/Sep/2015\:08\:19\:57 +0200] "GET /\~torre/Images/valid-html5.png HTTP/1.1" 200 1723 "http\://www.grappa.univ-lille3.fr/\~torre/Football/Confrontations/Ajaccio-Clermont.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"</code><br /><code>127.0.0.1 - - [22/Sep/2015\:08\:19\:57 +0200] "GET /\~torre/Images/FabienTorre.png HTTP/1.1" 200 478 "http\://www.grappa.univ-lille3.fr/\~torre/Football/Confrontations/Ajaccio-Clermont.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"</code></p><p>Un dernier petit exemple pour les hackers \:-). On peut lire avec un peu d'expérience ou de sagacité que la ressource (ici /FAQ-LaTeX/12.3.html) a été demandée depuis une page web (indiquée après le code de succès 200 et la taille de 7444 de cette ressource) qui est une adresse sur les serveurs de Google. En regardant mieux encore, on peut même lire que c'est à la suite d'une recherche à propos de "FAQ-LaTeX"... C'est en partie grâce à cette indication de provenance qu'on peut rémunérer les sites qui font de la publicité vers d'autres sites...</p><p><br /><code>127.0.0.1 - - [22/Sep/2015\:08\:22\:30 +0200] "GET /FAQ-LaTeX/12.3.html HTTP/1.1" 200 7444 "http\://www.google.fr/url?sa\=t&rct\=j&q\=&esrc\=s&source\=web&cd\=1&ved\=0CCQQFjAAahUKEwjo6IWtgIrIAhVFOxQKHdjEDfw&url\=http%3A%2F%2Fwww.grappa.univ-lille3.fr%2FFAQ-LaTeX%2F12.3.html&usg\=AFQjCNEtHaKlFbotxdHj6bxRzpkDN3NwkA" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv\:24.0) Gecko/20100101 Firefox/24.0"</code><br /><br /></p>
}


// question: 269  name: Les protocoles
::Les protocoles::[html]<p>Par quel protocole les clients et serveurs dialoguent-ils ? <br></br></p>{
	~<p>HTML<br></p>
	=<p><span style\="font-weight\:normal;"><span style\="font-size\:14.666666666666666px;font-family\:Arial;color\:\#434343;background-color\:transparent;font-weight\:400;font-style\:normal;font-variant\:normal;text-decoration\:none;vertical-align\:baseline;white-space\:pre-wrap;">HTTP</span></span></p>#Votre réponse est correcte.
}


// question: 272  name: La distribution
::La distribution::[html]<p>Quand un serveur a envoyé une image à un client, il doit attendre que ce client l'ait rendue avant de la distribuer à un autre client.</p>{TRUE####<p>Cette notion de "rendre" une ressource n'a pas de sens, à chaque fois les ressources sont copiées et ce sont des copies qui sont envoyées, ...</p><p>Le serveur conserve toujours ses ressources et peut en faire autant de copies que nécessaire.</p> }


```

# Exemple et récapitulatif


## Cours
[video]( https://vimeo.com/138623678 ){: .cours_video }
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

```compréhension

// question: 274  name: Composition d'une URL
::Composition d'une URL::[html]<p>Quelles informations sont indiquées dans une URL ?</p>{
	~%33.33333%<p>le nom du serveur</p>
	~%33.33333%<p>le nom d'une ressource</p>
	~%33.33333%<p>le protocole utilisé</p>
	~<p>si la ressource est une image ou un texte</p>
	~<p>l’adresse du client</p>
	####<p>URL \: Unified Ressource Locator, soit en français \: l'adresse d'une ressource. Elle contient évidemment \:</p><ul><li>le non du serveur sur laquelle elle est stockée</li><li>le nom de la ressource \: le nom du fichier et le 'chemin' (dossier/sousdossier/) pour y accéder</li><li>le protocole utilisé, pour le Web \: http\:// ou https\://</li></ul><p>Elle ne précise pas le type de la ressource et elle est évidemment indépendante de l'adresse des éventuels clients qui feraient une requête...</p>
}


// question: 275  name: HTTP vs HTTPS
::HTTP vs HTTPS::[html]<p>Quelle est la différence entre HTTP et HTTPS ? Grâce à HTTPS \:</p>{
	~<p>mes communications avec le serveur sont cachées</p>
	~%50%<p>le contenu de mes communications avec le serveur est crypté</p>
	~%50%<p>je peux m’assurer que le serveur est celui auquel je veux m’adresser</p>
	####<p>Le protocole https a 2 fonctions majeures. Il permet \:</p><ul><li>de crypter les échanges (requêtes/réponses) par exemple des mots de passe ou des codes de Carte Banquaire, seul le destinataire pourra les décrypter</li><li>d'authentifier les serveurs, par exemple pour éviter qu'un site pirate cherche à se faire passer pour le site d'une banque</li></ul>
}


// question: 276  name: Les balises HTML
::Les balises HTML::[html]<p>Quel est le rôle des balises en HTML ?</p>{
	~%50%<p>de délimiter des parties de texte</p>
	~%50%<p>de décrire la structure des documents</p>
	~<p>de signaler aux internautes des pages dangereuses</p>
	~<p>d'accélérer internet</p>
}


// question: 277  name: Les informations échangées entre clients et serveurs
::Les informations échangées entre clients et serveurs::[html]<p>Quelles autres informations que l’URL peuvent être échangées dans un échange entre un client et un serveur Web ?</p>{
	~%33.33333%<p>l’adresse IP du client</p>
	~%33.33333%<p>le nom du navigateur web \: firefox, opera, internet explorer, ….</p>
	~%33.33333%<p>la page présentée dans le navigateur au moment où la requête est effectuée</p>
	####<p>l’IP est toujours nécessaire pour indiquer au destinataire à qui il doit répondre. Mais potentiellement les 3 informations peuvent être échangées, et bien d'autres encore !</p>
}


// question: 278  name: Une page web
::Une page web::[html]<p>Quand on regarde une page web, toutes les informations viennent du même serveur.</p>{
	~<p>oui</p><p> </p>
	=<p>non</p>#<p>Votre réponse est correcte.</p>
	####<p>Une page Web est souvent constituée de plusieurs ressources. Chaque ressource fait l'objet d'un échange entre le client et un serveur, pas forcément toujours le même !</p>
}


// question: 279  name: Une URL
::Une URL::[html]<p>Qu'est-ce qu'une URL ?</p>{
	~<p>une ressource</p>
	=<p>l'adresse d'une ressource</p>#<p>Votre réponse est correcte.</p>
	~<p>un fichier</p>
}


```

# HTML

## HTML: contenu, structure, liens
[video]( https://vimeo.com/138623721 ){: .cours_video }
Allons maintenant voir plus en détail le fonctionnement ; le langage `html` a plusieurs caractéristiques très intéressantes. Nous avons vu qu'il permettait d'introduire des hyperliens dans un document, mais il possède d'autres atouts.


C'est un langage de description de document , c'est à dire qu'il permet d'expliquer comment le document est construit et donc comment un logiciel comme un navigateur peut l'afficher. Concrètement, `html` permet d'ajouter au contenu texte des éléments de structure du type : ce paragraphe est un titre, celui-là est un sous-titre, cet  est une légende, ce mot doit être mis en exergue...
Cette distinction contenu/structure est essentielle, elle est présente dans de nombreux domaine et nous y reviendrons souvent. La structure permet d'ajouter du sens aux parties de textes et à l'aide de règles de résentation de rendre une page `html` affichable sur de nombreux types d'écrans. Le navigateur calcule alors la présentation adaptée, par exemple pour une tablette, un smartphone ou un grand écran d'ordinateur.

En français la traduction de `html` est : langage de balisage pour documents hypertexte. Les balises vont indiquer la structure du document en titres, paragraphes etc ainsi que des liens vers d'autres ressources du Web. Les documents sont donc des textes décrivant des documents hypertexte. Mais que fait ensuite le client, le navigateur avec ce document hypertexte qu'il vient de recevoir ?

Grâce à la description faite du document et en fonction de ses capacités le navigateur va pouvoir recomposer le document et vous l'afficher. Les pages web que votre navigateur affiche sont des textes avec le plus souvent des images, formant un document complet. En fait ce document est réalisé par l'assemblage de nombreuses ressources. En effet, le langage `html` permet également de spécifier l'insertion d'images (ou d'autres ressources) à différents endroits d'un document. Les images ne sont pas à proprement parler insérées dans le document principal, mais un balisage indique qu'à cet endroit il faudra insérer une image.

## Rassembler les ressources
[video]( https://vimeo.com/138623756 ){: .cours_video }

Rappelons qu'une page affichée dans votre navigateur est en fait un assemblage de nombreuses ressources. Il faut donc dans un premier temps les rassembler.

Une image est une ressource au même titre que les autres documents. Elle est donc désignée par une URL. Notez bien que ce mécanisme d'URLs permet de désigner des images dans les pages web comme autant de ressources indépendantes. En conséquence, les images ne se trouvent pas forcément sur le même serveur que le document principal.

Examinons alors plus en détail ce qui se passe lorsque je clique sur un lien qui pointe vers une ressource de type texte mais qui cette fois contient des liens vers des images, ce que nous faisons tous les jours et qui constitue l'essentiel des pages que nous consultons. Le début du processus est rigoureusement identique à l'exemple précédent, mais au moment du calcul du résultat, (i.e. de l'affichage de la page Web par le navigateur), le client rencontre dans la description de sa page, un lien vers une ressource image . Il ne peut pas afficher cette image directement puisque le fichier n'est pas inclus , seul le lien vers cette ressource est spécifié.

Alors, sans rien nous demander , il effectue une autre requête (identique à la précédente mais avec l'url de l'image) pour obtenir cette ressource. La réponse à cette requête est une copie du fichier image indiqué. Le client peut alors l'intégrer à l'affichage de la page.

Ce processus se répète autant de fois qu'il y a d'images dans le document et ce, quelles que soient leurs tailles.

Cette remarque prendra tout son sens lorsque nous nous intéresserons aux traces que nous laissons et à la préservation de notre vie privée.


## Mise en forme
[video]( https://vimeo.com/138623826 ){: .cours_video }

Revenons maintenant à l'affichage de la page dans mon navigateur.

Le document que le client/navigateur reçoit contient du texte et des images (en lien) et il est structuré .

Mais a priori aucune indication n'est donnée pour définir comment les éléments doivent être affichés.

Un titre doit-il être en rouge, en noir, en gras, de quelle taille, aligné à gauche ou centré ?

Or, tous les fichiers étant décrit dans une norme commune , le langage HTML , tous les navigateurs proposent une mise en forme par défaut de chacun des éléments possibles d'un document.

Cette mise en forme est généralement basique et pas très esthétique mais elle permet de proposer sur n'importe quelle machine un affichage du contenu.

Lorsque nous surfons tous les jours, nous voyons bien qu'au contraire, les sites proposent des affichages très graphiques beaucoup plus sophistiqués que l'affichage par défaut.

C'est l'utilisation de feuilles de styles qui sont associées au document qui permet cela. Une feuille de styles définit les règles de présentation d'un document.

Ces feuilles de styles, qui constituent à nouveau une ressource avec leur propre url redéfinissent l'affichage des différents éléments de contenu en utilisant par exemple une charte graphique aux couleurs de l'organisation responsable du site.

Concrètement, dans le fichier du document principal, un lien particulier vers une ressource/feuille de style, déclenche pour le navigateur une requête pour obtenir cette feuille de style qui sera utilisée à la place des styles par défaut.

Le triptyque structure/contenu/présentation est fondamental pour la compréhension de ce qu'est un document numérique.

Il est réalisé par le couple HTML/feuilles de style sur le Web.

Mais une bonne utilisation du traitement de texte passe également par la maîtrise de cette décomposition en 3 parties.

```compréhension
// Question vide de type description (sans {}) pour présenter le support des questions suivantes
::Exercice::[html]
<p>Rendez-vous sur la page <a target="_blank" href="http://culturenumerique.univ-lille3.fr/activitesWeb/html/">http://culturenumerique.univ-lille3.fr/activitesWeb/html/</a> <br />Lisez, observez, gardez les pages ouvertes dans des onglets, puis répondez aux questions du quizz suivant </p>


// question: 283  name: Au delà du contenu
::Au delà du contenu::[html]<p>Pourquoi peut-on créer facilement une table des matières ou construire la liste des liens d’un document HTML ?</p>{}


// question: 282  name: Comprendre les balises
::Comprendre les balises::[markdown]Nous vous avons expliqué que les balises `<section>... </section>` servaient à délimiter les parties, les balises `<h1> ... </h1>` délimitent les titres de premier niveaux, à votre avis que signifient les balises `<p> ... </p>` ?{}


// question: 280  name: Repérer la feuille de styles
::Repérer la feuille de styles::[html]<p>Comparez les codes sources des 2 premières pages, seule une ligne supplémentaire a été insérée, elle précise l'utilisation d'une feuille de styles pour l'affichage du contenu. Indiquez le numéro de la ligne qui a changé et recopiez-la également.</p>{}


// question: 284  name: Décrire un document
::Décrire un document::[html]<p>Pourquoi s’échanger une description de document plutôt qu’un document lui-même est plus adéquat au Web ?</p>{
	~%33.33333%<p>tous les clients n’ont pas la même capacité d’affichage</p>
	~%33.33333%<p>la description contient plus d’informations \: structure + contenu</p>
	~%33.33333%<p>la structure permet d'ajouter du sens (ceci est un titre, etc...) explicitement.</p>
}


// question: 281  name: Exemple de mise en forme
::Exemple de mise en forme::[html]<p>Observez la mise en forme du titre principal dans la deuxième version et indiquez les caractéristiques d'affichage qui ont été choisies dans cette feuille de styles (ce qui change par rapport à la première version).</p>{
	~%25%la typo (la police de caractères)
	~l'ordre des mots a été changé
	~%25%la couleur des caractères
	~%25%l'alignement du paragraphe
	~%25%les caractères ont été transformés en majuscule
	~l'orthographe a été modifié
	####<p>Une feuille de styles ne peut pas changer l'ordre des mots ou l'orthographe, cela reviendrait à changer le contenu, seules les caractéristiques graphiques sont possibles, ici la police, la couleur, l'alignement et la 'casse' des caractères (ils sont affichés en majuscule).</p>
}


// question: 286  name: Les feuilles de style
::Les feuilles de style::[html]<p>Une feuille de style...</p>{
	~<p>décrit le contenu d'un document HTML</p>
	~%50%<p>permet de décrire la présentation graphique d'un document</p>
	~%50%<p>décrit par exemple la couleur du texte, la taille des marges</p>
	~<p>coordonne automatiquement les couleurs d'une page web</p>
	~<p>contrôle si on écrit comme Flaubert ou Blazac</p>
}


// question: 285  name: Structure et contenu
::Structure et contenu::[html]<p>Le langage HTML permet de décrire des documents en indiquant leur structure et leur contenu. Comment la structure est-elle décrite ?</p>{
	=<p>Par un balisage du texte</p>#Votre réponse est correcte.
	~<p>Par des couleurs et du gras ou la taille des caractères</p>
}


// question: 288  name: Une page Web
::Une page Web::[html]<p>Pour qu’un client affiche une page Web,...</p>{
	~<p>une seule requête vers un unique serveur suffit toujours</p>
	~<p>parfois plusieurs requêtes sont nécessaires mais toujours vers le même serveur</p>
	=<p>parfois plusieurs requêtes vers plusieurs serveurs sont nécessaires</p>#Votre réponse est correcte.
}


// question: 287  name: Expressivité de HTML
::Expressivité de HTML::[html]<p>Le langage HTML permet de représenter une image.</p>{TRUE#<p>Les images ne sont pas décrites en HTML. HTML ne permet que d'indiquer qu'à un certain endroit dans un document, se trouve une image.
####[html]En HTML, les images sont représentées dans un format qui leur est propre. Elles sont soit <a href="https://fr.wikipedia.org/wiki/Image_matricielle" target="_blank">matricielles</a> ou <a href="https://fr.wikipedia.org/wiki/Image_vectorielle" target="_blank">vectorielles</a>.</p><ul><li>Les images matricielles décrivent une image comme un assemblage de points de couleur, généralement dans un rectangle de dimensions données par des nombres de points en largeur et en hauteur. Les formats de représentation de ces images matricielles utilisées sur le web sont par exemple le <a href="https://fr.wikipedia.org/wiki/Graphics_Interchange_Format" target="_blank">GIF</a>, le <a href="https://fr.wikipedia.org/wiki/Portable_Network_Graphics" target="_blank">PNG</a>, le <a href="https://fr.wikipedia.org/wiki/JPEG" target="_blank">JPEG</a>.</li><li>Les images vectorielles sont la description d'une image par des formes et des opérations géométriques. Le format <a href="https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics" target="_blank">SVG</a> est utilisé sur le web. Peu d'autres le sont. </li></ul>}
```

```activité-avancée
::Activité sur les serveurs::[markdown]
Rendez-vous sur la page :
[pageServeurs.html](http://culturenumerique.univ-lille3.fr/activitesWeb/html/pageServeurs.html)
\n
Lisez, observez et répondez aux questions posées...
{}
```


# Les Cookies

## Cours
[video](https://vimeo.com/138623890 ){: .cours_video }
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

```compréhension

// question: 289  name: Cookie tiers
::Cookie tiers::[html]<p>Un cookie tiers c'est ...</p>{
	~<p>est un cookie découpé en 3 parties</p>
	~<p>un cookie partagé entre trois sites</p>
	=<p>un cookie déposé à la demande d'un serveur qui n'est pas celui de la page web visitée</p>#<p>Votre réponse est correcte.</p>
	####<p>Un cookie tiers est bien un cookie qui est déposé sur notre machine par un serveur qui n'est pas celui de la page Web que l'on visite. C'est une technique très souvent utilisée pour l'affichage de publicité ciblée.</p>
}


// question: 290  name: Possible ou impossible
::Possible ou impossible::[html]<p>Cochez toutes les affirmations vraies ou possibles. Certaines questions peuvent demander une petite recherche sur Internet. <br></br></p>{
	~%20%<p>on peut supprimer tous les cookies stockés sur sa machine</p>
	~%20%<p>on peut refuser tous les cookies</p>
	~%20%<p>on peut refuser les cookies de certains sites</p>
	~%20%<p>on peut refuser les cookies tiers</p>
	~<p>un serveur A peut voir les cookies déposés par un serveur B différent de A</p>
	~%20%<p>les cookies peuvent servir à constituer des profils à l'insu des internautes</p>
	~<p>les cookies ne servent qu'à la publicité</p>
	~<p>il n'y a pas de cookies sur les smartphones</p>
}


// question: 291  name: Un cookie
::Un cookie::[html]<p>Un cookie  est une information<br></br></p>{
	~<p>stockée sur un serveur web à la demande d'un client</p>
	=<p>stockée sur un client à la demande d'un serveur</p>#Votre réponse est correcte.
}

```

```activité-avancée

[html]<p>Rendez-vous sur les pages suivantes, lisez et effectuez les manipulations demandées :</p>
<ul><li><a target="_blank" href="http://culturenumerique.univ-lille3.fr/activitesWeb/cookies/cookie.php">http://culturenumerique.univ-lille3.fr/activitesWeb/cookies/cookie.php</a></li>
<li><a target="_blank" href="http://culturenumerique.univ-lille3.fr/activitesWeb/cookies/cookietiers.html">http://culturenumerique.univ-lille3.fr/activitesWeb/cookies/cookietiers.html</a></li></ul>
{}
```

## La messagerie électronique et les cookies

### Le cas des mails

Le mail est un autre exemple de système client/serveur et les programmes qui nous servent à lire nos messages sont des clients mail. Il en existe de nombreuses sortes mais leurs fonctionnalités sont comparables. Parmi les options possibles, ils proposent tous de choisir si les messages que l'on envoie et surtout ceux qu'on lit s'affichent au format texte ou au format HTML.

En effet, lorsque cette application de messagerie a été inventée, bien avant l'invention du web, les mails ne pouvaient contenir que du texte sans aucune mise en forme. Mais cette norme a évolué et il est possible de modifier la présentation du texte de nos messages et même d'y inclure des éléments de structure, d'y insérer des images ou d'autres ressources exactement comme dans une page web.

Lors de la lecture d'un tel message, le client mail qui a en charge l'affichage se comporte exactement comme un client web. Les différentes ressources font l'objet de requêtes HTTP telles que nous les avons décrites précédemment.

Les remarques sur les cookies et les mouchards s'appliquent donc comme pour le web. Très concrètement, la simple lecture d'un message au format HTML, peut donc envoyer beaucoup d'informations à des serveurs tiers du type : le mail a été lu, nous avons cliqué sur tel ou tel lien, etc, autant de choses qui ne sont pas possibles si le message n'est qu'un simple texte.

Les boutons de réseaux sociaux ont également la même fonction que sur les pages web.

Par exemple, à la réception d'une newsletter envoyée en masse, l'expéditeur peut savoir si nous avons lu le message ou pas, ce qui dans le cas de liste de diffusion de plusieurs dizaines de milliers d'adresses, permet de trier les adresses valides des adresses abandonnées. Les listes d'adresses valides (quelqu'un la lit régulièrement) se revendent très chères et sont entre autres à l'origine de nombreux spams.

Vous pouvez paramétrer votre client mail pour lire les messages comme si ils n'avaient pas été écrits en HTML mais comme un simple texte. Ou vous pouvez lui indiquer de ne jamais réaliser de requête web : vous ne verrez peut être pas les images et peut être que la mise en forme ne sera pas agréable ou optimale. En contrepartie aucune requête ne sera alors faite vers une ressource extérieure. Personne ne pourra donc « pister » vos actions. À vous de régler votre lecteur de mail avec les paramètres qui correspondent à ce que voulez faire.

De la même manière, vous pouvez paramétrer votre client mail pour envoyer des messages soit en texte seul soit au format HTML.

### Le cas des pièces jointes

Notons qu'une pièce jointe fait partie d'un message, il est envoyé avec le corps du message et ne constitue pas une ressource externe. On peut donc s'échanger des messages avec des images en pièce jointe sans utiliser l'affichage HTML.

```compréhension

// question: 292  name: La messagerie électronique et HTML
::La messagerie électronique et HTML::[html]<p>Sélectionnez les affirmations vraies.</p>{
	~<p>les messages électroniques sont toujours écrits en HTML</p>
	~<p>les messages comprenant des pièces jointes sont écrits en HTML</p>
	~%50%<p>les messages écrits en rose sont en HTML</p>
	~%50%<p>les messages avec des images dans le texte (pas en pièce jointe) ou dans la signature sont en HTML.</p>
	####<p>Par défaut, les messages électroniques (email) sont écrits en 'texte simple', donc pas en html. Des pièces jointes peuvent être ajoutés au texte. En revanche, dès que le texte est mis en forme (couleur, style, alignement, etc. ) ou qu'une image est insérée dans le corps du message, cela signifie que le mail est en html avec toutes les conséquences vues dans le cours.</p><p>On peut toujours paramétrer son client mail pour ne pas afficher le contenu HTML, évidemment les mises en page seront perdues, ...</p>
}


// question: 293  name: Messagerie électronique et cookies
::Messagerie électronique et cookies::[html]<p>Sélectionnez la bonne réponse ...</p>{
	~<p>la lecture d'un message écrit en HTML provoque toujours l'envoi de cookies</p>
	~<p>la lecture de messages en texte (non HTML) peut provoquer l'envoi de cookies</p>
	~<p>si la lecture d'un message provoque l'envoi de cookies, c'est uniquement vers l'expéditeur du message</p>
	=<p>Tout est faux</p>#<p>Votre réponse est correcte.</p>
	####<p>Tout est faux \: </p><ul><li>la lecture d'un message écrit en HTML peut provoquer l'envoi de cookies ; </li><li>la lecture de messages en texte ne provoque pas l'envoi de cookies, mais il est parfois difficile de discerner un message en simple texte et un message en HTML ! ; </li><li>un expéditeur de message n'est pas un serveur web (même si l'adresse peut être associée un serveur web) et de plus, si la lecture d'un message provoque l'envoi de cookies, ce cookie peut être un cookie tiers et envoyé à n'importe qui.</li></ul>
}
```

# Profils et réseaux sociaux

## Cours
Votre âge, votre adresse,   vos achats
récents, vos goûts musicaux, vos films préférés, vos amis, etc,
toutes ces données peuvent intéresser de nombreuses sociétés et
organisations soit pour vous surveiller soit pour vous vendre quelque
chose. Rassemblées, elles contribuent à définir votre /profil/.

### Profils et cookies

Grâce aux cookies contenant des numéros d'identification, des sites ou
 des jeux, sur PC, en ligne ou sur smartphone peuvent contribuer à
 créer et compléter nos profils. Souvent c'est même à notre insu, en
 mémorisant nos parcours sur le site, les pages visitées, etc.. Cette
 collecte peut même être assurée par le biais de sites partenaires grâce à la
 technique des cookies tiers.


### Les réseaux sociaux - pistage systématique

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

### Nos profils mis aux enchères

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

### La minute citoyenne
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

```compréhension

// question: 294  name: Les profils
::Les profils::[html]<p>Vrai ou faux ? Pour chaque affirmation ci-dessous cochez la case correspondante pour indiquer qu'elle est vraie.<br></br></p>{
	=<p>une partie de l'économie du web repose sur la collecte de données personnelles</p>
	~<p>quand un service sur le web est gratuit alors il se finance par la collecte de données personnelles</p>
	~<p>Les cookies et cookies tiers sont les seuls outils de la création de profils</p>
}

```

```activité-avancée

::A vous !::Attention, vous n'avez droit qu'à une seule tentative. Pour les questions ouvertes, répondez d'abord dans un document séparé, puis collez les réponses dans les zones prévues une fois votre travail terminé.

// question: 296  name: Cookies tiers or not cookies tiers ?
::Cookies tiers or not cookies tiers ?::[html]<p>Les navigateurs doivent-ils par défaut autoriser les cookies tiers ?</p>{}


// question: 297  name: J'aime ou j'aime pas ?
::J'aime ou j'aime pas ?::[html]<p>Un webmaster doit-il prévenir les internautes lorsqu'il décide d'inclure sur sa page un bouton associé à un script qui collecte des informations pour un tiers ?</p>{}


// question: 295  name: Pister or not pister ?
::Pister or not pister ?::[html]<p>Trouvez-vous normal qu'un réseau social piste ses adhérents sans les prévenir ?</p>{}


::Question de loyauté::[html]<p>Écoutez l'enregistrement "Quand nos smartphones sont espionnés" depuis
<a href="https://interstices.info/jcms/p_83464/quand-nos-smartphones-sont-espionnes">cette page</a>
puis répondez à la question qui suit.</p>{}

// question: 298  name: Exemple d'application qui ne respecte pas la loyauté
::Exemple d'application qui ne respecte pas la loyauté::[html]<p>Donnez un exemple d'application citée dans l'enregistrement qui ne respecte pas les principes de base de loyauté entre éditeur d'application et utilisateur.</p>{}

```


# Moteurs de recherche
## Cours

### Des ressources qui n'existent que quand on les demande...
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

### Un annuaire de toutes les ressources
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

###  Comment fonctionne un moteur de recherche aujourd'hui
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

### Collecte de données d'usage

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

### Modèle économique du moteur de recherche

 Pour une institution qui veut être visible sur internet, if faut
 assurer sa présence dans l'index. Mais cela n'est pas suffisant : il
 faut être en haut de la liste et donc apparaître important aux yeux du
 moteur de recherche.

 De bonnes pratiques en matière de conception de pages web peuvent y
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


### Aller plus loin

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

```compréhension

// question: 299  name: Combien de sites Web ?
::Combien de sites Web ?::[html]<p>Quelle est l'estimation actuelle du nombre de sites Web dans le monde ?</p><p>Faites quelques recherches pour trouver un ordre de grandeur.</p>{}


// question: 300  name: Recherche avancée 1
::Recherche avancée 1::[html]<p>Faites une recherche Google avec les deux mots \:</p><p><em>université Lille</em></p><p>Notez le nombre de pages trouvées.</p><p>Faites maintenant une recherche avec \:</p><p><em>"université Lille" <br></br></em></p><p>(en incluant les guillemets)</p><p>Avez vous autant de résultats ? Décrivez-les.</p>{}


// question: 301  name: Recherche avancée 2
::Recherche avancée 2::[html]<p>Faites une recherche avec \:</p><p><em>"université lille" -3 -2 -1. </em></p><p>Que se passe-t-il ?</p>{}

```

```activité-avancée

::Activité de recherche et réflexion::Attention, vous n'avez droit qu'à une seule tentative. Pour les questions ouvertes, répondez d'abord dans un document séparé, puis collez les réponses dans les zones prévues une fois votre travail terminé.


// question: 302  name: neutralité 1
::neutralité 1::[html]<p>Consultez l'interview suivante et expliquez en quoi il est important pour un moteur de recherche de donner une réponse neutre. <a href="http://www.inria.fr/actualite/actualites-inria/la-neutralite-ne-suffit-pas" target="_blank">http://www.inria.fr/actualite/actualites-inria/la-neutralite-ne-suffit-pas</a></p>{}


// question: 303  name: neutralité 2
::neutralité 2::[html]<p>Le gouvernement français travaille sur un projet de loi "<em>pour une République numérique</em>", consultable sur <a href="https://www.republique-numerique.fr" target="_blank">https://www.republique-numerique.fr</a><br></br>Nous vous invitons à enrichir vos connaissances en consultant ce site en détail.</p><p>Expliquez en quoi l'article consultable <a href="https://www.republique-numerique.fr/consultations/projet-de-loi-numerique/consultation/consultation/opinions/section-3-loyaute-des-plateformes/article-13-principe-de-loyaute-vis-a-vis-des-consommateurs" target="_blank">ici</a> répond au moins en partie à ce que souligne Serge Abiteboul dans son <a href="http://www.inria.fr/actualite/actualites-inria/la-neutralite-ne-suffit-pas" target="_blank">interview</a> à la question sur la neutralité des moteurs de recherche. Pour cela recopiez une phrase de l'interview et une phrase de l'explication de l'article de loi. </p>{}


// question: 304  name: neutralité 3
::neutralité 3::[html]<p>Le gouvernement français travaille sur un projet de loi "<em>pour une République numérique</em>", consultable sur <a href="https://www.republique-numerique.fr" target="_blank">https://www.republique-numerique.fr</a><br></br>Nous vous invitons à enrichir vos connaissances en consultant ce site en détail.</p><p>Testez vos connaissances en répondant aux 14 questions du quizz (<a href="http://www.gouvernement.fr/quiz-le-projet-de-loi-numerique" target="_blank">http://www.gouvernement.fr/quiz-le-projet-de-loi-numerique</a>) et répondez ci-dessous à la question suivante: <strong>quelles sont les deux questions dont les réponses vous ont le plus surpris ?</strong></p>{}



::Attention, l'abus de Google est dangereux pour la planète !::Attention, vous n'avez droit qu'à une seule tentative. Répondez d'abord dans un document séparé, puis collez les réponses dans la zone prévue une fois votre travail terminé.


// question: 305  name: Conséquences d'une recherche
::Conséquences d'une recherche::[html]<p>Comparez ces deux usages\:</p><p>1. Dans la barre de recherche (ou barre d'URL) je saisis \:<br></br><em>université de lille 3</em><br></br>et ensuite dans la page de résultats affichée je clique sur le lien vers l'université (lien vers http\://www.univ-lille3.fr)</p><p>2. Dans la barre d'URL (attention de ne pas confondre avec la barre de recherche !), je saisis \:<br></br><em>http\://www.univ-lille3.fr</em>.</p><p><strong>Questions</strong>\: Quelles sont les incidences de ces actions dans chacun des cas. Existe-t-il une différence en terme de consommation énergétique, ou de préservation de la vie privée ?</p>{}


::Des moteurs de recherche moins intrusifs...::Attention, vous n'avez droit qu'à une seule tentative. Répondez d'abord dans un document séparé, puis collez les réponses dans la zone prévue une fois votre travail terminé.


// question: 306  name: DuckDuckGo
::DuckDuckGo::[html]<p>Utilisez maintenant un nouveau moteur de recherche <a href\="https\://duckduckgo.com/" target\="_blank">https\://duckduckgo.com/</a>, testez-le \:</p><p>Qu'obtenez vous avec le mot \: Go</p><p>Qu'obtenez vous avec le mot \: Go!wfr</p><p>Qu'obtenez vous avec le mot \: Go!gfr</p><p>Décrivez les réponses obtenues et après quelques recherches personnelles, expliquez ce qu'est DuckDuckGo et pourquoi certains utilisateurs préfèrent l'utiliser.</p>{}

```


# Autres informations sensibles et bilan
## Autres informations
[video]( https://vimeo.com/138623956 ){: .cours_video }
On voit bien que les techniques qui se sont développées et qui continuent d'évoluer sur le Web sont puissantes et nous rendent beaucoup de services. En revanche, leur utilisation dans certains cas peut poser de graves questions de citoyenneté. Bien souvent, la donnée associée au cookie est un numéro d'identification permettant au serveur de retrouver dans ses bases des données propres à l'utilisateur.
Dans notre exemple de démarche d'inscription, ce pourrait être, l'étape à laquelle il est arrivé, son nom, ses choix de formation...  

Il est très important de comprendre qu'un tel numéro d'identification est un moyen très commun utilisé sur le web aussi bien que dans la vie non numérique. C'est la technique utilisée par la sécurité sociale (avec le numéro de sécurité sociale), pour vous suivre toute notre vie dans nos démarches de couverture sociale. C'est aussi ce qui se cache derrière les cartes d'achat ou promotionnelles des magasins, proposées avant tout pour nous suivre et assurer du marketing direct.
Donc bien des numéros nous identifient.

Mais dès lors que ces numéros d'identification sont rapprochés ou unifiés, la technique devient si puissante qu'on l'estime menaçante pour nos libertés.
Si bien que par exemple, le parlement a dû légiférer il y plus de 30 ans pour empêcher ou limiter l'usage du numéro de sécurité sociale dans les autres administrations de l'état.
Naturellement, avec l'avènement du numérique ce rapprochement de numéros d'identification devient très facile techniquement. Il convient de redoubler de vigilance...

## Bilan: du pour, du contre
[video]( https://vimeo.com/139925788 ){: .cours_video }

Il faut donc avoir conscience que la consultation d'une page laisse des traces sur mon disque dur et sur le réseau.
Toutes ces traces peuvent être considérées à divers degrés comme des informations personnelles.

Celles qui résident sur l’ordinateur que vous utilisez, qui peut appartenir à votre employeur, à l’université ou à un cybercafé sont techniquement lisibles par les administrateurs ou les propriétaires de l’ordinateur.
Les traces qui sont laissées à travers les réseaux, puis sur des serveurs que vous consultez ou des serveurs tiers sont potentiellement exploitables par de nombreux acteurs.
Il ne s’agit pas de dénoncer ces pratiques comme si elles étaient des malversations.

La mise en cache nous permet de gagner du temps, l’historique est un outil pratique pour rechercher des informations vues récemment, et les cookies sont indispensables au bon fonctionnement d’une très grande quantité de sites.
Par ailleurs, une bonne partie des sites que nous visitons n’existeraient plus si ils n’étaient pas financés par la publicité.
En revanche, il nous semble important que chacun ait conscience de ce qui se passe.
Aujourd’hui beaucoup croient surfer incognito dès lors qu’on ne voit pas leur écran sans penser qu’un simple clic sur le menu de l’historique peut révéler bien des choses.
Une infime minorité des internautes a conscience que les pratiques de web-marketing agressives que nous venons de décrire sont abondamment utilisées.
Une question essentielle dont nous devons tous prendre conscience est celle de la pseudo-gratuité du web :

Qui finance les services et les contenus qui sont à notre disposition sur le web ?
La publicité est-elle le seul moyen de financement ?
Jusqu’où sommes-nous prêts à laisser les publicitaires nous cibler ?
Que considérons-nous relever de la vie privée et des données confidentielles ?
Les pratiques de ciblage comportemental vous paraissent-elles légitimes dès lors que nous n’en sommes pas informés ?

On peut tous avoir des avis différents sur ces questions, et chacun devrait être libre de surfer en connaissance de cause.
Aujourd’hui, pour une bonne part du web, on peut considérer que : “SI C’EST GRATUIT, C’EST QUE LE PRODUIT C’EST VOUS”.
Vous avez néanmoins la possibilité de choisir les traces que vous êtes prêts à laisser derrière vous.

Les activités associées à ce module vont entre autre vous permettre de voir comment paramétrer votre navigateur pour faire vos propres choix.

```compréhension

// question: 307  name: Les données locales
::Les données locales::[html]<p>Cochez les bonnes affirmations dans cette liste<br></br></p>{
	~%25%<p>le cache permet d'accélérer l'affichage des pages web déjà visitées</p>
	~<p>le cache permet de naviguer sur le web icognito</p>
	~%25%<p>Si quelqu'un accède à mon ordinateur, il a techniquement la possibilité de connaître les sites web que j'ai récemment visités</p>
	~%25%<p>Grâce à l'historique vous pouvez retrouver la liste des sites que vous avez visités récemment</p>
	~<p>Grâce à l'historique vous pouvez revoir le contenu exact des pages que vous avez visitées récemment</p>
	~%25%<p>Grâce à l'historique vous pouvez, ré-ouvrir une fenêtre ou un onglet du navigateur récemment fermé</p>
	~<p>Si une page est dans l'historique, vous pouvez la retrouver dans le cache</p>
	####<ul><li>Le cache permet d'accélérer l'affichage des pages web  ;</li><li>Si quelqu'un accède à mon ordinateur, il a techniquement la possibilité de connaître les sites web que j'ai récemment visités en regardant le cache et l'historique<br></li><li>Vous pouvez retrouver la liste des sites que vous avez visités récemment dans l'historique. Dans le cache c'est techniquement possible de retrouver de telles informations également.<br></li><li>L'historique permet de ré-ouvrir une fenêtre ou un onglet du navigateur récemment fermé, mais vous ne pouvez pas toujours revoir le contenu exact des pages que vous avez visitées récemment car des données qui s'y trouvent peuvent être calculées en fonction de nombreux paramètres (date, autres visiteurs, etc...) ; <br></li><li>Il est possible qu'une adresse se trouve dans l'historique sans que la page soit stockée dans le cache</li></ul>
}

```

```activité-avancée
::Vider le cache et l'historique::Faites une capture de la fenêtre du navigateur qui propose de vider le cache et les autres données locales. Déposez-la dans ce devoir.{}


::L'intermédiation: votre analyse::[html]
<p>Pour terminer ce cours, nous vous proposons de regarder une vidéo d'une présentation par Stéphane Grumbach qui explique les impacts du web et des données numériques d'un point de vue sociétal.</p>
<p><a target="_blank" class="moz-txt-link-freetext" href="https://www.liglab.fr/evenements/keynote-speeches/stephane-grumbach-leconomie-lintermediation">https://www.liglab.fr/evenements/keynote-speeches/stephane-grumbach-leconomie-lintermediation</a> (1h11mn).</p>
<p>Citez les éléments dans ce séminaire de Stéphane Grumbach qui vous ont le plus surpris.<em>(Attention, vous n'avez droit qu'à une seule tentative. Cette question est ouverte, répondez d'abord dans un document séparé, puis collez votre réponse dans la zone prévue une fois votre travail terminé.)</em></p>
{}
```
