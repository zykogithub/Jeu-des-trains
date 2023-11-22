from module_jeu_des_gares import*
from module_jeu_des_lignes import*


print("Bonjour, bienvenu dans le jeu : IDF sur le bout des doigts \n Vous voulez testez votre connaissance du réseau francilien, alors ce jeu est fait pour vous ! \n")
print("Vous pouvez soit à : ",
                "\n -tapez 1 pour le jeu des gares", 
                "\n -tapez 2 pour lejeu des lignes ")
                
choix=int(input("\n Que choisissez vous ?\n"))




if choix==1:
    jeu_des_gares_()
elif choix==2:
    jeu_des_lignes_()

while(choix!=1 and choix!=2 ):
    print("Désolé mais cette option n'est pas possible ... \n")
    choix=print("Veuillez choisir soit  : ",
                        "\n -tapez 1 pour le jeu des gares ",
                        "\n -tapez 2 pour lejeu des lignes ")
    choix=int(input("\n Que choisissez vous ?\n"))
    if choix==1:
        jeu_des_gares_()
    elif choix==2:
        jeu_des_lignes_()
    
    

    