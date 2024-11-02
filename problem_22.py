def get_digits(n):
    """Retourne un tuple trié des chiffres d'un nombre"""
    return tuple(sorted(str(n)))

def is_six_digits(n):
    """Vérifie si un nombre a exactement 6 chiffres"""
    return 100000 <= n <= 999999

def are_anagrams(n1, n2):
    """Vérifie si deux nombres sont des anagrammes"""
    return get_digits(n1) == get_digits(n2)

def find_special_numbers():
    """Trouve les deux nombres spéciaux"""
    # On cherche des nombres à 6 chiffres
    results = []

    # Pour optimiser, on peut commencer à 100000/8 car n*8 doit avoir 6 chiffres
    start = 100000 // 8  # environ 12500
    end = 999999 // 8    # environ 124999

    # Stocke les nombres candidats qui vérifient la première condition (×8)
    candidates = []

    # Première passe : trouver les nombres dont le ×8 est une anagramme
    for n in range(start, end + 1):
        n8 = n * 8
        if is_six_digits(n) and is_six_digits(n8):
            if get_digits(n) == get_digits(n8):
                candidates.append(n)

    # Deuxième passe : parmi les candidats, trouver les paires d'anagrammes
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            if are_anagrams(candidates[i], candidates[j]):
                results.append((candidates[i], candidates[j]))

    return results

# Trouver les nombres
results = find_special_numbers()

# Afficher les résultats
for pair in results:
    print(f"\nPremier nombre : {pair[0]}")
    print(f"× 8 = {pair[0] * 8}")
    print(f"Deuxième nombre : {pair[1]}")
    print(f"× 8 = {pair[1] * 8}")
    print(f"Somme : {pair[0] + pair[1]}")