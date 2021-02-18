label choix_sirene:
    scene bg sirene
    with fade
    show Edalla:
        xalign -0.5
    with move
    show amma:
        xalign 1.5
    with move
    show Edalla at left
    with move
    n "La princesse des Océanos, Edalla s'en alla rejoindre son amie qu'elle considairait comme sa pettie sœur, la jeune tortue Amma."
    show amma at right
    with move
    tortue "Salutations princesse ! Vous allez b-b-bien ?"
    ppSirene "Bien et toi, Amma ?"
    tortue "Bien, m-m-merci, j'ai m-messire le-le Roi qui m'a d-demandé d-de vous passer un message."
    ppSirene "Je t'écoute Amma."
    tortue "Dans une heure messire le-le Roi veut vous voir dans la salle du trône."
    ppSirene "Tu ne connais pas la raison ?"

    menu:
        tortue "… N… N-Non."
        "Accepter et aller se changer":
            ppSirene "D'accord, je vais aller me changer de ce pas."
            jump confiance_sirene
        "Menacer Amma":
            ppSirene "Tu n'as pas intérêt à mentir à ta grande sœur."
            jump interrogatif_sirene

label interrogatif_sirene:
    menu:
        tortue "Je ne te… mens p-p-pas, p-princesse Edalla."
        "Faire confiance":
            ppSirene "D'accord, parce que je te fais confiance, rejoins moi à ma chambre dans trente minutes"
            jump confiance_sirene
        "Douter":
            ppSirene "Vraiment ?"
            jump rencontre_famille_avance_sirene

label confiance_sirene:
    show Edalla:
        xalign -0.5
    with move
    show amma:
        xalign 1.5
    with move

    scene bg ambassadeSirene
    show Morgon:
        xalign 1.5
    with move
    show Edalla at left
    with move
    show Morgon at right
    with move

    roiSirene "Ma fille, vous voilà !"
    ppSirene "Père, vous vouliez me voir ?"
    roiSirene "Oui tout à fait, j'ai des affaires à vous annoncez."
    roiSirene "Premièrement, nous allons à la capitale des Tyrriens, où nous aurons une session avec la Famille royale."
    roiSirene "Deuxièmement, nous avons décidés de proposer à cette session, un mariage entre toi et le prince Keidal tout ça pour retrouver la paix entre nous."
    ppSirene "Un mariage ?!"
    ppSirene "Quand avez vous pris cette décision ?"
    roiSirene "Nous l'avons pris avec le prince et le conseil des sages."
    ppSirene "Tout cela sans me demander mon avis ?!"
    roiSirene "Nous avons pensés aux citoyens en priorité, et cela fait partie de ta fonction de princesse, tu ne dois pas oublier que tu représentes notre peuple."
    ppSirene "Si cela peut offrir une nouvelle paix à notre famille… j'accepte"
    roiSirene "Je m'en excuse mais nous avons dû faire ce choix très rapidement." 
    roiSirene "Mais s'il devient irrespectueux ou il devient un cauchemar pour toi, tu auras le droit de rompre ce mariage." 
    show Morgon:
        xalign 1.5
    with move
    show Edalla:
        xalign -0.5
    with move
    hide Morgon
    hide Edalla
    jump discution_roi_sirene

label rencontre_famille_prevu_sirene:
    scene bg sirene
    with fade
    show Edalla triste:
        xalign -0.5
    with move
    show Morgon:
        xalign 1.5
    with move
    show Edalla triste at left
    with move
    show Morgon at right
    with move

    roiSirene "Vous êtes pile à l'heure ma fille !"
    roiSirene "Il faut que je vous explique ce qu'il va se passer."
    roiSirene "Nous avons besoin de vous pour faire un mariage arrangé."
    roiSirene "Nous devons avoir la paix entre les deux royaumes, vous serez la future femme du Prince des Elfes."
    jump accord_sirene

label rencontre_famille_avance_sirene:
    tortue "D'accord… mais tu ne te fâches p-pas."
    tortue "J'ai entendu messire le Roi d-dire que tu… p-pourrais être mariée au p-prince elfe."
    ppSirene "Comment ?!"
    tortue "Mais j'aurais p-p-pu mal entendre, p-princesse."
    ppSirene "Comment ont-ils décidés une chose pareille sans me consulter avant ?"
    tortue "Je ne sais p-pas p-p-princesse."
    show amma:
        xalign 1.5
    with move
    show Edalla:
        xalign -0.5
    with move
    hide Amma
    hide Edalla

    scene bg ambassadeSirene
    with fade
    show Edalla:
        xalign -0.5
    with move
    show Edalla at left
    with move
    show Morgon:
        xalign 1.5
    with move
    show Morgon at right
    with move
    #sirene triste
    roiSirene "Ma fille ? Vous êtes en avance, pourquoi une arrivée aussi précipitée."
    ppSirene "Attendez, Père, pourquoi une telle décision sans me consulter avant ?"
    roiSirene "Ah, vous sais déjà une des nouvelles que j'allais t'annoncer. Mais qui vous a annoncé cette nouvelle ?"
    show amma:
        xalign -0.5
    with move
    show amma:
        xalign 0.2
    with move
    tortue "C'est… m-moi"
    tortue "Désolé, mon Roi, j'ai innocemment entendu votre conversation avec le prince, et je n'ai pas réussi à le garder secret."
    tortue "Je vous p-prie de m'excuser."
    roiSirene "J'accepte vos excuses, mais pour cette fois-ci ma petite Amma."
    tortue "M-Merci !"
    show amma:
        xalign -0.5
    with move

    roiSirene "Donc, nous n'avons pas pris cette décision à la légère."
    roiSirene "Nous devons arrêter cette guerre avant que tout autre civil meurt, et cela nous apportera d'autres côté positif, et c'est un mal pour un bien." 
    roiSirene "Je sais que vous êtes assez intelligente pour comprendre cette décision."
    #sirene triste
    ppSirene "Je comprend bien que vous avez des arguments pour justifier ce choix et je ne peux vous dire non."
    ppSirene "La survie de notre peuple en dépend, mais j'aurais voulu être consultée et être prévenue."
    roiSirene "Je m'en excuse mais nous avons dû prendre cette décision très rapidement."
    roiSirene "Demain nous allons à la capitale des Tyrriens, et rencontrer la Famille royale, de plus il nous a envoyés un tableau du prince."
    menu: 
        "Se lamenter":
            ppSirene "…"
            show Edalla:
                xalign -0.5
            with move
            hide Edalla
            show Morgon:
                xalign 1.5
            with move
            hide roiSirene
            jump discution_tortue_sirene
        "Regarder le tableau":
            ppSirene "{i}Ce tableau présente un charmant jeune homme dont les traits laissent dégager une beauté masculine et une virilité accrue.{/i}" 
            ppSirene "{i}Habillé soigneusement et dégageant une aura de personne ferme et sérieuse.{/i}"
            jump discution_roi_sirene