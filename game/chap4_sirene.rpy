label discution_sirene:
    scene bg ambassadeElf
    with fade
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
    reineElf "Bien, nous sommes donc tous réunis pour metre un termes à ces conflits."
    roiSirene "Et donc marier nos enfants."
    roiSirene "Edalla, le destin d'Océanos repose sur toi."
    princeElf "Quelle est vôtre décision mademoiselle Edalla ?"
    menu:
        "Je désire prendre Hiris comme épouse":
            ppSirene "Je préfèrerais être avec Hiris plutôt qu'avec Keidal"
            jump declaration_sirene
        "J'accepte notre union avec le prince":
            ppSirene "Je prend Keidal pour époux."
            jump finMariageArrange_sirene

label finMariageArrange_sirene:
    #transition et mise en scène
    roiSirene "Qu'il en soit ainsi, que les dieux bénissent ce mariage et que la paix soit durable pour les années à venir."
    n "Ainsi, le prince Keidal et la princesse Edalla se marièrent et eurent beaucoup d’enfants."
    scene credits
    with fade
    #play music "audio/drama_1.mp3" fadeout 2.0
    pause 360
    return

label declaration_sirene:
    if (dragueReussi == True):
        jump finHeureuse_sirene   
    else:
        jump finTrise_sirene

label finHeureuse_sirene:
    n "Les souverains sont tous pris de surprise laissant un étrange silence."
    n "La princesse Hiris se lève de sa chaise."
    ppElf "J'accepte ! Je veux me marier avec Edalla."
    roiSirene "Eh bien Callyon, quelle est votre verdicte sur cette proposition ?"
    reineElf "Bien un mariage est un mariage, je suppose que nous pouvons tolérer une telle décision."
    n "Les deux princesses se marièrent et eurent beaucoup d’enfants."
    scene credits
    with fade
    #play music "audio/romantique.mp3" fadeout 2.0
    pause 360
    return

label finTrise_sirene:
    ppElf "Je refuse, je ne vous connais pas beaucoup."
    scene credits
    with fade
    #play music "audio/drama_2.mp3" fadeout 2.0
    pause 360
    return
    