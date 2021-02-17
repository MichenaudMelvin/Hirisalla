label rencontrePrincesse_sirene:
    #Notify("Chapitre 3")
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

    ppElf "Saluuut"
    ppElf "jme présente je suis une sirene"
    ppElf "blabla"
    ppSirene "ok"
    ppElf "c quoi ton avis sur ce mariage"
    menu:
        "On va en ville ?":
            ppSirene "On va en ville ?"
            jump discutionVille_sirene
        "On parle politique ?":
            ppSirene "On parle politique ?"
            jump discutionPolitique_sirene
        "On parle de notre vie ?":
            ppSirene "On parle de notre vie ?"
            jump vieDePrincesse_sirene

label discutionVille_sirene:
    scene bg villeElf
    with fade
    ppElf "ah oausi nik les vilageois"
    ppSirene "ouais carrement"
    menu:
        "On stalk les princes ?":
            jump dialogueSurPrinces_sirene
        "Mon amie amma peut observer les princes":
            jump qteTortue_sirene

label discutionPolitique_sirene:
    ppElf "on parle de truc politiques"
    ppSirene "ah ouais trop relou l'armé"
    menu:
        "On continue à parler en ville ?":
            ppSirene "On continue à parler en ville ?"
            jump discutionVille_sirene
        "Sortir de la pièce":
            ppSirene "ok je sui pas d'accord avec toa"
            ppElf "ah bah si c'est comme ça"
            ppElf "tu hors de ma vue"
            #faire une transition
            jump excusesPrincesse_sirene

label vieDePrincesse_sirene:
    $ qteDragueReussi = True
    ppElf "ouais je sais pas de quoi on peut parler"
    ppSirene "bah ferme ta gueule"
    scene bg ambassadeElf
    with fade
    jump discution_sirene

label qteTortue_sirene:
    $ qteObservationReussi = True
    ppSirene "cimer Amma, ta bien stalk les princes"
    jump discution_sirene


label dialogueSurPrinces_sirene:
    ppSirene "ouais nik les princes"
    ppElf "ouais carrement"
    scene bg ambassadeElf
    with fade
    jump discution_sirene

label excusesPrincesse_sirene:
    roiSirene "Tu t'excuse ?"
    ppSirene "Oui..."
    jump discution_sirene