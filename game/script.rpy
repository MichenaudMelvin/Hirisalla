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
    $ qteDragueReussi = False
    $ qteObservationReussi = False
    scene bg truc
    n "Le monde est abandonné par la guerre faisant rage depuis des siècles entre 2 camps, la Terre et la Mer, les elfes Tyrriens contre les sirènes d’Océanos."
    n "Mais en ces temps de guerres, ces 2 ennemis de toujours sont enfin parvenus à trouver un accord qui pourrait mettre un terme à cet interminable conflit."
    show Edalla:
        xalign 1.5
    with move
    show Hiris:
        xalign -0.5
    with move
    show Edalla at right
    with move
    show Hiris at left
    with move
    menu:
        n "Quel personnage voulez-vous incarner ?"
        "Edalla la sirène":
            jump choix_sirene
        "Hiris l'elf":
            jump choix_elf
    return
