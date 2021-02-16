screen qte:

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte')])
    # key trigger_key action ( Play("sound", "sounds/hit.mp3"), Return(1) ) <-- joue un son de réussite

    vbox:
        xalign x_align
        yalign y_align
        spacing 25

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36
            outlines [(2,"#000000",0,0)]

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"