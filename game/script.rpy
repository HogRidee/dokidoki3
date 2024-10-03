define player = Character("Poppy", color = "#d42845")
default book = False

label start:

    scene bg classroom
    with fade

    "Nuestro primer día, de mañana, los pájaros cantan, es soleado y caminamos alegres a punto de cruzar la puerta principal."

    show player
    with dissolve

    # hide -> when the character leaves the scene

    player "ah~ estoy tan emocionado por este primer día, es un nuevo empezar y estoy seguro que me irá genial----"

    "(pum, se escucha un golpe y la pantalla se pone en negro)"

    $ book = True

    player "aishhh qué golpe tan fuerte! P-p-per-perdón estaba distraído"

    #show player at -> right, left, center (default), truecenter