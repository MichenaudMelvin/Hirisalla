label rencontrePrincesse:
    #Notify("Chapitre 3")
    scene bg locauxSirene
    ppSirene "Saluuut"
    ppSirene "jme présente je suis une sirene"
    ppSirene "blabla"
    ppElf "ok"
    ppSirene "c quoi ton avis sur ce mariage"
    menu:
        "aller en ville":
            jump discutionVille_elf
        "Rester dans la chambre":
            jump discutionChambre_elf

label discutionVille_elf:
    ppSirene "ah oausi nik les vilageois"
    ppElf "ouais carrement"
    menu:
        "Ah ouais trop stylé votre ville de poisson":
            jump vieDePrincesse_elf
        "On va voir le prince ?":
            jump dialogueSurPrinces_elf

label discutionChambre_elf:
    ppSirene "on parle de truc politiques"
    ppElf "ah ouais trop relou l'armé"
    menu:
        "On continue à parler en ville ?":
            ppElf "On continue à parler en ville ?"
            jump discutionVille_elf
        "Continuer la discution":
            ppElf "ok je sui pas d'accord avec toa"
            ppSirene "ah bah si c'est comme ça"
            ppSirene "tu hors de ma vue"
            #faire une transition
            jump excusesPrincesse_elf
    
label vieDePrincesse_elf:
    $ qteDragueReussi = True
    ppSirene "ouais je sais pas de quoi on peut parler"
    ppElf "bah ferme ta gueule"
    jump ambassade_elf

label dialogueSurPrinces_elf:
    $ qteObservationReussi = True
    ppElf "ouais nik les princes"
    ppSirene "ouais carrement"
    jump ambassade_elf

label excusesPrincesse_elf:
    menu:
        reineElf "Tu t'excuse ?"
        "Oui":
            jump ambassadeExcuses_elf
        "Non":
            jump ambassadeNonExcuses_elf