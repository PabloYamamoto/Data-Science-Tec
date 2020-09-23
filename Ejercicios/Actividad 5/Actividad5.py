

def Ejercicio1():
    print("================================== Ejercicio 1 ===================================")
    print("Indica si la suma de dos números es impar")
    print("")
    num1 = int(input("Escriba el primer número: "))
    num2 = int(input("Escriba el segundo número: "))
    suma = num1+num2
    if(suma % 2 != 0):
        return True
    else: 
        return False 

def Ejercicio2():
    print("================================== Ejercicio 2 ===================================")
    print("Indica si el es número es divisble entre 3")
    print("")
    num = int(input("Ingresa el número a evaluar: "))
    if(num % 3 == 0):
        return True
    else:
        return False


def Ejercicio3():
    print("================================== Ejercicio 3 ===================================")
    print("Indica si el un número es divisble entre 7")
    print("")
    num = int(input("Ingresa el número a evaluar: "))
    if(num % 7 == 0):
        return True
    else:
        return False


def main():
    print(" ")
    Eje1 = Ejercicio1()
    print("La suma de los números es impar: " + str(Eje1))
    print("")
    print("==================================================================================")
    print(" ")
    Eje2 = Ejercicio2()
    print("El número es divisible entre 3: " + str(Eje2))
    print("")
    print("==================================================================================")
    print(" ")
    Eje3 = Ejercicio3()
    print("El número es divisible entre 7: " + str(Eje3))
    print("")
    print("==================================================================================")
    print(" ")



main()