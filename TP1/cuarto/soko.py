import copy

PARED = "#"
CAJA = "$"
JUGADOR = "@"
OBJETIVO = "."
CELDA_VACIA = " "

def crear_grilla(desc):
	"""Crea una grilla a partir de la descripción del estado inicial. CLAVE PARA EL MOVIMIENTO: 
	SIEMPRE los caracteres "inamovibles" van a la IZQUERDA (o en la pos[0])"""
	grilla = []
	
	for f in range(len(desc)):
		lista = list(desc[f])
		for i, e in enumerate(desc[f]):

			if e == "*":
				lista[i] = OBJETIVO + CAJA
			
			elif e == "+":
				lista[i] = OBJETIVO + JUGADOR

			elif e == "@":
				lista[i] = CELDA_VACIA + JUGADOR

			elif e == "$":
				lista[i] = CELDA_VACIA + CAJA

		grilla.append(lista)

	return grilla

def dimensiones(grilla):
	"""Devuelve una tupla con la cantidad de columnas y filas de la grilla."""
	return len(grilla[0]), len(grilla)

def hay_pared(grilla,c,f):
	"""Devuelve True si hay una pared en la columna y fila (c, f)."""
	return grilla[f][c] == PARED

def hay_objetivo(grilla,c,f):
	"""Devuelve True si hay un objetivo en la columna y fila (c, f)."""
	return grilla[f][c] in (OBJETIVO, OBJETIVO + CAJA, OBJETIVO + JUGADOR)

def hay_caja(grilla,c,f):
	"""Devuelve True si hay una caja en la columna y fila (c, f)."""
	return grilla[f][c] in (CELDA_VACIA + CAJA, OBJETIVO + CAJA)

def hay_jugador(grilla,c,f):
	"""Devuelve True si el jugador está en la columna y fila (c, f)."""
	return grilla[f][c] in (CELDA_VACIA + JUGADOR, OBJETIVO + JUGADOR)
	
def juego_ganado(grilla):
	"""Devuelve True si el juego está ganado."""
	c, f = dimensiones(grilla)
	for i in range(f):
		for j in range(c):
			if grilla[i][j] in (OBJETIVO, OBJETIVO + JUGADOR):
				return False
	return True

def mover(grilla, direccion):
	"""Mueve el jugador en la dirección indicada. La cual se ingresa como una tupla"""
	x, y = direccion
	f_j, c_j = posicion_jugador(grilla)
	nueva_grilla = copy.deepcopy(grilla)

	if not movimiento_permitido(grilla,direccion):
		return grilla

	else: #Movimiento permitido

		nueva_grilla[f_j][c_j] = nueva_grilla[f_j][c_j][0]  #"Borra" el signo de jugador y deja el inamovible (objetivo o vacio)
		nueva_grilla[f_j + y][c_j + x] = nueva_grilla[f_j + y][c_j + x][0] + JUGADOR #"Borra" el signo de caja dejando el inamovible y suma jugador
		
		if hay_caja(grilla, c_j + x, f_j + y):
			nueva_grilla[f_j + 2*y][c_j + 2*x] = nueva_grilla[f_j + 2*y][c_j + 2*x] + CAJA
			return nueva_grilla

		return nueva_grilla

def posicion_jugador(grilla):
	c, f = dimensiones(grilla)
	for i in range(f):         #Obtengo la posición del jugador, no puedo usar index xq da error en las filas que NO está
		for j in range(c):
			if hay_jugador(grilla,j,i): 
				return i , j

def movimiento_permitido(grilla,direccion):
	"""Dada una grilla y una dirección, devuelve True si el movimiento NO esta permitido"""
	x, y = direccion
	f_j, c_j = posicion_jugador(grilla)

	return not ((hay_pared(grilla, c_j + x, f_j + y)) or hay_caja(grilla, c_j + x, f_j + y) and not puedo_mover_caja(grilla,direccion))

def puedo_mover_caja(grilla,direccion):
	"""Dada una grilla y una dirección en la que TENGO UNA CAJA, devuelve si puedo moverla"""
	x, y = direccion
	f_j, c_j = posicion_jugador(grilla)

	return not (hay_pared(grilla, c_j + 2*x, f_j + 2*y) or hay_caja(grilla, c_j + x*2, f_j + y*2))


