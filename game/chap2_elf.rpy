$ possibiliteFuite = False

label discution_centaure: 
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
            jump info_rdv_reine
        "Non":
            jump info_rdv_centaure

label discution_reine:
    reineElf "Wesh"
    reineElf "cest un dialogue"
    jump info_rdv_reine

label info_rdv_centaure:
    centaure "OK"
    ppElf "c rigolo"
    $ possibiliteFuite = True
    jump plage

label info_rdv_reine:
    stop sound
    show callyon:
        xalign 1.5
    with move
    show callyon at right
    with move
    reineElf "VOila ce qui va ce passer"
    ppElf "OK lourd"
    ppElf "j'ai pas envie"
    jump plage

label plage:
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
            jump bonjour_hiris
        "Bonjour enchanté de faire votre connaissance":
            jump bonjour_enchante

label bonjour_hiris:
    ppElf "Bonjour je me présente, Hiris"
    jump presentationFamilleSirene

label bonjour_enchante:
    ppElf "Bonjour enchanté de faire votre connaissance"
    jump presentationFamilleSirene

label presentationFamilleSirene:
    roiSirene "Bonjour je suis Morgon, la roi"
    princeSirene "Bonjour je suis Metilay, le prince"
    menu:
        "Le prince est aussi beau que sur la peinture":
            jump ecouteConversation
        "Le prince n'est pas aussi beau que ce que j'imaginais":
            #not working // possibiliteFuite not definded
            if (possibiliteFuite == True):
                menu:
                    "Vous décidez de fuir":
                        jump fuite
                    "Vous décidez de rester":
                        jump ecouteConversation
            else:
                jump ecouteConversation

label ecouteConversation:
    roiSirene "blabla"
    princeSirene "blabla"
    roiSirene "Pour que la paix soit durable il nous faut un mariage"
    roiSirene "Notre fille est absente." 
    roiSirene "Elle a demandé a vous voir en privé"
    jump rencontrePrincesse

label fuite:
    ppElf "Je vais aux toilettes"
    jump rencontrePrincesse