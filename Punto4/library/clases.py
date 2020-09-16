
class Cuenta:
	def __init__(self):
		self.titular=input("Ingrese el nombre del titular de la cuenta >>")
		self.cantidad=float(input(f"Ingrese la cantidad de >> "))

	def mostrar(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)
 