label choix_elf:
    scene bg elf    
    play sound "audio/galop.ogg"
    pause 3
    stop sound
    #play music "audio/test_music.mp3"
    centaure "Salut Hiris ! J'ai une convocation de la Reine pour toi !"
    ppElf "Je t'écoute Garkiel"
    centaure "Tu as rendez-vous avec la Reine dans une heure, elle semble avoir quelque chose d'important à te dire."

    menu:
        "Vu ton visage, tu ne me cacherais pas quelque chose ?":
            jump interrogatif
        "D'accord, pas de soucis, je te fais confiance.":
            jump confiance

label interrogatif:
    centaure "Mais non, ne t'en fais pas, fais moi confiance."

    menu:
        "Dis-moi, tu sais très bien que je déteste qu'on ne me dise pas clairement les choses.":
            jump colere
        "C'est vrai ? Tu agis vraiment bizarrement.":
            jump suspicion
        "Bon d'accord, je te fais confiance.":
            jump confiance

label confiance:
    centaure "Super, bon courage, à demain !"
    #play sound "audio/galop.ogg"
    pause 3
    #stop sound
    n "Vous vous dirigez vers votre maison à l'heure demandée."
    jump rencontre_famille_prevu

label colere:
    centaure "Je ne devais rien te dire, tu es toujours aussi têtue..."
    centaure "La reine a décidé de te marier avec le prince d'Océanos."
    ppElf "Tu te fous de moi j'espère."
    centaure "Il faut que j'y aille, désolé !"

    #play sound "audio/galop.ogg"
    pause 3
    n "Garkiel s'en va au galop."  
    #stop sound
    n "Vous vous dirigez vers votre maison en furie."

    jump rencontre_famille_avance
    
label suspicion:
    centaure "Oui, c'est vrai, ne t'inquiète pas."
    ppElf "Gare à toi si tu m'as menti, tu vas le regretter."
    jump rencontre_famille_prevu

label rencontre_famille_prevu:
    reineElf "Tu es pile à l'heure ma fille !"
    reineElf "Il faut que je t'explique ce qu'il va se passer."
    reineElf "Nous avons besoin de toi pour faire un mariage arrangé."
    reineElf "Nous devons avoir la paix entre les deux royaumes, tu seras la future femme du Prince des Sirènes."
    return

label rencontre_famille_avance:
    reineElf "Tu es déjà là ma fille ?"
    reineElf "Que me vaut ta visite si précipitée ?"
    menu : 
        "Je sais que vous voulez me marier avec le Prince des Sirènes":
            jump description_mariage
        "On m'a expliqué ce que vous voulez faire de moi !":
            jump description_mariage

label description_mariage:           
    ppElf "Je sais ce que vous avez prévu de faire de moi avec le Prince des Sirènes !"
    reineElf "On a pas le choix ma chérie, c'est pour sauver notre royaume."
    reineElf "Tu dois te sacrifier pour tous nous sauver !"
    reineElf "Et puis le prince est magnifique ! *Description du Prince*"
    menu : 
        "Mais je m'en fiche !":
            jump contradiction
        "Il n'a pas l'air si mal...":
            jump accord

label contradiction:           
    ppElf "Mais je m'en fiche, il a des écailles, des oreilles en forme de nageoire, c'est affreux !"
    ppElf "Je ne pourrais jamais accepter cela."
    jump discution_centaure

label accord:
    ppElf "J'espère que la description est vraie Mère."
    jump discution_reine