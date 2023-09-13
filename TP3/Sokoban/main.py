import soko
import gamelib
from colas_pilas import Pila
from backtracking import buscar_solucion

TAM_CEL = 64 #El tamaño de los GIF
IMAGENES = {"@": "player", "$": "box", ".": "goal", "#": "wall", " ": "ground"}

def cargar_niveles():
    """Dado un archivo con los niveles del SOKOBAN con la forma de:
    Nivel
    nombre (opcional)
    descripción
    Devuelve una lista de listas. Estas representan a cada nivel. Dentro de estas hay dos listas:
    Una que guarda el nivel y nombre (opcional); y otra que guarda la descripción (Previamente deja a todas las lineas de mismo len"""
    total = []
    nivel = []
    nombre = []
    descrip = []
    with open("niveles.txt") as niveles:
        for linea in niveles:
            if linea == "\n": #Cuando encuentra un salto de linea (paso de nuvel) guarda el nivel (dentro tiene nombre y descrip) en total
                descrip = uniformar_cadenas(descrip)
                nivel.append(nombre)
                nivel.append(descrip)
                total.append(nivel)
                nombre, descrip, nivel = [], [], []

            elif "#" not in linea: #las cadenas que no son salto ni tienen # son el nivel y el nombre. se guardan en nombre
                nombre.append(linea.rstrip("\n"))

            elif "#" in linea: #las descripciones tienen, necesariamente, el caracter pared --> se guardan en descrip
                descrip.append(linea.rstrip("\n"))

        nivel.append(nombre) #Cuando se termina el archivo no hay un salto de linea solo y no entra a guardar el último nivel
        nivel.append(descrip)
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
    direcciones = {"NORTE": (0, -1), "SUR": (0, 1), "OESTE": (-1, 0), "ESTE": (1, 0), "REINICIAR": "REINICIAR", "SALIR":"SALIR", "DESHACER": "DESHACER", "PISTA":"PISTA"}
    teclas = {}
    with open("teclas.txt") as archivo:
        for linea in archivo:
            if linea == "\n":
                continue
            linea = linea.rstrip("\n").split(" = ")
            teclas[linea[0]] = direcciones[linea[1]]

    return teclas

def soko_dibujar(grilla):
    """Dada la descripción (estado) de un nivel del SOKOBAN, lo dibuja usando la librería gamelib
    PRE: La lista de descripción debe esta constituida por listas que contengan cada fila de esta, caracter por caracter. 
    El formato debe ser el propuesto por la función soko.juego_crear"""
    
    for f in range(len(grilla)):
        for c in range(len(grilla[0])):
            gamelib.draw_image('img/ground.gif',(c) * TAM_CEL, (f) * TAM_CEL)

            for elemento in grilla[f][c]:
                gamelib.draw_image(f'img/{IMAGENES[elemento]}.gif',(c) * TAM_CEL, (f) * TAM_CEL)
                

def main():
    descripcion = 1
    nombre = 0
    nivel = 0
    solucion_encontrada = None
    niveles = cargar_niveles()
    controles = cargar_teclas()
    juego = soko.crear_grilla(niveles[nivel][descripcion]) #crea la grilla según el nivel que se alcance (contador nivel que aumenta cuando se gana) y [1] es la posicion donde esta la descripcion

    movimientos = Pila()
    movimientos.apilar(juego)

    gamelib.resize(TAM_CEL * len(niveles[nivel][descripcion][nombre]), TAM_CEL * len(niveles[nivel][descripcion]))


    while gamelib.is_alive():

        if soko.juego_ganado(juego):
            nivel += 1
            juego = soko.crear_grilla(niveles[nivel][descripcion])
            movimientos = Pila() #reinicio la pila para el proximo nivel
            movimientos.apilar(juego)
            gamelib.resize(TAM_CEL * len(niveles[nivel][descripcion][0]), TAM_CEL * len(niveles[nivel][descripcion]))

        gamelib.draw_begin()
        gamelib.title(f"Sokoban: {niveles[nivel][nombre][0]}") #EN la posición 0 es en la que se guarda el numero de nivel y nombre (si lo tiene)
        soko_dibujar(juego)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break

        tecla = ev.key

        if tecla not in controles:
            continue

        if controles[tecla] == "SALIR":
            break

        if controles[tecla] == "REINICIAR":
            juego = soko.crear_grilla(niveles[nivel][descripcion])
            movimientos = Pila() #como se reinicia el juego, se reinicia la pila y se apila el primer movimiento
            movimientos.apilar(juego)
            continue

        if controles[tecla] == "DESHACER":
            if movimientos.solo_un_elemento():
                juego = movimientos.ver_ultima()
                continue

            movimientos.desapilar()    
            juego = movimientos.ver_ultima()
            continue

        if controles[tecla] == "PISTA":
            if not solucion_encontrada:
                solucion_encontrada, acciones = buscar_solucion(juego)
                i = len(acciones) - 1
                continue

            if solucion_encontrada:
                juego = soko.mover(juego, acciones[i])
                i -= 1
            continue

        solucion_encontrada = None #si cambio el estado final, debo encontrar otra secuencia de movimientos ganador
        anterior = juego
        juego = soko.mover(juego, controles[tecla])

        if anterior == juego: #Para no apilar estados identicos (cuando quiero moverme para el lado de una pared)
            continue

        movimientos.apilar(juego)

gamelib.init(main)


