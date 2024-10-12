define player = Character("Poppy", color = "#d42845")
define unknown = Character("???", color = "#808080")
define x = Character("X", color = "#808080")

label start:

    scene bg classroom
    with fade

    player "Ahhh~ estoy tan emocionado por este primer día, es un nuevo comienzo, y estoy seguro de que me irá genial..."

    scene bg black
    with dissolve
    play sound punch
    pause

    scene bg classroom
    with fade
    player "Aishhh, ¡qué golpe tan fuerte! P-p-perdón, estaba distraído..."

    show unknown
    with dissolve

    # hide -> when the character leaves the scene
 
    unknown "Ouchhh, perdón."

    "(Un zorro naranja... ¿me acaba de pedir perdón? Ni siquiera noté que me choqué con él...)"

    player "No te preocupes, la culpa fue mía jaja... Por casualidad, ¿sabes dónde queda...?"
    
    hide unknown
    with dissolve
    "(Oh... ya se fue... *Se encoge de hombros*)"

    player "Bueno, a seguir con mi buen día jaja~"
    with dissolve
    player "Me siento un poco desorientado... Debería pedir ayuda..."

    player "Ho-hola, disculpa, estoy buscando la clase 303..."

    show x
    with dissolve

    x "Oh, sí, claro, está al fondo a la derech..."

    #show player at -> right, left, center (default), truecenter