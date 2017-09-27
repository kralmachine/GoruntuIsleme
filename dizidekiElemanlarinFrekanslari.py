from random import randint
from moduller import getFrequencyOfElements

dizi = []
dnum = input("Dizinin eleman sayısını giriniz: ")
drange = input("Dizinin ust sınırını giriniz: ")

for i in range(0, int(dnum)):
    dizi.append(randint(0, int(drange)))

print("Oluşturulmuş dizimiz : {} ".format(dizi))

dizi.sort()

print("Sıralanmış hali: {} ".format(dizi))

print("Dizinin frekansı: {}".format(getFrequencyOfElements(dizi)))
