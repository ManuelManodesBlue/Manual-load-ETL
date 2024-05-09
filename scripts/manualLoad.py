import sqlite3
from sqlalchemy import create_engine
import glob
import os
import pandas as pd
import ast

# Directorio base donde se encuentran los archivos CSV y sus subdirectorios
base_dir = 'C:/workspace/blue-attached/respaldoS3/'
output_file = 'C:/workspace/blue-attached/manual-load/consolidate/archivo_normalizado.csv'

# Buscar todos los archivos CSV de forma recursiva
csv_files = glob.glob(os.path.join(base_dir, '**', '*.csv'), recursive=True)

# Lista para almacenar DataFrames
dataframes = []

# Procesar cada archivo CSV encontrado
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    
    # Comprobar si la columna 'receptiondetail_set' existe antes de procesarla
    if 'receptiondetail_set' in df.columns:
        df['receptiondetail_set'] = df['receptiondetail_set'].apply(ast.literal_eval)
        
        # Expandir la columna receptiondetail_set en varias columnas
        detail_df = pd.json_normalize(df['receptiondetail_set'].explode()).reset_index(drop=True)
        
        # Concatenar las nuevas columnas al DataFrame original
        df = pd.concat([df, detail_df], axis=1)
        
        # Eliminar la columna original receptiondetail_set
        df.drop(columns=['receptiondetail_set'], inplace=True)
    
    # Rellenar los espacios vacíos con los valores de las filas superiores que contienen texto
    df.fillna(method='ffill', inplace=True)
    
    # Agregar el DataFrame a la lista
    dataframes.append(df)

# Concatenar todos los DataFrames en uno solo
final_df = pd.concat(dataframes, ignore_index=True)

# Guardar el DataFrame final en un nuevo archivo CSV
final_df.to_csv(output_file, index=False)

# Mostrar el resultado
print(final_df)

