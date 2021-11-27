nb4 = 10
nb3 = 10

for nb4 in range (10000):
    for nb3 in range (1000):
        n = nb4 * nb3
        nn = n
        r = 0

        while (nn>0):
            u = nn%10
            r = r*10 + u
            nn = nn//10
            if n == r:
                if n>9000000:
                    print(n, "--")

        nb3 = nb3 + 1
    nb4 = nb4 + 1
