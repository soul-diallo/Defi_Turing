n = 2013

for i in range(1, n):
    n = n * i
print(n)

b = sum([int(c) for c in str(n)])
print(b)
