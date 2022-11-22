﻿# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define b = Character("Lucas")
define y = Character("[name]")
define h = Character("Alicia")
define c = Character("Alba")
define p = Character("Gabriel")
define g = Character("Alejandro")
define t = Character("Todos")
transform superLeft:
    xalign 0.0
    yalign 0.45
transform superRight:
    xalign 1.0
    yalign 0.45
transform center:
    xalign 0.5
    yalign 0.45
transform left:
    xalign 0.15
    yalign 0.45
transform right:
    xalign 0.9
    yalign 0.45
transform centerLeft:
    xalign 0.25
    yalign 0.45
transform centerRight:
    xalign 0.75
    yalign 0.45

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    #DEBUGGING AAAAA QUITAR ESTAS LINEAS
    # $ genero = "o"
    # $ pronombre = "el"
    # $ name = "Marica Chonda"

    #SELECCION PRONOMBRES#
    scene bg black with dissolve
    "Antes de empezar el juego, queremos que formes parte del juego, y nos gustaría saber si preferirías que te llamaran en femenino o en masculino"
    menu:
        "Masculino (Él)":
            $ genero = "o"
            $ pronombre = "el"
        "Femeninio(Ella)":
            $ genero = "a"
            $ pronombre = "ella"

    $ name = renpy.input("¿Y cual es tu nombre?")
    
    #--------------------------

    scene bg train tunnel with dissolve

    "Comienza una nueva vida, tras un largo viaje y mucho cambio. Tuvimos que mudarnos a la ciudad tras que Papá perdiera su trabajo"
    "Afortunadamente consiguió un trabajo gracias a un amigo en la ciudad de HighPeaks"
    "Tuvimos que mudarnos y he tenido que dejar a todos mis amigos atrás"
    "Hoy es mi primer día en mi nuevo instituto y voy con miedo"
    "Al menos mi padre me dijo que Lucas, un antiguo compañero de instituto, ahora estudia aquí"
    "Espero que se acuerde de mi, eramos muy buenos amigos antes de que se fuera hace 2 años..."
    "Espera, ¿esta era la parada en la que me tenía que bajar? ¿Dónde estoy? Esto me pasa por estar en babia"
    "Y para colmo en 10 minutos debería de estar ya en clase…"
    show lucas normal at superRight with moveinright
    "Espera, ¿ese chico no es Lucas? A lo mejor también llega tarde como siempre hacía antes"
    
    menu:
        "(Te acercas al chico)"

        "¿Lucas? ¿Eres tú?":
            jump acercarteLucas
        "(Darle una sorpresa)":
            jump sorpresaLucas

    label acercarteLucas:
    show lucas normal at center with move
    b "Depende de para qué. ¿Quién pregunta por.."
    show lucas surprised at center
    b "¿[name]? ¿Eres tú?"
    jump conocidoLucas

    label sorpresaLucas:
    show lucas angry1 at center with move
    b "¡OYE! Ten mas cui.."
    show lucas surprised at center
    b "¿[name]? ¿Eres tú?"
    jump conocidoLucas

    label conocidoLucas:
    show lucas laugh at center
    b "¡Cuánto tiempo! Hacia años que no nos vemos. ¿Cómo tú por aquí?"
    show lucas smile1 at center
    y "Me he mudado a High Peaks ahora por movidas familiares, así que supongo que somos compañeros de clase"
    show lucas smile2 at center
    b "¿En serio? ¡Eso es genial! La gente de High Peaks no tiene nada que ver con la escoria de nuestro antiguo instituto, ¿Recuerdas?"
    y "Como no me voy a acordar…tu llevas 2 años aqui pero yo me he mudado esta semana jajaja."
    b "¡Venga no hay tiempo que perder! Que vamos fatal de tiempo"

    scene bg old school with pixellate

    "(Instituto HighPeaks)"

    y "¡Guau, este instituto es gigante!"
    show lucas smile3 at superLeft with moveinleft
    b "Dejate de tantas vistas que llegamos tarde, quedamos en el recreo en la entrada y te presento a mi grupo de amigos"
    #BUSCAR ALGO DE MOVIMIENTO Y NO TELETRANSPORTACION
    show lucas smile3 at superRight with move
    b "¡Nos vemos en clase!"
    hide lucas smile3 with moveoutright
    #SONIDO DE ALGUIEN CORRIENDO AAA
    y "¡OYE!"
    scene bg black
    "(Tras varios minutos consigues encontrar el aula justo cuando suena el timbre)"
    #SONIDO TIMBRE AAA
    scene bg lecturehall with pixellate
    "*Riiing*"

    #CONOCE A ALICIA
    "Lo conseguí,ahora solo tengo que encontrar un asiento libre sin…"
    "*¡Ponk!*" with hpunch
    "(Te chocas con alguien y te das un golpe)"
    menu:
        "Ten más cuidado la proxima vez":
            jump cuidadoAlicia
        "(Pedir perdón por chocarte)":
            jump perdonAlicia
    label cuidadoAlicia:
    show alicia sad at center
    h "¡Ay jo lo siento! Perdona, no te había visto."
    h "¿Te he hecho daño? Ay lo siento mucho joe, no era mi intención… Toma"
    hide alicia sad
    show alicia smile1 at center
    "(Recibiste Tirita de Alicia)"
    b "Calma Alicia jajaja, solo ha sido un golpe"
    hide alicia smile2
    jump conocidoAlicia

    label perdonAlicia:
    show alicia smile1 at center
    h "¡Ay no seas boba! Soy yo que estoy siempre en los mundos de yupi y nunca me entero de nada. Toma, como un simbolo de paz jajaja"
    hide alicia smile1
    show alicia smile2 at center
    "Recibiste Tirita de Alicia."
    b "Alicia no tenemos tiempo para tus ñoñerias."
    hide alicia smile2
    jump conocidoAlicia

    label conocidoAlicia:
    show lucas smile1 at left
    show alicia smile1 at right
    
    b "Esta es [name], era mi mejor amig[genero] de mi antiguo instituto, y parece que ahora va a ser nuestr[genero] compi de clase. ¿NO ES GENIAL?"
    show alicia laugh at right
    h "¡Ay genial! Más gente en el grupo! Estoy deseando conocerte. ¿Pijamada este finde en mi casa?"
    show lucas smile3 at left
    b "¡De una! Luego en el recreo le presento al resto y les digo lo de la pijamada"
    hide alicia laugh
    show lucas smile1
    b "[name], cuando se acabe el recreo te presento a mi grupito, ya les he avisado por whatsthematter que tenemos una nueva personita jeje."
    scene bg black
    "(Termina la clase y llega al recreo)"

    #RECREO
    scene bg club
    "¿Esos no son Lucas y Alicia?"
    "Están con 3 personas más"
    show lucas smile2 at superLeft
    b "¡[name] ven aquí, te voy a presentar a mis amiguis!"
    show alicia smile1 at centerLeft
    b "A Alicia ya la conociste antes, es la chica que nos da la serotonina diaria."
    b "Es imposible conseguir enfadarla, y mira que lo hemos intentado jajaja"
    show alicia smile2 at centerLeft
    h "Ay tampoco es así… que [name] se va a pensar que estoy ida o algo "
    show lucas laugh at superLeft
    show alejandro laugh at center
    show alba laugh at centerRight
    show gabriel laugh at superRight
    t "Jajajaja"
    b "Este es Alejandro. No te dejes llevar por las apariencias, es un gymbro con todas las letras pero tiene buen corazón"
    show alejandro smirk at center
    b "Y siempre nos ayuda cueste lo que cueste, ¿a que sí corazón de melón?"
    show alejandro smile2 at center
    g "Lucas no intentes convencerme para ir a jugar después de clase que hoy estoy molido."
    show lucas sad at superLeft
    b "¡¡Joeee!!"
    show lucas smile2 at superLeft
    b "Enfin, a tu derecha del todo tenemos a nuestro querido Gabriel."
    show gabriel smile3 at superRight
    b "Tiene mejor melena que Alicia con la mejor weekly routine."
    b "Lavarse el pelo con la lluvia"
    show gabriel angry2 at superRight
    p "Pero bueno quieres que [name] sea nuestra amiga o estás intentando que no se acerque"
    show gabriel smile2 at superRight
    p "No le escuches, llamame Gabri, aunque todos me llamen Iluminao, adoro los animalitos y el campito aunque estemos en una ciudad..."
    menu:
        "¡Yo también! Que guay":
            jump veryFriendlyGabriel
        "*Encantad[genero], soy [name]":
            jump friendlyGabriel

    label veryFriendlyGabriel:
    p "¿Si? Podemos quedar un día y te enseño mi mascota. ¡Es un Border Coly precioso!"
    b "Pisa el freno que falta una por presentar, luego ya haced lo que querais tortolitos"
    p "Ups, perdón jajaja"
    jump conocidoGabriel

    label friendlyGabriel:
    p "[name], que nombre más bonito. ¿Y por qué te mudaste a.."
    b "las preguntas para más tarde tortolitos que me falta una por presentar"
    p "vale mamá"
    jump conocidoGabriel

    label conocidoGabriel:
    b "En fin, por donde iba..."
    b "Por último pero no menos importante, nuestra incomprendida de la vida, ¡Alba!"
    show alba annoyed
    c "Que sea más tímida no significa que sea una incomprendida..."
    b "Luego se suelta más, solo dale algo de tiempo. Hablando de lo que comentaba antes, ¿pijamada este finde todos juntos? ¡Alicia pone casa!"
    menu:
        "No se yo...":
            jump noPijamada
        "Venga vale":
            jump siPijamada
    
    label noPijamada:
    show alejandro smirk
    g "Venga anímate, parecemos majaras pero te lo vas a pasar genial en la pijamada."
    g "Alicia prepara una limonada sin azucar y tiene un gatete"
    jump pijamadaDecidido

    label siPijamada:
    h "¡Yey! Voy a ir diciendole a mi madre que compre las cosas para hacer una limonada"
    g "¡¡¡Recuerda que no tenga azucar!!!"
    b "Que sí gymbro, su madre ya sabe que tiene que hacer una limonada sosa como siempre jajaja"
    b "Bueno [name] pues recuerda que el viernes quedamos a las 20 donde el instituto para ir a casa de Alicia, ¿Vale?"
    menu:
        "Genial":
            jump pijamadaDecidido
        "Apuntado":
            jump pijamadaDecidido

    label pijamadaDecidido:
    scene bg black
    "(Pasas toda la semana con ellos hasta el viernes de la pijamada)"

    #PIJAMADA
    scene bg apartment exterior
    b "Y esta es la casa de Alicia, vamos a entrar cuanto antes que me muero de hambre"
    "*Tok tok*"
    p " Buenas Chiquetss, estamos en la cocina preparando la cena, dejad las mochilas en el salón y venid"
    b "¡Uh! ¿Qué ha hecho la madre de Alicia esta vez? Me muero por sus croquetitas Mmhh"
    p "Venid a la cocina y lo vereis jeje"

    scene bg encore kitchen

    h "¡Te juro que la limonada no tiene azúcar blanco, es estevia, que he visto a mi madre echarlo!"
    g "¡MENTIRA! Una limonada tan deliciosa, ¿sin nada de azucar? No me lo creo"
    c "Pues tienes croquetas bien grasientas de cena así que prepárate para el workout de mañana"
    g "¿QUÉEE?"
    p "Haz el favor de disfrutar de la cena y ya te preocuparás del ejercicio mañana, que la mami de Happy Flower lo ha hecho todo casero con todo su amor y no tiene aditivos ni mierdas"
    c "Peores son los batidos de proteinas con cosas raras que te metes al cuerpo"
    b "Zasca JAJAJAJAJ"
    b "[name] a ti te gustan las croquetas, ¿no? Que encima son caseras.."
    menu:
        "Pues...":
            jump tenerMalGusto
        "Obvio que sí":
            jump tenerBuenGusto

    label tenerMalGusto:
    b "Pues más para mí jeje, Happy flower tenía también sobras así que no te preocupes"
    c "Las croquetas de la madre de Alicia son un manjar que no todo el mundo sabe apreciar"
    g "Y dale, que sí que están muy ricas pero me lo poneis imposible para ponerme en forma.."
    jump empiezaPijamada

    label tenerBuenGusto:
    b "Quien rechace esta oferta de croquetas caseras está tomando la peor decisión de su vida"
    g "¿Podeis parar de meterme dagas? Que ya os he dicho que me las voy a comer tontos"
    b "Así me gusta, croquetitas para todos"
    jump empiezaPijamada

    label empiezaPijamada:
    h "En fin chicos, mi madre ha quedado mañana con sus amigas fuera de la ciudad para hacer un ‘Brunch’ con sus amigas así que hoy no duerme aquí"
    h "¡Así que tenemos noche libre para lo que queramos!"
    b "¡Noche de Pelis de Terror!"
    g "¡Jugar a verdad o reto!"
    h  "Prefiero verdad o reto antes que traumarme con mas pelis"
    p "Una amiga me habló de un documental de Notflix sobre toda la industria cárnica"
    p "¡Le gustó tanto que se hizo vegana tras vérselo, igual os gusta!"
    c "Voto por verdad o reto con tal de no comerme la chapa del siglo o un peñazo de peli"
    b "Y bien [name], ¿Qué quieres hacer tú?"
    menu:
        "Peli de terror":
            jump noVerdadOReto
        "Verdad o reto":
            jump verdadOReto
        "Documental de Notflix":
            jump noVerdadOReto

    label noVerdadOReto:
    h "3 contra 2, por lo que verdad o reto gana jeje"
    b "Bueeeno, vaale. Pero la proxima vez peli de terror"

    jump comerCroquetas

    label verdadOReto:
    g "Una chica con iniciativa. Así nos conoces mas a todos nosotros, ¿no?"
    c "Creo que con solo una semana aquí ya nos tiene calados a todos jajaja"

    jump comerCroquetas

    label comerCroquetas:
    b "¡Pues a devorar las croquetas y luego nos subimos a las habitaciones, nos ponemos el pijamita y jugamos hasta que nos durmamos!"
    scene bg black
    "*Ñam ñam ñam"
    #PONER SONIDITO DE COMER AAAAAAAAAAAAAAAAAAAAA

    b "¿Todavía sigues durmiendo con esa camiseta cutre? Que si no tienes pijama Alicia tendrá alguno por ahí"
    g "Já, já, já. Este es mi pijama, siempre tengo mucho calor por la noche y así duermo más cómodo"
    p "De hecho tiene razón, con menos ropa el sueño es más profundo porque el cuerpo se enfría y se autorregula más rápido que con el algodón de la ropa"

    h "..."
    c "..."
    b "..."
    menu:
        "...":
            jump risasCalifornianas
        "Sois unos frikis de narices":
            jump risasCalifornianas
        
    label risasCalifornianas:


    "HASTA EL HIGO"


    # Finaliza el juego:

    return
