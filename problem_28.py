cote = 3
first_elem= 1
last_elem = 1
somme = 1
chiffre = 1
n = 1

while cote != 2015:
    for i in range(4):
        chiffre = chiffre + (cote - 1)
        somme += chiffre

    cote += 2
    last_elem = chiffre
    first_elem = last_elem + (cote - 1)

print(somme)