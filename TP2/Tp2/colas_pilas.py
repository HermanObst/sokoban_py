class Nodo:
	def __init__(self, dato = None, prox = None):
		self.dato = dato
		self.prox = prox

	def __str__(self):
		return str(self.dato)

class IteradorCola:
	def __init__(self, cola):
		self.cola = cola
		self.actual = cola.prim

	def __next__(self):
		if not self.actual:
			raise StopIteration

		dato = self.actual.dato
		self.actual = self.actual.prox
		return dato

class Cola:
	def __init__(self):
		self.prim = None
		self.ult = None

	def encolar(self, x):
		"""Encola el elemento x"""
		nuevo = Nodo(x)
		if not self.ult:
			self.prim = nuevo
			self.ult = nuevo

		else:
			self.ult.prox = nuevo
			self.ult = nuevo

	def desencolar(self):
		"""desencola el primer elemento y devuelve su valor.
		Si está vacía, devuelve ValueError"""
		if self.prim is None:
			raise ValueError("La cola está vacía")

		valor = self.prim.dato
		self.prim = self.prim.prox
		if not self.prim:
			self.ult = None
		return valor

	def esta_vacia(self):
		return self.prim is None

	def __iter__(self):
		return IteradorCola(self)


class Pila:
	def __init__(self):
		self.items = []

	def apilar(self, x):
		self.items.append(x)

	def desapilar(self):
		if self.esta_vacia():
			raise IndexError("La pila está vacía")
		return self.items.pop()

	def esta_vacia(self):
		return len(self.items) == 0

	def ver_ultima(self):
		return self.items[-1]

			