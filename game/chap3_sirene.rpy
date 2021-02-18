label rencontrePrincesse_sirene:
    scene chambre_elfe
    with fade

    show edalla_normal:
        xalign -0.5
    with move
    show hiris:
        xalign 1.5
    with move
    show edalla_normal at left
    with move
    show hiris at right
    with move

    ppElf "Je me présente Hiris, fille de Callyon, c'est un honneur pour moi de pouvoir vous inviter sous mon toit."
    ppSirene "Enchanté Princesse Hiris, je suis Edalla la fille du roi des Océanos."
    menu:
        "Peut-on en parler ailleurs ?":
            ppSirene "Je me sens à l'étroit ici, c'est possible de poursuivre dans un endroit moins confiné ?"
            jump discutionVille_sirene
        "Je suis prête à me marrier":
            ppSirene "Je suis prête à me marrier avec ton frère."
            jump discutionPolitique_sirene
        "Je pense être prête à faire le bon choix pour mon peuple":
            ppSirene "Si c'est le seul moyen d'avoir la paix entre nos peuples, alors je me marierai avec ton frère."
            jump vieDePrincesse_sirene

label discutionVille_sirene:
    $ dragueReussi = True
    ppElf "Bien-sur, moi aussi je suis fatigué de rester entre ces murs, allons en ville."
    scene ville_elfe
    with fade
    show hiris:
        xalign 1.5
    with move
    show edalla_normal:
        xalign -0.5
    with move
    show edalla_normal at left
    with move
    show hiris at right
    with move
    hide edalla_normal
    show edalla_joie at left
    ppSirene "C'est vraiment magnifique ici, j'adore les couleurs et l'air est si pur…"
    hide hiris
    show hiris_happy at right
    ppElf "Contente de voir que cela vous plait princesse, vous avez faim ? Je connais une excellente auberge non loin d’ici."
    ppSirene "J'accepte votre proposition avec plaisir princesse Hiris."
    n "Hiris souris et prends la main droite d'Edalla pour se rendre devant un établissement discret aux premiers abords mais une fois à l’intérieur vous ressentez une atmosphère chaleureuse et réconfortante."
    ppSirene "Quel joli endroit, la musique est joyeuse, la présentation magnifique et l’odeur tout simplement exquise."
    ppElf "Bienvenue chez les Trois Centaures, aller venez, j'ai ma table habituelle juste ici."
    n "Une fois installée, vous commandez un plat typique."
    ppSirene "Cette auberge semble vous tenir à cœur Hiris."
    ppElf "Je viens ici depuis toute jeune, j'ai vécus d’innombrable souvenirs ici avec ma famille ou mes proches."
    ppElf "Je trouve que nous partageons beaucoup de points en commun ma chère."
    ppSirene "C'est plutôt bon signe pour les générations futures."
    n "Le serveur pose les plats sur la table, vous découvrez votre salade aux herbes curative, vous la dégustez avec beaucoup de gourmandise."
    ppElf "Allons nous balader, je connais des paysages magnifique ici."
    ppSirene "Je vous suis Hiris, où que vous alliez."
    n "Vous partez dans un champ juste toutes les deux, le coucher du soleil se pose doucement dans la vallée laissant les nuages blancs devenir rosâtre." 
    n "Vous regardez Hiris dans les yeux en souriant sans rien dire. Vous regagez l'ambassade le lendemain."
    scene ambassade_elfe
    with fade
    jump discution_sirene  

