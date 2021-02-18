label ambassadeExcuses_elf:
    scene bg ambassadeSirene
    show hiris:
        xalign -0.5
    with move
    show hiris at left
    with move
    show edalla:
        xalign 1.5
    with move
    show edalla at right
    with move
    ppElf "Je tiens à m’excuser pour les propos que j’ai tenu."
    ppSirene "Ne vous en faîtes pas, je vous pardonne."
    jump conseil_ambassade_excuse

label conseil_ambassade_excuse:
    hide edalla
    show morgon:
        xalign 1.5
    with move
    show morgon:
        xalign 0.75
    with move
    show callyon:
        xalign 1.5
    with move
    show callyon at right
    with move
    show hiris:
        xalign -0.5
    with move
    show hiris at left
    with move

    roiSirene "Nous sommes réunis aujourd'hui dans l’objectif de consolider une paix durable."
    reineElf "Tout à fait mon cher ami, nous sommes ici pour souhaiter l’union entre nos enfants respectifs."
    jump choix_mariage_goodEnding

label choix_mariage_goodEnding:
    menu:
        "Déclarer sa flamme à Edalla":
            jump fin_joyeuse
        "Accepter le mariage avec le Metilay":
            jump finMariageArrange_elf

label fin_joyeuse:
    show callyon:
        xalign 1.5
    with move
    hide callyon
    show edalla:
        xalign 1.5
    with move
    show edalla at right
    with move
    ppElf "Veuillez pardonner mon insolence mais je souhaiterais demander la main de la princesse Edalla."
    roiSirene "Si cela convient à ma fille, je n’y vois pas d’inconvénient."
    ppSirene "J’accepte d'épouser la princesse Hiris."
    n "Et ils vécurent heureux et eurent beaucoup d’enfants."

    scene credits
    play music "audio/romantique.mp3" fadeout 2.0
    pause 360
    return

label conseil_ambassade_nonExcuse:
    n "Les deux familles royales se réunissent dans l’ambassade et commence alors une discussion des plus importantes."
    roiSirene "Princesse des Tyrriens, fille de Callyon, j’ai ouï-dire ton désaccord envers cette union qui a pour but, je vous le rappelle, d’unir nos deux familles."
    jump ambassadeNonExcuses_elf

label ambassadeNonExcuses_elf:
    menu:
        roiSirene "Est-ce vrai ?"
        "Acquiescer et s'excuser":
            jump excuse_elf 
        "Acquiescer et ne pas s'excuser":
            jump finGuerre_elf

label finGuerre_elf:
    #transition et mise en scène
    ppElf "Je refuse de me marier avec un inconnu."
    roiSirene "Je vois. Dans ce cas la trêve sera rompue demain à l’aube."
    roiSirene "Veuillez quitter la ville."
    reineElf "Tu déshonores la famille, tu me déçois."

    n "Le peuple d'Océanos rompue la trêve et démarra les hostilités envers Tyrria le lendemain à l'aube."

    scene credits
    play music "audio/drama_2.mp3" fadeout 2.0
    pause 360

    return

label excuse_elf:
    ppElf "Je confirme avoir énoncée ces propos."
    ppElf "Je plussoie par aileurs qu'ils n'étaient pas appropriés et je m'en excuse."
    ppElf "J'étais encore un peu sous le choc d'apprendre une chose si importante sans avoir été concertée."
    ppElf "Je peux alors vous dire qu'il n'y a pas de problème concernant l'union de nos deux familles par un mariage."
    roiSirene "Qu'entendez-vous par un mariage ?"
    jump choix_mariage_badEnding

label choix_mariage_badEnding:
    menu:
        "Déclarer sa flamme à Edalla":
            jump fin_triste
        "Accepter le mariage avec le Metilay":
            jump MariageArrange_elf

label fin_triste:
    roiSirene "Si cela convient à ma fille, je n’y vois pas d’inconvénient."
    ppSirene "Je refuse mais j’accepte de lui donner mon amitié pour un monde de paix qui grandira dans la tranquillité et la sérénité."

    n "Edalla est en visite de courtoisie sur le territoire elfique pour retrouver sa nouvelle amie Hiris."
    n "Afin de lui rendre la pareille, elle lui fait visiter la ville à son tour."
    n "Cependant, un civil n’ayant pas pu pardonner aux peuple d’Océanos pour les morts qu’ils leurs ont apporté, aperçu la princesse sirène aux côtés de Hiris."
    n "Il bandit alors son arc et tira une flèche en plein cœur d’Edalla et c’est alors qu’elle mourut dans les bras de son amie en pleure."

    n "En apprenant la nouvelle, le peuple d'Océanos annula le traité de paix et démarra les hostilités envers Tyrria."

    scene credits
    play music "audio/drama_2.mp3" fadeout 2.0
    pause 360
    return

label MariageArrange_elf:
    roiSirene "Nous sommes réunis aujourd'hui dans l’objectif de consolider une paix durable."
    reineElf "Tout à fait mon cher ami, nous sommes ici pour souhaiter l’union entre enfants respectifs."
    pause 1
    princeSirene "Dame Hiris, acceptez-vous de me prendre pour époux ?"
    jump choix_mariage_edallaContre

label choix_mariage_edallaContre:
    menu:
        "Déclarer sa flamme à Edalla":
            ppElf "Veuillez pardonner mon insolence mais je souhaiterais demander la main de la princesse Edalla."
            jump fin_triste
        "Accepter le mariage avec le Metilay":
            jump finMariageArrange_elf

label finMariageArrange_elf:
    ppElf "Oui, je le veux."
    roiSirene "Je vous déclare mari et femme"

    n "Ils vécurent plus ou moins heureux et eurent des enfants."

    scene credits
    play music "audio/drama_1.mp3" fadeout 2.0
    pause 360

    return

    