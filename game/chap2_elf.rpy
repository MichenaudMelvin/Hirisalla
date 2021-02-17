label discution_centaure_elf: 
    show Hiris at left
    show centaure at right
    menu:
        centaure "Tu accepterais de te sacrifier pour ta patrie ?"
        "Oui":
            play sound "audio/galop.ogg"
            pause 3
            show centaure:
                xalign 1.5
            with move
            hide centaure
            jump info_rdv_reine_elf
        "Non":
            jump info_rdv_centaure_elf

label discution_reine_elf:
    reineElf "Wesh"
    reineElf "cest un dialogue"
    jump info_rdv_reine_elf

label info_rdv_centaure_elf:
    centaure "OK"
    ppElf "c rigolo"
    jump plage_elf

label info_rdv_reine_elf:
    stop sound
    show callyon:
        xalign 1.5
    with move
    show callyon at right
    with move
    reineElf "VOila ce qui va ce passer"
    ppElf "OK lourd"
    ppElf "j'ai pas envie"
    jump plage_elf

label plage_elf:
    scene bg plage
    with fade
    show Hiris at left
    ppElf "c la plage"
    ppElf "elle est la la ville"
    n "elipse de 2h"
    show princeSirene:
        xalign 1.5
    with move
    show roiSirene:
        xalign 1.5
    with move
    show princeSirene at right
    with move
    show roiSirene:
        xalign 0.85
    with move
    princeSirene "Bonjour"
    roiSirene "Bonsoir"

    menu:
        "Bonjour je me présente, Hiris":
            jump bonjour_hiris_elf
        "Bonjour enchanté de faire votre connaissance":
            jump bonjour_enchante_elf

label bonjour_hiris_elf:
    ppElf "Bonjour je me présente, Hiris"
    jump presentationFamilleSirene_elf

label bonjour_enchante_elf:
    ppElf "Bonjour enchanté de faire votre connaissance"
    jump presentationFamilleSirene_elf

label presentationFamilleSirene_elf:
    roiSirene "Bonjour je suis Morgon, la roi"
    princeSirene "Bonjour je suis Metilay, le prince"
    menu:
        "Le prince est aussi beau que sur la peinture":
            jump ecouteConversation_elf
        "Le prince n'est pas aussi beau que ce que j'imaginais":
            jump ecouteConversation_elf

label ecouteConversation_elf:
    roiSirene "blabla"
    princeSirene "blabla"
    roiSirene "Pour que la paix soit durable il nous faut un mariage"
    roiSirene "Notre fille est absente." 
    roiSirene "Elle a demandé a vous voir en privé"
    jump rencontrePrincesse_elf