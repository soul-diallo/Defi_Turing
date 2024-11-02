def count_combinations():
    # Conversion en centimes pour travailler avec des entiers
    target = 1000  # 10 francs = 1000 centimes
    coins = [5, 10, 20, 50, 100, 200, 500]  # Valeurs en centimes

    # Tableau pour stocker les résultats intermédiaires
    # dp[i] représente le nombre de façons d'obtenir i centimes
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: une façon d'obtenir 0 centime

    # Pour chaque pièce
    for coin in coins:
        # Pour chaque montant de 'coin' jusqu'à target
        for amount in range(coin, target + 1):
            # Ajouter le nombre de combinaisons possibles
            # en utilisant la pièce courante
            dp[amount] += dp[amount - coin]

    return dp[target]


# Calculer le résultat
result = count_combinations()
print(f"Il y a {result} façons différentes d'obtenir 10 francs avec des pièces suisses.")


# Vérification avec quelques exemples
def find_some_combinations(target_cents, coins, max_combinations=5):
    """Trouve quelques combinaisons possibles pour vérification"""
    combinations = []

    def backtrack(remaining, current_combination, start_idx):
        if remaining == 0:
            combinations.append(current_combination.copy())
            return
        if remaining < 0 or len(combinations) >= max_combinations:
            return

        for i in range(start_idx, len(coins)):
            current_combination.append(coins[i])
            backtrack(remaining - coins[i], current_combination, i)
            current_combination.pop()

    backtrack(target_cents, [], 0)
    return combinations


# Afficher quelques exemples de combinaisons pour vérification
coins = [500, 200, 100, 50, 20, 10, 5]  # en centimes
examples = find_some_combinations(1000, coins)

print("\nQuelques exemples de combinaisons :")
for combo in examples:
    # Convertir en format lisible
    formatted = []
    for cent in sorted(combo, reverse=True):
        if cent >= 100:
            formatted.append(f"{cent // 100} fr")
        else:
            formatted.append(f"{cent} ct")
    print(" + ".join(formatted))
