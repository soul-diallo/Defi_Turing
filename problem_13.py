# Le plus petit carré palindrome ayant un nombre pair de chiffres est 698896 = 8362².
#
# Quel est le carré palindrome suivant ?

def isPalindrom(stri):
    for i in range(len(stri)):
        if stri[i] == stri[len(stri)-1 - i]:
            pass
        else:
            return False
    return True

n = 837
while True:
    produit = n**2
    if isPalindrom(str(produit)) and len(str(produit)) % 2 ==0:
        break
    else: n+=1

print(produit,"--",n)
