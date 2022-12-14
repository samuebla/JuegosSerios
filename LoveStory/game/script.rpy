# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define b = Character("Lucas")
define y = Character("[name]")
define h = Character("Alicia")
define c = Character("Alba")
define p = Character("Gabriel")
define g = Character("Alejandro")
define t = Character("Todos")

#Personajes secundarios
define Camarero = Character("Camarero")
define ChicoRandom = Character("Chico con sudadera")

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
    
    #DEBUG
    jump pijamada

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
    scene bg black with pixellate
    "(Tras varios minutos consigues encontrar el aula justo cuando suena el timbre)"
    #SONIDO TIMBRE AAA
    scene bg lecturehall with dissolve
    "*Riiing*"

    jump introInstituto

    label introInstituto:
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
    show alicia sad at center with move
    h "¡Ay jo lo siento! Perdona, no te había visto."
    h "¿Te he hecho daño? Ay lo siento mucho joe, no era mi intención… Toma"
    hide alicia sad
    show alicia smile1 at center
    "(Recibiste Tirita de Alicia)"
    b "Calma Alicia jajaja, solo ha sido un golpe"
    hide alicia smile2
    jump conocidoAlicia

    label perdonAlicia:
    show alicia smile1 at center with move
    h "¡Ay no seas boba! Soy yo que estoy siempre en los mundos de yupi y nunca me entero de nada. Toma, como un simbolo de paz jajaja"
    hide alicia smile1
    show alicia smile2 at center
    "Recibiste Tirita de Alicia."
    b "Alicia no tenemos tiempo para tus ñoñerias."
    hide alicia smile2
    jump conocidoAlicia

    label conocidoAlicia:
    show alicia smile1 at center
    show alicia smile1 at right with move
    show lucas smile1 at left with moveinleft
    
    b "Esta es [name], era mi mejor amig[genero] de mi antiguo instituto, y parece que ahora va a ser nuestr[genero] compi de clase. ¿NO ES GENIAL?"
    show alicia laugh at right
    h "¡Ay genial! Más gente en el grupo! Estoy deseando conocerte. ¿Pijamada este finde en mi casa?"
    show lucas smile3 at left
    b "¡De una! Luego en el recreo le presento al resto y les digo lo de la pijamada"
    hide alicia laugh with moveoutright
    show lucas smile1
    b "[name], cuando se acabe el recreo te presento a mi grupito, ya les he avisado por whatsthematter que tenemos una nueva personita jeje."
    scene bg black with pixellate
    "(Termina la clase y llega al recreo)"

    #RECREO
    scene bg club with pixellate
    "¿Esos no son Lucas y Alicia?"
    "Están con 3 personas más"
    show lucas smile2 at superLeft with moveinleft
    b "¡[name] ven aquí, te voy a presentar a mis amiguis!"
    show alicia smile1 at centerLeft with moveinleft
    b "A Alicia ya la conociste antes, es la chica que nos da la serotonina diaria."
    b "Es imposible conseguir enfadarla, y mira que lo hemos intentado jajaja"
    show alicia smile2 at centerLeft
    h "Ay tampoco es así… que [name] se va a pensar que estoy ida o algo "
    show lucas laugh at superLeft 
    show alejandro laugh at center with moveinright
    show alba laugh at centerRight with moveinright
    show gabriel laugh at superRight with moveinright
    t "Jajajaja"
    show alba smile1 at centerRight
    show gabriel smile1 at superRight
    show lucas smile2 at superLeft
    b "El pelirrojo del medio es Alejandro. No te dejes llevar por las apariencias, es un gymbro con todas las letras pero tiene buen corazón"
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
    show lucas smile3 at superLeft

    b "Lavarse el pelo con la lluvia"
    show gabriel angry2 at superRight
    p "Pero bueno quieres que [name] sea nuestra amiga o estás intentando que no se acerque"
    show gabriel smile2 at superRight
    p "No le escuches, llamame Gabri, aunque todos me llamen Iluminao, adoro los animalitos y el campito aunque estemos en una ciudad..."
    menu:
        "¡Yo también! Que guay":
            jump veryFriendlyGabriel
        "Encantad[genero], soy [name]":
            jump friendlyGabriel

    label veryFriendlyGabriel:
    show gabriel smile3 at superRight
    p "¿Si? Podemos quedar un día y te enseño mi mascota. ¡Es un Border Coly precioso!"
    show lucas smile2 at superLeft
    b "Pisa el freno que falta una por presentar, luego ya haced lo que querais tortolitos"
    show gabriel smile1 at superRight
    p "Ups, perdón jajaja"
    jump conocidoGabriel

    label friendlyGabriel:
    show gabriel smile3 at superRight
    p "[name], que nombre más bonito. ¿Y por qué te mudaste a.."
    show lucas smile3 at superLeft
    b "las preguntas para más tarde tortolitos que me falta una por presentar"
    show gabriel smile1 at superRight
    p "vale mamá"
    jump conocidoGabriel

    label conocidoGabriel:
    show lucas smile1 at superLeft
    b "En fin, por donde iba..."
    b "Por último pero no menos importante, nuestra incomprendida de la vida, ¡Alba!"
    show alba annoyed at centerRight
    c "Que sea más tímida no significa que sea una incomprendida..."
    show lucas smile2 at superLeft
    b "Luego se suelta más, solo dale algo de tiempo. Hablando de lo que comentaba antes, ¿pijamada este finde todos juntos? ¡Alicia pone casa!"
    show alba smile1 at centerRight
    menu:
        "No se yo...":
            jump noPijamada
        "Venga vale":
            jump siPijamada
    
    label noPijamada:
    show alejandro smirk at center
    g "Venga anímate, parecemos majaras pero te lo vas a pasar genial en la pijamada."
    g "Alicia prepara una limonada sin azucar y tiene un gatete"
    show lucas smile3 at superLeft
    b "Nah, [name] viene si o si"
    b "Recuerda que el viernes quedamos a las 20 donde el instituto para ir a casa de Alicia, ¿Vale?"
    menu:
        "Ookey":
            jump pijamadaDecidido
        "Bueno vale":
            jump pijamadaDecidido

    jump pijamadaDecidido

    label siPijamada:
    show alicia delighted at centerRight with move
    h "¡Yey! Voy a ir diciendole a mi madre que compre las cosas para hacer una limonada"
    hide alicia delighted with moveoutright
    show alejandro sad at center
    g "¡¡¡Recuerda que no tenga azucar!!!"
    b "Que sí gymbro, su madre ya sabe que tiene que hacer una limonada sosa como siempre jajaja"
    b "Bueno [name] pues recuerda que el viernes quedamos a las 20 donde el instituto para ir a casa de Alicia, ¿Vale?"
    menu:
        "Genial":
            jump pijamadaDecidido
        "Apuntado":
            jump pijamadaDecidido

    label pijamadaDecidido:
    scene bg black with pixellate
    "(Pasas toda la semana con ellos hasta el viernes de la pijamada)"

    #PIJAMADA
    scene bg apartment exterior with fade
    show lucas normal at right with moveinright
    b "Y esta es la casa de Alicia, vamos a entrar cuanto antes que me muero de hambre"
    "*Tok tok*"
    show gabriel smile1 at left with moveinleft
    p " Buenas Chiquetss, estamos en la cocina preparando la cena, dejad las mochilas en el salón y venid"
    show lucas surprised
    b "¡Uh! ¿Qué ha hecho la madre de Alicia esta vez? Me muero por sus croquetitas Mmhh"
    show gabriel smile2
    p "Venid a la cocina y lo vereis jeje"

    scene bg encore kitchen with fade

    show alicia annoyed at centerLeft
    h "¡Te juro que la limonada no tiene azúcar blanco, es estevia, que he visto a mi madre echarlo!"
    show alejandro angry2 at centerRight with moveinright
    g "¡MENTIRA! Una limonada tan deliciosa, ¿sin nada de azucar? No me lo creo"
    show alejandro angry1
    show alba smug at superRight with moveinright
    c "Pues tienes croquetas bien grasientas de cena así que prepárate para el workout de mañana"
    show alejandro surprised
    g "¿QUÉEE?"
    show lucas smile1 at superLeft with moveinleft
    show alejandro sad
    p "Haz el favor de disfrutar de la cena y ya te preocuparás del ejercicio mañana, que la mami de Happy Flower lo ha hecho todo casero con todo su amor y no tiene aditivos ni mierdas"
    c "Peores son los batidos de proteinas con cosas raras que te metes al cuerpo"
    show lucas laugh
    show alicia laugh
    show alba laugh
    b "Zasca JAJAJAJAJ"
    show alba smile1
    show alicia smile1
    show lucas smile1
    b "[name] a ti te gustan las croquetas, ¿no? Que encima son caseras.."
    menu:
        "Pues...":
            jump tenerMalGusto
        "Obvio que sí":
            jump tenerBuenGusto

    label tenerMalGusto:
    show alba shocked at superRight
    show alejandro surprised at centerRight
    show lucas smirk
    b "Pues más para mí jeje, Happy flower tenía también sobras así que no te preocupes"
    c "Las croquetas de la madre de Alicia son un manjar que no todo el mundo sabe apreciar"
    show alejandro sad
    show alba smug
    g "Y dale, que sí que están muy ricas pero me lo poneis imposible para ponerme en forma.."
    jump empiezaPijamada

    label tenerBuenGusto:
    show lucas smirk at superLeft
    b "Quien rechace esta oferta de croquetas caseras está tomando la peor decisión de su vida"
    show alejandro sad
    g "¿Podeis parar de meterme dagas? Que ya os he dicho que me las voy a comer tontos"
    show lucas smile3
    b "Así me gusta, croquetitas para todos"
    jump empiezaPijamada

    label empiezaPijamada:
    show alejandro smile1
    show alba smile1
    h "En fin chicos, mi madre ha quedado mañana con sus amigas fuera de la ciudad para hacer un ‘Brunch’ con sus amigas así que hoy no duerme aquí"
    show alicia smile2
    h "¡Así que tenemos noche libre para lo que queramos!"
    show lucas laugh
    b "¡Noche de Pelis de Terror!"
    show alejandro smirk
    g "¡Jugar a verdad o reto!"
    show alicia annoyed
    h  "Prefiero verdad o reto antes que traumarme con mas pelis"
    show gabriel laugh at center
    p "Una amiga me habló de un documental de Notflix sobre toda la industria cárnica"
    p "¡Le gustó tanto que se hizo vegana tras vérselo, igual os gusta!"
    show alba annoyed
    c "Voto por verdad o reto con tal de no comerme la chapa del siglo o un peñazo de peli"
    show lucas smile1 at superLeft
    show alejandro smile1 at centerRight
    show gabriel smile1 at center
    b "Y bien [name], ¿Qué quieres hacer tú?"
    menu:
        "Peli de terror":
            jump noVerdadOReto
        "Verdad o reto":
            jump verdadOReto
        "Documental de Notflix":
            jump noVerdadOReto

    label noVerdadOReto:
    show alicia smile2
    show alba smile1
    h "3 contra 2, por lo que verdad o reto gana jeje"
    show lucas sad
    b "Bueeeno, vaale. Pero la proxima vez peli de terror"

    jump comerCroquetas

    label verdadOReto:
    show alejandro smirk
    show alba smile1
    show alicia smile1
    g "Una chica con iniciativa. Así nos conoces mas a todos nosotros, ¿no?"
    show alba smug
    c "Creo que con solo una semana aquí ya nos tiene calados a todos jajaja"

    jump comerCroquetas

    label comerCroquetas:
    show lucas smirk
    b "¡Pues a devorar las croquetas y luego nos subimos a las habitaciones, nos ponemos el pijamita y jugamos hasta que nos durmamos!"
    scene bg black with pixellate
    "*Ñam ñam ñam*"
    #PONER SONIDITO DE COMER AAAAAAAAAAAAAAAAAAAAA
    jump pijamada

    label pijamada:
    scene bg bathroom with dissolve
    show alejandro normal pajama at centerRight with moveinright
    show lucas smile1 pajama at centerLeft with moveinleft
    b "¿Todavía sigues durmiendo con esa camiseta cutre? Que si no tienes pijama Alicia tendrá alguno por ahí"
    show alejandro angry1 pajama
    g "Já, já, já. Este es mi pijama, siempre tengo mucho calor por la noche y así duermo más cómodo"
    show gabriel smile2 pajama at center with moveinleft
    p "De hecho tiene razón, con menos ropa el sueño es más profundo porque el cuerpo se enfría y se autorregula más rápido que con el algodón de la ropa"
    show gabriel smile3 pajama
    show alicia normal pajama at superRight with moveinright
    h "..."
    show alba normal pajama at superLeft with moveinleft
    c "..."
    show lucas normal pajama
    show alejandro normal pajama
    b "..."
    menu:
        "...":
            jump akwardSilence
        "Sois unos frikis de narices":
            jump respuestaBorde
        
    #FALTA AVANZAR A PARTIR DE AQUI CARAS Y DE TODO
    label akwardSilence:
    h "Jajajaj no se corta ni un pelo"
    c "Bien tirada"
    t "Jajajajaja"
    b "Ahora que veo que estamos bien activos vamos al salón un rato y cuando tengamos sueño nos subimos"
    jump risasSolucionado
    label respuestaBorde:
    b "Vale parejita autorregulame ésta"
    b "*fart*" with hpunch
    p "¡LUCAS!"
    h "¡EVACUACIÓN, TODOS AL SALÓN DE INMEDIATO!"
    jump risasSolucionado
    label risasSolucionado:
    c "Me bajo las mantitas, vamos allá."

    #Transicion al salon
    scene bg living room
    b "Pues hoy vamos a innovar un poco y vamos a jugar a Mechero"
    menu:
        "Yo no fumo":
            jump noFuma
        "¿Mechero?":
            jump siFuma
    label noFuma:
    b "No seas bob[genero] [name]"
    label siFuma:
    b "En Mechero alguien te hace una pregunta al oído, la respuesta a las preguntas siempre es una persona."
    b "Solo puedes responder a la pregunta elegiendo a una pregunta que esté en esta habitación."
    b "Le pasas el mechero a quien hayas elegido y se tira una moneda."
    b "Si es cara tienes que decir la pregunta que te han hecho."
    b "Si es cruz nadie salvo tú y el que te ha hecho la pregunta sabrá por qué has escogido a esa persona" 
    menu:
        b "¿Entendido?"
        "Si":
            jump expMecheroDone
        "No":
            jump siFuma
    
    label expMecheroDone:
    h "Bueno pues empiezo yo que para algo es mi casa jajaj, y voy a preguntar a..."
    h "Alba"
    "*Susurros*"
    "(Alba le pasa el mechero a Alejandro)"
    g "¿Que? Como salga cara y me hayas señalado por algo feo te vas a enterar boba"
    "*Sale cara*"
    h "Oh oh"
    g "¿Y bien?"
    c "Me ha preguntado que si solo pudiera escoger a una persona para sobrevivir a una apocalipsis zombie a quién escogería"
    g "Aww, ¿es porque estoy más fuerte que el resto?"
    c "Sí, por lo que tu carne tiene que estar mucho más sabrosa"
    b "Puajajajaja"
    h "JAJAJA Eso si que no me lo veia venir"
    g "???????"

    g "En fin, ahora me toca preguntar y escojo a Gabriel"
    "*Susurros*"
    "(Gabriel le pasa el mechero a Lucas)"
    "(Tiran el dado y sale cruz)"
    b "¡Oh venga ya! Nunca me entero de por qué me señalais"
    p "Para la proxima será jajaja"
    p "Hoy te quedas con la duda"
    b "Bueno pues me toca, ¡y voy a preguntar a [name]!"
    "*Gabriel te dice al oido:*"
    b "¿Con quién de aquí tendrías una relación amorosa?"
    menu:
        b "¿Quién te ha gustado más?"
        "Alba":
            $ pElegido = c
            $ generoPareja = "a"
            $ pronombrePareja = "ella"
            $ nombrePareja = "Alba"
            jump partnerChosen
        "Alicia":
            $ pElegido = h
            $ generoPareja = "a"
            $ pronombrePareja = "ella"
            $ nombrePareja = "Alicia"
            jump partnerChosen
        "Alejandro":
            $ pElegido = g
            $ generoPareja = "o"
            $ pronombrePareja = "él"
            $ nombrePareja = "Alejandro"
            jump partnerChosen
        "Gabriel":
            $ pElegido = p
            $ generoPareja = "o"
            $ pronombrePareja = "él"
            $ nombrePareja = "Gabriel"
            jump partnerChosen

    label partnerChosen:
    pElegido "Más te vale tirar cara Bestie"
    "(Sale cara)"
    b "Cagué, jaja."
    pElegido "¿Y bien?"
    b "Le pregunté quien le gustaba más de aquí."
    b "Lleva ya una semana, claramente se habrá decantado por alguien, ¿no?"
    if (pElegido == c):
        c "Oh, gra, gracias supongo. Pensaba que estaba demasiado borde contigo, me alegro que te guste mi personalidad"
    
    if (pElegido == h):
        h "¿Ay en serio? Pues a mi me pareces un encanto de persona, nunca nadie se suele fijar en mí porque me ven demasiado inocente..."
    
    if (pElegido == g):
        g "Ay que lind[genero], tú me pareciste monisim[genero] desde el primer dia que nos presentaron..."
        g "Igual congeniamos, jeje"
    
    if (pElegido == p):
        g "Y claro, va y escoge al chico delgado del mullet, ¿no?"
        p "Que me seleccione a mi antes que un chico fibraro con una weekly routine de gym y gym es completamente normal Alejandro"
        p "Eres más que un chico con músculos pero tienes que dejar de centrarte en eso todo el rato."
        p "Por donde iba, me alegra saberlo [name], he disfrutado mucho de tu compañía esta semana yo también..."
    
    b "*Bostezo*"
    b "Bueno, ya es muy tarde, ¿no? Igual es hora de irse a la cama y enfriar un poco esto."

    h "Si, yo estoy ya muy cansada..."

    pElegido "Psst, ¿te gustaría quedarnos un rato hablando? Me gustaría hablar contigo de lo que has mencionado antes..."
    menu:
        "Si":
            jump siHablarUnRato
        "No":
            jump noHablarUnRato
    
    label noHablarUnRato:
    pElegido "Venga porfi... solo son 2 minutos..."

    label siHablarUnRato:
    pElegido "Solo quería que supieras que es reciproco..."
    pElegido "Y se que solo llevas una semana con nosotros, pero podríamos conocernos mejor y ver si congeniamos..."
    pElegido "¿Te parece tener una cita la semana que viene? Yo invito"
    menu:
        "¡Genial!":
            jump siIrCita
        "Mm... Venga, vale":
            jump siIrCita

    label siIrCita:
    pElegido "¡Genial! Nos vemos la semana que viene"


    #PRIMERA CITA
    label PrimeraCita:

    "(Pasas la semana en el instituto, relacionandote cada vez más con [nombrePareja] y llega el día de la cita)"
    "(Ambos quedais en un restaurante de la ciudad que te ha recomendado [pronombrePareja])"

    if (generoPareja == "o"):
        y "(Se ha puesto elegante y todo…)"
        menu:
            "Que guapo estás":
                jump primerElogioCita
            "Que raro te veo, no te pega":
                jump noPrimerElogioCita
        label primerElogioCita:
        pElegido "¿Tu crees? Gracias, me ves tranquilo pero me he tirado 20 minutos pensando que ponerme jajaja"
        jump finPrimerElogioCita
        label noPrimerElogioCita:
        pElegido "Oh.. La verdad es que justo lo he estrenado hoy, solo quería intentar impresionar jajaja me lo apunto para la siguiente"
        jump finPrimerElogioCita

    label finPrimerElogioCita:
    Camarero "Muy buenas. Hoy estamos un poco llenos así que vais a tener que esperar un momento. En cuanto se vaya una mesa os meto"
    pElegido "Sin problema, podemos esperar"
    pElegido "Podemos aprovechar esta espera para hacer una cosa mientras tanto.."
    pElegido "Siento que estas dos semanas has estado muy cómoda con nosotros, pero no has participado mucho y no te conocemos mucho."
    pElegido "¿Te parece si nos hacemos la típica ronda de preguntas para conocernos mejor?"
    pElegido "Se que es un poco infantil pero así me cuentas algo de tí..."
    if (pElegido != c):
        pElegido "No me callo ni debajo del agua y a veces no dejo hablar..."
    else:
        pElegido "No suelo hablar mucho y eso dificulta más todo..."
        pElegido "No tengo buenas habilidades sociales"
    menu:
        "Venga, vamos a jugar":
            jump empiezaElOtroRondaPreguntas
        "Vale, pero empiezas tú preguntando":
            jump empiezaElOtroRondaPreguntas
    label empiezaElOtroRondaPreguntas:
    pElegido "¡Genial! Comienzo preguntando yo"
    pElegido "Hmm... ¿Te consideras extrovertid[genero] o introvertid[genero]?"
    menu:
        "Extrovertid[genero]":
            jump extrovertida
        "Introvertid[genero]":
            jump introvertida
    label extrovertida:
    if (pElegido == g):
        pElegido "Ya somos 2, aunque me da a mi que ya te sabias mi respuesta jajaja"
    if (pElegido == h):
        pElegido "Ya somos 2, aunque me da a mi que ya te sabias mi respuesta jajaja"
    if (pElegido == c):
        pElegido "A ver si se me pega algo de ti, yo soy algo más callada pero en confianza hablo de más jajaja"
    if (pElegido == p):
        pElegido "A ver si se me pega algo de ti, yo soy algo más callado pero en confianza hablo de más jajaja"
    jump finExtrovertidaIntrovertida
    label introvertida:
    if (pElegido == g):
        pElegido "Se nota que al menos en confianza hablas más, eres un solecito una vez se te conoce"
    if (pElegido == h):
        pElegido "Se nota que al menos en confianza hablas más, eres un solecito una vez se te conoce"
    if (pElegido == c):
        pElegido "Estamos igual entonces, entre introvertid[genero]s nos la pasamos mejor aunque la gente se piense que quedamos y no hablamos nunca jajajaja"
    if (pElegido == p):
        pElegido "Estamos igual entonces, entre introvertid[genero]s nos la pasamos mejor aunque la gente se piense que quedamos y no hablamos nunca jajajaja"
    jump finExtrovertidaIntrovertida

    label finExtrovertidaIntrovertida:
    pElegido "Ahora te toca preguntarme"
    menu:
        "¿Que buscas tener conmigo?":
            jump preguntaPrimeraCitaSeria
        "¿Cual es tu signo del zodiaco?":
            jump zodiacoPrimeraCita
    
    label preguntaPrimeraCitaSeria:
    pElegido "La gente suele buscar algo esporádico o sexo rápido. Pero me has encantado como persona y no descarto tener algo serio..."
    pElegido "Siempre y cuando tú estes de acuerdo, claro..."
    jump finPrimeraPreguntaAPareja
    label zodiacoPrimeraCita:
    pElegido "Si te soy sincer[genero] no tengo ni idea. El que sea más compatible contigo espero jajaja"
    jump finPrimeraPreguntaAPareja

    label finPrimeraPreguntaAPareja:
    pElegido "Emm... Me toca preguntar a mi"
    pElegido "¿Te consideras alguien impulsivo que se deja llevar por las emociones o eres más racional y objetiv[genero]?"
    menu:
        "Impulsiv[genero] y pasional":
            jump pasional
        "Racional y objetiv[genero]":
            jump racional
    label pasional:
    if (pElegido == g):
        pElegido "Se nos va a dar fatal lo de planear quedadas juntos jajaja, pero al menos se que ambos tenemos sentimientos fuertes"
    if (pElegido == h):
        pElegido "Se nos va a dar fatal lo de planear quedadas junt[genero]s jajaja, pero al menos se que amb[genero]s tenemos sentimientos fuertes"
    if (pElegido == c):
        pElegido "Dicen que los polos opuestos se atraen jajaja"
        pElegido "Así nos complementamos..."
    if (pElegido == p):
        pElegido "Dicen que los polos opuestos se atraen jajaja"
        pElegido "Así nos complementamos..."
    jump finPasionalRacional
    label racional:
    if (pElegido == g):
        pElegido "Dicen que los polos opuestos se atraen jajaja"
        pElegido "Así nos complementamos..."
    if (pElegido == h):
        pElegido "Dicen que los polos opuestos se atraen jajaja"
        pElegido "Así nos complementamos..."
    if (pElegido == c):
        pElegido "Ya me veo planeando contigo la quedada de dentro de 3 meses con antelación jajaja"
    if (pElegido == p):
        pElegido "Ya me veo planeando contigo la quedada de dentro de 3 meses con antelación jajaja"
    jump finPasionalRacional

    label finPasionalRacional:
    pElegido "Personalmente creo que tenemos mucha química."
    pElegido "Igual estoy algo ñoñ[genero] pero siento que es algo que puede ser duradero..."
    pElegido "Pero vamos a fluir y ver que tal."
    pElegido "Mientras tanto vamos a comer, que ya veo al camarero venir a llamarnos"

    "(La cita fue redonda, realmente es tu pareja ideal)"

    "(Pasaron un par de semanas y todo fue como un sueño)"
    "(Nunca habías conocido a alguien que te cuidara y se preocupara tanto por ti.)"
    "(Te hacía sentir como en una nube, aunque no siempre todo era perfecto...)"


    "¿Pero dónde te has metido [nombrePareja]? A este paso vamos a llegar tarde."

    "*¡Ponk!*" with hpunch
    ChicoRandom "Aiba, perdon, no te había visto."
    menu:
        "La próxima vez mira por donde vas.":
            jump choqueMajo
        "No pasa nada, yo tampoco te había visto.":
            jump choqueBorde
    label choqueMajo:
    ChicoRandom "Lo siento de verdad, llego tarde para ver Cosmic Frontier y voy acelerado."
    y "¡Vas a ver Cosmic Frontier! ¡Yo también! Si tan solo [nombrePareja] no llegase tarde :("
    jump finChoqueRandom
    label choqueBorde:
    ChicoRandom "¿Lo que hace llegar tarde a ver una película, eh?"
    y "A quien se lo vas a contar aquí llevo esperando 30 minutos a [nombrePareja] que llega tardísimo."
    jump finChoqueRandom
    label finChoqueRandom:
    ChicoRandom "Jajajaja es como yo entonces, no seas muy dur[genero] cuando llegue, algunos somos muy despistados."
    y "Y tanto, jajajaja"
    y "Ya veo ya jajajaja"
    pElegido "¡Eh! ¿Y tú quién eres? ¡¿Estas ligando con mi novi[genero]?!"
    ChicoRandom "Oh no no, ya me iba que llego tarde, bueno nos vemos."
    menu:
        "¡Hasta otra!":
            jump despedirseRandom
        "¡Disfruta de la peli!":
            jump despedirseRandom
    label despedirseRandom:
    pElegido "¿Y ese quien era? ¿Llego tarde 15 minutos y te pones a ligar con otro?"
    menu:
        "¡Pero qué dices! ¡Llegaba tarde, como tu y se ha chocado conmigo, nada más!":
            jump sinceroCelos
        "Siiii por supuesto, llegabas tan tarde que ya me estaba buscando un reemplazo jajajaja.":
            jump noSinceroCelos
    label sinceroCelos:
    pElegido "Pues no estoy yo muy segur[generoPareja] de que así sea como le sonrías y miras a un extraño que se ha chocado contigo."
    jump finCelos
    label noSinceroCelos:
    pElegido "¿Me estas vacilando? A mi no me hace ni puta gracia saber que tonteas con cualquiera."
    jump finCelos
    
    label finCelos:
    menu:
        "¿Pero me lo estás diciendo en serio? ¡Que no era nada de verdad no te preocupes, no me ha dicho ni su nombre!":
            jump reaccionCelos
        "Te estas emparanoiando que flipas ti[generoPareja], quitate la tontería y vamos a ver la peli que ya estará empezando":
            jump reaccionCelos
    label reaccionCelos:
    pElegido "Vale, pero que sepas que esto no me ha gustado un pelo, espero que no se repita."
    "...¿Que coño?"
    "Ese momento fue un poco raro, no se que le pasó a [nombrePareja]."
    "Pero el resto de la cita fue super bien, y nos encantó la película, espero que todo siga así de bien."

    
    #Escena control de ropa
    label ControlRopa:
    "(Unos días más tarde ibas a salir de fiesta con tus nuevos amigos)"
    "(Hacía mucho que no salías así que te hacía mucha ilusión y compraste un conjunto nuevo solo para esa noche.)"

    b "Buah, tengo muchísimas ganas de salir esta noche, va a ser espectacular."
    pElegido "Pues a mi no me hace especial ilusión."
    pElegido "Estoy algo cansad[generoPareja] y no me apetece que salgamos los 3 juntos."
    b "Pues bien que te gustaba antes de empezar a salir con [name] jajaja."
    pElegido "Jajajaja, pero lo dicho, ya estoy con [name], no necesito a nadie más."
    b "Bueno puedes salir para pasar un buen rato con tus amigos, que salir de fiesta no es solo para ligar, ¿a ti no te apetece [name]?"
    menu:
        "Siii, tengo muchísimas ganas de salir, y pasarlo bien con todo el mundo":
            jump ganasDeSalir
        "Bueno, no me apetece mucho, pero va a ir todo el mundo, así que no puedo faltar":
            jump noGanasDeSalir
    
    label ganasDeSalir:
    b "¡Así se habla!"
    pElegido "Pues no se porque tienes tantas ganas de ir."
    pElegido "Si siempre que salimos a beber acabas haciendo el ridículo jajaja"
    pElegido "Pero bueno, si hay que ir se va cielo, allá tú."
    jump finGanasDeSalir
    label noGanasDeSalir:
    b "Venga yaa, sois unos frikis, si va a ser increíble."
    pElegido "Oye pero si no quieres no vamos, ¿eh?"
    b "No, eso si que no, si faltais no os lo perdono. ME NIEGO."
    jump finGanasDeSalir
    label finGanasDeSalir:
    b "El caso, ¿ya sabéis lo que os vais a poner?"
    pElegido "Yo iré normalit[generoPareja], no voy en chándal porque se está lavando jajaja."
    b "Jajaja ¿Y tu [name]? ¿Te pondrás lo que te compraste el otro día?"
    pElegido "Ah, ¿te compraste un outfit? Cómo es que no me lo has enseñado."
    menu:
        "Quería sorprenderte...":
            jump queriaSorprenderte
        "No pensé que necesitase enseñartelo antes supongo":
            jump queriaSorprenderte
    label queriaSorprenderte:
    pElegido "Bueno pues ya enséñamelo, ¿no?"
    b "Mira, es este... ¡Es una pasada! Vas a ser la persona más atractiva de toda la fiesta."
    pElegido "Pero esto... ¿Tú te has mirado en un espejo?"
    pElegido "Jajaja"
    pElegido "No se, pareciese que quieres que todo el mundo se fije en ti, tampoco hace falta tanto."
    menu:
        "Pero... pensé que te gustaría...":
            jump opinionTraje
        "No sé, me gustaba como me quedaba, no veo el problema.":
            jump opinionTraje
    label opinionTraje:
    pElegido "Quiero decir"
    pElegido "No te ves tan mal"
    pElegido "Pero parece que solo quieres llamar la atención, ¿no?"
    pElegido "No hace falta que todo el mundo de la fiesta te conozca."

    b "¿Qué más da? Ve a la fiesta como te dé la gana y punto."
    pElegido "Bueeeno venga, un día es un día supongo..."
    pElegido "Pero ya hablaremos cuando volvamos de la fiesta"
    pElegido "No me gusta que tomes decisiones sin consultarmelo antes."
    pElegido "Te quiero mucho"
    b "¡FIESTA, FIESTA, FIESTA!"

    #Cambio de escena

    #(Pantalla en negro, cambio de escena en casa)
    "(Los padres de [nombrePareja] se han ido un par de dias a la casa antigua por el papeleo de la mudanza.)"
    "(Así que [nombrePareja] te ha invitado a pasar la noche y ver una peli en su nueva casa)"

    pElegido "Buenas cielo, ¿cómo está mi niñ[genero]?"
    pElegido "¿List[genero] para la maratón de pelis de terror?"
    menu:
        "Em... prefiero que sean de otro género porfi, no me gusta el terror":
            jump noTerror
        "¿Y si en vez de peli nos saltamos ese paso y vamos a lo importante? Jejeje":
            jump noTerrorHorny
    label noTerror:
    pElegido "¿Otra vez vamos a tener esta conversación?"
    pElegido "Te dije que te invitaba solo si la peli era de terror"
    pElegido "Nunca me escuchas y al final el que se jode siempre soy yo."
    y "¿Me vas a hacer irme a casa entonces?"
    pElegido "Pues ya supongo que no"
    pElegido "Que luego tus amigos te dicen que el malo soy yo cuando sabes perfectamente que te quiero y que no es así."
    pElegido "Pero bueno, pasa y ahora vemos que hacemos, alguna solucion habrá."

    "(Pasamos al salón)"
    pElegido "Bueno sea como sea estás aquí"
    jump finTerror

    label noTerrorHorny:
    if (generoPareja == "a"):
        pElegido "Pero te dije que te vinieras mon[genero]"
        pElegido "Ya sabes que me gusta mucho verte maquillada y guapa, y has venido como si estuvieras de resaca..."
        y "Cariño vengo a pasar la noche contigo no al galardón de los Goya"
    if (generoPareja == "o"):
        pElegido "Pero te dije que hoy no fueras a hacer ejercicio."
        pElegido "Ya sabes que me gusta mucho como estás ahora y solo me has hecho quedarme esperandote como un estupido..."
        y "Cariño ya sabes que el ejercicio es algo que me gusta y me relaja."

    jump finTerror

    label finTerror:

    pElegido "Solo te pedí 1 cosa y no me has hecho ni caso"
    pElegido "Como seas así con tus amigos, normal que estés apartada del grupo"
    pElegido "Al menos compénsame esta noche en la habitacion, ¿no? Jajaja"
    pElegido "Vamos ahora y luego hablamos jejeje..."

    "(Al final pasasteis una buena noche, cada vez con más confianza y cariño, más acostumbrados el uno al otro, empezando a desarrollar una rutina de pareja)"

    # Finaliza el juego:

    return
