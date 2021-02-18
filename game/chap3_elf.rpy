label rencontrePrincesse:
    #Notify("Chapitre 3")
    scene bg ambassadeSirene
    with fade

    show hiris:
        xalign 1.5
    with move
    show edalla:
        xalign -0.5
    with move
    show hiris at right
    with move
    show edalla at left
    with move

    ppSirene "Bonjour, vous devez être la princesse Hiris qui épousera mon frère."
    ppSirene "Je me présente, je suis la princesse Edalla, la fille du roi Morgon."
    ppSirene "J'aimerai parler avec toi de ce mariage."
    ppElf "Bonjour Edalla, enchantée de faire votre connaissance. J'accepte votre invitation à discuter."
    ppSirene "Merci bien Princesse, avant toute chose, j’aimerais connaître votre point de vue vis-à-vis de ce mariage."
    ppElf "Je reste mitigée sur le mariage, je ne le connais pas et je suis encore jeune."
    ppElf "Pourriez-vous, s'il vous plaît, me parler un peu de lui et me partager votre avis ?"
    ppSirene "Je comprends votre inquiétude cependant je sais que mon frère est quelqu’un de bien, vous ne serez pas déçue."
    ppSirene "Que diriez-vous d’aller discuter de divers sujets ailleurs ? "
    ppElf "Avec plaisir, où souhaiteriez-vous aller ?"
    ppSirene "Comme vous préférez, nous pouvons aller nous balader en ville ou rester dans l'ambassade pour parler plus tranquillement."
    menu:
        "Aller en ville":
            jump discutionVille_elf
        "Rester dans l'ambassade":
            jump discutionChambre_elf

label discutionVille_elf:
    n "Vous décidez d'aller vous balader en ville."
    ppElf "Je ne serais pas contre d'aller me balader à vos côtés en ville !"
    scene bg villeSirene
    with fade
    show edalla:
        xalign -0.5
    with move
    show hiris:
        xalign 1.5
    with move
    show edalla at left
    with move
    show hiris at right
    with move
    ppSirene "Bienvenue dans la capitale d'Océanos."
    ppElf "C'est ravissant, c’est un endroit bien différent de mon pays."
    n "Vous marchez et discutez quelques temps avec la princesse."
    ppSirene "Je change de sujet mais, avez-vous mangé ?"
    ppSirene "Nous pourrions aller manger toutes les deux et continuer notre discussion ?"
    ppElf "Ce serait avec plaisir."
    ppSirene "Très bien, venez avec moi, je vais vous montrer nos spécialités locales."
    n "Vous vous promenez avec Edalla dans la ville tout en discutant et vous arrivez devant une auberge."
    n "Vous vous installez à une table et Edalla vous recommande un plat typique de la région."
    stop music fadeout 2.0
    play music "audio/auberge.mp3" fadeout 2.0
    ppElf "Cette auberge est vraiment magnifique !"
    ppSirene "Évidemment, je ne pouvais pas me permettre de vous emmener dans une mauvaise auberge, je vous ai choisis la meilleure de toute !"
    ppElf "Merci, vous êtes adorable."
    ppElf "Depuis quand connaissez-vous cette endroit ?"
    ppSirene "J’y viens depuis petite avec mon frère, cette auberge a toujours existée, aussi loin que je m’en souvienne."
    ppSirene "Mais cette ville n’a pas toujours été aussi animée, cela n’a changé qu’à partir du couronnement de mon père."
    stop music fadeout 3.0
    ppSirene "À l’époque où mon grand-père gouvernail..."
    ppElf "..."
    ppSirene "..."
    ppElf "..."
    ppSirene "Pardon..."
    ppSirene "J'ai bu la tasse."
    play music "audio/auberge.mp3" fadeout 2.0
    ppSirene "A l’époque où mon grand-père gouvernait, les rues étaient vides et inanimés." 
    ppSirene "Tous les gens, même les enfants étaient enrôlés pour rejoindre l’armée."
    ppElf "Je comprends, nous avons connu une situation similaire dans notre pays..."
    ppSirene "..."
    pause 1
    ppSirene "Oh les plats arrivent !"
    pause 3
    #son couverts
    n "Vous continuez de déguster votre repas en discutant avec la princesse Edalla."
    pause 3
    ppElf "C'était vraiment délicieux !"
    ppSirene "Ça me fait plaisir de vous l'entendre dire." 
    ppSirene "Il me semble que vous aviez à faire, je ne voudrais pas vous retarder plus longtemps."
    menu:
        "Continuer à discuter":
            jump vieDePrincesse_elf
        "Aller voir le prince":
            jump dialogueSurPrinces_elf

