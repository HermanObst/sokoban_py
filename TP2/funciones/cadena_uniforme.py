def cadenas_uniformes(lista_cadenas):
	cadenas_uniformes = []
	maxim = max(len(x) for x in lista_cadenas)
	print(maxim)
	for cadena in lista_cadenas:
		while len(cadena) < maxim:
			cadena += " "
		cadenas_uniformes.append(cadena)

	return cadenas_uniformes

print(cadenas_uniformes(['####', '# .#', '#  ###', '#*@  #', '#  $ #', '#  ###', '####']))