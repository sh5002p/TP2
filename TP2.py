# Permuter les valeurs de deux variables
def permuter(x, y):
    x, y = y, x
    return x, y

# Entrer les valeurs de x et y
x = int(input("Entrez x: "))
y = int(input("Entrez y: "))

# Afficher les valeurs avant la permutation
print("Avant permutation:")
print("x :", x)
print("y :", y)
ex2:# Demander l'âge de l'utilisateur
print("Donnez votre age :")

# Lire la réponse de l'utilisateur et l'enregistrer dans une variable age de type entier
age = int(input())

# Calculer l'année de naissance (à un an près) de l'utilisateur et l'enregistrer dans la variable
annee = 2022 - age

# Afficher l'année de naissance ainsi calculée
print("Votre annee de naissance est :", annee)
ex3:
# Demander à l'utilisateur d'entrer trois nombres
print("Entrez la premiere valeur :")
a = int(input())
print("Entrez la deuxieme valeur :")
b = int(input())
print("Entrez la troisieme valeur :")
c = int(input())

# Afficher les valeurs entrees
print("Les valeurs entrees sont : a =", a, ", b =", b, "et c =", c)

# Permuter les valeurs
a, b, c = c, a, b

# Afficher les valeurs permutees
print("Permutation: a ==> b, b ==> c, c ==> a")
print("Les valeurs permutees sont : a =", a, ", b =", b, "et c =", c)
ex4:
# Constante indiquant le nombre de personnes pour lesquelles est conçue la recette de base
BASE = 4

# Variables représentant les quantités d'ingrédients nécessaires pour BASE personnes
fromage = 800.0
eau = 2.0
ail = 2.0
pain = 400.0

# Demander à l'utilisateur d'entrer le nombre de convives pour lequel on veut préparer la recette
print("Entrez le nombre de personne(s) conviées à la fondue :")
nbConvives = int(input())

# Adapter les quantités de chaque ingrédient en faisant une règle de trois
nouveauFromage = fromage * nbConvives / BASE
nouvelleEau = eau * nbConvives / BASE
nouveauAil = ail * nbConvives / BASE
nouveauPain = pain * nbConvives / BASE

# Afficher la recette pour le nombre de convives voulus
print("Pour faire une fondue fribourgeoise pour", nbConvives, "personne(s), il vous faut :")
print("-", nouveauFromage, "gr de fromage")
print("-", nouvelleEau, "dl d'eau")
print("-", nouveauAil, "gousse(s) d'ail")
print("-", nouveauPain, "gr de pain")
ex5:
nombre = int(input("Entrez un nombre entier: "))

if nombre > 0:
    print("Le nombre est positif.")
else:
    print("Le nombre est négatif.")

if nombre == 0:
    print("Le nombre est zéro.")
else:
    if nombre % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")
ex6:
import random

nombre = random.randint(0, 100)

if nombre < 50:
    print("Pile !")
else:
    print("Face !")
ex7:
import random

nombre = random.randint(0, 99)

if nombre < 66:
    print("Pile !")
else:
    print("Face !")

ex8:
def est_dans_intervalle(x):
    return (x > 2 and x < 10) or (x > 0 and x < 1) or (x > -10 and x < -2)

x = float(input("Entrez un nombre décimal : "))

if est_dans_intervalle(x):
    print("x appartient à I")
else:
    print("x n'appartient pas à I")
