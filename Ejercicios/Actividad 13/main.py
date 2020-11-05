# coding=utf-8

import pandas as pd
import numpy as np


def ReadCSV():
    tabla = pd.read_csv("Ciencia Ficción - Datos.csv")
    return tabla

def CrearDF(tabla):
    p1 = tabla['AI']
    p2 = tabla['2001']
    p3 = tabla['Matrix']
    p4 = tabla['Blade Runner']
    p5 = tabla['Exmachina']
    p6 = tabla['Yo, Robot']
    return p1, p2, p3, p4, p5, p6

def DesplegarDF(p1, p2, p3, p4, p5, p6):
    print("========== DataFrame 1 ==========")
    print(p1)
    print(" ")
    print("========== DataFrame 2 ==========")
    print(p2)
    print(" ")
    print("========== DataFrame 3 ==========")
    print(p3)
    print(" ")
    print("========== DataFrame 4 ==========")
    print(p4)
    print(" ")
    print("========== DataFrame 5 ==========")
    print(p5)
    print(" ")
    print("========== DataFrame 6 ==========")
    print(p6)
    print(" ")

def Promedios(p1, p2, p3, p4, p5, p6):
    print("========== Promedio DataFrame AI ===========")
    print(round(np.mean(p1), 2))
    print(" ")
    print("========== Promedio DataFrame 2001 =========")
    print(round(np.mean(p2), 2))
    print(" ")
    print("========== Promedio DataFrame Matrix =======")
    print(round(np.mean(p3), 2))
    print(" ")
    print("========== Promedio DataFrame Blade Runner =")
    print(round(np.mean(p4), 2))
    print(" ")
    print("========== Promedio DataFrame Exmachina ====")
    print(round(np.mean(p5), 2))
    print(" ")
    print("========== Promedio DataFrame Yo, Robot ====")
    print(round(np.mean(p6), 2))
    print(" ")


def Tabla3(tabla):
    print("========== Tabla 3 ==========")
    print(" ")
    tabla3 = tabla.drop(['Exmachina', 'Yo, Robot', 'AI', 'Matrix', 'Y'], axis = 1)
    tabla3 = tabla3.iloc[[0,1,2,3,4,5,6,7,8,9], [1,2]]
    print(tabla3)
    print(" ")


def Tabla4(tabla):
    print("================================ Tabla 4 ================================")
    print(" ")
    tabla = tabla.drop(['Yo, Robot', 'Y'], axis = 1)
    tabla4 = tabla.drop(4, axis = 0)
    print(tabla4)



def main():
    p1, p2, p3, p4, p5, p6 = CrearDF(ReadCSV())
    DesplegarDF(p1, p2, p3, p4, p5, p6)
    Promedios(p1, p2, p3, p4, p5, p6)
    Tabla3(ReadCSV())
    Tabla4(ReadCSV())



main()