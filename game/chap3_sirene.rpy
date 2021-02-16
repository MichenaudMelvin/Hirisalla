label rencontrePrincesse_sirene:
    #Notify("Chapitre 3")
    scene bg ambassadeSirene
    with fade

    show Hiris:
        xalign 1.5
    with move
    show Edalla:
        xalign -0.5
    with move
    show Hiris at right
    with move
    show Edalla at left
    with move

    ppSirene "Saluuut"
    ppSirene "jme présente je suis une sirene"
    ppSirene "blabla"
    ppElf "ok"
    ppSirene "c quoi ton avis sur ce mariage"
    menu:
        "aller en ville":
            jump discutionVille_sirene
        "Rester dans la chambre":
            jump discutionChambre_sirene

label discutionVille_sirene:
    scene bg villeSirene
    with fade
    ppSirene "ah oausi nik les vilageois"
    ppElf "ouais carrement"
    menu:
        "Ah ouais trop stylé votre ville de poisson":
            jump vieDePrincesse_sirene
        "On va voir le prince ?":
            jump dialogueSurPrinces_sirene

label discutionChambre_sirene:
    ppSirene "on parle de truc politiques"
    ppElf "ah ouais trop relou l'armé"
    menu:
        "On continue à parler en ville ?":
            ppElf "On continue à parler en ville ?"
            jump discutionVille_sirene
        "Continuer la discution":
            ppElf "ok je sui pas d'accord avec toa"
            ppSirene "ah bah si c'est comme ça"
            ppSirene "tu hors de ma vue"
            #faire une transition
            jump excusesPrincesse_sirene
    
label vieDePrincesse_sirene:
    $ qteDragueReussi = True
    ppSirene "ouais je sais pas de quoi on peut parler"
    ppElf "bah ferme ta gueule"
    scene bg ambassadeSirene
    with fade
    jump ambassadeExcuses_sirene

label dialogueSurPrinces_sirene:
    $ qteObservationReussi = True
    ppElf "ouais nik les princes"
    ppSirene "ouais carrement"
    scene bg ambassadeSirene
    with fade
    jump ambassadeExcuses_sirene

label excusesPrincesse_sirene:
    menu:
        reineElf "Tu t'excuse ?"
        "Oui":
            jump ambassadeExcuses_sirene
        "Non":
            jump ambassadeNonExcuses_sirene