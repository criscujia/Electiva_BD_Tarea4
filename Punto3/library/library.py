
class Banco:
	def __init__(self):
		nombre = input("Digite su nombre =>")
		self.cliente=Cliente(nombre)

	def operacion(self):
		cantidade = int (input("Digite la cantidad a depositar => "))
		self.cliente.depositar(cantidade)
		cantidare = int (input("Digite la cantidad a retirar => "))
		self.cliente.extraer(cantidare)


	def depositos(self):
		total=self.cliente.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente.imprimir()


class Cliente:

	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0

	def depositar(self,cantidad):
		self.cantidad+=cantidad

	def extraer(self,cantidad):
		self.cantidad-=cantidad

	def devolver_cantidad(self):
		return self.cantidad

	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)