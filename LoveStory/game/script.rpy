# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define b = Character("Lucas")
define y = Character("[name]")
define h = Character("Alicia")
define g = Character("Alba")
define p = Character("Gabriel")
define g = Character("Alejandro")
define t = Character("Todos")
transform left:
    xalign 0.0
    yalign 0.35
transform right:
    xalign 0.8
    yalign 0.35
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
    show alicia sad
    h "¡Ay jo lo siento! Perdona, no te había visto."
    h "¿Te he hecho daño? Ay lo siento mucho joe, no era mi intención… Toma"
    hide alicia sad
    show alicia smile1
    "(Recibiste Tirita de Alicia)"
    b "Calma Alicia jajaja, solo ha sido un golpe"
    jump conocidoAlicia

    label perdonAlicia:
    show alicia smile1
    h "Ay no seas boba! Soy yo que estoy siempre en los mundos de yupi y nunca me entero de nada! Toma, como un simbolo de paz jajaja"
    hide alicia smile1
    show alicia smile2
    "Recibiste Tirita de Alicia."
    b "Alicia no tenemos tiempo para tus ñoñerias."
    jump conocidoAlicia

    label conocidoAlicia:
    show lucas smile1 at right
    
    b "Esta es [name], era mi mejor amig[genero] de mi antiguo instituto, y parece que ahora va a ser nuestr[genero] compi de clase. ¿NO ES GENIAL?"
    h "Ay genial! Más gente en el grupo! Estoy deseando conocerte. Pijamada este finde en mi casa?"
    b "De una! Luego en el recreo le presento al resto y les digo lo de la pijamada!"
    b "[name], cuando se acabe el recreo te presento a mi grupito, ya les he avisado por whatsthematter que tenemos una nueva personita jeje."
    scene bg black
    "(Termina la clase y llega al recreo)"
    scene bg club
    "¿Esos no son Lucas y Alicia?"
    "Parece que están con otras 3 personas, voy a saludar"
    b "¡[name] Ven aquí, te voy a presentar a mis amiguis!"
    b "A Alicia ya la conociste antes, es la chica que nos da la serotonina diaria."
    b "Es imposible conseguir enfadarla, y mira que lo hemos intentado jajajajaja"
    h "Ay tampoco es así… que [name] se va a pensar que estoy ida o algo jajaja"
    t "Jajajaja"
    b "Este es Alejandro. No te dejes llevar por las apariencias, es un gymbro con todas las letras pero tiene buen corazón"
    b "Y siempre nos ayuda cueste lo que cueste, ¿a que sí corazón de melón?"
    g "Lucas no intentes convencerme para ir a jugar después de clase que hoy estoy molido."
    b "Joeee!!"
    b "Enfin, a mi izquierda tenemos a nuestro querido Gabriel."
    b "Tiene mejor melena que Alicia con la mejor weekly routine."
    b "Lavarse el pelo con la lluvia"
    p "Pero bueno quieres que [name] sea nuestra amiga o estás intentando que no se acerque?"
    p "No le escuches, llamame Iluminao, adoro los animalitos y el campito aunque estemos en una ciudad..."
    menu:
        "¡Yo también! Que guay":
            jump veryFriendlyGabriel
        "*Encantad@, soy [name]":
            jump friendlyGabriel

    label veryFriendlyGabriel:
    "SIN IMPLEMENTAR"
    jump conocidoGabriel

    label friendlyGabriel:
    "SIN IMPLEMENTAR"
    jump conocidoGabriel

    label conocidoGabriel:

    b "Y por último pero no menos importante, nuestra incomprendida de la vida, Alba!"
    g "Que sea más tímida no significa que sea una incomprendida..."
    b "Luego se suelta más, solo dale algo de tiempo jajaj. En fín, pijamada este finde todos juntos? Alicia pone casa!"
    menu:
        "No se yo...":
            jump noPijamada
        "Venga vale":
            jump siPijamada
    
    label noPijamada:
    g "Venga, parecemos majaras pero te lo vas a pasar genial en la pijamada."
    g "Alicia prepara una limonada sin azucar y tiene un gatete"
    jump pijamadaDecidido

    label siPijamada:
    h "Yey! Voy a ir diciendole a mi madre que compre las cosas para hacer una limonada"
    g "¡¡¡Recuerda que no tenga azucar!!!"
    b "Que sí gymbro, su madre ya sabe que tiene que hacer una limonada sosa como siempre jajaja"
    jump pijamadaDecidido

    label pijamadaDecidido:
    scene bg black
    "TO BE CONTINUED"

    # Finaliza el juego:

    return
