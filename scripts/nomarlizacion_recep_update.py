import os
import pandas as pd

# Directorio raíz donde se encuentran los archivos CSV
root_dir = "C:/workspace/blue-attached/respaldoS3"

# Lista para almacenar los DataFrames de cada archivo CSV
dfs = []

# Lista para almacenar las rutas de los archivos
file_paths = []

# Recorrer el directorio raíz y sus subdirectorios
for root, dirs, files in os.walk(root_dir):
    # Para cada archivo en los subdirectorios
    for file in files:
        # Comprobar si el archivo es un archivo CSV
        if file.endswith(".csv"):
            # Construir la ruta completa al archivo
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
            # Leer el archivo CSV y añadirlo a la lista de DataFrames
            df = pd.read_csv(file_path)
            # Añadir la ruta del archivo como una columna en el DataFrame
            df['file_path'] = file_path
            dfs.append(df)

# Concatenar todos los DataFrames en uno solo
df = pd.concat(dfs, ignore_index=True)

# Exportar el DataFrame resultante a un archivo CSV
consolidated_file_path = "C:/workspace/blue-attached/manual-load/consolidate/consolidated_data_recep_update.csv"
df.to_csv(consolidated_file_path, index=False)

print("\nEl archivo consolidado se ha guardado en:", consolidated_file_path)
