label discution_sirene:
    ppElf "ouais lourd on est a l'ambassade"
    ppSirene "ouais lourd on fait un accord de paix ouais"
    princeSirene "Wesh du coup, on fait koi ????????"
    if (qteObservationReussi == True):
        menu:
            "declaration":
                jump declaration_sirene
            "mariage arrangé":
                jump finMariageArrange_sirene
            "romance entre princes":
                jump discutionEntrePrinces_sirene
    else:
        menu:
            "declaration":
                jump declaration_sirene
            "mariage arrangé":
                jump finMariageArrange_sirene

label finMariageArrange_sirene:
    #transition et mise en scène
    ppSirene "trop relou jvoulais pas etre avec ce fdp"
    return

label discutionEntrePrinces_sirene:
    show princeElf:
        xalign 1.5
    with move
    show princeSirene:
        xalign -0.5
    with move
    show princeElf at right
    with move
    show princeSirene at left
    with move

    menu:
        princeElf "on baise ?"
        "Oui":
            jump finPrinceLove_sirene
        "Non":
            show princeElf:
                xalign 1.5
            with move
            show princeSirene:
                xalign -0.5
            with move
            hide princeSirene
            hide princeElf
            jump finMariageArrange_sirene

label finPrinceLove_sirene:
    princeElf "trop bien"
    princeSirene "oui"
    #fin et mise en scène
    return

label declaration_sirene:
    menu:
        ppSirene "blabla"
        "Je t'aime":
            jump discutionEntrePrincesses_sirene
        "nik":
            jump finMariageArrange_sirene

label discutionEntrePrincesses_sirene:
    show Edalla:
        xalign 1.5
    with move
    show Hiris:
        xalign -0.5
    with move
    show Edalla at right
    with move
    show Hiris at left
    with move

    ppSirene "ok"
    ppSirene "on fait koi"
    ppElf "jsp"
    if (qteDragueReussi == True):
        jump finHeureuse_sirene   
    else:
        jump finTrise_sirene

label finHeureuse_sirene:
    ppSirene "<3"
    #mise en scène et fin
    return

label finTrise_sirene:
    ppSirene ":'("
    ppElf ":'("
    #mise en scène et fin
    return
    