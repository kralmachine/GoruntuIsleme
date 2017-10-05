from random import randint
import numpy as np
import timeit

def listeDondur(size):
    temp = []
    for i in range(int(size)):
        temp.append(randint(0, 9))
    return temp

def arttir(liste, n):
    temp = []
    for i in range(len(liste)):
        temp.append(liste[i] + n)
    return temp

liste_boyut = input("Liste boyutunu giriniz: ")
liste1 = listeDondur(liste_boyut)
print("Birinci listemiz: {} ".format(liste1))

n = int(input("Diziye kaç ekleyelim: "))

liste_arttirilmis = arttir(liste1, n)

print(liste_arttirilmis)


# liste_numpy = np.array(listeDondur(liste_boyut))
# print("Numpy dizisi: {} ".format(liste_numpy))
#
# n = input("Diziye kaç ekleyelim: ")
# print("Diziye {} eklenmiş hali: {} ".format(n, liste_numpy + int(n)))
