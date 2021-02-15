define n = Character("Narrateur")

define ppElf = Character("Hiris") #Femme
define reineElf = Character("Callyon") #Femme

define ppSirene = Character("Edalla") #Femme
define roiSirene = Character("Morgon") #Homme
define princeSirene = Character("Metilay") #Homme

define centaure = Character("Garkiel") #Centaure
define tortue = Character ("Amma") #Tortue

label start:

    scene bg room

    show eileen happy

    menu:

        n "Chosisez un point de vue"
        
        "Point de vue de la sirène":
            jump pdv_sirene

        "Point de vue de l'elf":
            jump pdv_elf

    return
