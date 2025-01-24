import pandas as pd
import os
from google.cloud import storage

# Configuración para simulaciones durante las pruebas
RUNNING_TESTS = os.getenv("RUNNING_TESTS") == "true"

# Leer el archivo FIFA
file_path = "data/FIFA-21 Complete.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"El archivo {file_path} no se encuentra.")

df = pd.read_csv(file_path, sep=";")

# Validar las columnas
print(f"Columnas: {df.columns}")
print(f"Número de filas: {len(df)}")

# Verificar si hay valores nulos
print("Valores nulos por columna:")
print(df.isnull().sum())

# Validar rango de valores en columnas importantes
if df["age"].min() < 15 or df["age"].max() > 50:
    print("Advertencia: Edad fuera del rango esperado.")

# Conjunto completo de posiciones válidas en FIFA 2021
valid_positions = {
    "GK", "RB", "RWB", "CB", "LB", "LWB",
    "CDM", "CM", "CAM", "RM", "LM",
    "RW", "LW", "CF", "ST"
}

# Verificar posiciones combinadas
def validate_positions(positions):
    """Valida posiciones individuales y combinadas."""
    for pos in positions.split("|"):
        if pos not in valid_positions:
            return False
    return True

# Validar si las posiciones son correctas
if "position" in df.columns and not df["position"].isnull().any():
    invalid_positions = df[~df["position"].apply(validate_positions)]
    if not invalid_positions.empty:
        print("Advertencia: Hay posiciones no válidas en los datos.")
        print("Posiciones no válidas:\n", invalid_positions["position"].unique())
    else:
        print("Todas las posiciones son válidas.")
else:
    print("Advertencia: La columna 'position' contiene valores nulos o no está presente.")

# Eliminar filas duplicadas basadas en todas las columnas
original_row_count = len(df)
df = df.drop_duplicates()
print(f"Filas eliminadas por duplicados: {original_row_count - len(df)}")

# Limpiar el campo 'team' (quitar comillas y espacios extras)
df["team"] = df["team"].str.strip().str.replace('"', '', regex=False)

# Validar los valores de 'overall' y 'potential'
overall_range = (0, 100)
potential_range = (0, 100)

if df["overall"].min() < overall_range[0] or df["overall"].max() > overall_range[1]:
    print("Advertencia: Valores de 'overall' fuera del rango esperado.")

if df["potential"].min() < potential_range[0] or df["potential"].max() > potential_range[1]:
    print("Advertencia: Valores de 'potential' fuera del rango esperado.")

# Guardar archivo limpio
cleaned_file_path = "data/FIFA-21 Complete Cleaned.csv"
df.to_csv(cleaned_file_path, index=False, sep=";")
print(f"Archivo limpio guardado en: {cleaned_file_path}")

# Manejo de conexión a Google Cloud Storage
if not RUNNING_TESTS:
    # Asegúrate de que las credenciales estén configuradas correctamente
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if credentials_path is None:
        raise RuntimeError("La variable GOOGLE_APPLICATION_CREDENTIALS no está configurada.")

    # Ejemplo de conexión a GCS
    client = storage.Client()
    print("Conexión a GCS exitosa.")
else:
    print("Simulando conexión a GCS durante las pruebas.")
