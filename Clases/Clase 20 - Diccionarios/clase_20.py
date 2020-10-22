# -*- coding: utf-8 -*-
"""Clase 20.ipynb


Un histograma es una gráfica de distribución de valores en donde se mide cuántos valores de cierto tipo hay en un conjunto de datos. El histograma se puede invocar mediante la función 'hist()' de pyplot.
"""

import matplotlib.pyplot as plt

z = [2,2,3,5,7,6,5,7,2,4,10,9,7,1,1,3,8,10,8,5,2,3,4]
plt.hist(z)
plt.show()

"""Así, el primer argumento de la  función *hist* es una lista o arreglo. Es posible invocar a la función con un segundo argumento, que será la cantidad de barras que queremos que se desplieguen. Su etiqueta es *bins* y si no se da, el valor por default es 10. También podemos cambiar el color con la etiqueta *color*"""

plt.hist(z, bins = 4, color = 'black')
plt.show()  
#plt.savefig("Gráfica1.png")

"""Otra cosa que podemos cambiar, es la orientación del histograma, con la etiqueta *orientation*"""

plt.hist(z, color = 'green', orientation = 'horizontal' )
plt.show()

"""Cabe mencionar que las instrucciones de etiquetado de los ejes, el título y los ticks también se pueden usar aquí"""

plt.hist(z, color = 'yellow')
plt.xlabel("Eje X")
plt.ylabel("Cantidad")
plt.title("Histograma de prueba")
plt.xticks([2,3,7,8], ['x', 'y', 'z', 'w'])
plt.grid(True)
plt.show()

"""Note que aunque las divisiones realizadas por la función *xtics* fueron sólo 4, el histograma sigue teniendo la cantidad de barras especificadas (en este caso 10, pues no se incluyó el parámetro *bins* y por tanto, se usó 10)

**Ejercicio 1** La siguiente es una tabla con la frecuencia promedio de las letras en el español

A 12,53%
B	1,42%
C	4,68%
D	5,86%
E	13,68%
F	0,69%
G	1,01%
H	0,70%
I	6,25%
J	0,44%
K	0,02%
L	4,97%
M	3,15%
N	6,71%
Ñ	0,31%
O	8,68%
P	2,51%
Q	0,88%
R	6,87%
S	7,98%
T	4,63%
U	3,93%
V	0,90%
W	0,01%
X	0,22%
Y	0,90%
Z	0,52%

Cree una función **cuenta** que cuente la cantidad de veces que aparece cada letra del abecedario en un texto y que guarde los valores en una lista. Luego use esta lista y despliegue un histograma con estos datos y con las siguientes instrucciones:
1) Las barras en color verde.
2) Con tantas barras como letras del abecedario.
3) Con título "Frecuencia de letras en español".
4) El eje horizontal etiquetado "Letras del abecedario".
5) El eje vertical etiquetado "Cantidad"
6) Las divisiones (ticks) del eje horizontal que sean TODAS las letras del abecedario.

**Diccionarios**

Un *diccionario* en python es una nueva estructura de datos que permite almacenar parejas de datos *llave:valor* relacionados. La sintaxis de un diccionario es muy sencilla
"""

mundo = {'Canadá': 'América', 'España': 'Europa', 'Libia':'África', 'Australia': 'Oceanía'}
type(mundo)

"""En el ejemplo de arriba, las palabras Canadá, España, Libia y Australia son las *llaves* y los valores (palabras) América, Europa, África, y Oceanía, son los *valores* correspondientes a dichas llaves.

Pero, ¿cuál es la ventaja de un diccionario sobre una lista? Pudimos haber creado dos listas, una con los nombres de los países y otra con los nombres de los continentes. La parte clave aquí es que en un diccionario, las llaves y los valores están relacionados. Por ejemplo, suponga que quiere obtener el valor de la llave *España*. Con diccionarios **podemos usar indexado con las llaves**
"""

print(mundo['España'])
print(mundo['Australia'])

"""Tal como está, no funciona el indexado usual de listas"""

mundo[1]

"""Un método muy útil de los diccionarios es *keys*, el cual regresa todas las llaves del diccionario"""

print(mundo.keys())

"""Un par de detalles importantes en cuanto a diccionarios, es que NO SE PUEDEN REPETIR las llaves. Si se hace, las llaves repetidas (con sus respectivos valores) serán eliminados del diccionario. Además, NO ES POSIBLE PONER COMO LLAVES LISTAS NI ARREGLOS (en general, ningún objeto mutable)"""

capitales = {'Francia': 'París', 'Grecia': 'Atenas', 'Honduras': 'Tegucijalpa', 'Grecia': 'Esparta'}
print(capitales)

mal_dicc = {[1,2,3]: 6, [4,7,8]:9}

"""Para incluir datos a un diccionario, simplemente se especifica la llave entre corchetes y el valor"""

capitales['Japón'] = 'Kyoto'
print(capitales)

"""Para cambiar un valor de alguna llave, se usa la misma sintaxis"""

capitales['Japón'] = 'Tokyo'
print(capitales)

"""Note que dado que las llaves son únicas, python entiende que lo que queremos hacer es cambiar el valor de la llave Japón, no incluir un nuevo dato. Por otro lado, para borrar datos, se usa la función *del*"""

del(capitales['Grecia'])
print(capitales)

"""Otro detalle importante acerca de los diccionarios, es que las llaves pueden ser de distintos tipos, así como los valores"""

dicc = {True:1, "Falso":0, 10: "hola"}
print(dicc.keys())

"""Además podemos saber si en cierto diccionario se encuentra una llave, usamos la función *in*"""

print('México' in capitales)

print('México' in capitales)
print('Japón' in capitales)

"""Por último, los datos en los valores SÍ pueden ser de cualquier tipo (a diferencia de las llaves). En particular pueden ser listas o diccionarios."""

paises = {'Italia': {'capital':'Roma', 'continenete':'Europa'}, 'Egipto': {'capital': 'El Cairo', 'continente': 'África'},
         'México': {'capital': 'Distrito Federal', 'continente': 'América'}}


#print(paises.keys())
print(paises['Egipto'])

paises['México']['continente']

paises['México']['capital'] = 'Ciudad de México'
print(paises)

print(paises['México'].keys())

paises.keys()

'continente' in paises['México']

lista = [{'a':1}, {'b':[1,2,3,4,5,6], 'c':False}]
print(lista[1])
print(lista[1].keys())
print(lista[1]['b'][0])



