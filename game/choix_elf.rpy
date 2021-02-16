label choix_elf:
    scene bg elf    
    n "Vous allez être téléporter dans l'univers des elfs"
    ppelf "Où suis-je ?"

    menu:
        "J'ai l'impression que tu me caches un truc.":
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
    jump rencontre_famille_prevu

label colere:
    centaure "Je ne devais rien te dire, tu es toujours aussi têtue..."
    centaure "Un mariage arrangé a été organisé entre toi et le Prince des Sirènes."
    ppelf "Tu te fous de moi j'espère."
    centaure "Il faut que j'y aille, désolé !"

    n "Garkiel s'en va au galop."
    n "Ellipse narrative."

    jump rencontre_famille_avance
    
label suspicion:
    centaure "Oui, c'est vrai, ne t'inquiète pas."
    ppelf "Gare à toi si tu m'as menti, tu vas le regretter."
    jump rencontre_famille_prevu

label rencontre_famille_prevu:
    reineelf "Tu es pile à l'heure ma fille !"
    reineelf "Il faut que je t'explique ce qu'il va se passer."
    reineelf "Nous avons besoin de toi pour faire un mariage arrangé."
    reineelf "Nous devons avoir la paix entre les deux royaumes, tu seras la future femme du Prince des Sirènes."
    return

label rencontre_famille_avance:
    reineelf "Tu es déjà là ma fille ?"
    reineelf "Que me vaut ta visite si précipitée ?"

    menu : 
        "Je sais que vous voulez me marier avec le Prince des Sirènes":
            jump description_mariage
        "On m'a expliqué ce que vous voulez faire de moi !":
            jump description_mariage

label description_mariage:           
    ppelf "Je sais ce que vous avez prévu de faire de moi avec le Prince des Sirènes !"
    reineelf "On a pas le choix ma chérie, c'est pour sauver notre royaume."
    reineelf "Tu dois te sacrifier pour tous nous sauver !"
    reineelf "Et puis le prince est magnifique ! *Description du Prince*"

    menu : 
        "Mais je m'en fiche":
            jump contradiction
        "Il n'a pas l'air si mal...":
            jump accord

label contradiction:           
    ppelf "Mais je m'en fiche, il a des écailles, des oreilles en forme de nageoire, c'est affreux !"
    ppelf "Je ne pourrais jamais accepter cela."
    return
label accord:
    ppelf "J'espère que la description est vraie Mère."
    return



