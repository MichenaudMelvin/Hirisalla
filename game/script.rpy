define n = Character("Narrateur")

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
    n "Le monde est abondé par la guerre faisant rage depuis des siècles entre 2 camps, la Terre et la Mer, les elfes Tyrriens contre les sirènes d’Océanos."
    n "Mais en ces temps de guerres, ces 2 ennemis de toujours sont enfin parvenus à trouver un accord qui pourrait mettre un terme à cet interminable conflit."
    n "Quel personnage voulez-vous incarner ?"

    menu :
        "Point de vue de la Sirène":
            jump choix_sirene
        "Point de vue de l'Elf":
            jump choix_elf