label discution_tortue_sirene:
    scene bg ambassadeSirene
    with fade
    show Edalla:
        xalign -0.5
    with move
    show amma:
        xalign 1.5
    with move
    show Edalla at left
    with move
    show amma at right
    with move
    #faire des bégaiement parce que je sais pas le faire
    n "Edalla après s'être enfuite du château, allait se recuillir auprès d'Amma à propos de son mariage forcé avec le prince des Tyrriens."
    tortue "Et donc, tu accepterais de te sacrifier pour ta patrie ?"
    ppSirene "Oui…"
    ppSirene "Je ne pense pas vraiment avoir d'autres choix…"
    show amma:
        xalign 1.5
    with move
    hide tortue
    jump info_rdv_roi_sirene

label discution_roi_sirene:
    n "Le jour d’après, au château du peuple des Océanos, la princesse allait se recueillir auprès de son père avant son voyage vers le monde terrestre."
    jump info_rdv_roi_sirene

# à replace --> refaire le dialogue avec amma

label info_rdv_roi_sirene:
    show Morgon:
        xalign 1.5
    with move
    show Morgon at right
    with move
    roiSirene "Edalla ma fille, êtes-vous vraiment sur de vôtre choix ?"
    ppSirene "Oui père j’accepte ce mariage pour mon peuple."
    roiSirene "Me voici ravis, ce conflit ridicule va enfin se terminer, nous partons dans l'après-midi sur le territoire de tyrriens."
    ppSirene "Mais comment allons nous nous déplacer vers le peuple des Elfes ?"
    roiSirene "Nous utiliserons les bulles de déplacement terrestre spécialement conçues par nos consœurs nymphes pour cette rencontre purememnt pacifique."
    ppSirene "Magnifique, je vais me préparer pour l'occasion."
    show Edalla:
        xalign -0.5
    with move
    scene bg plage
    with fade
    #elipse en gros
    pause 3
    show Edalla:
        xalign -0.5
    with move
    show Edalla at left
    with move
    roiSirene "Reine Callyon, c’est un honneur pour nous de pouvoir entrer dans ce lieux aussi chaleureux."
    reineElf "Je suis heureuse de voir que nos décisions sont pour un futur meilleur."

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
