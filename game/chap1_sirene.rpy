label choix_sirene:
    scene bg sirene
    tortue "Salut Hiris ! J'ai une convocation de la Reine pour toi !"
    ppSirene "Je t'écoute Garkiel"
    tortue "Tu as rendez-vous avec la Reine dans une heure, elle semble avoir quelque chose d'important à te dire."

    menu:
        "Vu ton visage, tu ne me cacherais pas quelque chose ?":
            jump interrogatif_sirene
        "D'accord, pas de soucis, je te fais confiance.":
            jump confiance_sirene

label interrogatif_sirene:
    tortue "Mais non, ne t'en fais pas, fais moi confiance."
    menu:
        "Tu es sûre ?":
            jump rencontre_famille_avance_sirene
        "ok":
            jump rencontre_famille_prevu_sirene

label confiance_sirene:
    tortue "Super, bon courage, à demain !"
    n "Vous vous dirigez vers votre maison à l'heure demandée."
    jump rencontre_famille_prevu_sirene

label rencontre_famille_prevu_sirene:
    roiSirene "Tu es pile à l'heure ma fille !"
    roiSirene "Il faut que je t'explique ce qu'il va se passer."
    roiSirene "Nous avons besoin de toi pour faire un mariage arrangé."
    roiSirene "Nous devons avoir la paix entre les deux royaumes, tu seras la future femme du Prince des Sirènes."
    jump accord_sirene

label rencontre_famille_avance_sirene:
    roiSirene "Tu es déjà là ma fille ?"
    roiSirene "Que me vaut ta visite si précipitée ?"
    menu : 
        "Je sais que vous voulez me marier avec le Prince des Sirènes":
            jump description_mariage_sirene
        "On m'a expliqué ce que vous voulez faire de moi !":
            jump description_mariage_sirene

label description_mariage_sirene:
    ppSirene "Je sais ce que vous avez prévu de faire de moi avec le Prince des Sirènes !"
    roiSirene "On a pas le choix ma chérie, c'est pour sauver notre royaume."
    roiSirene "Tu dois te sacrifier pour tous nous sauver !"
    roiSirene "Et puis le prince est magnifique ! *Description du Prince*"
    menu : 
        "Mais je m'en fiche !":
            jump contradiction_sirene
        "Il n'a pas l'air si mal...":
            jump accord_sirene

label contradiction_sirene:           
    ppSirene "Mais je m'en fiche, il a des écailles, des oreilles en forme de nageoire, c'est affreux !"
    ppSirene "Je ne pourrais jamais accepter cela."
    jump discution_tortue_sirene_sirene

label accord_sirene:
    ppSirene "J'espère que la description est vraie Mère."
    jump discution_roi_sirene