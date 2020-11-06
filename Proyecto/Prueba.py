import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def ReadCSV():
    data = pd.read_csv("/Users/pablo/Desktop/Escuela/Tercer Semestre/Matematicas y Ciencias de Datos/Ciencia de Datos - Tec/A01022382_BasedeDatos.xlsx")
    print(data)

def main():
    ReadCSV()

main()