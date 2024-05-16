from random import*
from module_toutes_les_gares import* #dans ce module, il y a la variable
from time import*
#gare_dico qui stocke toutes les gares et leurs lignes respectives sous forme d'une
#liste de dictionnaire, chaque clef est le nom d'une gare, chaque valeur est une
#liste de chaine de caratère, et chaque chaine est une ligne qui passe par la gare
  
""" algorithme du jeu
        1 tant que l'utilisateur n'a pas dit stop ou a mis le nombre maximum d'entrée, ajouter une valeur dans la liste de répons
        2 parcourir la liste rattachée à la gare et comparer chaque élément de la liste réponse à celle de la gare  
        3 S'il y a une correspondance, retiré l'élément de la liste réponse
        4 ensuite, voici les résultats que le jeu peut donner :
            1 Si la liste réponse est vide : bonne réponse
            2 Si la liste réponse n'a pas changé de taille : mauvaise réponse
            3 Si la liste a changé de taille mais n'est pas vide : afficher les éléments de la liste de la gare pour dire qu'ils sont 
            en bonne réponse 
            Puis afficher les éléments restant pour dire qu'ils sont en mauvaise réponse
        """

MAXIMUM=10 #nombre maximal de réponse autorisé
DUREE_MAX = 60  # 1 minutes de temps de jeu maximum

def jeu_des_gares_():

# fonction pour générer l'élément aléatoire
    selectionGare=randint(0,len(gare_dico)-1) #pour générer un entier aléatoirement, entier qui servira à cibler une gare car chaque dico
    # de la liste ont pour seul clef le nom de la gare. Donc ce nombre aléatoire renverra nécessairement vers la gare,
    #  qui est la clef du dico

    #cle_jeue et variable_reponse sont déclarées en global pour pouvoir récupérer la clef, soit le nom de la gare
    #et la valeur de la clef, soit la liste des lignes traversées par la gare

    cle_jeu=None
    valeur_reponse=[]  
    for cle,valeur in gare_dico[selectionGare].items():
        cle_jeu=cle
        valeur_reponse=valeur


    # variable pour connaitre le nombre de réponse à saisir 


    #debut du jeu :

# fonction affichage début
    print("Vous voici dans le jeu : devine la gare ! \n Le jeu est simple :",
          " Nous allons donnez un nom de gare, il faudra donner la(es) ligne(s) qui la traverse(nt) \n  ",
          "par exemple, si je donne la gare Louis-Jean, vous devez dire chaque ligne qui la travrse.\n"
          "Bien, évidement, vous avez seulement 1 minutes pour toutes le donées, alors dépéchez-vous !",
          "Bonne chance !")
    print("Quelle(s) est (sont) les lignes traversée(s) à la gare de : ",cle_jeu," ?")
    print("Ecrivez sous la forme : RER A ou RER B, etc")


    #debut de l'algorithme du jeu 
