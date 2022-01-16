"""Exo 1:
Écrire un programme qui détermine la valeur de la racine carrée d’un entier sans jamais utiliser la fonction racine carrée.
On procédera par approximation successive.
Prenons par exemple la racine carrée de N=10.
On teste la valeur 5.  5x5 = 25 résultat supérieur à 10.
Donc le nombre recherché sera compris entre 0 et 5
On teste 2,5. 2,5 x 2,5 = 6,25 qui est inférieur à 10.
Donc le nombre recherché sera compris entre 2,5 et 5.
On teste donc (2,5+5)/2= 3,75. 3,75x3,75 vaut 14,0625 donc plus grand que 10.
Le nombre recherché est donc entre 2,5 et 3,75.
On teste (2,5+3,75)/2  qui vaut 3,125. 3,125*3,125 vaut 9,765625.
Donc le nombre recherchée est entre 3,125 et 3,75. On teste (3,125+3,75)/2 etc.
On remarque qu’à chaque fois, on obtient deux nombres NBas et NHaut qui encadre la valeur de la racine carrée. L’intervalle entre ces deux nombres devient de plus en plus petit. On arrêtera les itérations du calcul lorsque la différence entre Nbas et NHaut sera plus petit que 0,001."""


n= int(input("saisissez un nombre pour connaitre sa racine carré:> "))
precision = 0.001
sup = n
inf = 0
i = 0

while i:
    i+=1
    sup = 0.5 * inf
    inf = 0.5*(sup + n / sup)
    
    if (abs(inf - sup) < precision): break
    
    
print("La racine carré est de", n, "est",inf)






    

    
    
