label discution_centaure_sirene: 
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
            jump info_rdv_reine_sirene
        "Non":
            jump info_rdv_centaure_sirene

label discution_reine_sirene:
    reineElf "Wesh"
    reineElf "cest un dialogue"
    jump info_rdv_reine_sirene

label info_rdv_centaure_sirene:
    centaure "OK"
    ppElf "c rigolo"
    $ possibiliteFuite = True
    jump plage_sirene

label info_rdv_reine_sirene:
    stop sound
    show callyon:
        xalign 1.5
    with move
    show callyon at right
    with move
    reineElf "VOila ce qui va ce passer"
    ppElf "OK lourd"
    ppElf "j'ai pas envie"
    jump plage_sirene

label plage_sirene:
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
        "Bonjour je me présente, edalla":
            jump bonjour_edalla_sirene
        "Bonjour enchanté de faire votre connaissance":
            jump bonjour_enchante_sirene

label bonjour_edalla_sirene:
    ppElf "Bonjour je me présente, edalla"
    jump presentationFamilleSirene_sirene

label bonjour_enchante_sirene:
    ppElf "Bonjour enchanté de faire votre connaissance"
    jump presentationFamilleSirene_sirene

label presentationFamilleSirene_sirene:
    roiSirene "Bonjour je suis Morgon, la roi"
    princeSirene "Bonjour je suis Metilay, le prince"
    menu:
        "Le prince est aussi beau que sur la peinture":
            jump ecouteConversation_sirene
        "Le prince n'est pas aussi beau que ce que j'imaginais":
            if (possibiliteFuite == True):
                menu:
                    "Vous décidez de fuir":
                        jump fuite
                    "Vous décidez de rester":
                        jump ecouteConversation_sirene
            else:
                jump ecouteConversation_sirene

label ecouteConversation_sirene:
    roiSirene "blabla"
    princeSirene "blabla"
    roiSirene "Pour que la paix soit durable il nous faut un mariage"
    roiSirene "Notre fille est absente." 
    roiSirene "Elle a demandé a vous voir en privé"
    jump rencontrePrincesse_sirene

label fuite:
    ppElf "Je vais aux toilettes"
    jump rencontrePrincesse_sirene