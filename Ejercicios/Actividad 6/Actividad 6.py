def PedirNombre():
    nombre = input("Hola, introduce tu nombre: ")
    print("Hola " + nombre)

def PedirNumero():
    num = int(input("Introduce un número: "))
    if(num % 2 == 0):
        print("True")
    else:
        print("False")

def main():
    PedirNombre() 
    PedirNumero()


main()