
class Cuenta:
	def __init__(self):
		self.titular=input("Ingrese el nombre del titular de la cuenta >>")
		self.cantidad=float(input(f"Ingrese la cantidad de dinero>> "))

	def mostrar(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)

class CajaAhorro(Cuenta):
	def __init__(self):
		super().__init__()

	def mostrar(self):
		print("Cuenta de caja de ahorros")
		super().mostrar()

class PlazoFijo(Cuenta):
	def __init__(self):
		super().__init__()
		self.plazo=int(input("Ingrese el plazo fijo en dias >>"))
		self.interes=float(input("Ingrese el interes en decimal >>"))
 
 
	def importe(self):
		importe=self.cantidad*self.interes/100
		print("El total de interés es: ",importe)

	def mostrar(self):
		print("Cuenta a plazo fijo: ")
		super().mostrar()
		print(f"Plazo en días: {self.plazo}")
		print(f"Interés: {self.interes}")
		self.importe()