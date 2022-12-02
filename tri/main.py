
import random

tab2 = [64, 86, 36, 166, 10, 748, 2, 13, 245, 2]
tab = [64, 86, 36, 166, 10, 748, 2, 13, 245, 2]



def insertSort(A):
    compteurComparaison = 0
    compteurEchange = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        compteurEchange += 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
            compteurComparaison += 1
            compteurEchange += 3
        A[j + 1] = key
    return compteurEchange + compteurComparaison




def selecSort(A):
    compteurEchange2 = 0
    compteurComparaison2 = 0
    for i in range(len(A)):
        min = i
        compteurEchange2 += 1
        for j in range(i + 1, len(A)):
            compteurComparaison2 += 1
            if A[min] > A[j]:
                min = j
                compteurEchange2 += 3
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
    return compteurEchange2 + compteurComparaison2


def bubbleSort(A):
    compteurEchange = 0
    compteurComparaison = 0
    for k in range(len(A) - 1):
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                compteurEchange += 3
                compteurComparaison += 1
    return compteurEchange + compteurComparaison

print(bubbleSort(tab))

def tri_bulle(liste):
    echange = True
    comparaison = 0
    echanges = 0
    while echange == True:
        comparaison += 1
        echange = False
        echanges += 3
        k = 0
        for i in range(0, len(liste)-1 - k):
            if liste[i] > liste[i+1]:
                echange = True
                liste[i], liste[i+1] = liste[i+1], liste[i]
                echanges += 3
            comparaison += 1
    return comparaison + echanges

print(tri_bulle(tab2))

def stat(min, max, step, nbr):
    for i in range(min, max + step, step):
        acc = 0
        acc2 = 0
        acc3 = 0
        acc4 = 0
        for n in range(nbr):
            ls = [random.randint(0, 100) for _ in range(i)]
            ls2 = [random.randint(0, 100) for _ in range(i)]
            ls3 = [random.randint(0, 100) for _ in range(i)]
            ls4 = [random.randint(0, 100) for _ in range(i)]
        acc += bubbleSort(ls)
        acc2 += selecSort(ls2)
        acc3 += insertSort(ls3)
        acc4 += tri_bulle(ls4)
        print("Bubble opti sort: " + str((i, acc / nbr)))
        print("Selection sort: " + str((i, acc2 / nbr)))
        print("Insert sort: " + str((i, acc3 / nbr)))
        print("Bubble sort: " + str((i, acc4 / nbr)))


stat(10, 20, 5, 10)

"""
def triselection
i,j: entier
tmp,small : entier
t: tableau n
Début
   Pour i de 1 à n-1 faire
     small <- i
     Pour j de i+1 à n faire
          Si t[j] < t[small] alors
                small <- j
          Fin si
     Fin pour
     tmp <- t[small]
     t[small] <- t[i]
     t[i] <- tmp
   Fin pour
FIN 

Def tribulleopti
    k: entier
    tmp: entier
    Pour I de n à 2 faire
        Pour k de 1 à i-1 faire
            Si tab[k] > tab[k+1] alors
                tmp <- tab[k]
                tab[k] <- tab[k+1]
                tab[k+1] <- tmp
            Fin si
        Fin pour
    Fin pour
Fin


DEBUT tri_bulle (parametre tab: tableau)
    variable n <- longueur de tab
    POUR i de 0 à n FAIRE
        POUR j de 0 à n-i-1 FAIRE
            SI tab[j] > tab[j+1] ALORS
                ECHANGER DE PLACE tab[j] et tab[j+1]
    RETOURNER tab
"""


