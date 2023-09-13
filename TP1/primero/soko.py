import copy

def crear_grilla(desc):
	"""Crea una grilla a partir de la descripción del estado inicial"""
	grilla = []
	
	for i in range(len(desc)):
		grilla.append(list(desc[i]))

	return grilla

def dimensiones(grilla):
	"""Devuelve una tupla con la cantidad de columnas y filas de la grilla."""
	filas = len(grilla)
	columnas = len(grilla[0])

	return columnas, filas 

def hay_pared(grilla,c,f):
	"""Devuelve True si hay una pared en la columna y fila (c, f)."""
	if grilla[f][c] == "#":
		return True
	return False

def hay_objetivo(grilla,c,f):
	"""Devuelve True si hay un objetivo en la columna y fila (c, f)."""
	if grilla[f][c] in (".","*","+"):
		return True
	return False

def hay_caja(grilla,c,f):
	"""Devuelve True si hay una caja en la columna y fila (c, f)."""
	if grilla[f][c] in ("$","*"):
		return True
	return False

def hay_jugador(grilla,c,f):
	"""Devuelve True si el jugador está en la columna y fila (c, f)."""
	if grilla[f][c] in ("@","+"):
		return True
	return False

def juego_ganado(grilla):
	"""Devuelve True si el juego está ganado."""
	c, f = dimensiones(grilla)
	for i in range(f):
		for j in range(c):
			if grilla[i][j] in (".","+"):
				return False
	return True

def mover(grilla, direccion):
	"""Mueve el jugador en la dirección indicada. La cual se ingresa como una tupla"""
	nueva_grilla = copy.deepcopy(grilla)
	f_j, c_j = posicion_jugador(grilla)
	x, y = direccion

	if hay_pared(grilla, c_j + x, f_j + y): #Verifico si hay una pared en la posicion que me voy a mover (posicion del jugador + movimiento (nunca x e y van a valer al mismo tiempo != 0))
		return grilla

	elif hay_caja(grilla, c_j + x, f_j + y) and hay_pared(grilla, c_j + 2*x, f_j + 2*y):
		return grilla

	elif hay_caja(grilla, c_j + x, f_j + y) and hay_caja(grilla, c_j + 2*x, f_j + 2*y):
		return grilla

	elif hay_caja(grilla, c_j + x, f_j + y) and hay_objetivo(grilla, c_j + 2*x, f_j + 2*y):
		nueva_grilla[f_j][c_j] = " "
		nueva_grilla[f_j + y][c_j + x] = "@"
		nueva_grilla[f_j + 2*y][c_j + 2*x] = "*"
		return nueva_grilla

	elif hay_caja(grilla, c_j + x, f_j + y):
		nueva_grilla[f_j][c_j] = " "
		nueva_grilla[f_j + y][c_j + x] = "@"
		nueva_grilla[f_j + 2*y][c_j + 2*x] = "$"
		return nueva_grilla

	nueva_grilla[f_j][c_j] = " "
	nueva_grilla[f_j + y][c_j + x] = "@"
	return nueva_grilla

def posicion_jugador(grilla):
	c, f = dimensiones(grilla)
	for i in range(f):         #Obtengo la posición del jugador, no puedo usar index xq da error en las filas que NO está
		for j in range(c):
			if hay_jugador(grilla,j,i): 
				return i , j


















