<p  align="center">

<img  src="assets/python.gif"  alt="Python Logo"  width="75"  height="75">

</p>

# Python-Kurs 🐍

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/crippaemanuele/python/blob/master/README.md)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/crippaemanuele/python/blob/master/README.it.md)
[![es](https://img.shields.io/badge/lang-en-green.svg)](https://github.com/crippaemanuele/python/blob/master/README.es.md)
[![de](https://img.shields.io/badge/lang-de-yellow.svg)](https://github.com/crippaemanuele/python/blob/master/README.de.md)
[![fr](https://img.shields.io/badge/lang-fr-purple.svg)](https://github.com/crippaemanuele/python/blob/master/README.fr.md)

## _Von den Grundlagen bis zur objektorientierten Programmierung und mehr, mit Beispielen_

Alle Übungen sind verfügbar unter:

![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Der gesamte Code wird mit geschrieben:

![Visual Studio Code](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

Dieses Repository wurde für Personen (Studenten oder Autodidakten) erstellt, die die Grundlagen der Programmierung kennenlernen möchten ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue).

## Topics

Hier ist ein Index der behandelten Themen (inspiriert von <https://roadmap.sh/python/>):

### Grundlagen

#### Einige Fragen zu Python

- **Warum?** Aufgrund seiner Flexibilität kann Python in jedem Bereich eingesetzt werden, den Sie benötigen: von den einfachsten Programmen bis hin zu Data Science und maschinellem Lernen.

- **Was?** Python ist eine Programmiersprache, die in den 90er Jahren geboren wurde, aber erst später populär wurde. Es ist eine **interpretierte** Sprache, was bedeutet, dass ein Interpreter (eingebettet in Python-Installationspakete) den Code Zeile für Zeile "liest" und ausführt, es ist sehr einfach zu verstehen und zu verwenden und kann die Grundlage sein, um andere zu lernen Programmiersprache.

- **Woher?** Python-Programme können aus der eingebetteten IDE (Integrated Development Enviroment) entwickelt werden, die IDLE ist oder, wie in diesem Kurs, von Ihnen verwendet werden kann [Visual Studio Code](https://code.visualstudio.com/).

- **Wie?** Am Ende dieses Kurses haben Sie ein Verständnis dafür, was Programmieren bedeutet, und ein kleines Projekt, das mit Schritt-für-Schritt-Anleitungen erstellt wurde.

#### Variablen und Datentyp  

 **Was ist eine Variable?** Stellen wir es uns als eine Schublade (_unsere Variable_) vor, auf der sich ein Etikett (_der Variablenname_) befindet. In diese Schublade können Sie "Dinge" (_unsere Informationen_) legen, und wenn Sie die Dinge nicht aus der Schublade entfernen, bleiben sie darin.

 Realisieren ist eine **Variable**, ein Bereich in unserem Computer, in dem wir Informationen speichern können, die für unser Programm nützlich sind.

 In Python lautet die Syntax zum Erstellen einer Variablen:

 ```python

 x=1

 ```

 Our variables can be defined as some data-types. We can divide the data-types in two big categories:

 **Primitive.** These data-type are the fundamental ones they are **integer** (which defines all the integer numbers), **float** (which defines floating point numbers), **complex** (which defines complex numbers, with j as the imaginary part), **boolean** (which defines 0 [false] or 1 [true] values used for logical and boolean operations), **str** (which defines all the text types).

 Here a list of how to define every data-type seen above:

 ```python

 x=int(255)  #integer

 x=float(1.00)  #floating point

 w=complex(5+3j)  #complex

 x=bool(true) #boolean

 x=str('this is a string')  #text (or string)

 ```

> Note that this **is not** a necessary operation, in fact Python can
> use variables without assigning them a specific data-type.  Although
> is necessary in some cases.

#### Lists, Dictionaries

Using a variable we can store only 1 information at time, there are some structures in Python that allows us to store multiple information, these strcuctures are called **lists**, here is the syntax to create one

```python
list1=["item1", "item2", "item3"] #string list
intList=[1,2,3,4,5,6] #int list
boolList=[True, False, False] #bool list
mixed=["item",1,True] #lists can contain also mixed types
```  

> As you can se it's like creating a variable but we have to use the
> square brackets **[]** to define the elements separated them with the comma
> **,**  

A list has these 3 characteristics:

1. Ordered  
 ↳ Lists are ordered, that means that if you add an element it will be added at the end of our list
2. Changeable  
 ↳ This means that we can **add**, **change**, **remove** items from the list after creating it
3. Duplicates  
 ↳ Since lists have indexes we can have duplicated values  
In order to access items of a list we can use this syntax:

```python
list1[1] #access to the element in position 1 (2)
```

> Note that to count positions of the items we start from **0**, so the first item of the _intList_ will be ```intList[0]=>1```

#### Casting

A fatal operation in programming is **casting**, what does that mean? It means to force a data-type into another one, let me explain...
Imagine having a division between to float values and you want only to have the integer value of the quotient, here is how you do that!

 ```python
 x=float(250)
 y=float(256)
 div=int(x/y)

 ```

> Note that you **cannot** cast a data-type into any other one, for some
> data-types you need some **functions** (_like parsing_).

#### If, For & While  

**What if I want to make my program go in different paths based on some event?**
To do so we use **IF** conditions, if conditions are mathematical and logical expressions that return only two possible values:

 1. True (1)
 2. False (0)

Let's say we want to check what is the bigger number between 10 and 9, here  is the syntax:

```python
a=9
b=10
if(a>b):
  print("9 is grater than 10")
else
  print("10 is grater than 9")
```

> Note that in this case the outcome of the espression is "false" so the only code executed will be the one after the "else"

Here is a list of the operators we can use in the if clause:
| Mathematical | Logical |
|--------------|---------|
| `<` _(less than)_            | `and` _(returns true only if both are true)_ |
| `>` _(grater than)_        | `or` _(returns true if at least one is true)_ |
| `<=` _(less or euqal to)_        | `not` _(negates the boolean expression, if true becomes false)_ |
| `>=`  _(grater or equal to)_       |  |
| `==` _(equal to)_       |  |
| `!=` _(not equal to)_       |  |  

**If I have to repeat a small (or big) portion of code a certain numbers of times?**  
In order to do that we can use **FOR** loops that allows us to repeat portions of code a specific amount of times by specifying an index (i), here is the syntax:

```python
for i in range(100): #this loop prints the first 100 numbers
  print(i)
```  

You can also specify a range of values, like this:

```python
for i in range(50,100): #this loop prints the numbers from 50 to 100 
  print(i)
```  

**Lastly, if I don't know how many times i have to repeat my loop?**  
Possibly you will have a condition that will stop your loop, loops structured this way are called **WHILE** loops, here is thier syntax:  

```python
while(x>10):
  x+=1
  print(x)
```

#### Strings

#### Functions

#### Recursion

### Object Oriented programming

#### What is an object?

#### Object vs Instance

#### Classes

#### Inheritance

#### Methods

### Data structures and algorithms

#### Linked lists

#### Heaps, Stacks, Queues

#### Trees (and Binary-trees)

#### Sorting algorithms (Bubble-sort, merge-sort, insertion-sort)

### Graphic User Interface

### Frameworks

## Links

## Credits

The logo has been created by [EscuelaDevRock](https://giphy.com/devrock)

## Installation

For the installation I recommand this tutorial, made from [ProgrammingKnowledge](https://www.youtube.com/@ProgrammingKnowledge), [link to the video](https://www.youtube.com/watch?v=ZcP0Du4KFSU)
