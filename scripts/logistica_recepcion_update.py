import pandas as pd
from datetime import datetime
import numpy as np
import traceback  # Módulo para obtener la traza de errores
from sqlalchemy import create_engine

# Ruta absoluta para el archivo CSV
file_path = "C:/workspace/blue-attached/manual-load/consolidate/consolidated_data_recep_update.csv"

# Función para leer y procesar el archivo CSV
def procesar_csv_2_con_pandas(file_path):
    try:
        # Lee el archivo CSV
        df_update = pd.read_csv(file_path, delimiter=',')

        # Lista de columnas a renombrar
        columnas_renombrar = {
            'owner': 'cliente',
            'comment': 'operacion',
            'reception_nbr': 'numero_de_documento',
            'description': 'descripcion',
            'requested_qty': 'total_pedido',
            'received_qty': 'total_recepcionado',
            'created_at': 'fecha_recepcion_finalizada',
            'employee_rut': 'usuario',
            'details_out': 'estado_de_recepcion',
            'caja': 'caja_lpn',
            'document_nbr': 'documento_referencia'
        }

        # Renombrar las columnas si existen
        df_update.rename(columns=columnas_renombrar, inplace=True)
    
        hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Verificar si las columnas críticas existen
        if 'fecha_recepcion_finalizada' in df_update.columns:
            # Si existe, copiar sus valores a la nueva columna 'fecha_recepcion_comienzo'
            df_update['fecha_recepcion_comienzo'] = df_update['fecha_recepcion_finalizada']
        else:
            # Si no existe, inicializar con NaN y convertir a datetime
            df_update['fecha_recepcion_comienzo'] = np.nan
            df_update['fecha_recepcion_comienzo'] = pd.to_datetime(df_update['fecha_recepcion_comienzo'])
        
        # Crear columnas adicionales y configurarlas
        df_update['proveedor'] = ''
        df_update['fecha_ejecucion'] = hoy
        df_update['fecha_ejecucion'] = pd.to_datetime(df_update['fecha_ejecucion'])

        # Mostrar las primeras filas para verificar
        print("Primeras 5 filas:\n", df_update.head())

        # Definir columnas deseadas
        columnas_deseadas = [
            'cliente', 'operacion', 'proveedor', 'numero_de_documento', 'sku', 'descripcion',
            'total_pedido', 'total_recepcionado', 'fecha_recepcion_comienzo',
            'fecha_recepcion_finalizada', 'usuario', 'caja_lpn', 'estado_de_recepcion', 'documento_referencia',
            'qty', 'container_created_at', 'fecha_ejecucion'
        ]

        # Reindexar con las columnas deseadas
        df_update = df_update.reindex(columns=columnas_deseadas)

        # Mostrar las primeras filas para verificar
        print("Primeras 5 filas:\n", df_update.head())

        usuario = 'logistica'
        contrasena = 'cargadatos'
        nombre_bd = 'dwh'
        direccion_servidor = '172.16.7.109'
        puerto = '5432'
        url_conexion = f'postgresql://{usuario}:{contrasena}@{direccion_servidor}:{puerto}/{nombre_bd}'
        engine = create_engine(url_conexion)
        nombre_tabla_append = 'logistica_recepcion_update'
        schema_name = 'dev'

        df_update.to_sql(nombre_tabla_append, con=engine, schema=schema_name, if_exists='append', index=False, method='multi')


    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {file_path}")
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está vacío")
    except Exception as e:
        print("Error: Ocurrió un error al procesar el archivo CSV.")
        print("Detalles del error:")
        traceback.print_exc()  # Muestra la traza completa del error para identificar la línea exacta

# Llama a la función para procesar el archivo CSV
procesar_csv_2_con_pandas(file_path)
