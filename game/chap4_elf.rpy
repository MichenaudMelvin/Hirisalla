label ambassadeExcuses_elf:
    stop music fadeout 2.0
    play music "audio/ambassade.mp3" fadeout 2.0
    scene chambre_sirene
    with fade
    show hiris:
        xalign -0.5
    with move
    show hiris at left
    with move
    show edalla_normal:
        xalign 1.5
    with move
    show edalla_normal at right
    with move
    ppElf "Je tiens à m’excuser pour les propos que j’ai tenu."
    ppSirene "Ne vous en faîtes pas, je vous pardonne."
    jump conseil_ambassade_excuse_elf

label conseil_ambassade_excuse_elf:
    stop music fadeout 2.0
    play music "audio/ambassade.mp3" fadeout 2.0
    show edalla_normal:
        xalign 1.5
    with move
    hide edalla_normal
    show morgon_normal:
        xalign 1.5
    with move
    show morgon_normal:
        xalign 0.75
    with move
    show callyon_normal:
        xalign 1.5
    with move
    show callyon_normal at right
    with move
    show hiris:
        xalign -0.5
    with move
    show hiris at left
    with move
    roiSirene "Nous sommes réunis aujourd'hui dans l’objectif de consolider une paix durable."
    reineElf "Tout à fait mon cher ami, nous sommes ici pour souhaiter l’union entre nos enfants respectifs."
    jump choix_mariage_goodEnding_elf

label choix_mariage_goodEnding_elf:
    menu:
        "Déclarer sa flamme à Edalla":
            jump fin_joyeuse_elf
        "Accepter le mariage avec le Metilay":
            jump finMariageArrange_elf

label fin_joyeuse_elf:
    show callyon_normal:
        xalign 0.75
    with move
    show edalla_normal:
        xalign 1.5
    with move
    show edalla_normal at right
    with move
    ppElf "Veuillez pardonner mon insolence mais je souhaiterais demander la main de la princesse Edalla."
    show callyon_surprise at center
    with move
    hide callyon_normal

    show edalla_surprise at right
    hide edalla_normal
    roiSirene "Si cela convient à ma fille, je n’y vois pas d’inconvénient."
    show edalla_normal at right
    hide edalla_surprise
    show edalla_joie at right
    hide edalla_normal
    ppSirene "J’accepte d'épouser la princesse Hiris."
    show hiris_happy at left
    hide hiris

    n "La princesse Edalla accepta la demande de la princesse Hiris."
    n "La vie des deux princesses est remplie de joie et leur amour fît en sorte que le bien des deux cités ne soit jamais remis en cause à nouveau."
    scene credits
    with fade
    stop music fadeout 2.0
    play music "audio/romantique.mp3" fadeout 2.0
    window hide
    pause 360
    return

label conseil_ambassade_nonExcuse_elf:
    stop music fadeout 2.0
    play music "audio/ambassade.mp3" fadeout 2.0
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

    scene credits
    with fade
    stop music fadeout 2.0
    play music "audio/drama_2.mp3" fadeout 2.0
    n "Le peuple d'Océanos rompue la trêve et démarra les hostilités envers Tyrria le lendemain à l'aube."
    n "La guerre ne s'arrêtera sans doute jamais et sera encore plus meurtrière qu'elle ne l'a jamais été."
    window hide
    pause 360
    return

label excuse_elf:
    ppElf "Je confirme avoir énoncée ces propos."
    ppElf "Je plussoie par aileurs qu'ils n'étaient pas appropriés et je m'en excuse."
    ppElf "J'étais encore un peu sous le choc d'apprendre une chose si importante sans avoir été concertée."
    ppElf "Je peux alors vous dire qu'il n'y a pas de problème concernant l'union de nos deux familles par un mariage."
    roiSirene "Qu'entendez-vous par un mariage ?"
    jump choix_mariage_badEnding_elf

label choix_mariage_badEnding_elf:
    menu:
        "Déclarer sa flamme à Edalla":
            jump fin_triste_elf
        "Accepter le mariage avec le Metilay":
            jump MariageArrange_elf

label fin_triste_elf:
    ppElf "Je souhaiterais prendre pour épouse votre fille, Edalla."
    roiSirene "Si cela convient à ma fille, je n’y vois pas d’inconvénient."
    ppSirene "Je ne peux pas accepter cela en si peu de temps... J’accepte toutefois de lui donner mon amitié pour un monde de paix qui grandira dans la tranquillité et la sérénité."

    scene credits
    with fade
    stop music fadeout 2.0
    play music "audio/drama_2.mp3" fadeout 2.0
    n "Edalla est en visite de courtoisie sur le territoire elfique pour retrouver sa nouvelle amie Hiris."
    n "Afin de lui rendre la pareille, elle lui fait visiter la ville à son tour."
    n "Cependant, un civil, n’ayant pas pu pardonner aux peuple d’Océanos pour les morts qu’ils leurs ont apportés, aperçu la princesse sirène aux côtés de Hiris."
    n "Il bandit alors son arc et tira une flèche en plein cœur d’Edalla et c’est alors qu’elle mourut dans les bras de son amie en pleure."

    n "En apprenant la nouvelle, le peuple d'Océanos annula le traité de paix et démarra les hostilités envers Tyrria."
    window hide
    pause 360
    return

label MariageArrange_elf:
    roiSirene "Nous sommes réunis aujourd'hui dans l’objectif de consolider une paix durable."
    reineElf "Tout à fait mon cher ami, nous sommes ici pour souhaiter l’union entre enfants respectifs."
    pause 1
    princeSirene "Dame Hiris, acceptez-vous de me prendre pour époux ?"
    jump choix_mariage_edallaContre_elf

label choix_mariage_edallaContre_elf:
    menu:
        "Déclarer sa flamme à Edalla":
            ppElf "Veuillez pardonner mon insolence mais je souhaiterais demander la main de la princesse Edalla."
            jump fin_triste
        "Accepter le mariage avec le Metilay":
            jump finMariageArrange_elf

label finMariageArrange_elf:
    show callyon_normal:
        xalign 1.5
    with move
    hide callyon_normal

    show metilay_heureux:
        xalign 1.5
    with move
    show metilay_heureux at right
    with move
    ppElf "J'accepte avec plaisir ce que nous avions prévu."
    roiSirene "J'entend bien."
    roiSirene "Metilay, fils du roi d'Océanos et Prince de la cité du même nom, souhaitez-vous prendre pour épouse Hiris, fille de la Reine de Tyrria et princesse de la cité du même nom ?"
    princeSirene "Oui, je le veux."
    roiSirene "Hiris, fille de la Reine de Tyrria et princesse de la cité du même nom, souhaitez-vous prendre pour épouse Hiris, fils du roi d'Océanos et Prince de la cité du même nom ?"
    ppElf "Oui, je le veux."

    n "La princesse de Tyrria accepta la demande de Metilay, prince d'Océanos."
    n "Leur vie est belle et le restera grâce à la paix se trouvant entre les deux cités."
    n "La princesse ne le montre pas, mais elle regrette de ne pas avoir déclarée sa flamme à la princesse Edalla lorsqu'elle en avait l'occasion."

    scene credits
    with fade
    stop music fadeout 2.0
    play music "audio/drama_1.mp3" fadeout 2.0
    window hide
    pause 360

    return