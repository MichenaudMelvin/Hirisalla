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
    $ arr_keys = ["a", "c", "e", "K_UP", "K_SPACE"]

    call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    while cont == 1:
        call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        # to repeat the qte events until it is missed

    #play sound "sounds/miss.mp3" <-- joue un son de fail
    ppElf "Tu as {b}perdu{/b}"

    return