label choix_elf:
    scene bg elf   
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
            jump interrogatif
        "Lui faire confiance":
            jump confiance

label interrogatif:
    ppElf "Vu ton visage, tu ne me cacherais pas quelque chose ?"
    centaure "Mais non, ne t'en fais pas, fais moi confiance."

    menu:
        "Lever le ton":
            jump colere
        "Être suspicieux":
            jump suspicion
        "Avoir confiance":
            jump confiance

label confiance:
    ppElf "Très bien, merci Garkiel."
    ppElf "Dans ce cas, je vais y aller."
    centaure "Super, bon courage, à demain !"
    play sound "audio/depart_centaure.mp3"
    pause 3
    stop sound
    n "Vous vous dirigez vers votre maison à l'heure demandée."
    jump rencontre_famille_prevu

label colere:
    ppElf "Dis-moi, tu sais très bien que je déteste qu'on ne me dise pas clairement les choses."
    centaure "Je ne devais rien te dire, tu es toujours aussi têtue..."
    centaure "La reine a décidé de te marier avec le prince d'Océanos."
    ppElf "Tu te fous de moi j'espère."
    centaure "Il faut que j'y aille, désolé !"

    play sound "audio/depart_centaure.mp3"
    pause 3
    n "Garkiel s'en va au galop."  
    show centaure:
        xalign 1.5
    with move
    hide centaure
    stop sound
    n "Vous vous dirigez vers votre maison en furie."
    show hiris:
        xalign -0.5
    with move
    hide hiris
    jump rencontre_famille_avance
    return

label suspicion:
    ppElf "C'est vrai ? Tu agis vraiment bizarrement."
    centaure "Oui, c'est vrai, ne t'inquiète pas."
    ppElf "Gare à toi si tu m'as menti, tu vas le regretter."
    jump rencontre_famille_prevu

label rencontre_famille_prevu_elf:
    stop music fadeout 2.0
    play music "audio/theme_elfe.mp3" fadeout 2.0
    scene ambassade
    with fade  
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
    reineElf "Tu es pile à l'heure ma fille !"
    reineElf "Il faut que je t'explique ce qu'il va se passer."
    reineElf "Nous avons besoin de toi pour arrêter cette guerre qui a déjà bien trop durée."
    reineElf "Tu seras la future femme du Prince d'Océanos."
    menu :
        "Être en désaccord":
            jump desaccord
        "Se résigner":
            jump resignation

label desaccord:
    ppElf "C'est en aucun cas ce dont j'ai envie Mère !"
    reineElf "Tu n'as pas le choix, c'est la seule solution possible."
    jump tableau_prince

label resignation:
    ppElf "Et il n'y a vraiment aucun autre moyen d'établir la paix ?"
    reineElf "Non aucun, je suis désolée de devoir te forcer."
    jump tableau_prince

label rencontre_famille_avance_elf:
    stop music fadeout 2.0
    play music "audio/theme_elfe.mp3" fadeout 2.0
    scene ambassade 
    with fade
    show hiris:
        xalign -0.5
    with move
    show hiris at left
    show callyon:
        xalign 1.5
    show callyon at right
    with move
    reineElf "Tu es déjà là ma fille ?"
    reineElf "Que me vaut ta visite si précipitée ?"
    menu:
        "Lui dire ce que vous savez":
            jump description_mariage
        "Lui dire subtilement que vous êtes au courant":
            jump description_mariage

label description_mariage_elf:
    ppElf "Je sais ce que vous avez prévu de faire de moi !"
    reineElf "On a pas le choix ma chérie, c'est pour sauver notre royaume."
    reineElf "Tu dois te marier pour tous nous sauver !"
    reineElf "Et puis le prince est magnifique !"
    jump tableau_prince

label tableau_prince:
    reineElf "Regarde le tableau !"
    menu : 
        "Critiquer":
            jump contradiction
        "Complimenter subtilement":
            jump accord

label contradiction:           
    ppElf "Mais je m'en fiche, il a des écailles, des oreilles en forme de nageoire, c'est affreux !"
    ppElf "Je ne pourrais jamais accepter cela."
    jump discution_centaure

label accord_elf:
    ppElf "Si c'est la seule solution, on va dire que cela aurait pu être pire."
    jump discution_reine_elf