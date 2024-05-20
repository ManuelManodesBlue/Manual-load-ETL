import os
import pandas as pd

def consolidar_csv(directorio):
    # Lista para almacenar los DataFrames de los archivos CSV
    dfs = []
    
    # Configura el manejo de líneas mal formadas
    pd.options.mode.use_inf_as_na = True
    
    # Recorre todos los archivos y subdirectorios
    for root, dirs, files in os.walk(directorio):
        for file in files:
            # Verifica si el archivo es un archivo CSV
            if file.endswith('.csv'):
                # Intenta leer el archivo CSV
                path = os.path.join(root, file)
                try:
                    df = pd.read_csv(path)
                    dfs.append(df)
                except pd.errors.ParserError as e:
                    print(f"Error al leer el archivo {path}: {e}")
    
    # Concatena todos los DataFrames en uno solo
    if dfs:
        df_consolidado = pd.concat(dfs, ignore_index=True)
        
        # Exporta el DataFrame consolidado a un nuevo archivo CSV
        ruta_consolidada = os.path.join(directorio, 'consolidado.csv')
        df_consolidado.to_csv(ruta_consolidada, index=False)
        
        print(f'Se han consolidado {len(dfs)} archivos CSV en {ruta_consolidada}')
    else:
        print('No se encontraron archivos CSV para consolidar.')

# Directorio donde se encuentran los archivos CSV
directorio = r'C:\workspace\blue-attached\primer-formato-respaldo\pruebas'

# Llama a la función para consolidar los archivos CSV
consolidar_csv(directorio)
