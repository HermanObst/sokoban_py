import soko
import gamelib

TAM_CEL = 64 #El tamaño de los GIF

def cargar_niveles():
    """Dado un archivo con los niveles del SOKOBAN con la forma de:
    Nivel
    nombre (opcional)
    descripción
    Devuelve una lista de listas. Estas representan a cada nivel. Dentro de estas hay dos listas:
    Una que guarda el nivel y nombre (opcional); y otra que guarda la descripción (Previamente deja a todas las lineas de mismo len"""
    total = []
    nivel = {}
    nombre = ""
    descrip = []
    with open("niveles.txt") as niveles:
        for linea in niveles:
            if linea == "\n": #Cuando encuentra un salto de linea (paso de nuvel) guarda el nivel (dentro tiene nombre y descrip) en total
                descrip = uniformar_cadenas(descrip)
                nivel["nombre"] = nombre
                nivel["descripcion"] = descrip
                total.append(nivel)
                nombre, descrip, nivel = "", [], {}

            elif "#" not in linea: #las cadenas que no son salto ni tienen # son el nivel y el nombre. se guardan en nombre
                sin_salto = linea.rstrip("\n")
                nombre += f"{sin_salto} "

            elif "#" in linea: #las descripciones tienen, necesariamente, el caracter pared --> se guardan en descrip
                descrip.append(linea.rstrip("\n"))

        nivel["nombre"] = nombre #Cuando se termina el archivo no hay un salto de linea solo y no entra a guardar el último nivel
        nivel["descripcion"] = descrip
        total.append(nivel)

    return total

def uniformar_cadenas(lista_cadenas):
    """Dade una lista de cadenas, calcula cual tiene el máximo len y va agregando " "
    en todas las demás, hasta que queden del mismo tamaño"""
    cadenas_uniformes = []
    maxim = max(len(x) for x in lista_cadenas)
    for cadena in lista_cadenas:
        while len(cadena) < maxim:
            cadena += " "
        cadenas_uniformes.append(cadena)

    return cadenas_uniformes

def cargar_teclas():
    """Dado el archivo con las especificaciones de los controles, devuelve un diccionario
    que contiene como clave la tecla del teclado y como valor el comando específico que recibe 
    soko.mover para actualizar el estado del juego"""
    direcciones = {"NORTE": (0, -1), "SUR": (0, 1), "OESTE": (-1, 0), "ESTE": (1, 0), "REINICIAR": "REINICIAR", "SALIR":"SALIR"}
    teclas = {}
    with open("teclas.txt") as archivo:
        for linea in archivo:
            if linea == "\n":
                continue
            linea = linea.rstrip("\n").split(" = ")
            teclas[linea[0]] = direcciones[linea[1]]

    return teclas

def soko_dibujar(grilla, nivel, niveles):
    """Dada la descripción (estado) de un nivel del SOKOBAN, lo dibuja usando la librería gamelib
    PRE: La lista de descripción debe esta constituida por listas que contengan cada fila de esta, caracter por caracter. 
    El formato debe ser el propuesto por la función soko.juego_crear"""
    
    gamelib.draw_begin()
    gamelib.title(f"Sokoban: {niveles[nivel]['nombre']}") 

    for f in range(len(grilla)):
        for c in range(len(grilla[0])):
            gamelib.draw_image('img/ground.gif',(c) * TAM_CEL, (f) * TAM_CEL)

            if soko.hay_objetivo(grilla,c,f):
                gamelib.draw_image(f'img/goal.gif',(c) * TAM_CEL, (f) * TAM_CEL)

            if soko.hay_caja(grilla,c,f):
                gamelib.draw_image(f'img/box.gif',(c) * TAM_CEL, (f) * TAM_CEL)

            if soko.hay_jugador(grilla,c,f):
                gamelib.draw_image(f'img/player.gif',(c) * TAM_CEL, (f) * TAM_CEL)

            if soko.hay_pared(grilla,c,f):
                gamelib.draw_image(f'img/wall.gif',(c) * TAM_CEL, (f) * TAM_CEL)

                
    gamelib.draw_end()

def main():
    nivel = 0
    niveles = cargar_niveles()
    controles = cargar_teclas()
    juego = soko.crear_grilla(niveles[nivel]["descripcion"]) #crea la grilla según el nivel que se alcance (contador nivel que aumenta cuando se gana) y [1] es la posicion donde esta la descripcion


    gamelib.resize(TAM_CEL * len(niveles[nivel]["descripcion"][0]), TAM_CEL * len(niveles[nivel]["descripcion"]))


    while gamelib.is_alive():

        soko_dibujar(juego, nivel, niveles)

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key

        if tecla not in controles:
            continue

        if controles[tecla] == "SALIR":
            break

        if controles[tecla] == "REINICIAR":
            juego = soko.crear_grilla(niveles[nivel]["descripcion"])
            continue

        juego = soko.mover(juego, controles[tecla])

        if soko.juego_ganado(juego):
            nivel += 1
            juego = soko.crear_grilla(niveles[nivel]["descripcion"])
            gamelib.resize(TAM_CEL * len(niveles[nivel]["descripcion"][0]), TAM_CEL * len(niveles[nivel]["descripcion"]))

gamelib.init(main)


