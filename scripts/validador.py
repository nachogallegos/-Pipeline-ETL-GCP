import pandas as pd

# Leer el archivo
df = pd.read_csv("data/ventas.csv")

# Mostrar las primeras filas
print(df.head())

# Validar el número de columnas
print(f"Columnas: {df.columns}")
print(f"Número de filas: {len(df)}")
