import os
import pandas as pd
import ast

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
            # Agregar una columna con la ruta del archivo
            df['file_path'] = file_path
            dfs.append(df)

# Concatenar todos los DataFrames en uno solo
df = pd.concat(dfs, ignore_index=True)

# Normalización
details_list = []
for index, row in df.iterrows():
    details = ast.literal_eval(row['receptiondetail_set'])
    for detail in details:
        detail['owner'] = row['owner']
        detail['reception_nbr'] = row['reception_nbr']
        detail['doctype'] = row['doctype']
        detail['created_date'] = row['created_date']
        detail['closed'] = row['closed']
        detail['status'] = row['status']
        detail['expected_date'] = row['expected_date']
        detail['provider_id'] = row['provider_id']
        detail['reception_type'] = row['reception_type']
        detail['file_path'] = row['file_path']  # Utilizar la ruta del archivo del DataFrame principal
        details_list.append(detail)

details_df = pd.DataFrame(details_list)

# Eliminar la columna receptiondetail_set del DataFrame principal
df.drop(columns=['receptiondetail_set'], inplace=True)

# Visualizar los DataFrames resultantes
print("DataFrame principal:")
print(df)
print("\nDataFrame de detalles:")
print(details_df)

# Exportar el DataFrame resultante a un archivo CSV
consolidated_file_path = "C:/workspace/blue-attached/manual-load/consolidate/consolidated_data_recep.csv"
details_df.to_csv(consolidated_file_path, index=False)

print("\nEl archivo consolidado se ha guardado en:", consolidated_file_path)
