define n = Character(_("Narrateur"), color="#ffffff", what_outlines=[(1, "#000000")]) #Narrateur

define ppSirene = Character(_("Edalla"), color="#fe432d", what_outlines=[(1, "#000000")]) #Femme
define roiSirene = Character("Morgon", color="9bc6c2", what_outlines=[(1, "#000000")]) #Homme
define princeSirene = Character("Metilay", color="bbe4e0", what_outlines=[(1, "#000000")]) #Homme

define ppElf = Character(_("Hiris"), color="#926d99", what_outlines=[(1, "#000000")]) #Femme
define reineElf = Character("Callyon", color="#f3e106", what_outlines=[(1, "#000000")]) #Femme
define princeElf = Character("Keidal", color="#925a12", what_outlines=[(1, "#000000")]) #Homme

define centaure = Character(_("Garkiel"), color="#eec5a9", what_outlines=[(1, "#000000")]) #Centaure
define tortue = Character ("Amma", color="#7d9062", what_outlines=[(1, "#000000")]) #Tortue

label start:
    $ excuseHiris = False
    $ desaccordHiris = False
    $ dispute = False
    $ dragueReussi = False
    scene fond_introduction
    n "Le monde est abandonné par la guerre faisant rage depuis des siècles entre deux camps, la Terre et la Mer, les elfes Tyrriens contre les sirènes d’Océanos."
    n "Mais en ces temps de guerres, ces deux ennemis de toujours sont enfin parvenus à trouver un accord qui pourrait mettre un terme à cet interminable conflit."
    show hiris:
        xalign 1.5
    with move
    show edalla_normal:
        xalign -0.5
    with move
    show hiris at right
    with move
    show edalla_normal at left
    with move
    menu:
        n "Quel personnage voulez-vous incarner ?"
        "Edalla la sirène":
            show hiris:
                xalign 1.5
            with move
            stop music fadeout 4.0
            jump choix_sirene
        "Hiris l'elf":
            show edalla_normal:
                xalign -0.5
            with move
            stop music fadeout 4.0
            jump choix_elf
    return