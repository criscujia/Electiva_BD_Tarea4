from os import system

def añadirContactos(self):
		print("-----------------------------")
		print("Añadir nuevo contacto")
		nombre=input("Inserte el nombre >> ")
		telefono=int(input("Inserte el teléfono >> "))
		email=input("Inserte el email >>")
		self.contactos.append({'nombre':nombre,'telefono':telefono,'email':email})


def listaContactos(self):
		print("-----------------------------")
		print("Lista de contactos")
		if len(self.contactos) == 0:
			print("No hay contactos en la agenda")
		else:
			for i in range(len(self.contactos)):
				print(self.contactos[i]['nombre'])


def buscarContacto(self):
		print("-----------------------------")
		print("Buscador de contactos")
		nombre=input("Inserte el nombre del contacto a buscar >> ")
		b = 0
		for i in range(len(self.contactos)):
			if nombre == self.contactos[i]['nombre']:
				b = 2
				print("Datos del contacto >>")
				print("Nombre: ",self.contactos[i]['nombre'])
				print("Teléfono: ",self.contactos[i]['telefono'])
				print("E-mail: ",self.contactos[i]['email'])
				return i
		if b == 0:
			print(f'\n El nombre del contacto  {nombre}  no ha sido encontrado\n')

def editarContacto(self):
		print("-----------------------------")
		print("Editar contacto")
		data=buscarContacto(self)
		condition=False
		while condition==False:
			print("Inserta la opcion que quieres editar >> ")
			print("1. Nombre")
			print("2. Teléfono")
			print("3. E-mail")
			print("4. Volver")
			option=int(input("Inserte la opción deseada >> "))
			if option==1:
				nombre=input("Inserte el nuevo nombre: ")
				self.contactos[data]['nombre']=nombre
			elif option==2:
				telefono=input("Inserte el nuevo teléfono: ")
				self.contactos[data]['telefono']=telefono
			elif option==3:
				email=input("Inserte el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==4:
				condition=True
 