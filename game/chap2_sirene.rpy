label discution_tortue_sirene:
    scene chambre_sirene
    with fade
    show edalla_triste:
        xalign -0.5
    with move
    show amma_normal:
        xalign 1.5
    with move
    show edalla_triste at left
    with move
    show amma_normal at right
    with move
    n "Après s'être enfuite du château, Edalla allait se recuillir auprès d'Amma à propos de son mariage forcé avec le prince des Tyrriens."
    tortue "Et donc, tu accepterais de te sacrifier pour ta patrie ?"
    ppSirene "Oui…"
    hide edalla_triste
    show edalla_pleure at left
    ppSirene "Je ne pense pas vraiment avoir d'autres choix…"
    show amma_normal:
        xalign 1.5
    with move
    hide amma_normal
    jump info_rdv_roi_sirene

label discution_roi_sirene:
    n "Le jour d'après, au château du peuple des Océanos, la princesse allait se recueillir auprès de son père avant son voyage vers le monde terrestre."
    jump info_rdv_roi_sirene

label info_rdv_roi_sirene:
    scene ambassade_sirene
    with fade
    show edalla_triste:
        xalign -0.5
    with move
    show Morgon:
        xalign 1.5
    with move
    show edalla_triste at left
    with move
    show Morgon at right
    with move
    
    roiSirene "Edalla ma fille, êtes-vous vraiment sur de vôtre choix ?"
    ppSirene "Oui père j'accepte ce mariage pour mon peuple."
    roiSirene "Me voici ravis, ce conflit ridicule va enfin se terminer, nous partons dans l'après-midi sur le territoire de tyrriens."
    ppSirene "Mais comment allons nous nous déplacer vers le peuple des Elfes ?"
    hide edalla_triste
    show edalla_joie at left
    roiSirene "Nous utiliserons les bulles de déplacement terrestre spécialement conçues par nos consœurs nymphes pour cette rencontre purememnt pacifique."
    ppSirene "Magnifique, je vais me préparer pour l'occasion."
    show edalla_joie:
        xalign -0.5
    with move

    scene chambre_sirene
    with fade
    show edalla_normal:
        xalign -0.5
    with move
    show amma_normal:
        xalign 1.5
    with move
    show edalla_normal at left
    with move
    show amma_normal at right
    with move
    menu:
        tortue "Edalla tu voudrais parler de ton mariage plus en détail ?"
        "Parler du marriage":
            ppSirene "Amma, puis-je te parler sérieusement ?"
            jump reflexion_sirene
        "Preferez se reposer":
            ppSirene "Non, désolée Amma, je préfère me reposer un peu"
            jump decouverteFamilleRoyale_sirene

label reflexion_sirene:
    tortue "Bien sûr princesse."
    hide edalla_normal
    show edalla_triste at left
    ppSirene "Je doute encore sur mon mariage malgré le fait que je veux protéger mon peuple, je n'ai pas vraiment envie de vivre aux côtés d’une personne que je n’aime pas."
    menu:
        tortue "Que dit vôtre cœur princesse ?"
        "Je pense que j'ai besoin de réfléchir encore":
            ppSirene "Je ne suis pas tout à fait sûre de prendre ma décision."
            jump decouverteFamilleRoyale_sirene
        "Je pense être prête à ma marier":
            ppSirene "Il est mieux pour mon peuple que je me marie."
            jump decouverteFamilleRoyale_sirene

label decouverteFamilleRoyale_sirene:
    #elipse de 1h
    scene ville_sirene
    with fade
    show morgon_normal:
        xalign -0.5
    with move
    show edalla_normal:
        xalign -0.5
    with move
    show edalla_normal at left
    with move
    show callyon_normal:
        xalign 1.5
    with move
    show callyon_normal:
        xalign 0.85
    with move
    show morgon_normal:
        xalign 0.15
    with move
    show keidal_normal:
        xalign 1.5
    with move
    show keidal_normal at right
    with move
    
    roiSirene "Reine Callyon, c'est un honneur pour nous de pouvoir entrer dans ce lieux aussi chaleureux."
    reineElf "Je suis heureuse de voir que nos décisions sont pour un futur meilleur."
    princeElf "Dans ce cas commençons les présentations."
    menu:
        "Je me présente, Edalla":
            hide edalla_normal
            show edalla_joie at left
            ppSirene "Bonjour, je me présente, Edalla fille du roi"
            jump presentationFamilleSirene_sirene
        "Enchanté de faire votre connaissance":
            hide edalla_normal
            show edalla_joie at left
            ppSirene "Bonjour, je suis la princesse, enchanté de faire votre connaissance"
            jump presentationFamilleSirene_sirene

label presentationFamilleSirene_sirene:
    hide edalla_joie
    show edalla_normal at left
    princeSirene "Je suis Metilay, fils du roi Morgon, enchanté également."
    princeElf "Je suis Keidal, fils aîné de la Reine Callyon, c'est un plaisir de faire votre connaissance."
    menu:
        "Le prince est aussi beau que sur la peinture":
            ppSirene "{i}Il est aussi beau que ce sur le tableau.{/i}"
            jump ecouteConversation_sirene
        "Le prince n'est pas aussi beau que ce que j'imaginais":
            hide edalla_normal
            show edalla_triste at left
            ppSirene "{i}Il ne ressemble pas tout à fait à ce que j'ai vu sur le tableau hier.{/i}"
            jump ecouteConversation_sirene

label ecouteConversation_sirene:
    reineElf "Hiris est actuellement dans ces appartements. J'ai jugé qu'il était plus utile de présenter nos fiancés en premiers"
    roiSirene "Bien, pour que la paix soit durable il nous faut un mariage."
    reineElf "Mademoiselle Edalla, je vous prie de rejoindre ma fille, Hiris, pour parler de vôtre marriage à toutes les deux."
    reineElf "Elle doit être dans sa chambre."
    ppSirene "Bien… j'y vais de ce pas."
    jump rencontrePrincesse_sirene