import gamelib

IMAGENES = {"@": "player", "$": "box", ".": "goal", "#": "wall", " ": "ground"}

def soko_dibuja(grilla):
    """Dada la descripción (estado) de un nivel del SOKOBAN, lo dibuja usando la librería gamelib
    PRE: La lista de descripción debe esta constituida por listas que contengan cada fila de esta, caracter por caracter. 
    El formato debe ser el propuesto por la función soko.juego_crear"""

    for f in range(len(grilla)):
        for c in range(len(grilla[0])):
            gamelib.draw_image('img/ground.gif',(c + 1/2) * TAM_CELDA, (f + 1/2) * TAM_CELDA)

            for elemento in grilla[f][c]:
                gamelib.draw_image(f'img/{IMAGENES[elemento]}.gif',(c + 1/2) * TAM_CELDA, (f + 1/2) * TAM_CELDA)                


