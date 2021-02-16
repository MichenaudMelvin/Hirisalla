label ambassadeExcuses_elf:
    ppSirene "ouais lourd on est a l'ambassade"
    ppElf "ouais lourd on fait un accord de paix ouais"
    jump discution_elf

label ambassadeNonExcuses_elf:
    ppSirene "blabla c pa coul de pas s'excuzer"
    ppElf "ouais mais c'est pas toi qui décide"
    menu:
        ppSirene "Tu t'excuse ou pas ?"
        "Oui":
            jump discution_elf 
        "Non":
            jump finGuerre_elf

label finGuerre_elf:
    #transition et mise en scène
    ppElf "wesh c pa cool on est mort"
    return

label discution_elf:
    princeElf "Wesh on fait koi ????????"
    $ qteObservationReussi = True
    if (qteObservationReussi == True):
        jump discutionEntrePrinces_elf
    else:
        menu:
            "declaration":
                jump declaration_elf
            "mariage arrangé":
                jump finMariageArrange_elf
            "romance entre princes":
                jump discutionEntrePrinces_elf

label finMariageArrange_elf:
    #transition et mise en scène
    ppElf "trop relou jvoulais pas etre avec ce fdp"
    return

label discutionEntrePrinces_elf:
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
            jump finPrinceLove_elf
        "Non":
            show princeSirene:
                xalign 1.5
            with move
            show princeElf:
                xalign -0.5
            with move
            jump finMariageArrange_elf

label finPrinceLove_elf:
    princeSirene "trop bien"
    princeElf "oui"
    #fin et mise en scène
    return

label declaration_elf:
    menu:
        ppElf "blabla"
        "Je t'aime":
            jump discutionEntrePrincesses_elf
        "nik":
            jump finMariageArrange_elf

label discutionEntrePrincesses_elf:
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
        jump finHeureuse_elf   
    else:
        jump finTrise_elf

label finHeureuse_elf:
    ppElf "<3"
    #mise en scène et fin
    return

label finTrise_elf:
    ppElf ":'("
    ppSirene ":'("
    #mise en scène et fin
    return
    