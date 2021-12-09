# Quelle est la valeur du premier nombre triangulaire à avoir plus de mille diviseurs ?

def affichageNbreNaturel(n):
    nbr = 0
    for i in range(1, n + 1):
        for j in range(i):
            nbr += 1
        print(nbr, end=" ")


def getNbFactors(n):

    nbFacteurs = 0
    for i in range(1, int((n**0.5) + 1)):
        if n % i == 0:
            nbFacteurs+=1

    return nbFacteurs*2

# affichageNbreNaturel(3)
nbFactors = 0
while nbFactors <= 5:
    nbr = 0
    i = 1
    while i>=1:
        for j in range (i):
            nbr +=1
        i+=1
        nbFactors = getNbFactors(nbr)
        if nbFactors >1000:
            break
print(nbr)