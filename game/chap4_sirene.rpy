label ambassadeExcuses_sirene:
    ppSirene "ouais lourd on est a l'ambassade"
    ppElf "ouais lourd on fait un accord de paix ouais"
    jump discution_sirene

label ambassadeNonExcuses_sirene:
    ppSirene "blabla c pa coul de pas s'excuzer"
    ppElf "ouais mais c'est pas toi qui décide"
    menu:
        ppSirene "Tu t'excuse ou pas ?"
        "Oui":
            jump discution_sirene 
        "Non":
            jump finGuerre_sirene

label finGuerre_sirene:
    #transition et mise en scène
    ppElf "wesh c pa cool on est mort"
    return

label discution_sirene:
    princeElf "Wesh on fait koi ????????"
    if (qteObservationReussi == True):
        jump discutionEntrePrinces_sirene
    else:
        menu:
            "declaration":
                jump declaration_sirene
            "mariage arrangé":
                jump finMariageArrange_sirene
            "romance entre princes":
                jump discutionEntrePrinces_sirene

label finMariageArrange_sirene:
    #transition et mise en scène
    ppElf "trop relou jvoulais pas etre avec ce fdp"
    return

label discutionEntrePrinces_sirene:
    show princeSirene:
        xalign 1.5
    with move
    show princeElf:
        xalign -0.5
    with move
    show princeSirene at right
    with move
    show princeElf at left
    with move

    menu:
        princeSirene "on baise ?"
        "Oui":
            jump finPrinceLove_sirene
        "Non":
            show princeSirene:
                xalign 1.5
            with move
            show princeElf:
                xalign -0.5
            with move
            hide princeElf
            hide princeSirene
            jump finMariageArrange_sirene

label finPrinceLove_sirene:
    princeSirene "trop bien"
    princeElf "oui"
    #fin et mise en scène
    return

label declaration_sirene:
    menu:
        ppElf "blabla"
        "Je t'aime":
            jump discutionEntrePrincesses_sirene
        "nik":
            jump finMariageArrange_sirene

label discutionEntrePrincesses_sirene:
    show Hiris:
        xalign 1.5
    with move
    show Edalla:
        xalign -0.5
    with move
    show Hiris at right
    with move
    show Edalla at left
    with move

    ppElf "ok"
    ppElf "on fait koi"
    ppSirene "jsp"
    if (qteDragueReussi == True):
        jump finHeureuse_sirene   
    else:
        jump finTrise_sirene

label finHeureuse_sirene:
    ppElf "<3"
    #mise en scène et fin
    return

label finTrise_sirene:
    ppElf ":'("
    ppSirene ":'("
    #mise en scène et fin
    return
    