label pdv_elf:
    
    n "Histoire de l'elf"

    h "Bonsoir"

    screen button_hover_example():
        frame:
            xalign 0.5 ypos 50
            button:
                action Notify(_("You clicked the button."))
                hovered Notify(_("You hovered the button."))
                unhovered Notify(_("You unhovered the button."))
                text _("Click me.") style "button_text"
    
    h "BBBBBBB"
    return