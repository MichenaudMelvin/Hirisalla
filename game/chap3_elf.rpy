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
            jump discutionVille
        "Rester dans la chambre":
            jump discutionChambre

label discutionVille:
    ppSirene "on parle de truc politiques"
    ppElf "ah ouais trop relou l'armé"
label discutionChambre:

#fin chapitre 2
#debut chapitre 3


