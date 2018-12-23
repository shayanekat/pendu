#katchera
#Shayane
#aero 2 D1
#———————————————————————————————————————————————————————————
#        TP2 : Le  Jeu du pendu en version amelioree
#———————————————————————————————————————————————————————————

    # IPSA IN21 TP2: jeu du pendu
    # Ce code utilise un fichier dictionnaire de mots français
    # sous licence GNU GPL : http://www.winedt.org/Dict/
    # Les définitions des mots sont tirées du CNRTL: cnrtl.fr


import IN21_TP2_libpendu as lp
#import time

rep = "oui"

while rep == "oui":
    print("===== JEU DU PENDU =====")

    #pseudo = input("entrez votre nom : ")
    mot = lp.motAleatoire()
    essai=0
    nberr = 0
    print("nombre d'essai :",essai)
    print("=================================================")
    mot_cherche = []
    jouee = []

    for i in range(len(mot)):
        mot_cherche.append("_")
    mot_trouve = "".join(mot_cherche)

    while mot_trouve != mot and nberr <= 9:

        lettre = input("entrer une lettre a essayer : ")
        while lettre in jouee :
            lettre = input("entrer une lettre a essayer : ")
        jouee.append(lettre)
        essai+=1
        if lettre in mot:
            for i in range(len(mot)):
                if mot[i] == lettre:
                    mot_cherche[i] = lettre
            mot_trouve = "".join(mot_cherche)
            print("nombre d'essai :",essai)
        else:
            nberr+=1

        print("mot du joueur :",mot_trouve)
        print("lettres jouees :",jouee)

        if nberr==1:
            print("__")

        if nberr==2:
            print(" / ")
            print(" / ")
            print(" / ")
            print(" / ")
            print("_/_")

        if nberr==3:
            print("  __")
            print(" / ")
            print(" / ")
            print(" / ")
            print(" / ")
            print("_/_")

        if nberr==4:
            print("  __")
            print(" /  ◊")
            print(" / ")
            print(" / ")
            print(" / ")
            print("_/_")

        if nberr==5:
            print("  __")
            print(" /  ◊")
            print(" / /")
            print(" / ")
            print(" / ")
            print("_/_")


        if nberr==6:
            print("  __")
            print(" /  ◊")
            print(" / //")
            print(" /  /")
            print(" / ")
            print("_/_")

        if nberr==7:
            print("  __")
            print(" /  ◊")
            print(" / ///")
            print(" /  /")
            print(" / ")
            print("_/_")

        if nberr==8:
            print("  __")
            print(" /  ◊")
            print(" / ///")
            print(" /  /")
            print(" / /")
            print("_/_")

        if nberr==9:
            print("  __")
            print(" /  ◊")
            print(" / ///")
            print(" /  /")
            print(" / / /")
            print("_/_")

        print("=================================================")

    if mot_trouve == mot:
        print("==GAGNEE==")
        print("vous avez fais",essai,"essais")
        print(mot_trouve,":")
        print(lp.getAllDefStr(mot))

    else :
        print("==PERDU==")
        print("vous avez fais",essai,"essais")
        print("le mot a trouver etait :",mot,":")
        print(lp.getAllDefStr(mot))

    rep = input("voulez vous faire une nouvelle partie? oui ou non : ")
    
