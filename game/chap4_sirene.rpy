label discution_sirene:
    ppElf "ouais lourd on est a l'ambassade"
    ppSirene "ouais lourd on fait un accord de paix ouais"
    princeSirene "Wesh du coup, on fait koi ????????"
    menu:
        "declaration":
            jump declaration_sirene
        "mariage arrangé":
            jump finMariageArrange_sirene

label finMariageArrange_sirene:
    #transition et mise en scène
    ppSirene "trop relou jvoulais pas etre avec ce fdp"
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
    