label discutionPolitique_sirene:
    $ dispute = True
    ppElf "Je vous trouve bien solennelle, essaye d’être un peu plus naturelle."
    hide edalla_normal
    show edalla_gene at left
    ppSirene "Je vais essayer de faire de mon mieux."
    ppElf "Vous êtes bien trop gentille Edalla."
    ppSirene "Oh vous savez, tout le monde me dit ça…"
    ppElf "Personnellement je ne comprends pas comment vous pouvez accepter si facilement de prendre la décision de rester avec quelqu’un que vous ne connaissez pas."
    hide edalla_gene
    show edalla_normal at left
    ppSirene "Les coraux sont rouges depuis des siècles, ces conflits méritent d'être finis une bonne fois pour toute."
    ppElf "Ce n’est pas à vous de payez les conséquences du passées."
    ppSirene "Non, mais j’assume les choix de mes ancêtres et je pense que vous devrez en faire de même Princesse."
    #play sound "audio/claque.mp3"
    hide hiris
    show hiris_angry at right
    ppElf "A qui croyez vous parler ? Sirène je suis la fille de la reine, un peu de respect !"
    ppElf "Callyon, mon honneur et ma famille sont aussi importants que mon peuple." 
    ppElf "Nous subissons également des lourdes pertes, la nature ne pousse même plus sur certaines zones de batailles."
    hide edalla_normal
    show edalla_triste at left
    pause 1
    hide edalla_triste
    show edalla_pleure at left
    ppSirene "…"
    show edalla_pleure:
        xalign -0.5
    with move
    show hiris_angry:
        xalign 1.5
    with move
    scene ambassade_elfe
    with fade
    jump excusesPrincesse_sirene

label vieDePrincesse_sirene:
    ppElf "Je vous envie ma chère Edalla, vous avez un sens du patriotisme limite maladive."
    ppSirene "Ne vous moquez pas de moi, vous aurez fait pareille à ma place."
    ppElf "Je ne sais pas, j’aurais sûrement décidée de dicter ce que me dit mon cœur."
    ppSirene "Ne me mentez pas Hiris."
    hide hiris
    show hiris_surprise at right
    n "Edalla prenait doucement la main d'Hiris."
    hide hiris_surprise
    show hiris at right
    ppSirene "Je vis pour moi et pour les miens chaque minute et chaque seconde."
    ppElf "Vous êtes bien tactile pour une fiancée."
    hide edalla_normal
    show edalla_gene at left
    ppSirene "Excusez-moi, toucher les gens me permet de me calmer"
    hide edalla_gene
    show edalla_normal at left
    ppSirene "Et vous ? Que faites vous pour vous détendre ?"
    ppElf "Pour me détendre ? Eh bien, je prends un bain, je lis des romans couchés sur les arbres et caressés par le vent ou j’écoute les chants dans les prairies vertes de Tyrria."
    ppSirene "Très bien dans ce cas laissez-moi vous offrir un cadeau."
    window hide
    play music "audio/chant_sirene.mp3" fadeout 1.0
    pause 8
    window show
    stop music fadeout 3.0
    ppSirene "C'était un chant merveilleux, j’apprécie énormément ce présent, je suis heureuse de vous avoir rencontré Edalla."
    hide hiris
    show hiris_happy at right
    ppElf "C’est le meilleur des compliments, princesse."
    hide edalla_normal
    show edalla_surprise at left
    pause 1
    hide edalla_surprise
    show edalla_joie at left
    ppSirene "Bien, je pense que nous devons retourer à l'ambassade."
    show edalla_joie:
        xalign -0.5
    with move
    show hiris_happy:
        xalign 1.5
    with move

    scene ambassade_elfe
    with fade
    show edalla_normal:
        xalign 1.5
    with move
    show hiris:
        xalign -0.5
    with move
    show edalla_normal at right
    with move
    show hiris at left
    with move
    jump discution_sirene

label excusesPrincesse_sirene:
    show edalla_pleure:
        xalign -0.5
    with move
    show callyon_colere:
        xalign 1.5
    with move
    show callyon_colere at right
    with move
    show edalla_pleure at left
    with move
    reineElf "Edalla, allez-vous vous excusez pour vos propos."
    ppSirene "Oui… Désolée… "
    ppSirene "Je regrette vraiment ce que j'ai pu dire à Hiris."
    reineElf "Bon, passons au sujet du mariage."
    show morgon_normal:
        xalign -0.5
    with move
    show morgon_normal:
        xalign 0.15
    with move
    hide edalla_triste
    show edalla_triste at left
    show keidal_normal:
        xalign 1.5
    with move
    show keidal_normal:
        xalign 0.85
    with move
    hide callyon_colere
    show callyon_normal at right
    jump discution_sirene