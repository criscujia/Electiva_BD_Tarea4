class Alumno:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del alumno >>")
        self.nota=float(input(f"Ingrese la nota del {self.nombre} >>"))

    def mostrar(self):
        print(f"El nombre del alumno es:  {self.nombre} ")
        print(f"La nota del alumno es:  {self.nota} ")
    
    def mensaje(self):
        if self.nota>=3:
            print(f"El alumno {self.nombre} aprobo con una nota de {self.nota}")
        else:
            print(f"El alumno {self.nombre} reprobo con una nota de {self.nota}")