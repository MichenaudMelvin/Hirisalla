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

label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte
    # can change to "call screen qte_button" to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return
