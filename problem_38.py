def next_conway_term(term):
    """Calcule le terme suivant de la suite de Conway"""
    result = ""
    current_digit = term[0]
    count = 1

    for digit in term[1:]:
        if digit == current_digit:
            count += 1
        else:
            result += str(count) + current_digit
            current_digit = digit
            count = 1

    result += str(count) + current_digit
    return result

def count_ones(term):
    """Compte le nombre de '1' dans un terme"""
    return term.count('1')

# Calcul de T50 avec T1 = 2
term = "2"
for i in range(49):  # 49 itérations pour aller de T1 à T50
    term = next_conway_term(term)

# Compte le nombre de 1 dans T50
result = count_ones(term)
print(f"Le nombre de 1 dans T50 est : {result}")