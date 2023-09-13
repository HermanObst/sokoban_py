import copy

PARED = "#"
CAJA = "$"
JUGADOR = "@"
OBJETIVO = "."
OBJETIVO_CAJA = "*"
OBJETIVO_JUGADOR = "+"
CELDA_VACIA = " "

def crear_grilla(desc):
	"""Crea una grilla a partir de la descripción del estado inicial"""
	grilla = []
	
	for f in range(len(desc)):
		grilla.append(list(desc[i]))

	return grilla

def dimensiones(grilla):
	"""Devuelve una tupla con la cantidad de columnas y filas de la grilla."""
	return len(grilla[0]), len(grilla)

def hay_pared(grilla,c,f):
	"""Devuelve True si hay una pared en la columna y fila (c, f)."""
	return grilla[f][c] == PARED

def hay_objetivo(grilla,c,f):
	"""Devuelve True si hay un objetivo en la columna y fila (c, f)."""
	return grilla[f][c] in (OBJETIVO, OBJETIVO_CAJA, OBJETIVO_JUGADOR)

def hay_caja(grilla,c,f):
	"""Devuelve True si hay una caja en la columna y fila (c, f)."""
	return grilla[f][c] in (CAJA, OBJETIVO_CAJA)

def hay_jugador(grilla,c,f):
	"""Devuelve True si el jugador está en la columna y fila (c, f)."""
	return grilla[f][c] in (JUGADOR, OBJETIVO_JUGADOR)
	
def juego_ganado(grilla):
	"""Devuelve True si el juego está ganado."""
	c, f = dimensiones(grilla)
	for i in range(f):
		for j in range(c):
			if grilla[i][j] in (OBJETIVO, OBJETIVO_JUGADOR):
				return False
	return True

def mover(grilla, direccion):
	"""Mueve el jugador en la dirección indicada. La cual se ingresa como una tupla"""
	x, y = direccion
	f_j, c_j = posicion_jugador(grilla)

	if not movimiento_permitido(grilla,direccion):
		return grilla

	elif hay_caja(grilla, c_j + x, f_j + y) or (hay_caja(grilla, c_j + x, f_j + y) and hay_objetivo(grilla, c_j + x, f_j + y)):
		return caja_adelante(grilla,direccion)

	return no_objetos_adelante(grilla,direccion)

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

def caja_adelante(grilla, direccion):
	"""Dada una grilla y una dirección que va hacia una caja, modifica la grilla"""
	nueva_grilla = copy.deepcopy(grilla)
	f_j, c_j = posicion_jugador(grilla)
	x, y = direccion

	if hay_objetivo(grilla, c_j + x, f_j + y):

	
	nueva_grilla[f_j][c_j] = CELDA_VACIA
	nueva_grilla[f_j + y][c_j + x] = JUGADOR


	if hay_objetivo(grilla, c_j + 2*x, f_j + 2*y):
		
		nueva_grilla[f_j + 2*y][c_j + 2*x] = OBJETIVO_CAJA
		return nueva_grilla

	nueva_grilla[f_j + 2*y][c_j + 2*x] = CAJA
	return nueva_grilla

def no_objetos_adelante(grilla, direccion):
	"""Dada una grilla y una dirección, si no hay objetos adelante, modifica la grilla segun el caso"""
	nueva_grilla = copy.deepcopy(grilla)
	f_j, c_j = posicion_jugador(grilla)
	x, y = direccion

	nueva_grilla[f_j][c_j] = CELDA_VACIA

	if hay_objetivo(grilla, c_j + x, f_j + y):
		nueva_grilla[f_j + y][c_j + x] = OBJETIVO_JUGADOR
		return nueva_grilla

	nueva_grilla[f_j + y][c_j + x] = JUGADOR
	return nueva_grilla

