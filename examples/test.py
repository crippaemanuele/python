#[EN] This file is used to tets the examples before uploading them in the repo 
#[IT] Questo file è usato per testare gli esempi prima di caricarli nella repo
#[ES] Este archivo se utiliza para tets los ejemplos antes de subirlos en el repo
#[DE] Diese Datei wird verwendet, um die Beispiele zu testen, bevor sie in das Repo hochgeladen werden
#[FR] Ce fichier est utilisé pour tester les exemples avant de les télécharger dans le dépôt

#For simplicity, the text of the exercises will be in English

#Exercise 1: "Write a program that determines the future value of your €1000 investment based on a 2.5% interest rate within 5 years of investment."
print("__________________________________________________________________________________________________________________________________________________________________")
tax=0.025
inv=1000
final=0
for i in range(5):
    final+=inv+inv*tax
    inv=final
print(f"The final value of the investment is {final}")