"""Exo 1
Ecrire un programme qui demande à l’utilisateur 3 nombres entiers positifs et plus petits que 40000, puis effectue la moyenne de ces trois nombres et affiche la valeur de cette moyenne.
Le code n'effectuera pas de vérification concernant l'intervalle de 0 à 40000.""" 

n = [int(i) for i in input("Entre 3 nombres entiers positifs compris entre 1 et 40000>").split()]
print(n)
moyenne= float(sum(n)//3) 
print(moyenne)
