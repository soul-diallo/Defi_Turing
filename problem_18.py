def get_proper_divisors(n):
    """Retourne la liste des diviseurs propres d'un nombre"""
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # éviter de compter deux fois la racine carrée
                divisors.append(n // i)
    return divisors

def is_abundant(n):
    """Détermine si un nombre est abondant"""
    return sum(get_proper_divisors(n)) > n

def find_abundant_numbers(limit):
    """Trouve tous les nombres abondants jusqu'à une limite"""
    return [n for n in range(1, limit + 1) if is_abundant(n)]

def find_non_abundant_sums(limit):
    """Trouve les nombres qui ne peuvent pas être écrits comme somme de deux nombres abondants"""
    abundant_numbers = find_abundant_numbers(limit)
    abundant_sums = set()

    # Générer toutes les sommes possibles de deux nombres abondants
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sum_abundant = abundant_numbers[i] + abundant_numbers[j]
            if sum_abundant <= limit:
                abundant_sums.add(sum_abundant)

    # Trouver les nombres qui ne sont pas dans l'ensemble des sommes
    non_abundant_sums = []
    for n in range(1, limit + 1):
        if n not in abundant_sums:
            non_abundant_sums.append(n)

    return non_abundant_sums

# Calcul pour la limite 2013
limit = 2013
result = sum(find_non_abundant_sums(limit))
print(f"La somme des nombres non exprimables comme somme de deux nombres abondants jusqu'à {limit} est : {result}")