
class Cuenta:
	def __init__(self):
		self.titular=input("Ingrese el nombre del titular de la cuenta >>")
		self.cantidad=float(input(f"Ingrese la cantidad de >> "))

	def mostrar(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)


class PlazoFijo(Cuenta):
	def __init__(self):
		super().__init__()
		self.plazo=int(input("Ingrese el plazo fijo en dias >>"))
		self.interes=float(input("Ingrese el interes en decimal >>"))
 
 
	def importe(self):
		importe=self.cantidad*self.interes/100
		print("El total de interés es: ",importe)