# coding = utf-8
import numpy as np

def fun1(x):
    return x*x

def fun2(x):
    return x**3

def fun3(x):
    return np.sin(x)

def fun4(x):
    return np.exp(x**2)

def integral(a, b, n, f):
    ancho = (b-a)/n
    puntos = [i for i in range(n)]
    valores = [i for i in range(n)]
    for i in puntos:
        x = puntos[i]/n
        puntos[i] = (x)
    
    suma = 0
    for i in valores:
        val = f(puntos[i])*ancho
        valores[i] = val
        suma += val
    
    return suma
    
    

print(integral(0, 1, 1000000, fun4))