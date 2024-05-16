from random import*
from jeu.module_toutes_les_gares import* #dans ce module, il y a la variable
#ligne_dico qui stocke toutes les lignes et leurs gares respectives sous forme d'une
#liste de dictionnaire, chaque clef est le nom d'une ligne, chaque valeur est une
#liste de chaine de caratère, et chaque chaine est une gare traversé par la ligne
from time import*
import os
def jeu_des_lignes_():
    gare_selectionne=randint(0,len(ligne_dico)-1) #pour générer un entier aléatoirement, entier qui servira à cibler une gare car chaque dico
    # de la liste ont pour seul clef le nom de la gare. Donc ce nombre aléatoire renverra nécessairement vers la gare,
    #  qui est la clef du dico

    #cle_jeue et variable_reponse sont déclarées en global pour pouvoir récupérer la clef, soit le nom de la gare
    #et la valeur de la clef, soit la liste des lignes traversées par la gare

    cle_jeu=None
    valeur_reponse=[]  
    for cle,valeur in ligne_dico[gare_selectionne].items():
        cle_jeu=cle
        valeur_reponse=valeur



    # variable pour connaitre le nombre de réponse à saisir 


    #debut du jeu :

    # fonction affichage début
    print("Bonjour, Bienvenue dans le jeu : devine la ligne ! \n Le jeu est simple :",
          " Nous allons donnez le nom d'une ligne, il faudra donner les gares qu'elle traverse \n  ",
          "Bien, évidement, vous avez seulement 5 minutes pour toutes le donées, alors dépéchez-vous !"
          "Bonne chance !")
    print("Quelles  sont les gares que  traversent la ligne du : ",cle_jeu," ?")
    print("Ecrivez explicitement le nom des gares")


    # fonction algo coeur du jeu 
        # fonction initialisation

    tour=0 #variable utilisé dans la boucle du jeu pour éviter qu'il n'ait trop de réponse rentré par l'utilisateur
    MAXIMUM=50 #nombre maximal de réponse autorisé
    DUREE_MAX = 300  # 5 minutes de temps de jeu maximum
    debut = time()
    temps_ecoule = time() - debut #pour calculer l'écoulement du temps
    # print("Vous ne pourrez pas rentrer au dela de", 5-tour, "réponses")
    # reponse=input("Ecrivez une réponse. \n Tapez STOP pour arrêter de réponse")
    # reponse.upper() #normalisation des réponses en majuscule, donc cette ligne sert à mettre en majuscule la réponse rentrée
    # liste_reponse=[]
    # liste_reponse.append(reponse)



    print("Vous ne pourrez pas rentrer au dela de", MAXIMUM-tour, "réponses")

    #répétition du jeu jusqu'à ce que le joueur arrête de jouer ou qu'on n'ait atteint le nombre maximum de lignes enregistré dans 
    # le dico g.ligne_dico
    liste_reponse=[]
    reponse=None
        # fonction saisi utilisateur
    
    while (reponse!="STOP" and tour<MAXIMUM and temps_ecoule<=DUREE_MAX  ):#and time<2min 
        temps_ecoule = time() - debut
        if reponse!="STOP":
            reponse=input("Ecrivez une nouvelle réponse. \n Tapez STOP pour arrêter de réponse \n")
            reponse.upper() 
            liste_reponse.append(reponse)
            tour+=1
            print("Vous ne pourrez pas rentrer au dela de", MAXIMUM-tour, "réponses")

        # fonction supprimer stop
    if liste_reponse[-1]=='STOP' :
        del liste_reponse[-1] #étant donné que lorsque l'utilisateeur rentrait stop, cela rentrait dans cette liste, 
    #il a fallu supprimer STOP de la liste de la réponse
        # fonction vérification des donées
    taille_reponse=len(liste_reponse) #sera comparé avece la future taille de la liste de réponse, qui perdra un élément si 
    #l'élément correspond à la liste valeur_reponse

    for i in range (len(liste_reponse)-1):
        essaie=liste_reponse[i]
        for j in range (len(valeur_reponse)-1):
            if essaie==valeur_reponse[j]: #condition qui dit que si un élément de la liste liste_reponse correspond à un élément de la 
                #liste valeur_reponse, alors supprimer l'élément de la liste liste_reponse 
                del liste_reponse[i-1]


        # fonction des réponses


    if temps_ecoule==DUREE_MAX:
        print("Dommage, vous avez dépassez le temps imparti \n Voyons ensemble les réponses que vous avez donée : ")
        if len(liste_reponse)==0 and tour>1 : #donc si la la liste liste_reponse une fois la boucle ci-dessus a été faite est vide, alors 
                              #nécessairement, tous les éléments de réponses sont bon. Cela se fait grace à la varible taille_liste, qui stockait 
                              # la taile de la liste liste_reponse avant la boucle ci-dessus 

            print("Bravo, vous avez donnez la bonne réponse : \n")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])

        elif len(liste_reponse)==taille_reponse:  #à l'inverse, si elle n'a pas changé de taille par rapport à son ancienne taille, alors aucune 
                                                  #des réponses rentrés ne sont bonnes

            print("Dommage, vous n'avez pas donnée de bonne réponse...\n Voici la(es) réponse(s) qu'il fallait : \n")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])


        else : #dernier cas : la liste ne vaut ni taille_reponse, ni 0. Alors, certains éléments sont bons, mais d'autres mauvais 

            print("Bravo, vous avez donnez comme bonne réponse : \n")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])
            print("Cependant, vous avez oublier comme réponse réponse : \n")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])
    elif  0<temps_ecoule<DUREE_MAX:
        print("Bien joué ! Vous avez réussi à donner tout ce que vous avez pu. \n Voyons ensemble vos réponses : \n" "J'espère que vous avez pas triché")
        if len(liste_reponse)==0 and tour>1 : 

            print("Bravo, vous avez donnez la bonne réponse : \n")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])

        elif len(liste_reponse)==taille_reponse:  

            print("Dommage, vous n'avez pas donnée de bonne réponse...\n Voici la(es) réponse(s) qu'il fallait : \n")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])



        else : 

            print("Bravo, vous avez donnez comme bonne réponse : \n")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])
            print("Cependant, vous avez oublier comme réponse réponse : \n")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])
    else:
        print("Bien joué ! Vous avez réussi à donner tout ce que vous avez pu. \n Voyons ensemble vos réponses : \n")
        if len(liste_reponse)==0 and tour>1 : 

            print("Bravo, vous avez donnez la bonne réponse : \n")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])

        elif len(liste_reponse)==taille_reponse:  

            print("Dommage, vous n'avez pas donnée de bonne réponse...\n Voici la(es) réponse(s) qu'il fallait : \n")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])



        else : 

            print("Bravo, vous avez donnez comme bonne réponse : \n")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])
            print("Cependant, vous avez oublier comme réponse réponse : \n")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])
