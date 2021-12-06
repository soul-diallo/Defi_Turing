# Miroir d'un nombre

def miroir(n):
    nbre = str(n)
    nbre_miroir = ""
    for i in range(len(nbre)):
        nbre_miroir += nbre[len(nbre) - 1 - i]

    return int(nbre_miroir)


n = 10000000
for i in range(1000000,n // 4):
    if miroir(i) == 4 * i:
        print(i)
