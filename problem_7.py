from pip._vendor.urllib3.connectionpool import xrange


def eratosthene(n,lim):
    if n < 2:
        return []
    n += 1
    tableau = [False, False] + [True] * (n - 2)
    tableau[2::2] = [False] * ((n - 2) // 2 + n % 2) # suppression des nb pairs
    premiers = [2] # initialisation du tableau des nb 1ers (2 est 1er)
    racine = int(n ** 0.5)
    racine = racine + [1, 0][racine % 2] # pour que racine soit impair
    for i in xrange(3, racine + 1, 2):
        if tableau[i]:
            # on enregistre le nouveau nb 1er
            premiers.append(i)
            # on élimine i et ses multiples
            tableau[i::i] = [False] * ((n - i) // i + int((n - i) % i > 0))
    for i in xrange(racine, n, 2):
        if tableau[i]:
            # on enregistre le nouveau nb 1er (pas de multiples à supprimer
            premiers.append(i)
    rang = premiers[lim]
    total = len(premiers)
    print(rang)
    print(total)
    #print(premiers)


print(eratosthene(100000000, 23455))

