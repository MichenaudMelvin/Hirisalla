label pdv_elf:
    
    ppElf "Histoire de l'elf"
    menu:
        ppElf "chapitre deux quelle discution : "
        "avec l'ami":
            jump discution_centaure
        "avec la reine":
            jump discution_reine
    
    return

label discution_centaure:
    menu:
        centaure "Tu acepterais de te sacrifier pour ta patrie ?"
        "Oui":
            jump info_rdv_reine
        "Non":
            jump info_rdv_centaure

label discution_reine:
    reineElf "Wesh"
    reineElf "cest un dialogue"
    jump info_rdv_reine

label info_rdv_centaure:
    centaure "OK"
    ppElf "c rigolo"
    jump plage

label info_rdv_reine:



label plage:
