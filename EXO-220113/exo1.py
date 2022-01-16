"""Exo 1
Ecrire un programme qui demande à l’utilisateur 3 nombres entiers positifs et plus petits que 40000, puis effectue la moyenne de ces trois nombres et affiche la valeur de cette moyenne.
Le code n'effectuera pas de vérification concernant l'intervalle de 0 à 40000.""" 

print("Saisir 3 nombres entiers positifs et plus petits que 40000 \n")
nombre1 = int(input('Tapez la valeur de la variable1 : '))
nombre2 = int(input('Tapez la valeur de la variable2 : '))
nombre3 = int(input('Tapez la valeur de la variable3 : '))

print("voici les valeurs de variable1, de variable2 et variable3\n");
print("première variable = ", nombre1)
print("deuxième variable = ", nombre2)
print("troisième variable = ", nombre3)

if nombre1 < 0 or nombre2 < 0 or nombre3 < 0:
    print("Une ou plusieurs des valeurs entrées est inférieure à 0. Veuillez rentrer une autre valeur.") 
    
elif nombre1 > 40000 or nombre2 > 40000 or nombre3 > 40000:
    print("Une ou plusieurs des valeurs entrées est superieure à 40000. Veuillez rentrer une autre valeur.") 

else:
    total = (nombre1 + nombre2 + nombre3)
    print("Total = ", total)

    resultat = total / 3
    print("La moyenne des valeurs entrées est: ", resultat)
