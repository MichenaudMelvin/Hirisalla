label pdv_elf:
    
    ppElf "Histoire de l'elf"

    menu:
        ppElf "Tu veux faire des QTE ?"
        "Oui":
            jump qte
        "Non":
            return

label qte:
    $ cont = 0
    $ arr_keys = ["K_a", "K_c", "K_e", "K_UP", "K_SPACE"]

    call qte_setup(0.5, 1, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.5)

    while cont == 1:
        call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)

    #play sound "sounds/miss.mp3" <-- joue un son de fail
    ppElf "Tu as {b}perdu{/b}"

    return
