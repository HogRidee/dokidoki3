define player = Character("Poppy", color = "#d42845")
define unknown = Character("???", color = "#808080")
define x = Character("X", color = "#808080")
define y = Character("Y", color = "#808080")
define unknown2 = Character("???", color = "#808080")

#show player at -> right, left, center (default), truecenter

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

    show x at right
    with dissolve

    x "Oh, sí, claro, está al fondo a la derech..."

    show y at center
    with dissolve

    y "¡Espera! ¿No eres tú el que acaba de chocar con...?"

    x "Es verdad... ¿Eres tú el que hizo que nuestro ídolo...?"

    player "¿Yo? Pero si no hice na..."

    y "Piérdete, no queremos verte cerca de él."

    player "P-pe... pp-pero... (suspira) Supongo que el día no ha empezado bien..."

    hide x
    hide y

    "(Poppy sigue caminando cabizbajo por los pasillos, evitando las miradas y los murmullos que se desatan a su alrededor. Todo parecía ir bien, pero ahora las cosas habían cambiado de golpe. Las risas, las miradas incómodas, el susurro de \"ahí va el que chocó con él\"...)"

    player "¿Por qué tenía que ser él...? (se frota los ojos, tratando de contener las lágrimas.)"

    "(Llega al final del pasillo, buscando un rincón para esconderse. Encuentra un pequeño lugar detrás del edificio, donde nadie suele pasar. Se sienta en el suelo, abrazando sus rodillas.)"

    player "No puedo creer que esto me esté pasando el primer día..."

    "(De repente, escuchas pasos detrás de ti. Alguien se acerca suavemente.)"
    play sound walking
    pause

    unknown2 "Hey... ¿estás bien?"

    "(Levantas la vista y ves a un chico alto, de pelaje oscuro, con ojos amables que te miran con preocupación.)"

    show unknown2
    with dissolve

    player "No, no lo estoy... todo va mal..."

    "(El desconocido se sienta a tu lado, sin decir nada al principio, solo dejando que el silencio hable.)"

    unknown2 "A veces... los días no salen como uno espera..."

    "(Lo miras de reojo, sintiéndote un poco más calmado con su presencia. El chico se acerca más, sus brazos rozando suavemente los tuyos, haciendo que no puedas evitar sentir una mezcla de consuelo y algo más que empieza a revolverse en tu interior.)"

    unknown2 "Es... está bien. No tienes que disculparte. Sé exactamente cómo se siente…"

    

