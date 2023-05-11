import random 

montant=int(input("quel est le montant à dépenser?"))
mise=int(input("quel est votre mise?"))
while (mise>montant):
    print("Erreur, vous ne pouvez pas avoir une mise supérieur à votre montant !")
    montant=int(input("quel est le montant à dépenser?"))
    mise=int(input("quel est votre mise?"))

nbaleatoire=random.randint(1,6)
compteur=1
entier=int(input("devine un nombre entre 1 et 5 et tu as 3 essais : ")) 
while (entier>5 or entier<1):
    print("Erreur, Il faut entrer un nombre entre 1 et 5 :")
    entier=int(input("devine un nombre entre 1 et 5 et tu as 3 essais :")) 
     
    
while entier!=nbaleatoire and compteur<3 :
    mise=int(input("Faux, quel est votre nouvelle mise?"))
    entier=int(input("Devine un nombre entre 1 et 3 : "))
    compteur+=1 
    while (entier>5 or entier<1):
        print("Erreur , Il faut entrer un nombre entre 1 et 5 : ")
        entier=int(input("devine un nombre entre 1 et 5 et tu as 3 essais :")) 

if (entier!=nbaleatoire and compteur==3):
    recompense1=int(montant-mise)
    print("game over,tu as perdu", mise, "tu repars avec : ", recompense1)
    reponse=str(input("Voulez-vous continuer à jouer oui ou non ? "))
    while (reponse=="oui"):
        import random 

        montant=int(input("quel est le montant à dépenser?"))
        mise=int(input("quel est votre mise?"))
        while (mise>montant):
            print("Erreur, vous ne pouvez pas avoir une mise supérieur à votre montant !")
            montant=int(input("quel est le montant à dépenser?"))
            mise=int(input("quel est votre mise?"))

        nbaleatoire=random.randint(1,6)
        compteur=1
        entier=int(input("devine un nombre entre 1 et 5 et tu as 3 essais : ")) 
        while (entier>5 or entier<1):
            print("Erreur, Il faut entrer un nombre entre 1 et 5 :")
            entier=int(input("devine un nombre entre 1 et 5 et tu as 3 essais :")) 
     
    
        while entier!=nbaleatoire and compteur<3 :
            mise=int(input("Faux, quel est votre nouvelle mise?"))
            entier=int(input("Devine un nombre entre 1 et 3 : "))
            compteur+=1 
            while (entier>5 or entier<1):
                print("Erreur , Il faut entrer un nombre entre 1 et 5 : ")
                entier=int(input("devine un nombre entre 1 et 5 et tu as 3 essais :")) 

        if (entier!=nbaleatoire and compteur==3):
            recompense1=int(montant-mise)
            print("game over,tu as perdu", mise, "tu repars avec : ", recompense1)
            reponse=str(input("Voulez-vous continuer à jouer oui ou non ? "))
            
        elif (entier==nbaleatoire and compteur==3 ):
            mise1=mise*5
            total=mise1+montant
            print("victoire, tu as deviné le nombre en " , compteur , "tu as gagné  :" , mise1 ,"et tu repars avec : " ,total)
            break

        elif (entier==nbaleatoire):
            mise1=mise*5
            total=mise1+montant
            print("victoire, tu as deviné le nombre en " , compteur , "coups et tu as gagné  :" , mise1 ,"tu repars avec : " ,total)
            break
        


 
elif (entier==nbaleatoire and compteur==3 ):
    mise1=mise*5
    total=mise1+montant
    print("victoire, tu as deviné le nombre en " , compteur , "tu as gagné  :" , mise1 ,"et tu repars avec : " ,total)

elif (entier==nbaleatoire):
    mise1=mise*5
    total=mise1+montant
    print("victoire, tu as deviné le nombre en " , compteur , "coups et tu as gagné  :" , mise1 ,"tu repars avec : " ,total)




