# Trouver la somme des nombres premiers compris entre 1 et 10'000'000.
import math


def isPrime(n):
    if n <= 3:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


somme = 0
nbr = bool
for i in range(3, 10000000, 2):
    nbr = isPrime(i)
    if nbr == True:
        somme = somme + i
print(somme + 2)
