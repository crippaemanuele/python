<p  align="center">

<img  src="assets/python.gif"  alt="Python Logo"  width="75"  height="75">

</p>

# Cours de Python 🐍

[![en](https://img.shields.io/badge/lang-en-white.svg)](https://github.com/crippaemanuele/python/blob/master/README.md)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/crippaemanuele/python/blob/master/README.it.md)
[![es](https://img.shields.io/badge/lang-es-red.svg)](https://github.com/crippaemanuele/python/blob/master/README.es.md)
[![de](https://img.shields.io/badge/lang-de-yellow.svg)](https://github.com/crippaemanuele/python/blob/master/README.de.md)
[![fr](https://img.shields.io/badge/lang-fr-purple.svg)](https://github.com/crippaemanuele/python/blob/master/README.fr.md)

## _Des bases à la programmation orientée objet et plus encore, avec des exemples_.

Tous les exercices seront disponibles sur :

![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Et tout le code est écrit en utilisant :

![Visual Studio Code](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

Ce référentiel est créé pour les personnes (étudiants ou autodidactes) qui veulent connaître les bases de la programmation en ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue).

## Sujets

Voici un index des sujets abordés (inspiré de <https://roadmap.sh/python/>) :

### Bases

#### Questions sur python

- **Pourquoi?** Grâce à sa flexibilité, python peut être utilisé dans tous les domaines dont vous pouvez avoir besoin : des programmes les plus simples à la science des données et à l'apprentissage automatique.

- **Quoi ?** Python est un langage de programmation né dans les années 90, mais qui n'est devenu populaire que plus tard. C'est un langage **interprété**, ce qui signifie qu'un interpréteur (intégré aux paquets d'installation de Python) "lira" ligne par ligne le code et l'exécutera. Il est très facile à comprendre et à utiliser et peut servir de base à l'apprentissage de tout autre langage de programmation.

- Les programmes Python peuvent être développés à partir de l'IDE (Integrated Development Enviroment) intégré, IDLE, ou, comme dans ce cours, vous pouvez utiliser [Visual Studio Code] (https://code.visualstudio.com/).

- **Comment?** À la fin de ce cours, vous comprendrez ce qu'est la programmation et vous aurez un petit projet construit avec des guides étape par étape.

#### Variables et types de données

 **Qu'est ce qu'une variable ?** Imaginons un tiroir (_notre variable_), sur lequel se trouve une étiquette (_le nom de la variable_). Dans ce tiroir, vous pouvez mettre des "choses" (_nos informations_) et, à moins que vous ne les retiriez du tiroir, elles y resteront.

 Pour faire vrai, une **variable** est une zone d'espace dans notre ordinateur où nous pouvons stocker des informations utiles à notre programme.

 En Python, la syntaxe pour créer une variable est la suivante :

 ```python

 x=1

 ```

 Nos variables peuvent être définies comme des types de données. Nous pouvons diviser les types de données en deux grandes catégories :

 **Primitive.** Ces types de données sont les plus fondamentaux : **integer** (qui définit tous les nombres entiers), **float** (qui définit les nombres à virgule flottante), **complex** (qui définit les nombres complexes, avec j comme partie imaginaire), **boolean** (qui définit les valeurs 0 [faux] ou 1 [vrai] utilisées pour les opérations logiques et booléennes), **str** (qui définit tous les types de texte).

 Voici une liste de la façon de définir chaque type de données vu ci-dessus :

 ```python

 x=int(255) #intégral

 x=float(1.00) #point flottant

 w=complexe(5+3j) #complexe

 x=bool(true) #booléen

 x=str('ceci est une chaîne') #texte (ou chaîne)

 ```

> Notez que ce n'est pas une opération nécessaire, en fait Python peut utiliser des variables sans leur attribuer de valeur.
> Python peut utiliser des variables sans leur attribuer un type de données spécifique.  Bien que
> est nécessaire dans certains cas.

#### Listes, Dictionnaires

En utilisant une variable nous ne pouvons stocker qu'une seule information à la fois, il existe des structures en Python qui nous permettent de stocker plusieurs informations, ces structures sont appelées **listes**, voici la syntaxe pour en créer une

```python
list1=["item1", "item2", "item3"] #liste de chaînes de caractères
intList=[1,2,3,4,5,6] #liste d'indices
boolList=[True, False, False] #liste de bools
mixed=["item",1,True] #les listes peuvent aussi contenir des types mixtes
```  

> Comme vous pouvez le voir, c'est comme créer une variable mais nous devons utiliser les
> crochets **[]** pour définir les éléments en les séparant par une virgule.
> **,**  

Une liste a ces 3 caractéristiques :

1. Ordonnée  
 ↳ Les listes sont ordonnées, ce qui signifie que si vous ajoutez un élément, il sera ajouté à la fin de notre liste.
2. Modifiables  
 ↳ Cela signifie que nous pouvons **ajouter**, **changer**, **supprimer** des éléments de la liste après l'avoir créée.
3. Duplicata  
 ↳ Puisque les listes ont des index, nous pouvons avoir des valeurs dupliquées.  
Afin d'accéder aux éléments d'une liste, nous pouvons utiliser cette syntaxe :

```python
list1[1] #accès à l'élément en position 1 (2)
```

> Notez que pour compter les positions des éléments, nous partons de **0**, donc le premier élément de la _intList_ sera ``intList[0]=>1``

#### Casting

Une opération fatale en programmation est le **casting**, qu'est-ce que cela signifie ? Cela signifie forcer un type de données dans un autre, laissez-moi vous expliquer...
Imaginez que vous avez une division entre deux valeurs flottantes et que vous voulez seulement avoir la valeur entière du quotient, voici comment faire !

 ```python
 x=float(250)
 y=float(256)
 div=int(x/y)

 ```

> Notez que vous ne pouvez pas transformer un type de données en n'importe quel autre.
> pour certains types de données, il faut des **fonctions** (_comme l'analyse syntaxique_).


