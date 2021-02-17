label discution_tortue_sirene: 
    show Edalla at left
    show tortue at right
    #rajouter des dialogues ici
    tortue "Tu accepterais de te sacrifier pour ta patrie ?"
    ppSirene "Oui..."
    show tortue:
        xalign 1.5
    with move
    hide tortue
    jump info_rdv_roi_sirene

label discution_roi_sirene:
    roiSirene "Wesh"
    roiSirene "cest un dialogue"
    jump info_rdv_roi_sirene

label info_rdv_roi_sirene:
    show callyon:
        xalign 1.5
    with move
    show callyon at right
    with move
    roiSirene "voila les info sur le rdv"
    ppSirene "OK lourd"
    ppSirene "j'ai pas envie"
    #elipse de 1h
    scene bg truc
    with fade
    pause 3
    n "elipse de 1h"
    ppSirene "ouais c relou"
    tortue "ouais tu doit faire qoi ?"
    menu:
        ppSirene "ouai je doit bz le prince, c pa ouf"
        "Lui demmander conseil (à armma)":
            jump reflexion_sirene
        "Preferez se reposer":
            jump decouverteFamilleRoyale_sirene

label reflexion_sirene:
    menu:
        ppSirene "hmm..."
        "Réfléchir en tant que femme":
            ppSirene "ouai je réfléchi mais je sias pas usr koi"
            jump plage_sirene
        "Réfléchir en tant que souveraine":
            ppSirene "ouais trop relou d'etre une souveraine"
            jump plage_sirene

label plage_sirene:
    scene bg plage
    with fade
    show Edalla at left
    ppSirene "c la plage"
    ppSirene "un coup de fil"
    ppSirene "on est là"
    ppSirene "stylé la ville des elf"
    n "elipse de 2h"
    jump decouverteFamilleRoyale_sirene

label decouverteFamilleRoyale_sirene:
    #elipse de 1h
    show princeElf:
        xalign 1.5
    with move
    show reineElf:
        xalign 1.5
    with move
    show princeElf at right
    with move
    show reineElf:
        xalign 0.85
    with move
    princeElf "Bonjour"
    reineElf "Bonsoir"

    menu:
        "Bonjour je me présente, Edalla":
            jump bonjour_edalla_sirene
        "Bonjour enchanté de faire votre connaissance":
            jump bonjour_enchante_sirene

label bonjour_edalla_sirene:
    ppSirene "Bonjour je me présente, Edalla"
    jump presentationFamilleSirene_sirene

label bonjour_enchante_sirene:
    ppSirene "Bonjour enchanté de faire votre connaissance"
    jump presentationFamilleSirene_sirene

label presentationFamilleSirene_sirene:
    reineElf "Bonjour je suis Morgon, la reine"
    princeElf "Bonjour je suis Keidal, le prince"
    menu:
        "Le prince est aussi beau que sur la peinture":
            jump ecouteConversation_sirene
        "Le prince n'est pas aussi beau que ce que j'imaginais":
            jump ecouteConversation_sirene

label ecouteConversation_sirene:
    reineElf "blabla"
    princeElf "blabla"
    reineElf "Pour que la paix soit durable il nous faut un mariage"
    reineElf "Notre fille est absente." 
    reineElf "Elle a demandé a vous voir en privé"
    jump rencontrePrincesse_sirene