# fonction algo coeur du jeu
    # fonction initialisation
    tour=0 #variable utilisé dans la boucle du jeu pour éviter qu'il n'ait trop de réponse rentré par l'utilisateur
    debut = time()
    temps_ecoule = time() - debut
    # print("Vous ne pourrez pas rentrer au dela de", 5-tour, "réponses")
    # reponse=input("Ecrivez une réponse. \n Tapez STOP pour arrêter de réponse")
    # reponse.upper() #normalisation des réponses en majuscule, donc cette ligne sert à mettre en majuscule la réponse rentrée
    # liste_reponse=[]
    # liste_reponse.append(reponse)



    print("Vous ne pourrez pas rentrer au dela de", MAXIMUM-tour, "réponses")

    #répétition du jeu jusqu'à ce que le joueur arrête de jouer ou qu'on n'ait atteint le nombre maximum de lignes enregistré dans 
    # le dico g.gare_dico
    # fonction pour récupérer les entrées
    liste_reponse=[]
    reponse=None
    while (reponse!="STOP" and tour<MAXIMUM and temps_ecoule<=DUREE_MAX  ): 
         
        if reponse!="STOP":
            reponse=input("Ecrivez une nouvelle réponse. \n Tapez STOP pour \
                           arrêter de réponse \n")
            reponse.upper() #normalisation des réponses en majuscule, donc 
                            #cette ligne sert à mettre en majuscule la réponse rentrée
            liste_reponse.append(reponse)
            tour+=1
            temps_ecoule = time() - debut
            print("Vous ne pourrez pas rentrer au dela de", MAXIMUM-tour, \
                  "réponses")

    # fonction pour supprimer le STOP
    if liste_reponse[-1]=='STOP' : 
        del liste_reponse[-1] #étant donné que lorsque l'utilisateeur rentrait stop, cela rentrait dans cette liste, 
    #il a fallu supprimer STOP de la liste de la réponse

    # fonction de comparaison de la réponse avec les propositions
    taille_reponse=len(liste_reponse) #sera comparé avece la future taille de la liste de réponse, qui perdra un élément si 
    #l'élément correspond à la liste valeur_reponse

    for i in range (len(liste_reponse)-1):
        essaie=liste_reponse[i]
        for j in range (len(valeur_reponse)-1):
            if essaie==valeur_reponse[j]: #condition qui dit que si un élément de la liste liste_reponse correspond à un élément de la 
                #liste valeur_reponse, alors supprimer l'élément de la liste liste_reponse 
                del liste_reponse[i]


    #fonction de sortie



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
        print("Bien joué ! Vous avez réussi à donner tout ce que vous avez pu. \n Voyons ensemble vos réponses : \n" )
        if len(liste_reponse)==0 and tour>1 : 
            print("Bravo, vous avez donnez la bonne réponse : \n")
            print("J'espère que vous avez pas triché")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])

        elif len(liste_reponse)==taille_reponse:  

            print("Dommage, vous n'avez pas donnée de bonne réponse...\n Voici la(es) réponse(s) qu'il fallait : \n")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])
        else : 

            print("Bravo, vous avez donnez comme bonne réponse : \n")
            print("J'espère que vous avez pas triché")
            for i in range(len(liste_reponse)-1):
                print(liste_reponse[i])
            print("Cependant, vous avez oublier comme réponse réponse : \n")
            print("Du coup, vous avez mal triché, petit morveux !!!")
            for i in range(len(valeur_reponse)-1):
                print(valeur_reponse[i])

    else:
        print("Bien joué ! Vous avez réussi à donner tout ce que vous avez pu. \n Voyons ensemble vos réponses : \n")
        if len(liste_reponse)==0 and tour>1 : 
            print("Bravo, vous avez donnez la bonne réponse : \n")
            for i in range(1,len(liste_reponse)-1):
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


def deservi_par_():
    
    # affichage du début
    print("Vous voici dans le jeu : dessevi par \n Le jeu est simple : \n :\
        Vous devez devinez si une gare passe bien par une ligne.",
        "Par exemple s'il est demandé est que la gare Louis-Jean passe bien par la ligne",
        "6, vous devez répondre oui ou non \n \
        Vous aurez 10 questions et à la fin, une note sur 10 vous sera donné. \n \
        Pour chaque question, vous n'aurez que 30 secondes pour répondre. \n",
        "Bonne chance !!")
    # fonction pour stocker toutes les gares et toutes les lignes dans des liste
    toute_les_ligne = []
    for i in range(0,len(gare_dico)-1):
        for ligne in gare_dico[i].values():
            for j in range(len(ligne)-1):
                if ligne[j] not in toute_les_ligne:
                    toute_les_ligne.append(ligne[j])
    toute_les_gare = []
    for i in range(0,len(gare_dico)-1):
        for gare in gare_dico[i].keys():
            if gare not in toute_les_gare:
                toute_les_gare.append(gare[j])
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