<<<<<<< Updated upstream
label discution_centaure_elf:
    scene bg elf
=======
label discution_centaure: 
    scene ville_elfe
>>>>>>> Stashed changes
    with fade
    show hiris_angry:
        xalign -0.5
    with move
    show hiris_angry at left
    with move
    show centaure:
        xalign 1.5
    with move
    show centaure at right
    with move
    centaure "Je ne suis pas non plus d'accord que ce soit toi qui ai le devoir de te sacrifier pour les autres."
    centaure "Mais nous n'avons pas le choix, tu peux tous nous sauver."
    menu:    
        centaure "Serais-tu capable de te marier pour le bien de tous ?"
        "Se résigner":
            play sound "audio/galop.ogg"
            pause 3
            show centaure:
                xalign 1.5
            with move
            hide centaure
            jump discution_reine_elf
        "Refuser":
            jump info_rdv_centaure_elf

label discution_reine_elf:
    stop sound
    scene ambassade_elfe
    with fade
    show Hiris:
        xalign -0.5
    with move
<<<<<<< Updated upstream
    show Hiris at left
    show callyon:
=======
    show hiris at left
    show callyon_normal:
>>>>>>> Stashed changes
        xalign 1.5
    with move
    show callyon_normal at right
    with move
    ppElf "J'y ai réfléchis ma Reine."
    reineElf "Je vous écoute."
    ppElf "J'accomplirai mon devoir afin d’apporter la paix, la sécurité et la prospérité à notre peuple."
    reineElf "Merci de ton dévouement, nous rejoindrons la plage dans un premier temps puis nous irons dans leur village par convoi royal."
    ppElf "Leur village se situe sous l’eau, comment sommes-nous censés respirer ?"
    reineElf "De ce que j’ai appris, nous n’aurons pas à aller sous l’eau, le village est protégé par une bulle d’air"
    ppElf "Je vois, je vous retrouve demain sur la plage pour le départ."
    jump plage

label info_rdv_centaure:
    ppElf "Je ne peux pas accepter un tel destin, je refuse de me marier avec lui."
    centaure "Je suis de ton avis, mais ce sont les ordres de la reine, tu n'as pas le choix."
    centaure "Le rendez-vous aura lieu dans leur cité."
    centaure "Le premier point de ralliement sera sur la plage."
    centaure "Nous pourrons ensuite accéder à leur cité sous-marine."
    ppElf "Et comment sommes-nous supposés respirer sous l'eau ?"
    centaure "Ne t'en fais pas, d'après les dires, nous n'aurons pas besoin d'aller sous l'eau."
    jump plage_elf

<<<<<<< Updated upstream
label plage_elf:
    scene bg plage
    show Hiris at left
=======
label plage:
    scene ville_sirene
    show hiris at left
>>>>>>> Stashed changes
    with fade
    show Hiris at left
    ppElf "{i} Il semblerait que je sois arrivée au point de rendez-vous. {/i}"
    show hiris_surprise at left
    hide hiris
    ppElf "{i} Woaw, voilà à quoi ressemble la cité des Sirènes. {/i}"
    n "Vous vous dirigez vers la cité des Sirènes à l'aide du convoi royal."
    play music "audio/theme_sirene.mp3" fadeout 2.0
    scene ambassade_sirene
    show hiris at left
    with fade  
    pause 2
    show metilay_normal:
        xalign 1.5
    with move
    show metilay_normal:
        xalign 0.85
    with move
    show morgon_normal:
        xalign 1.5
    with move
    show morgon_normal at right
    with move

    menu:
        "Bonjour, je me présente, Hiris.":
            jump bonjour_hiris_elf
        "Bonjour messieurs, ravi de faire votre connaissance.":
            jump bonjour_enchante_elf

label bonjour_hiris_elf:
    ppElf "Bonjour je me présente, Hiris, la princesse des Elfes en personne."
    jump presentationFamilleSirene_elf

label bonjour_enchante_elf:
    ppElf "Bonjour messieurs, ravi de faire votre connaissance."
    jump presentationFamilleSirene_elf

label presentationFamilleSirene_elf:
    roiSirene "Bonjour, enchanté mademoiselle, je suis Morgon, le roi d'Océanos."
    princeSirene "Echanté de faire votre connaissance, ma gente demoiselle, je suis Metilay, le prince de la même cité."
    menu:
        "Le prince est aussi ravissant que sur le tableau.":
            jump ecouteConversation_elf
        "Le prince n'est pas aussi attrayant que ce que j'imaginais.":
            jump ecouteConversation_elf

label ecouteConversation_elf:
    roiSirene "Comme mon messager vous l’a transmis, je suis d’avis que cette guerre a déjà bien assez durée."
    roiSirene "C'est alors que j'ai pensé que le moyen d'y mettre un terme définitivement était un mariage arrangé qui unirait nos clans pour l’éternité."
    princeSirene "Par ailleurs, la princesse de cette Cité aurait aimé vous rencontrer en privé." 
    jump rencontrePrincesse_elf