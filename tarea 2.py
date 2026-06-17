#Desafío A: Importación y Carga (Pandas)---------------------------------------------

import pandas as pd
import numpy as np 

df_musica = pd.read_csv("spotify_datos.csv", encoding="latin-1")

#Desafío B: El Motor Numérico (NumPy)-------------------------------------------------

#transforme el texto en numeros asegurando que no haya errores de nulos y use coerce
#en caso de que falle con un caracter invalido este lo reemplaxa por un dato vacio
#haciendo que la columna stream sea solo numerica 
df_musica["streams"] = pd.to_numeric(df_musica ["streams"], errors= "coerce")

#transforme los valores en columnas por medio de un array de numpy, por lo cual sera más rapido 
streams_array = df_musica["streams"].dropna().to_numpy()
print(streams_array)

#use las funciones de numpy en lugar de los bucles for, evitando bucles 
promedio = np.mean(streams_array)
print(f"el promedio total de reproducciones es de: {promedio}")

maximo= np.max(streams_array)
print(f"el maximo de reproducciones en genral es de: {maximo:}")

#uso idxmax() para encontrar la fila donde está el valor máximo de streams, y con .loc[] extraigo el nombre ("track_name") de esa misma fila.
cancion_numero1 =df_musica.loc[df_musica["streams"].idxmax(), "track_name"]
print(f"la maxima cantidad de reprodicciones para la cancion numero 1 es: {maximo} y es {cancion_numero1} el nombre de esta")


#Desafío C: Modularización y Control de Flujo (Funciones)-----------------------------------------------




#GLOSARIO de cosas que aprensí y use en la tarea
# import pandas as pd / import numpy as np: Llama a las librerías de trabajo y les asigna un alias (pd y np) para agilizar la escritura en el código.
# pd.read_csv(): Función de Pandas que lee un archivo de texto separado por comas y lo transforma en una estructura de tabla (DataFrame).
# pd.to_numeric(): Fuerza la conversión de los datos de una columna al formato matemático (int o float).
# errors="coerce": Parámetro de seguridad. Si el sistema encuentra un carácter inválido (como una letra en una columna de números), no detiene el programa, sino que lo reemplaza por un dato vacío (NaN).
# .dropna(): Elimina de la ejecución cualquier celda que contenga datos nulos (NaN) para evitar errores en las operaciones matemáticas.
# .to_numpy(): Convierte una columna de Pandas a un array (matriz/vector) nativo de NumPy, el cual procesa cálculos estadísticos de manera mucho más veloz.
# np.mean(): Fórmula de NumPy que calcula el promedio (la media aritmética) de un array.
# np.max(): Fórmula de NumPy que extrae el valor numérico más alto dentro del array.
# def clasificar_exito(): Declara el inicio de una función personalizada. Es un bloque de código reutilizable.
# .apply(): Método de Pandas que toma una función específica y la ejecuta automáticamente a través de cada uno de los registros de una columna.
# .to_csv(): Empaqueta el DataFrame final y lo guarda físicamente en el ordenador. El parámetro index=False evita que se genere una columna extra en el archivo con el conteo numérico de las filas.
# .idxmax(): Método de Pandas que busca y devuelve el índice (la posición de la fila) donde se encuentra el valor más alto de una columna.