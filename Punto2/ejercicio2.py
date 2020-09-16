from library.ejercicio import*


class Agenda:
	
	def __init__(self):
	
		self.contactos=[]
 
	def menu(self):
		while True:        

			print (">>Selecciona una opción")
			print ("\t1 - Añadir contacto")
			print ("\t2 - Lista de contactos")
			print ("\t3 - Buscar contacto")
			print ("\t4 - Editar contacto")
			print ("\t5 - Cerrar agenda")

	
			opcionMenu=int(input("Inserta una opciòn >> "))
			if opcionMenu==1:
				añadirContactos(self)
			elif opcionMenu==2:
				listaContactos(self)
			elif opcionMenu==3:
				buscarContacto(self)
			elif opcionMenu==4:
				editarContacto(self)
			elif opcionMenu==5:
				print("Cerrando agenda..")
				break
			else:
				print ("")
				input("La opcion ingresada no es valida... \npulse una tecla para continuar")
			self.menu()
 
 
agenda=Agenda()
agenda.menu()