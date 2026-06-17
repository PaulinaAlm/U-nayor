import pandas as pd
import numpy as np

df_musica = pd.read_csv("spotify_datos.csv", encoding="latin-1")

#transforme el texto en numeros
#errors coerce = vacio en lugar de error
df_musica["streams"] = pd.to_numeric(df_musica ["streams"], errors= "coerce")

#.dropna = eliminar las filas vacias
streams_array = df_musica["streams"].dropna().to_numpy()
print(streams_array)

promedio = np.mean(streams_array)
print(f"promedio: {promedio}")

max= np.max(streams_array)
print(f"el maximo es: {max:}")

# Funcion para clasificar el exito de una cancion segun sus streams
# Utiliza condiciones con rangos que no se superponen
def clasificar_exito(streams):
    if streams >= 1_000_000_000:
        return "Megaexito"
    elif streams >= 500_000_000:
        return "Exito"
    elif streams >= 100_000_000:
        return "Popular"
    else:
        return "Poco conocida"

# Crear nueva columna aplicando la funcion clasificar_exito a cada valor de streams
# Se usa .apply() para aplicar la funcion fila por fila sin bucles manuales
df_musica["clasificacion"] = df_musica["streams"].apply(clasificar_exito)

# Exportar el DataFrame con la nueva columna a un archivo CSV
df_musica.to_csv("spotify_datos_clasificados.csv", index=False, encoding="latin-1")
print("Archivo exportado: spotify_datos_clasificados.csv")
