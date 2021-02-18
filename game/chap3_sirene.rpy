label rencontrePrincesse_sirene:
    scene bg ambassadeElf
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

    ppElf "Je me présente Hiris, fille de Callyon, c'est un honneur pour moi de pouvoir vous inviter sous mon toit."
    ppElf "Enchanté Princesse Hiris."
    menu:
        "Peut-on en parler ailleurs ?":
            ppSirene "Je me sens à l'étroit ici, c'est possible de poursuivre dans un endroit moins confiné ?"
            jump discutionVille_sirene
        "Je suis prête à ma marrier":
            ppSirene "Je suis prête à me marrier avec ton frère."
            jump discutionPolitique_sirene
        "Je suis prête à faire le bon choix pour mon peuple":
            ppSirene "Si c'est le seul moyen d'avoir la paix entre nos peuples, alors je me marierai avec ton frère."
            jump vieDePrincesse_sirene

label discutionVille_sirene:
    $ dragueReussi = True
    ppElf "Bien-sur, moi aussi je suis fatigué de rester entre ces murs, allons en ville"
    scene bg villeElf
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
    ppSirene "C'est vraiment magnifique ici, j'adore les couleurs et l'air est si pur…"
    ppElf "Contente de voir que cela vous plait princesse, vous avez faim ? Je connais une excellente auberge non loin d’ici."
    ppSirene "J'accepte votre proposition avec plaisir princesse Hiris."
    n "Hiris souris et prends votre main droite pour se rendre devants un établissement discret au premier abord mais une fois à l’intérieur vous récente une ambiance chaleureuse et réconfortante."
    ppSirene "Quel joli endroit, la musique est joyeuse, la présentation magnifique et l’odeur tout simplement exquise."
    ppElf "Bienvenue chez les Trois Centaures, aller venez, j'ai ma table habituelle juste ici."
    n "Une fois installé, vous commandez un plat typique."
    ppSirene "Cette auberge semble vous tenir à cœur Hiris."
    ppElf "Je viens ici depuis toute jeune, j'ai vécus d’innombrable souvenirs ici avec ma famille ou mes proches."
    ppElf "Je trouve que nous partageons beaucoup de points en commun ma chère."
    ppSirene "C'est plutôt bon signe pour les générations futures."
    n "Le serveur pose les plats sur la table, vous découvrez votre salade aux herbes curative, vous la dégustez avec beaucoup de gourmandise."
    ppElf "Allons nous balader, je connais des paysages magnifique ici."
    ppSirene "Je vous suis Hiris, ou que vous aillez."
    n "Vous partez dans un champ juste toutes les deux, le coucher du soleil se pose doucement dans la vallée laissant les nuages blancs devenir rosâtre." 
    n "Vous regardez Hiris dans les yeux en souriant sans rien dire."
    jump discution_sirene  

label discutionPolitique_sirene:
    ppElf "Je vous trouve bien solennelle, essaye d’être un peu plus naturelle."
    ppSirene "Je vais essayer de faire de mon mieux."
    ppElf "Vous êtes trop gentille Edalla."
    ppSirene "Vous aussi, tout le monde me dit ça…"
    ppElf "Personnellement je ne comprends pas comment vous pouvez accepter si facilement de prendre la décision de rester avec quelqu’un que vous ne connaissez pas."
    ppSirene "Les coraux sont rouges depuis des siècles, ces conflits méritent d'être finis une bonne fois pour toute."
    ppElf "Ce n’est pas à vous de payez des conséquences du passées."
    ppSirene "Non, mais j’assume les choix de mes ancêtres et je pense que vous devrez en faire de même Princesse."
    #play sound "audio/claque.mp3"
    ppElf "A qui croyez vous parler, sirène je suis la fille de la reine."
    ppElf "Callyon, mon honneur et ma famille sont aussi importants que mon peuple." 
    ppElf "Nous subissons également des lourdes pertes, la nature ne pousse même plus sur certaines zones de batailles."
    ppSirene "…"
    scene bg ambassadeElf
    with fade
    jump excusesPrincesse_sirene

label vieDePrincesse_sirene:
    ppElf "Je vous envie ma chère Edalla, vous avez un sens du patriotisme limite maladive."
    ppSirene "Ne vous moquez pas de moi vous aurais fait pareille à ma place."
    ppElf "Je ne sais, pas j’aurais sûrement décider de dicter ce que me dit mon cœur."
    ppSirene "Je ne me mens pas à moi-même, Hiris."
    n "Edalla prenait doucement la main d'Hiris."
    ppSirene "Je vis pour moi et pour les miens chaque minute et chaque seconde."
    ppElf "Vous êtes bien tactile pour une fiancée."
    ppSirene "Excusez-moi, toucher les gens me permet de me calmer tu fais quoi pour te détendre."
    ppElf "Pour me détendre ? Eh bien, je prends un bain, je lis des romans couchés sur les arbres caressés par le vent ou j’écoute les chants dans les prairies vertes de Tyrria."
    ppSirene "Très bien dans ce cas laissez-moi vous offrir un cadeau."
    #chant de sièrne
    #play music "audio/chant_sirene.mp3" fadeout 1.0
    pause 8
    ppSirene "C'était merveilleux, j’apprécie énormément ce présent, je suis heureuse de vous avoir rencontré Edalla."
    #stop music fadeout 3.0
    ppElf "C’est le meilleur des compliments, princesse."
    ppSirene "Bien, je pense que nous devons retourer à l'ambassade."
    scene bg ambassadeElf
    with fade
    jump discution_sirene

label excusesPrincesse_sirene:
    reineElf "Edalla, allez-vous vous excusez pour vos propos."
    ppSirene "Oui… Désolé…"
    ppSirene "Je regrette vraiment ce que j'ai pu dire à Hiris"
    reineElf "Bien, passons au sujet du mariage."
    jump discution_sirene