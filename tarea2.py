import pandas as pd
import numpy as np

# ================================================================
# DESAFÍO A: IMPORTACIÓN Y CARGA (PANDAS)
# ================================================================

# Se intenta cargar el archivo con utf-8; si falla, se usa latin1
# (necesario por caracteres especiales en nombres de artistas)
try:
    df_musica = pd.read_csv("spotify_datos.csv", encoding="utf-8")
except UnicodeDecodeError:
    df_musica = pd.read_csv("spotify_datos.csv", encoding="latin1")

print("Archivo cargado correctamente")
print(df_musica.head())

# ================================================================
# DESAFÍO B: EL MOTOR NUMÉRICO (NUMPY)
# ================================================================

# La columna 'streams' puede contener valores no numéricos o comas,
# por lo que se limpia antes de convertir
df_musica["streams"] = (
    df_musica["streams"]
    .astype(str)
    .str.replace(",", "")
    .str.strip()
)

# to_numeric convierte a número; errors='coerce' convierte
# cualquier valor inválido en NaN en vez de lanzar error
df_musica["streams"] = pd.to_numeric(df_musica["streams"], errors="coerce")

# Se elimnan los NaN y se convierte a array de NumPy
streams_array = df_musica["streams"].dropna().to_numpy()

# Cálculo del promedio y máximo usando NumPy (sin usar bucles for)
promedio = np.mean(streams_array)
maximo = np.max(streams_array)

print(f"\nEl promedio de reproducciones es: {promedio:,.0f}")
print(f"La cantidad máxima de reproducciones es: {maximo:,.0f}")

# ================================================================
# DESAFÍO C: MODULARIZACIÓN Y CONTROL DE FLUJO (FUNCIONES)
# ================================================================

# Función que clasifica una canción según su número de reproducciones.
# Los umbrales son en millones: >1.000M, entre 500M y 1.000M, o <500M
def clasificar_exito(reproducciones):
    if reproducciones >= 1_000_000_000:   # más de 1.000 millones
        return "Hit Mundial"
    elif reproducciones >= 500_000_000:   # entre 500M y 1.000M
        return "Éxito"
    else:                                 # menos de 500 millones
        return "Estándar"

# ================================================================
# DESAFÍO D: APLICACIÓN AL DATASET
# ================================================================

# Se aplica la función a cada valor de la columna 'streams'
# usando .apply(), que evita usar un bucle for explícito
df_musica["Categoria_Exito"] = df_musica["streams"].apply(clasificar_exito)

# Vista previa del resultado
print("\nVista previa con categorías:")
print(df_musica[["track_name", "artist(s)_name", "streams", "Categoria_Exito"]].head(10))

# Conteo por categoría
print("\nDistribución de categorías:")
print(df_musica["Categoria_Exito"].value_counts())

# Exportación del DataFrame final a CSV
df_musica.to_csv("resultados_tarea2.csv", index=False)
print("\nArchivo 'resultados_tarea2.csv' exportado correctamente.")
