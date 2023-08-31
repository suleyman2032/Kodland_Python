import random
sifre_kar="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzun = int(input("şifre uzunlunu girin:"))
sifre = ""
for i in range(uzun):
    sifre += random.choice(sifre_kar)   
print(sifre)