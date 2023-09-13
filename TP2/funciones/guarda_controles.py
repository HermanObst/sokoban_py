def levanta_controles():
	"""Dado el archivo con las especificaciones de los controles, devuelve un diccionario
	que contiene como clave la tecla del teclado y como valor el comando específico que recibe 
	soko.mover para actualizar el estado del juego"""
	teclas = {}
	with open("teclas.txt") as archivo:
		for linea in archivo:
			if linea == "\n":
				continue
			linea = linea.rstrip("\n").split(" = ")
			
			if linea [1] == "NORTE":
				linea[1] = (0,-1)
			elif linea [1] == "SUR":
				linea[1] = (0,1)
			elif linea[1] == "OESTE":
				linea[1] = (-1,0)
			elif linea[1] == "ESTE":
				linea[1] = (1,0)

			teclas[linea[0]] = linea[1]

	return teclas

print(levanta_controles())
