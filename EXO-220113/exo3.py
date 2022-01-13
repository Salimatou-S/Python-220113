"""Exo 3
Ecrire un programme qui réalise la saisie par l’utilisateur d’un nombre et qui indique si ce nombre est divisible par 3 ou pas.
On pourra par exemple utiliser le modulo (%)"""

n=int(input("Rentrez un nombre svp : >"))
if n%3 == 0:
    print("Ce nombre est divisible par 3")
else:
    print("Ce nombre n'est pas divisible par 3")