def jeuDesert():
    # affichage du début
    print("Vous voici dans le jeu : desert \n Le jeu est simple : \n :\
        Vous devez devinez si une ligne posséde bien la gare.",
        "Par exemple s'il est demandé est que la ligne 6 désert bien la gare Louis-Jean",
        " vous devez répondre oui ou non \n \
        Vous aurez 10 questions et à la fin, une note sur 10 vous sera donné. \n \
        Pour chaque question, vous n'aurez que 30 secondes pour répondre. \n",
        "Bonne chance !!")
    # fonction pour stocker toutes les gares et toutes les lignes dans des liste
    lignesIleDeFrance = []
    for i in range(len(ligne_dico)-1):
        for ligne in ligne_dico[i].values():
            for j in range(len(ligne)-1):
                if ligne[j] not in lignesIleDeFrance:
                    lignesIleDeFrance.append(ligne[j])
    garesIleDeFrance = []
    for i in range(len(ligne_dico)-1):
        for gare in ligne_dico[i].keys():
            if gare not in garesIleDeFrance:
                garesIleDeFrance.append(gare[j])
    
'''
algo du jeu :
    initialiser une liste de de dico avec comme clef 'question_f{i}' gare,valeur,valeur de vérité valeur de taille 10
    prendre une gare et une ligne 
    stocker la valeur de vérité de si la gare est déservi par la ligne
        s'il tape oui : attribuer à la valeur utilisateur vrai
        s'il répond non : attribuer à la valeur utilisateur faux
    vérifier l'égalité entre les deux :
        s'il y a égalité : 
            stocké la réponse dans la liste bonne réponse qui contient un dico avec comme clef un string nommé question_f{i} et comme valeur couple avec la gare et la ligne
            ajouté deux point au joeur
        sinon :
            stocké la réponse dans la liste mauvaise réponse qui contient un dico avec comme clef un string nommé question_f{i} et comme valeur couple avec la gare et la ligne proposé
            afficher la valeur de vérité de la réponse sous forme : et non c'était faux
    
'''
