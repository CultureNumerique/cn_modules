# Comment les éléments de cours "Culture Numérique" sont-ils produits ?

Nous détaillons ici la chaine éditoriale adoptée pour la production des modules mis à dispositions sur ce dépôt.  
Nous utilisons un fichier dit "maitre" comme matrice de base pour générer le cours. La syntaxe employée est basée sur le MarkDown, que nous avons étendus pour nos besoins spécifiques. Ces ajouts consistent en des conventions et l'usage d'extensions proposées par la [librairie Python de MarkDown](https://pythonhosted.org/Markdown/extensions). 

### Structure globale d'un cours Culture Numérique
Un cours se décompose en sections et sous-sections. Chaque sous-sections peut être de la forme suivante:  
1. élément de cours simple (texte + images)  
2. élément de cour incluant une ou plusieurs animations (video) accompagnée à chaque fois par la version texte lisible en mode "zen"
3. auto-évaluation sous forme de quiz 
4. exercice d'approfondissement incluant un énoncé (texte riche) et un espace pour fournir une réponse sous forme de texte libre

### Elément de cours simple
Rédigé en MarkDown avec les extensions Python suivantes
####ajouter des classes CSS 

Avec des [Attribute list](https://pythonhosted.org/Markdown/extensions/attr_list.html): Pour permettre d'ajouter des classes CSS à une image ou à un bloc de texte, pour permettre une mise en page enrichie.
Un exemple pour ajouter un attribut en ligne à un lien:  
`[link](http://example.com){: class="foo bar" .titre title="Some title!" }`  
qui produit le HTML suivant:  
`<p><a href="http://example.com" class="foo bar titre" title="Some title!">link</a></p>`  

Notez que pour ajouter des classes on peut soit spécifier `.une_classe` ou `class='une_classe`

#### Commentaires invisibles
TODO

### Elément de cours avec animations vidéo
Ici il y a 2 étapes:  
- a) avant la réalisation des vidéos, on ajoute des blocs 'Idéee animation' pour décrire ce que pourrait contenir l'animation qui sera intégrée par la suite
- b) une fois la vidéo réalisé, on intègre le lien vers la vidéo qui sera ensuite intégrée via une iframe

####a) Notes pour idées d'animation
On se base ici sur la syntaxe des 3 backticks initialement proposée par l'extension GitHub de Markdown et supportée par les [Fenced Code blocks de l'extension Python](https://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html): en utilisant 3 backticks ````` en début et ````` à la fin du block, on génère un bloc code. Nous y ajoutons ici un mot clé *à la ligne* juste après les 3 premiers backtick comme suit  

    ```
    [Animation]  
    ```

Ce qui produit le bloc suivant:  

    [Animation]
    Peut être des lettres simples en suite de 0 et de 1, et des
    compositions en mots/composition de suites de 0 et 1...  est-ce
    qu'on fait passer l'idée de coder/décoder et sa contraction en codec?  


####b) Lien vers une vidéo d'animation
Sur le même principe que les *attribute lists*, on spécifie qu'il s'agit d'un lien vers une vidéo aen spécifiant la classe `lien_video`:  

    [Introduction au web](https://player.vimeo.com/video/138623497){: .lien_video } 

ou  

    [Introduction au web](https://player.vimeo.com/video/138623497){: class="lien_video" } 
    
Pour déterminer le texte associé à la vidéo, on regarde l'emplacement par rapport au début d'une section ou d'une sous-section. Si le lien est placé sur la ligne juste après le titre de section, alors c'est tout le texte de cette section qui sera associée à la vidéo; idem pour le cas d'une sous-section.  
Exemple:
```
# Le web et internet
## Le web
[Introduction au web](https://player.vimeo.com/video/138623497){: lien_video } 
```
Dans ce cas, tout le texte de la sous-section sera associé à la vidéo.



###  Activités

Les activités peuvent être de 2 types et sont représentées par une classe de bloc de code:
- auto-évaluation: `activite`
- Exercices d'approfondissement: `activite-avancee`
On utilise ici les "fenced code blocks" en spécifiant la syntaxe juste à côté des backticks:

        ```activite
        ```

Ces activités sont rédigées en GIFT; chaque question est séparée par une ligne vide. Exemple:

        ```activite-avance
        
        ::La représentation numérique d'un livre peut inclure des données qui ne se limitent pas au texte. Donnez quelques exemples:: {
        #### Le genre, la date de création, ...
        }
        
        ::Fonctionnalités d'un éditeur de textes::
        [html]<p>Parmi les  fonctionnalités suivantes, lesquelles sont possibles ?
        </p>
        {
        ~%25%copier/couper/coller#tous les éditeurs le permettent
        ~%25%rechercher et remplacer#très souvent disponible
        ~%25%avancer de mots en mots#souvent par la conjonction CRTL-flèches
        ~%25%corriger l'orthographe#certains le font
        ~%-100%mettre en gras#l'éditeur ne permet pas d'enregistrer des mises en forme (il est possible toutefois d'écrire des commandes de mise en forme : un mot n'est pas en gras mais un texte dans un langage peut exprimer l'ordre de mettre en gras)
        }
        ```
