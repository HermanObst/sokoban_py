import soko

MOVIMIENTOS = ((-1, 0), (1, 0), (0, 1), (0, -1))

def h (estado):
	"""Dada un estado del sokoban representado de forma mutable, 
	devuelve ese estado en forma inmutable"""
	estado_inmutable = tuple(tuple(x) for x in estado)

	return estado_inmutable

def buscar_solucion(estado_inicial):
	visitados = set()
	return backtrack(estado_inicial, visitados)

def backtrack(estado, visitados):
	visitados.add(h(estado))

	if soko.juego_ganado(estado):
		return True, ()

	for movimiento in MOVIMIENTOS:
		nuevo_estado = soko.mover(estado, movimiento)

		if h(nuevo_estado) in visitados:
			continue

		solucion_encontrada, acciones = backtrack(nuevo_estado, visitados)

		if solucion_encontrada:
			return True, acciones + ((movimiento), )

	return False, None

		


