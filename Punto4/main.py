
from library.clases import*

def main():    
    caja1 = CajaAhorro()
    caja1.mostrar()
    print("-----------------------------------------------------------------")
    print("Cuenta con interes a plazo fijo >>")
    plazo1=PlazoFijo()
    plazo1.mostrar()

if __name__ == "__main__":
    main()
