def has_distinct_digits(year):
    """Vérifie si une année est composée de chiffres tous différents"""
    return len(str(year)) == len(set(str(year)))

def analyze_years(start_year, end_year):
    """Analyse les années pour trouver celles avec des chiffres différents
    et la plus longue période entre deux telles années"""

    # Liste des années avec chiffres différents
    distinct_years = []

    # Trouver toutes les années avec des chiffres différents
    for year in range(start_year, end_year + 1):
        if has_distinct_digits(year):
            distinct_years.append(year)

    # Calculer la plus longue période entre deux années consécutives
    max_gap = 0
    for i in range(1, len(distinct_years)):
        gap = distinct_years[i] - distinct_years[i-1]
        max_gap = max(max_gap, gap)

    return {
        'count': len(distinct_years),
        'max_gap': max_gap,
        'years': distinct_years
    }

# Analyser les années de 1 à 2013
result = analyze_years(1, 2013)

# Calculer le produit des résultats
product = result['count'] * result['max_gap']

print(f"Nombre d'années avec chiffres différents : {result['count']}")
print(f"Plus longue période : {result['max_gap']} ans")
print(f"Produit des résultats : {product}")

# Pour vérification, afficher quelques années avec la plus longue période
for i in range(len(result['years'])-1):
    gap = result['years'][i+1] - result['years'][i]
    if gap == result['max_gap']:
        print(f"\nPériode la plus longue trouvée entre {result['years'][i]} et {result['years'][i+1]}")