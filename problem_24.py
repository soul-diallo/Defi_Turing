from itertools import permutations

lst = [''.join(p) for p in permutations("0123456789")]
print(lst[1999999])

