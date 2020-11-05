# -*- coding: utf-8 -*-
"""

**Clase 21: Pandas**

Aunque los diccionarios son una estructura de datos muy útil, y es menester el conocer su uso, nosotros en realidad los usaremos como un paso intermedio para una estructura de datos más acorde a nuestro estudio de Ciencia de Datos.

Imaginemos que tenemos datos agrupados en una tabla. ¿Cómo podríamos almacenarlos usando python? Podemos hacerlo de varias maneras: una lista de listas, un arreglo dos dimensional, un diccionario, etc. El arreglo NO es una opción viable, dado que comunmente los valores de una tabla cambian de tipo de columna a columna (vea el ejemplo siguiente) y los arreglos sólo nos permiten almacenar datos del mismo tipo. Además, note que lo más común es que en una tabla se tengan nombres en las columnas, así que lo más lógico sería guardar dicha tabla como un diccionario, donde los nombres de las columnas serían las llaves del diccionario.
"""

nombres = ['Poe', 'Lovecraft', 'García Márquez', 'Zafón', 'King', 'Asimov','Quiroga', 'Clarke', 'Tolkien', 'Dick']
novelas = ['El Silencio', 'Dagón', 'Cien años de Soledad', 'La sombra del viento', 'Eso', 'Yo Robot','Cuentos de Locura',
           '2001 una odisea espacial', 'El Señor de los Anillos', 'Ubik']

año = [1849, 1937, 2014, "--",  "--", 1992, 1937, 2008, 1973, 1982]
generos = ['terror', 'terror', 'realismo mágico', 'realismo mágico', 'terror', 'ciencia ficción', 'terror', 
           'ciencia ficción', 'fantasía', 'ciencia ficción']

autores = {'nombre': nombres, 'libro': novelas, 'muerte' : año, 'género': generos}

          

#autores = {'nombre': nombres, 'libro': novelas, 'muerte' : año, 'género': generos}
print(autores)

"""Podemos usar toda la potencia del diccionario"""

print(autores['libro'])
print(autores['muerte'])
print(autores['nombre'][3])

"""Sin embargo, note que no se despliega como tabla y que además no es muy útil el indexado de esta manera. Quisiéramos poder hacer algo como en los arreglos 2D, en donde podíamos accesar con notación [m,n]. Para ésto, usaremos los *DataFrame* de **pandas**.

**Pandas** es otra biblioteca de python que permite (entre otras cosas) manejar bases de datos en formato de tablas. Veamos algunas de sus funciones básicas.
"""

import pandas as pd

"""Pandas nos permitirá trabajar con tablas de datos mediante el tipo de dato *DataFrame*. Existen dos maneras de construir un *DataFrame*. La primera es mediante un diccionario (de manera similar a como se crea un arreglo a partir de una lista) usando la función *DataFrame()* de pandas, que puede aceptar un diccionario como argumento."""

pd_autores = pd.DataFrame(autores)

print(pd_autores)

"""Note que, sin embargo, python en automático numera los renglones empezando en cero. Si nosotros quisiéramos ponerles una etiqueta a los renglones, es posible mediante el atributo *index* del diccionario, el cual acepta una **LISTA** con las etiquetas de los renglones que queremos para la tabla."""

pd_autores.index = ['EAP', 'HPL', 'GM', 'CRZ', 'SK', 'IA', 'HdQ', 'ACC', 'JRR', 'PKD']

print(pd_autores)

type(pd_autores)

pd_autores

"""¡Bellísimo! Note que si bien es cierto que en un diccionario los valores de las llaves pueden ser de cualquier tipo, para crear un DataFrame a partir de un diccionario **es necesario que los valores de las llaves sean listas del mismo tamaño** (de lo contrario python arrojará un error). Otra cosa importante, es que *index* es un **atributo** del diccionario, no una función (¿recuerda el atributo *shape* de un arreglo?)

El atributo *index* del DataFrame es importante. Note que no podríamos crearlo usando una lista en el diccionario, pues las listas deben de ser del mismo tamaño. Además como ya se imaginará, el atributo *index* tiene su propia funcionalidad.

Independientemente de lo bien que se ve un *DataFrame*, de nada serviría si no podemos acceder a sus datos de manera rápida. Para esto podemos usar indexado. Dado que este *DataFrame* proviene de un diccionario, supongo que ya no se sorprenderá de lo que viene
"""

pd_autores['libro']
#type(pd_autores['libro'])

"""Como ya lo notó, algo raro está pasando. Para seguir trabajando con un *DataFrame*, tenemos que hacer los siguiente"""

pd_autores[['libro']]

"""Note que ahora incluso se imprimió el nombre (etiqueta) de la columna. Además desapareció la descripción del último renglón. Así, si queremos hacer indexado en las columnas y obtener un *DataFrame*, necesitamos **dobles corchetes**. Podemos comprobar que el resultado obtenido sigue siendo un *DataFrame*"""

type(pd_autores[['libro']])

"""Inlcuso podemos seleccionar varias columnas a la vez, cosa que no podemos hacer con diccionarios"""

pd_autores[['libro', 'género']]

autores['libro', 'género']

"""Y además lo podemos hacer en el orden que queramos"""

pd_autores[['muerte', 'nombre']]

"""También podemos seleccionar renglones enteros, esta vez, usando el slicing y **sólo el slicing** común y corriente por posición"""

pd_autores[1:5]

"""Un comentario importante es que sólo se puede hacer slicing y NO indexado en los renglones"""

pd_autores[1]

pd_autores[1:2]

"""Note, sin embargo, que con esta sintaxis sólo es posible extraer columnas enteras o renglones enteros. Si quisiéramos usar un slicing parecido al de los arreglos 2D obtendríamos un error."""

pd_autores[[1:4], ['nombre', 'libro']]     #arreglo[1:6,7:11]





























