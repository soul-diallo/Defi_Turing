# Triplet pythagoricien

def compute():
    somme_des_3_termes = 3600
    prodMax = 0
    for a in range(1, somme_des_3_termes + 1):
        for b in range(a + 1, somme_des_3_termes + 1):
            c = somme_des_3_termes - a - b
            if a * a + b * b == c * c:
                # It is now implied that b < c, because we have a > 0
                print(a,' ',b,' ',c)
                if a*b*c > prodMax :
                    prodMax = a*b*c
                #return str(a * b * c)
    return prodMax

if __name__ == "__main__":
    print(compute())