label discutionChambre_elf:
    ppElf "Je ne serais pas contre de rester me reposer un peu en discutant avec vous !"
    ppSirene "Sans problème, je vous en prie, installez-vous."
    ppElf "Je vous en remercie."
    ppSirene "Je m'excuse de cette question si soudaine mais..."
    ppSirene "Que pensez-vous de mon frère ?"
    ppElf "Pour le peu que je connaisse le prince, je reste mitigée, j'ai quelques difficultés à me projeter sur un potentiel marriage."
    ppSirene "Je comprend votre inquiétude mais c'est nécessaire pour maintenir la paix pour les générations futures de nos peuples respectifs."
    ppElf "J'en ai pleinement conscience, mais il est inévitable que j'aimerai avoir la liberté de mes choix."
    ppElf "Pourquoi serait-ce à moi d'endosser ce fardeau que nos ancêtres nous ont légués ?"
    ppSirene "Ce n'est pas une décision qu'une personne peut négliger, ce mariage à un engagement politique conséquent."
    ppSirene "Dites-vous que c'est le prix à payer pour ce que votre peuple nous à fait subir à l'époque."
    ppElf "..."
    ppSirene "..."
    menu:
        "Demander à aller en ville":
            ppElf "Est-ce que vous seriez intéressée pour sortir en ville et discuter toutes les deux ?"
            jump discutionVille_elf
        "Maintenir son opinion":
            ppElf "Je ne suis quand même pas convaincue."
            ppSirene "Comment pouvez-vous être aussi égoïste alors que vous avez entre vos mains le destin de deux peuples et du futur de tous."
            ppElf "Je suis contre une union forcée, j'ai besoin de pouvoir effectuer mes propres choix."
            ppSirene "La conversation n’a pas d’issue, je n'ai plus la force de parler avec quelqu’un qui refuse d’admettre les torts de son pays."
            ppSirene "Sortez de chez moi !"
            play sound "audio/porte.mp3"
            show hiris:
                xalign 1.5
            with move
            jump excusesPrincesse_elf
    
label vieDePrincesse_elf:
    ppElf "Ne vous en faites pas, on a encore du temps devant nous."
    ppSirene "Si vous insistez, nous pouvons continuer notre discussion en nous promenant si cela vous convient."
    ppElf "Ce serait avec plaisir."
    stop music fadeout 3.0
    ppElf "Parlez moi un peu de vous, quels sont vos centres d'intérêts ?"
    ppSirene "J’ai pour passion la chanson, vous aimeriez avoir une démonstration ?"
    ppElf "Avec plaisir !"
    play music "audio/chant_sirene.mp3" fadeout 1.0
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    stop music fadeout 3.0
    ppElf "Vous chantez tellement bien !"
    ppSirene "Merci, vous me flattez."
    ppSirene "Il faudrait qu'on y aille, votre devoir vous attends."
    show edalla:
        xalign -0.5
    with move
    hide edalla
    show hiris:
        xalign -0.5
    with move
    hide hiris
    scene bg ambassadeSirene
    with fade
    jump conseil_ambassade_excuse

