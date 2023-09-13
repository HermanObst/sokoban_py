def cargar_archivo():
	"""Dado un archivo con los niveles del SOKOBAN con la forma de:
	Nivel
	Nombre (opcional)
	descripción
	Devuelve una lista de listas. Estas representan a cada nivel. Dentro de estas hay dos listas:
	Una que guarda el nivel y nombre (opcional) y otra que guarda la descripción"""
	total = []
	nivel = []
	nombre = []
	descrip = []
	with open("nivel.txt") as niveles:
		for linea in niveles:
			if linea == "\n": #Cuando encuentra un salto de linea (paso de nuvel) guarda el nivel (dentro tiene nombre y descrip) en total
				descrip = cadenas_uniformes(descrip)
				nivel.append(nombre)
				nivel.append(descrip)
				total.append(nivel)
				nombre, descrip, nivel = [], [], []

			elif "#" not in linea: #las cadenas que no son salto ni tienen # son el nivel y el nombre. se guardan en nombre
				nombre.append(linea.rstrip("\n"))

			elif "#" in linea: #las descripciones tienen, necesariamente, el caracter pared --> se guardan en descrip
				descrip.append(linea.rstrip("\n"))

		nivel.append(nombre)
		nivel.append(descrip)
		total.append(nivel)

	return total

def cadenas_uniformes(lista_cadenas):
	cadenas_uniformes = []
	maxim = max(len(x) for x in lista_cadenas)
	print(maxim)
	for cadena in lista_cadenas:
		while len(cadena) < maxim:
			cadena += " "
		cadenas_uniformes.append(cadena)

	return cadenas_uniformes

