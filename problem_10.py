# Trouver la somme des nombres premiers compris entre 1 et 10'000'000.
import math


def isPrime(n):
    flag = False
    if n <= 3:
        return True
    for i in range(2, int(n**0.5)+1, 2):
        if n % i != 0:
            flag = True
        else:
            return False
    return flag


somme = 0
for i in range(2,10):
    if isPrime(i):

        somme = somme + i
        print(i)
        #print(somme)
print(somme)
