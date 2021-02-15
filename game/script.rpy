define n = Character("Narrateur")

define ppElf = Character("Hiris") #Femme // rajouter une couleur associé au personnage
define reineElf = Character("Callyon") #Femme
define princeElf = Character("Keidal") #Homme

define ppSirene = Character("Edalla") #Femme
define roiSirene = Character("Morgon") #Homme
define princeSirene = Character("Metilay") #Homme

define centaure = Character("Garkiel") #Centaure
define tortue = Character ("Amma") #Tortue

label start:

    scene bg room

    show Narrateur

    menu:

        n "Chosisez un point de vue"
        
        "Point de vue de la sirène":
            jump pdv_sirene

        "Point de vue de l'elf":
            jump pdv_elf

    return
