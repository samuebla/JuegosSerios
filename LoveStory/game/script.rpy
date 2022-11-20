# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define b = Character("Lucas")
define y = Character("[name]")
define h = Character("Alicia")
define g = Character("Alba")
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
    $ genero = "o"
    $ pronombre = "el"
    $ name = "Marica Chonda"
    jump entrarDone

    #SELECCION PRONOMBRES#
    scene bg black
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



    scene bg train tunnel

    "Al fin ha llegado el día, tras un largo viaje y mucho cambio. Tuvimos que mudarnos a la ciudad tras que Papá perdiera su trabajo"
    "Afortunadamente consiguió un trabajo gracias a un amigo en la ciudad de HighPeaks."
    "Desgraciadamente tuvimos que mudarnos a la ciudad y he tenido que dejar a todos mis amigos atrás"
    "Hoy es mi primer día en mi nuevo instituto y he de decir que tengo algo de miedo"
    "¿Y si ya tienen todos sus grupitos montados?"
    "¿Y si nadie me acepta tal y como soy?"
    "Aghhh, bueno al menos piensa que es una nueva oportunidad, ¿quién sabe lo que el futuro me depara?"
    "Al menos hay una única persona a la que conozco, pero hace mucho que no hablamos, dudo que siquiera me reconozca"
    "Un chico llamado Lucas iba a mi antiguo colegio pero tuvo que mudarse a la ciudad por problemas familiares"
    "Hubo mucho revuelo en el pueblo, durante unas cuantas semanas no había un rincón donde no fuera el principal tema de conversación"
    "Este chico se mudó a esta misma ciudad, así que probablemente le vea si tenemos la suerte de estar en la misma clase"
    "Espera, ¿esta era la parada en la que me tenía que bajar? ¿Dónde estoy? Nooo, cogí el metro en sentido contrario"
    "Y en 10 minutos debería de estar ya en clase… No puede ser que vaya a llegar tarde el primer día…"
    scene bg black
    "(Media hora más tarde…)"
    scene bg uni
    "Vale, esta debería de ser la parada. Ahora, ¿dónde se supone que está el instituto?"
    "Espera, ¿ese chico no es Lucas? A lo mejor también llega tarde como siempre hacía antes, quizás podría darme indicaciones"
    
    menu:
        "(Te acercas al chico)"

        "¿Lucas? ¿Eres tú?":
            jump acercarteLucas
        "(Darle una sorpresa)":
            jump sorpresaLucas

    label acercarteLucas:
    b "Hombre! Cuanto tiempo! Que haces tú por aquí, hacia años que perdimos el contacto"
    y "2 exactamente, me he mudado a High Peaks ahora, así que supongo que somos compañeros de clase"
    b "Genial! Estoy deseando presentarte a mis amigos, lo vas a flipar! Son un poco peculiares pero nada que ver con la escoria de nuestro antiguo instituto, recuerdas?"
    y "Como no me voy a acordar…tu llevas 2 años aqui pero yo me he mudado esta semana jajajaja."
    b "Venga no hay tiempo que perder! Que al final no llegamos a clase"
    jump conocidoLucas

    label sorpresaLucas:
    "SIN IMPLEMENTAR"
    jump conocidoLucas

    label conocidoLucas:

    scene bg old school

    "(Instituto HighPeaks)"
    y "Guau, este instituto es gigante pero…¿Por qué la verja está cerrada?"
    b "El director es muy estricto con la hora de entrada, y si llegas tarde tienes que llamar y te penalizan, pero ya me conoces, siempre tengo un plan B jeje."
    "(Lucas levanta un cartón que estaba apoyado al otro lado del muro del instituto y me señala para que le siga.)"
    y "¡No puedo ir y colarme el primer día de clase!"
    b "Caalma, nadie se dará cuenta, ¿o acaso quieres recibir tu primer castigo sin si quiera haberte presentado a la clase, eh?"

    menu:
        "Seguir a Lucas":
            jump seguirLucas
        "Llamar al timbre":
            jump llamarTimbre
    label seguirLucas:
    y "Como odio que siempre acabes convenciéndome de todo"
    b "Jajaja como los viejos tiempos. Venga, vamos."
    "Una vez dentro Lucas me guió por el edificio hasta la planta donde están las aulas de segundo año."
    scene bg black
    "Me quedé hablando con Lucas en el baño hasta que se terminara la primera hora y poder entrar sin problema a la segunda"
    "No ha cambiado nada de nada, es como si le hubiera visto ayer..."
    "Y pensar que llevabamos 2 años sin vernos…"
    jump entrarDone

    label llamarTimbre:
    "SIN IMPLEMENTAR"
    scene bg black
    jump entrarDone

    #CONOCE A ALICIA
    label entrarDone:

    "*Ding, dong, ding, dong*"
    "*Ding, dong, dong, ding*"
    "Ahí está, el cambio de clase, debería de aprovechar ahora para entrar al aula"
    scene bg lecturehall
    "Bien, parece que el profesor ya ha salido, menos mal. Veamos ahora solo tengo que encontrar un asiento libre sin…"
    "*¡Ponk!*"
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
    g "Que sea más tímida no significa que sea una incomprendida..."
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
    jump pijamadaDecidido

    label pijamadaDecidido:
    scene bg black
    "TO BE CONTINUED"

    # Finaliza el juego:

    return
