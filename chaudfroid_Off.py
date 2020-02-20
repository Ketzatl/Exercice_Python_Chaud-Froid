# /usr/bin/python
# -*- coding:utf-8 -*
"""
Exercice Chaud Froid
Morgan Nott
Samuel Wroblewski

18 Novembre 2019
Python 3.6.8
"""
from random import randint,choice


# définition de constantes nécessaire au bon déroulement du programme.

MIN = 0
MAX = 100

# définition de la fonction de choix de difficulté, elle sera la première a être appellée et donc la première a être codée
# elle demande un chiffre a l'utilisateur, et retourne le nombre de tentative autorisé déterminée par l'énoncé.

def niveauDifficulte():
    essai = 0
    while essai not in [10,20,30] :
        get_difficult = input("Bonjour Maitre,\n si vous voulez faire une partie facile, tappez 1 \n si vous voulez faire une partie moyenne, tappez 2 \n si vous voulez faire une partie difficile, tappez 3 =>  ")
        

        if str(get_difficult) == "1" :
            print("vous avez choisis Facile \n")
            essai = 30
        elif str(get_difficult) == "2":
            print("vous avez choisis Moyen \n")
            essai = 20
        elif str(get_difficult) == "3":
            print("vous avez choisis difficile \n")
            essai = 10
        else:
            print("Lisez moi bien Maitre \n")
            essai = 0

    return essai
        


# définition de la fonction permettant a l'utilisateur de faire un choix.
# si la réponse n'est pas entre 0 et 100, l'utilisateur doit refaire un choix
# il y à actuellement un problème, lorsque l'on fait un mauvais choix, puis un bon, il retourne NONE
# solution faire une boucle ( ) / ou non conseillé, faire un return traitementRep() dans le else

def traitementRep():
    réponse = -1
    while MIN > réponse or réponse > MAX:
        réponse = int(input("Maitre, veuillez choisir un nombre entre 0 et 100, non inclus =>  "))
        if MIN > réponse or réponse > MAX :
            print("Ce nombre dépasse ma capacité de calcul, Maitre, veuillez rééssayer")
    if MIN <= réponse and réponse <= MAX:
            print("votre choix est le : " + str(réponse) + " Maitre.")
            return réponse
       

def chaudFroid(val,dist1,dist2):
    réponse = traitementRep()
    if val == réponse:
        return "trouve"
    elif abs(réponse-val) < dist1:
        print("vous êtes chaud, maitre")
        return "chaud"
    elif abs(réponse-val) > dist2:
        print("vous êtes froid, maitre")
        return "froid"
    else:
        print("vous êtes tiède, maitre")
        return "tiede"
        



# définition de la fonction permettant au programme de dire à l'utilisateur si il est froid, tiède ou chaud.
# la boucle s'arrête en fonction de la difficultée choisis par le joueur.
# cette fonction retourne true, si le joueur a gagné, False si il a perdu.

def jeu(nbEssai, dist1, dist2):
    val = randint(0,100)
    
    essai = nbEssai
    while essai > 0:
        temperature = chaudFroid(val,10,30)
        if (temperature in ["chaud" , "froid" , "tiede"]) and essai != 0:
            essai -= 1
            print("vous avez encore " + str(essai) +" essai, Maitre\n")
            
            
        elif temperature== "trouve":
            return True
    return False

"""
def chaudFroid(val, dist1, dist2):
    if val == traitementRep():
        return "trouve"
    elif abs(traitementRep()-val) < dist1:
        return "chaud"
    elif abs(traitementRep()-val) > dist2:
        return "froid"
    else:
        return "tiede"

       
        if val == traitementRep():
            return True
        elif abs(traitementRep()-val) < dist1:
            print("Vous êtes chaud, Maitre")
            nbEssai -=1
        elif abs(traitementRep()-val) > dist2:
            print("Vous êtes froid Maitre")
            nbEssai -=1
        else:
            print("Vous êtes tiède Maitre")
            nbEssai =-1
    return False
"""
def main():
    finPartie= jeu(niveauDifficulte(),10,30)
    if finPartie == False:
        print("Vous avez perdu")
    elif finPartie == True:
        print("Vous avez gagné")



main()
