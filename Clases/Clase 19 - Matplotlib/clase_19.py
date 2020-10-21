# -*- coding: utf-8 -*-
"""Clase 19.ipynb


**texto en negrita**# **Clase 19: matplotlib**

En esta clase empezaremos a desarrollar los métodos que nos permitirán visualizar un conjunto de datos. Para ello, comenzaremos con el estudio de la biblioteca **matplotlib**.

Como siempre, lo primero que debemos de hacer es importar la biblioteca. En este caso importaremos sólo una sub biblioteca de matplotlib llamada **pyplot**, la cual se especializa en generar gráficas.
"""

import matplotlib.pyplot as plt

"""Podemos crear una gráfica de puntos con la función *scatter()*, la cual acepta como argumentos dos LISTAS DEL MISMO TAMAÑO. Esta función básicamente tabula los datos dados."""

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.scatter(x,y)
plt.show()

# en repl.it
# plt.savefig("nombre.png")
# plt.clf() -> Instrucción para que se limpie la pantalla y no se encimen las gráficas, si quiero graficas encimadas, quito esta instrucción

"""Note que la función *scatter* no despliega la gráfica. Para hacerlo, se usa la función *show()*.

Si lo que queremos es una gráfica en donde los puntos aparezcan conectados mediante una línea, lo que necesitamos es la función *plot()*. Ésta se comporta exactamente igual que *scatter* salvo que conecta los puntos.
"""

plt.plot(x,y)
#plt.savefig("Figuara2.png")
plt.show()

"""Es necesaria la función *show()*, porque tal vez quisiéramos agregar más información a la gráfica. Por ejemplo, poner nombre a los ejes coordenados o poner un título.

A continuación se presentan los datos de la población mundial hasta 2015, y la predicción del Banco Mundial para el año 2050 (fuente: Wikipedia). Los datos están escritos en listas para poder crear una gráfica.
"""

años = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040, 
        2045, 2050]
pob = [2.525, 2.758,3.018, 3.322, 3.682, 4.061, 4.440, 4.853, 5.310, 5.735, 6.127, 6.520, 6.930, 7.349, 7.795, 8.184, 
       8.549, 8.888, 9.199, 9.482, 9.735]

plt.plot(años, pob)
plt.scatter(años, pob)
plt.xlabel("Años")
plt.ylabel("Población (miles de millones)")
plt.title("Población Mundial")
plt.show()

"""También podemos asignar valores específicos en los ejes (siempre y cuando tengan sentido) usando la función *xticks()* y *yticks()*, que aceptan como argumento una lista de valores con los cuales queremos que se dividan los ejes. Por ejemplo, en la gráfica anterior, quisiéramos que la población comenzara en 2 mil millones en lugar de 3 mil millones."""

plt.plot(años, pob)
plt.xlabel("Años")
plt.ylabel("Población (miles de millones)")
plt.yticks([2,4,6,8,10])
plt.show()

"""Incluso podemos etiquetar los valores de los ejes usando la misma función *yticks()*. Para hacerlo, pasamos como argumentos a la función dos listas del mismo tamaño. La primera debe contener los intervalos en los cuales queremos dividir el eje respectivo, y la segunda las etiquetas correspondientes de dichos intervalos."""

plt.plot(años, pob)
plt.xlabel("Años")
plt.ylabel("Población")
plt.title("Población Mundial")
plt.yticks([2,4,6,8,10], ['2mM', '4mM', '6mM', '8mM', '10mM'])
plt.show()

"""Volvamos por un momento al caso de la gráfica de puntos. La función *scatter()* acepta otros argumentos, entre los cuales podemos controlar el tamaño de los puntos, su color y su opacidad."""

x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]

plt.scatter(x1, y1, s = 1000, c = 'black', alpha = 0.5) # Alpha es la opacidad de los puntos, el rango es de 0 a 1
plt.plot(x1,y1)
plt.show()

"""Así, el argumento *s* indica el tamaño de los puntos, *c* indica el color y *alpha* lo opacidad de los puntos. Note que estos parámetros pueden aparecer en distintos órdenes (a excepción de los valores de los ejes X y Y), siempre y cuando pongamos su etiqueta. Note la ventaja de poner la instrucción 'show()' hasta el final. Además, los valores de la opacidad van de 0 a 1.

Otra característica que podemos modificar (aunque no es muy común) es el "marcador" de la gráfica, con la etiquieta 'marker' dentro de la fucnión 'scatter()'
"""

x1 = [1,2,3,4,5]
y1 = [10,20,30,40,50]

plt.scatter(x1, y1, s = 200, c = 'black', alpha = 0.8, marker = '+')
#plt.plot(x1,y1)
plt.show()

"""Algo muy útil es que la función 'scatter()' y la función 'plot()' aceptan también arreglos de numpy como argumentos."""

import numpy as np

x = range(10)  #[0,1,2,3,4,5,6,7,8,9]

np_x = np.array(x)
np_y = np_x * 5

plt.scatter(x, np_y,  c = 'red', s = 100)
plt.show()

"""Además, es posible especificar los parámetros del color y tamaño para CADA UNO de los puntos. Lo único que hay que hacer es poner listas para los valores de estos parámetros. Obviamente, todas estas listas deben ser DEL MISMO TAMAÑO y este tamaño debe de ser igual al de las listas de los ejes X y Y."""

x = range(10)
y = [16,1,32,64,128,4,2,256,8,512]
tamaño = [100,200,30,40,1200,60,70,800,90,100]
color = ['red', 'red', 'blue', 'blue', 'black', 'black', 'yellow', 'yellow', 'green', 'green']

plt.scatter(x, y, s = tamaño, c = color, alpha = 0.6)
plt.show()

"""También podemos agregar texto en coordenadas específicas de la gráfica mediante la instrucción *plt.text()* que acepta tres argumentos. Los dos primeros son las coordenadas del punto en donde queremos poner texto, y el tercero es el texto que queremos incluir."""

x = range(10)
y = [16,1,32,64,128,4,2,256,8,512]
tamaño = [100,200,30,40,1200,60,70,800,90,100]
color = ['red', 'red', 'blue', 'blue', 'black', 'black', 'yellow', 'yellow', 'green', 'green']

plt.scatter(x, y, s = tamaño, c = color, alpha = 0.6)
plt.text(4, 128, 'Punto 5')
plt.text(6.5, 256, 'Punto 7')
plt.show()

"""Por último, podemos añadir una cuadrícula de fondo en nuestras gráficas con la instrucción *grid()*."""

x = range(70)
np_x = np.array(x)  #[0 1 2 3 ..]
np_x = np_x * 0.1   # [0, 0.1, 0.2, 0.3, 0.4,...]              f(x) = 2^x

y = []  
for i in np_x:
    y.append(2**i)
plt.plot(np_x,y, c = 'black')
plt.grid(True)                  # pone una malla como background
plt.show()

"""En el siguiente ejemplo, queda claro el por qué es útil la función 'show()'"""

x = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
y = []

def cuadratica(z):          # f(x) = x^2
  return z**2

for i in x:
    y.append(cuadratica(i))
                
plt.plot(x,y)
np_x = np.array(x)
np_y = 3*np_x + 10          # g(x) = 3*x + 10  
np_exp = 2**np_x
plt.plot(np_x,np_y)
plt.grid(True)
plt.show()




np_y = -2*np_x**3 + 3*np_x**2 + 1

"""# **Actividad en clase 11**

Grafique las funciones *f(x) = x^2 - 4* y *g(x) = -x^2 + 4* de tal manera que se desplieguen como se ve en la figuara (ver repl.it)

"""

plt.scatter([2,3],[3,2])