label dialogueSurPrinces_elf:
    stop music fadeout 2.0
    play music "audio/theme_elfe.mp3" fadeout 2.0
    ppElf "Merci de m’avoir accordé votre temps et veuillez m’excuser, je me dois de retrouver le prince."
    ppSirene "N'ayez pas d'inquiétude, je vous laisse retourner à vos occupations."
    ppSirene "Merci pour cet après-midi princesse Hiris."
    ppElf "De même pour vous princesse Edalla."
    show edalla:
        xalign -0.5
    with move
    hide edalla
    show hiris:
        xalign -0.5
    with move
    hide hiris
    n "Vous marchez vers le château royal et vous tombez sur le prince sur le chemin mais il ne vous voit pas." 
    n "Vous voyez une silhouette à ses côtés et vous décidez de l’observer discrètement."

    menu :
        "Monter à l'arbre pour mieux voir":
            jump mauvais_choix_elf
        "Se pencher derrière le buisson":
            jump mauvais_choix_elf
        "Ne rien faire":
            jump bon_choix_elf

label bon_choix_elf:
    pause 1
    n "Vous patientez quelques secondes et décider de ne plus vous cacher."      
    pause 1
    show metilay:
        xalign -0.5
    with move
    show metilay:
        xalign 0.15
    with move
    show keidal:
        xalign -0.5
    with move
    show keidal at left
    with move
    ppElf "KEIDAL ?! Que fais-tu ici ?"
    princeElf "Je suis en train de discuter avec un ami, rien de plus."
    ppElf "Vous êtes vachement proche quand même."
    show metilay:
        xalign 0.35
    with move
    princeElf "Non, pas spécialement. Viens, retournons à l'ambassade, une longue journée nous attend."
    show hiris:
        xalign -0.5
    with move
    jump ambassadeExcuses_elf
    
label mauvais_choix_elf:
    stop music fadeout 1.0
    pause 1
    n "Vous perdez l'équilibre pendant l'observation."
    play sound "audio/chute_personnage.mp3"
    pause 1
    pause 1
    pause 1
    play music "audio/theme_elfe.mp3" fadeout 2.0
    show metilay:
        xalign -0.5
    with move
    show metilay at left
    with move
    princeSirene "Princesse Hiris ! Vous allez bien ?"
    ppElf "Oui, je vous en remercie, j’ai cru apercevoir quelqu’un avec vous, je n’ai pas voulu vous déranger."
    princeSirene "Non ce n’était qu’un ami, mais êtes-vous sûr que tout va bien ?"
    ppElf "N'ayez crainte, tout va bien."
    princeSirene "Voulez-vous aller vous promener ? Je connais une excellente auberge."
    ppElf "Je suis désolée, je viens tout juste de manger. Allons plutôt nous promener dans un parc si vous le voulez bien."
    ppElf "J’aimerai connaître votre point de vue sur notre union arrangée."
    princeSirene "Je suis très honoré de me marier avec une femme aussi ravissante que vous." 
    #roug-Hiris
    ppElf "..."
    princeSirene "Oh excusez-moi, je ne voulais pas vous mettre mal à l’aise." 
    ppElf "Non tout va bien, vous m’avez surpris mais je suis contente que vous soyez aussi gentil et romantique." 
    princeSirene "Vous m’envoyez ravi." 
    stop music fadeout 2.0
    scene bg ambassadeSirene
    with fade
    jump conseil_ambassade_excuse_elf

label excusesPrincesse_elf:
    scene bg elf
    with fade
    n "Le lendemain..."
    show centaure:
        xalign -0.5
    with move
    show centaure at left
    with move
    show hiris:
        xalign 1.5
    with move
    show hiris at right
    with move

    centaure "Princesse nous partons à nouveau pour les terres des hommes poissons, pour décider de votre avenir."
    ppElf "Je suis la seule qui décide de quel avenir prendre, pour mon peuple et pour moi, partons."

    scene bg villesirene
    with fade
    show hiris:
        xalign 1.5
    with move
    show hiris at right
    with move
    menu:
        n "Une fois dans l'ambassade, vous croisez la princesse qui ne semble pas vous voir."
        "Présenter ses excuses":
            jump ambassadeExcuses_elf
        "Ignorer":
            scene bg ambassadesirene_elf
            with fade

            show morgon:
             xalign 1.5
            with move
            show morgon:
                xalign 0.75
            with move

            show callyon:
                xalign 1.5
            with move
            show callyon at right
            with move

            show hiris:
                xalign -0.5
            with move
            show hiris at left
            with move

            jump conseil_ambassade_nonExcuse_elf