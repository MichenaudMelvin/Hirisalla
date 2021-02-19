label choix_elf:
    window hide
    scene chapitreun
    with fade
    pause 2
    
    scene ville_elfe  
    with fade
    show hiris:
        xalign -0.5
    with move
    show hiris at left
    with move
    show centaure:
        xalign 1.5
    with move
    show centaure at right
    with move
    play music "audio/theme_elfe.mp3" fadeout 2.0
    play sound "audio/arrive_centaure.mp3"
    pause 3
    stop sound
    centaure "Salut Hiris ! J'ai une convocation de la Reine pour toi !"
    ppElf "Je t'écoute Garkiel"
    centaure "Tu as rendez-vous avec la Reine dans une heure, elle semble avoir quelque chose d'important à te dire."

    menu:
        "Lui poser une question à propos du rendez-vous":
            jump interrogatif_elf

        "Lui faire confiance":
            jump confiance_elf

label interrogatif_elf:
    ppElf "Vu ton visage, tu ne me cacherais pas quelque chose ?"
    centaure "Mais non, ne t'en fais pas, fais moi confiance."

    menu:
        "Lever le ton":
            jump colere_elf
        "Être suspicieux":
            jump suspicion_elf
        "Avoir confiance":
            jump confiance_elf

label confiance_elf:
    ppElf "Très bien, merci Garkiel."
    ppElf "Dans ce cas, je vais y aller."
    centaure "Super, bon courage, à demain !"
    n "Vous vous dirigez vers votre maison à l'heure demandée."
    show hiris:
        xalign -0.5
    with move
    play sound "audio/depart_centaure.mp3"
    show centaure:
        xalign 1.5
    with move
    pause 3
    stop sound
    jump rencontre_famille_prevu_elf

label colere_elf:
    ppElf "Dis-moi, tu sais très bien que je déteste qu'on ne me dise pas clairement les choses."
    centaure "Je ne devais rien te dire, tu es toujours aussi têtue…"
    centaure "La reine a décidé de te marier avec le prince d'Océanos."
    hide hiris
    show hiris_angry at left
    ppElf "Tu te fous de moi j'espère."
    centaure "Il faut que j'y aille, désolé !"
    show centaure:
        xalign 1.5
    with move
    hide centaure
    play sound "audio/depart_centaure.mp3"
    pause 3
    n "Garkiel s'en va au galop."  
    stop sound
    n "Vous vous dirigez vers votre maison en furie."
    show hiris_angry:
        xalign -0.5
    with move
    hide hiris_angry
    jump rencontre_famille_avance_elf

label suspicion_elf:
    ppElf "C'est vrai ? Tu agis vraiment bizarrement."
    centaure "Oui, c'est vrai, ne t'inquiète pas."
    ppElf "Gare à toi si tu m'as menti, tu vas le regretter."
    show hiris:
        xalign -0.5
    with move
    play sound "audio/depart_centaure.mp3"
    show centaure:
        xalign 1.5
    with move
    pause 3
    stop sound
    jump rencontre_famille_prevu_elf

label rencontre_famille_prevu_elf:
    stop music fadeout 2.0
    play music "audio/theme_elfe.mp3" fadeout 2.0
    scene ambassade_elfe
    with fade  
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
    reineElf "Tu es pile à l'heure ma fille !"
    reineElf "Il faut que je t'explique ce qu'il va se passer."
    reineElf "Nous avons besoin de toi pour arrêter cette guerre qui a déjà bien trop durée."
    reineElf "Tu seras la future femme du Prince d'Océanos."
    menu :
        "Être en désaccord":
            jump desaccord_elf
        "Se résigner":
            jump resignation_elf

label desaccord_elf:
    $ desaccordHiris = True
    show hiris_angry at left
    hide hiris
    ppElf "C'est en aucun cas ce dont j'ai envie Mère !"
    show callyon_colere at right
    hide callyon_normal
    reineElf "Tu n'as pas le choix, c'est la seule solution possible."
    jump tableau_prince_elf

label resignation_elf:
    $ desaccordHiris = False
    ppElf "Et il n'y a vraiment aucun autre moyen d'établir la paix ?"
    reineElf "Non aucun, je suis désolée de devoir te forcer."
    jump tableau_prince_elf

label rencontre_famille_avance_elf:
    stop music fadeout 2.0
    play music "audio/theme_elfe.mp3" fadeout 2.0
    scene ambassade_elfe 
    with fade
    show hiris_angry:
        xalign -0.5
    with move
    show hiris_angry at left
    show callyon_normal:
        xalign 1.5
    show callyon_normal at right
    with move
    reineElf "Tu es déjà là ma fille ?"
    reineElf "Que me vaut ta visite si précipitée ?"
    jump description_mariage_elf

label description_mariage_elf:
    ppElf "Je sais ce que vous avez prévu de faire de moi !"
    reineElf "On a pas le choix ma chérie, c'est pour sauver notre royaume."
    reineElf "Tu dois te marier pour tous nous sauver !"
    reineElf "Et puis le prince est magnifique !"
    hide hiris_angry
    show hiris at left
    jump tableau_prince_elf

label tableau_prince_elf:
    menu : 
        reineElf "Regarde le tableau du prince !"
        "Critiquer":
            jump contradiction_elf
        "Complimenter subtilement":
            if (desaccordHiris == True):
                show hiris at left
                hide hiris_angry
                show callyon_normal at right
                hide callyon_colere
                jump accord_elf
            else:
                jump accord_elf

label contradiction_elf:   
    show hiris_angry at left        
    hide hiris
    ppElf "Mais je m'en fiche, il a des écailles, des oreilles en forme de nageoire, c'est affreux !"
    ppElf "Je ne pourrais jamais accepter cela."
    show hiris_angry:
        xalign -0.5
    with move
    jump discution_centaure_elf

label accord_elf:
    ppElf "Si c'est la seule solution, on va dire que cela aurait pu être pire."
    show hiris:
        xalign -0.5
    with move
    show callyon_normal:
        xalign 1.5
    with move

    window hide
    scene chapitredeux
    with fade
    pause 2

    jump discution_reine_elf