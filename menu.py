from module_jeu_des_gares import*
from module_jeu_des_lignes import*


print("Bonjour, bienvenu dans le jeu : IDF sur le bout des doigts \n Vous voulez testez votre connaissance du réseau francilien, alors ce jeu est fait pour vous ! \n")
print("Vous pouvez soit à : ",
                "\n -tapez 1 pour le jeu des gares", 
                "\n -tapez 2 pour lejeu des lignes ")
                
choixTypeDeJeu=int(input("\n Que choisissez vous ?\n"))


while(choixTypeDeJeu!=1 and choixTypeDeJeu!=2):
    print("Désolé mais cette option n'est pas possible ... \n")
    print("Veuillez choisir soit  : ",
                        "\n -tapez 1 pour le jeu des gares ",
                        "\n -tapez 2 pour lejeu des lignes ")
    choixTypeDeJeu=int(input("\n Que choisissez vous ?\n"))

if choixTypeDeJeu==1:
    print("maintenant, vous pouvez choisir à : \n\t - deviner les lignes de chaque gare en tapant 1",
           "\n\t -deviner si une gare est bien desservu par la ligne en tapant 2")
    choixJeu=int(input("\n Que choisissez vous ?\n"))
    if choixJeu==1:
        jeu_des_gares_()
    else :
        deservi_par_()
else :
    print("maintenant, vous pouvez choisir à : \n\t - deviner les lignes de chaque gare en tapant 1",
           "\n\t -deviner si une gare est bien desservu par la ligne en tapant 2")
    choixJeu=int(input("\n Que choisissez vous ?\n"))
    if choixJeu==2:
        jeu_des_lignes_()
    else :
        jeuDesert()
     