<p  align="center">

<img  src="assets/python.gif"  alt="Python Logo"  width="75"  height="75">

</p>

# Cours de Python 🐍

[!en](https://img.shields.io/badge/lang-en-white.svg)](https://github.com/crippaemanuele/python/blob/master/README.md)
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

- Quoi ? Python est un langage de programmation né dans les années 90, mais qui n'est devenu populaire que plus tard. C'est un langage **interprété**, ce qui signifie qu'un interpréteur (intégré aux paquets d'installation de Python) "lira" ligne par ligne le code et l'exécutera. Il est très facile à comprendre et à utiliser et peut servir de base à l'apprentissage de tout autre langage de programmation.

- Les programmes Python peuvent être développés à partir de l'IDE (Integrated Development Enviroment) intégré, IDLE, ou, comme dans ce cours, vous pouvez utiliser [Visual Studio Code] (https://code.visualstudio.com/).

- Comment ? À la fin de ce cours, vous comprendrez ce qu'est la programmation et vous aurez un petit projet construit avec des guides étape par étape.

#### Variables et types de données

 **Imaginons un tiroir (_notre variable_), sur lequel se trouve une étiquette (_le nom de la variable_). Dans ce tiroir, vous pouvez mettre des "choses" (_nos informations_) et, à moins que vous ne les retiriez du tiroir, elles y resteront.

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

