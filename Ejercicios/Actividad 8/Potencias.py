
def Eje1():
    
    x = int(input("Introduce la potencia hasta la que se va a calcular: "))
    sum = 0
    for i in range(1,x+1,1):
        sum += 3**i
    
    print(sum)

def Eje2():
    x = int(input("Introduce la potencia hasta la que se va a calcular: "))
    sum = 0
    for i in range(1,x+1,1):
        sum += 10*i-5
    print(sum)

def Eje1R(x):
    if(x == 1):
        return 3
    else:
        return Eje1R(x-1) + 3**x


def Eje2R(x):
    if(x == 1):
        return 5
    else:
        return Eje2R(x-1)+(10*x-5)

def main():
    print("============================= Ejercicio 1 ==================================")
    Eje1()
    print("============================================================================")
    print("============================= Ejercicio 2 ==================================")
    Eje2()
    print("============================================================================")
    print("========================== Ejercicio 1 Recursivo ============================")
    y = int(input("Introduce el número: "))
    print(Eje1R(y))
    print("============================================================================")
    print("========================== Ejercicio 2 Recursivo ============================")
    x = int(input("Introduce el número: "))
    print(Eje2R(x))
    print("============================================================================")
    
    



main()