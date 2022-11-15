# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define b = Character("Bestie")
define r = Character("La puta de su madre")

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg train

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show bestie normal

    # Presenta las líneas del diálogo.

    b "Y la puta de tu madre que tal mea Juan"

    hide bestie normal

    show randomgirl delighted

    r "Bastante bien gracias por preguntar rey"

    # Finaliza el juego:

    return
