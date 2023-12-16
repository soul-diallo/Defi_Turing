# Le rectangle-6400 
#Dans un rectangle de longueur 4 et de largeur 3, on peut dessiner 12 carrés de côté 1, 6 carrés de côté 2 et 2 carrés de côté 3. Au total, on peut dessiner 20 carrés. Nous dirons que c'est un rectangle-20.
#Quelle est l'aire du rectangle-6400 dont la forme est la plus proche d'un carré ?
#N.B. Les dimensions sont entières tant pour le rectangle que pour les carrés.

for x in range (1,100):
    for y in range (1,100):
        d = abs(x-y)
        nb =d*x*(x+1)/2+x*(x+1)*(2*x+1)/6
        if(nb == 6400):
            print("x="+str(x)+" y="+str(y)+" Aire = "+str(x*y))

# x=15 y=58 Aire = 870
# x=24 y=19 Aire = 456
# x=24 y=29 Aire = 696