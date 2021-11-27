"""""
def is_prime(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors

#Tri des diviseurs dans l'ordre décroissant
divs = divisors(20130101)
divs.sort(reverse=True)
#Lit un par un les diviseurs et teste s'ils sont premiers.
#Si c'est le cas, on affiche le diviseur et sort de la boucle.
for i in divs:
    if is_prime(i):
        print(i)
        break
"""


number = 20130101
factor = 2
while number > factor:
    if (number % factor == 0):
        number = number / factor
        factor = 2
    else:
        factor += 1

print(factor)