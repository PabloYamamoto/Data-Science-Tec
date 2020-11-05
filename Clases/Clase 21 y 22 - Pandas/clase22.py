# -*- coding: utf-8 -*-
"""Clase22a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11X0lhr7WOkTbBFLZZm_RKTAXTssZHohI

**Clase 22: Pandas 2**

En esta clase seguiremos estudiando los *DataFrames* de **pandas**. En particular, veremos una nueva forma de crear un *DataFrame*, esta vez, a partir de una tabla en lugar de un diccionario. Además, aprenderemos una forma más versátil de acceder a los datos.

Existen otras dos maneras de acceder a los datos de un *DataFrame* usando funciones específicas de **pandas**.

La primera forma es usar las etiquetas de las filas y las columnas. ¿Recuerda que en un *DataFrame* tanto las columnas como las filas tienen etiquetas? Bueno, las usaremos junto con la función *loc()* que usa "label base indexing".
"""

import pandas as pd

nombres = ['Poe', 'Lovecraft', 'García Márquez', 'Zafón', 'King', 'Asimov','Quiroga', 'Clarke', 'Tolkien', 'Dick']
novelas = ['El Silencio', 'Dagón', 'Cien años de Soledad', 'La sombra del viento', 'Eso', 'Yo Robot','Cuentos de Locura',
           '2001 una odisea espacial', 'El Señor de los Anillos', 'Ubik']
año = [1849, 1937, 2014, "--",  "--", 1992, 1937, 2008, 1973, 1982]
generos = ['terror', 'terror', 'realismo mágico', 'realismo mágico', 'terror', 'ciencia ficción', 'terror', 
           'ciencia ficción', 'fantasía', 'ciencia ficción']

autores = {'nombre': nombres, 'libro': novelas, 'muerte' : año, 'género': generos}

pd_autores = pd.DataFrame(autores)

pd_autores

pd_autores.loc[[1,2,3,4,5]]
#pd_autores.loc[[1]]

"""Recuerde que es posible poder etiquetas en los renglone con el atributo *index*. Ésto será muy importante esta clase"""

pd_autores.index = ['EAP', 'HPL', 'GM', 'CRZ', 'SK', 'IA', 'HdQ', 'ACC', 'JRR', 'PKD']
pd_autores

pd_autores[['nombre']]

"""La función *loc* nos permitirá acceder tanto a las columnas como a los renglones con sus etiquetas (note los dobles corchetes)"""

pd_autores.loc[['CRZ']]

"""Recuerde que con los renglones, antes esto NO era posible, más que con slicing"""

pd_autores[['CRZ']]

pd_autores[3:4]

"""La ventaja es que con *loc()* podemos desplegar varios renglones"""

pd_autores.loc[['CRZ', 'SK', 'HPL']]

"""Note que incluso lo hemos hecho en el orden que queríamos.

¿Cuál es la diferencia con los corchetes normales?
"""

pd_autores[3:6]

"""En primera, con *loc()* podemos hacerlo en el orden que queramos, mientras que con simple corchete y slicing no. Otra ventaja es que con slicing y corchetes sólo se puede acceder a renglones enteros y columnas enteras, mientras que con *loc()* lo podemos hacer como si fueran matrices

Por ejemplo, imagine que queremos extraer la información de los renglones correspondientes a Poe, Tolkien y Dick, pero sólo las columnas correspondientes a *libro* y *género*. Lo hacemos de la siguiente manera
"""

z = pd_autores.loc[['EAP', 'JRR', 'PKD'], ['libro', 'género']]    #arreglo[2:6, 7:11]
z

"""¡Increíble! Note que se despliegan los datos en el orden en el que los pidamos, no en el orden en el cual estaban originalmente en el *DataFrame*. Lo que sí es importante es que si incluimos filas y renglones en listas separadas por coma, la primer lista debe de ser la de las etiquetas de los renglones."""

pd_autores.loc[['ACC', 'PKD', 'IA', 'HPL'], ['libro', 'nombre']]

"""Sería una pena que no pudiéramos seleccionar columnas completas con *loc()*. Por ejemplo, imagine que queremos extraer las columnas enteras de *nombre* y *libro*"""

pd_autores.loc[[:], ['nombre', 'libro']]

"""¡Uy! ¡No puede ser! Desafortunadamente, la sintaxis es algo incómoda"""

pd_autores.loc[:, ['nombre', 'libro']]

"""Bueno, hemos visto entonces la importancia de las etiquetas en un *DataFrame*, nos permiten hacer selección *por etiquetas*.

¿Qué pasa si queremos hacer indexado con números en un *DataFrame*? Ya sabemos que lo podemos hacer en las filas, ¿qué hay de las columnas? Necesitamos la función *iloc()* ("integer based label")

Al usar *iloc()*, las filas y las columnas están etiquetadas con índices enteros en orden. Por ejemplo, si quisiéramos desplegar las filas con índice 5 y 3
"""

pd_autores.iloc[[5,3]]

"""Note que lo anterior no era posible antes. Además, también podemos seleccionar sólo algunas columnas"""

pd_autores.iloc[[5,3], [3,0]]

"""Note cómo estamos haciendo exactamente los mismo que con *loc()*, pero ahora las etiquetas son los números de las filas y las columnas (empezando en cero). Además, lo podemos hacer en el orden que queramos. Sin embargo, recuerde que una regla es básica: al igual que con los arreglos, la primera lista debe corresponder a las filas, y la segunda a las columnas.

¿Qué pasa si queremos columnas enteras? La idea es la misma que con *loc()*. Por ejemplo, suponga que queremos extraer toda la columna de libros. La siguiente instrucción funciona
"""

pd_autores.iloc[:,[1]]

"""Crear un *DataFrame* de un diccionario es sencillo, simplemente mediante la función *DataFrame()* de **pandas**. Sin embargo, la manera más natural de crear una tabla en python, es obviamente, mediante otra tabla. La manera más rápida de hacerlo, por ejemplo, a partir de un archivo de excel, es primero guardar el archivo en formato **csv utf 98**. Esto crea un archivo con *valores separados por comas (csv)*. Dichos archivos se pueden leer en python mediante la instrucción de pandas *read_csv('path')*

Lo más conveniente es mover el archivo al directorio donde estemos trabajando. Si no lo sabemos, python nos lo dice
"""

pwd

"""Ahora, simplemente, leemos el archivo con la instrucción **read_csv()**"""

tabla = pd.read_csv("nombre_del_archivo")

tabla

"""¡Perfecto! Ahora lo que queremos es cambiar las etiquetas de los renglones. En este caso, yo quisiera que una columna específica de la tabla sea la columna de etiquetas, a diferencia de crear la propia usando el atributo *index*. Esto se puede hacer pasando un parámetro extra a la función **read_csv()**"""

tabla = pd.read_csv("nombre_del_archivo", index_col = 0)

tabla

"""Obviamente podemos incluir nuevas columnas, pero tendríamos que introducir los datos o mano o exportarlos primero. Desde luego, lo más común es introducir los datos en Excel y ya que la tabla esté completa, la importamos. Sin embargo, lo que sí es necesario muchas veces, es eliminar filas o columnas. Ésto se hace con un sólo método **drop()**. Dentro de 'drop()', le debe indicar a Python la etiqueta del renglón o columna que quiere eliminar, además le debe indicar si quiere borrar un renglón ó una columna mediante el argumento 'axis', el cual es **0** para rengón y **1** para columna"""



