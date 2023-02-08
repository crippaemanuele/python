#[EN] This file is used to tets the examples before uploading them in the repo 
#[IT] Questo file è usato per testare gli esempi prima di caricarli nella repo
#[ES] Este archivo se utiliza para tets los ejemplos antes de subirlos en el repo
#[DE] Diese Datei wird verwendet, um die Beispiele zu testen, bevor sie in das Repo hochgeladen werden
#[FR] Ce fichier est utilisé pour tester les exemples avant de les télécharger dans le dépôt

#For simplicity, the text of the exercises will be in English

#Exercise 1: "Write a program that determines the future value of your €1000 investment based on a 2.5% interest rate within 5 years of investment."
from math import sqrt


print("ESERCIZIO 1")
print("__________________________________________________________________________________________________________________________________________________")
tax=2.5/100
inv=1000
final=0
for i in range(5):
    final+=inv+inv*tax
    inv=final
print(f"The final value of the investment is {final} \n")

#Exercise 2: "Find the values of x: (x+1)(x-3)(x+11)=0"
print("ESERCIZIO 2")
print("__________________________________________________________________________________________________________________________________________________")
x1=1*-1
x2=-3*-1
x3=11*-1
print(f"L'equazione è verificata per x1={x1}, x2={x2}, x3={x3} \n")

#Exercise 3: "Calculate the sum of the first 10 elements of An=10+4n"
print("ESERCIZIO 3")
print("__________________________________________________________________________________________________________________________________________________")
sum=0
for i in range(10):
    sum += 10+(4*i)
print(f"La somma dei primi dieci numeri di An è {sum} \n")

#Exercise 4: "Calculate the distance between the given points: A(5,3) and B(3,-1)."
print("ESERCIZIO 4")
print("__________________________________________________________________________________________________________________________________________________")
Xa=5
Xb=3
Ya=3
Yb=-1
distance=sqrt(((Xb-Xa)**2)+((Yb-Ya))**2)
print(f"La distanza tra i punti A(5,3) e B(3,-1) è {distance} \n")

#Esercizio 5: "Scrivi un programma che calcoli il punto medio di due segmenti: A(1,5) e B(3,-2)."
print("ESERCIZIO 5")
print("__________________________________________________________________________________________________________________________________________________")
Xa=1
Xb=3
Ya=5
Yb=-2
Xm=(Xa+Xb)/2
Ym=(Ya+Yb)/2
print(f"Il punto medio tra A e B è M=({Xm};{Ym}) \n")

#Esercizio 6: "Calcolare la media geometrica dei seguenti numeri: 4, 3, 4.5, 5"
print("ESERCIZIO 6")
print("__________________________________________________________________________________________________________________________________________________")
mul=4*3*4.5*5
G_avg=pow(mul,1/4)
print(f"La media geometrica dei numeri dati è: {G_avg} \n")