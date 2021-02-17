﻿define n = Character("Narrateur")

define ppSirene = Character(_("Edalla"), color="#FFA500") #Femme
define roiSirene = Character("Morgon") #Homme
define princeSirene = Character("Metilay") #Homme

define ppElf = Character(_("Hiris"), color="#FFFF00") #Femme
define reineElf = Character("Callyon") #Femme
define princeElf = Character("Keidal") #Homme

define centaure = Character("Garkiel") #Centaure
define tortue = Character ("Amma") #Tortue

label start:
    stop music fadeout 5.0
    $ qteDragueReussi = False
    scene bg truc
    n "Le monde est abandonné par la guerre faisant rage depuis des siècles entre deux camps, la Terre et la Mer, les elfes Tyrriens contre les sirènes d’Océanos."
    n "Mais en ces temps de guerres, ces deux ennemis de toujours sont enfin parvenus à trouver un accord qui pourrait mettre un terme à cet interminable conflit."
    show Hiris:
        xalign 1.5
    with move
    show Edalla:
        xalign -0.5
    with move
    show Hiris at right
    with move
    show Edalla at left
    with move
    menu:
        n "Quel personnage voulez-vous incarner ?"
        "Edalla la sirène":
            show Hiris:
                xalign 1.5
            with move
            jump choix_sirene
        "Hiris l'elf":
            show Edalla:
                xalign -0.5
            with move
            jump choix_elf
    return