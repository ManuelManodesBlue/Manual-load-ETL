import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# Ruta absoluta para el archivo CSV
file_path = "C:/workspace/blue-attached/manual-load/consolidate/archivo_normalizado.csv"

# Función para leer y procesar el archivo CSV
def procesar_csv_con_pandas(file_path):
    try:
        # Lee el archivo CSV
        df_asn = pd.read_csv(file_path)
        
        # Renombrar las columnas si es necesario
        columnas_renombrar = {
            'owner': 'cliente',
            'reception_nbr': 'numero_de_documento',
            'doctype': 'tipo_de_documento',
            'created_date': 'fecha_creacion',
            'closed': 'estado_recepcion',
            'status': 'status',
            'expected_date': 'fecha_eta',
            'provider_id': 'proveedor',
            'reception_type': 'tipo_de_entrega',
            'item_nbr': 'sku',
            'line': 'line',
            'qty': 'cantidad'
        }

        df_asn.rename(columns=columnas_renombrar, inplace=True)
           
        hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Inclusión de columnas calculadas
        df_asn['total_pedido'] = df_asn.groupby('numero_de_documento')['cantidad'].transform('sum')
        df_asn['total_pedido'] = df_asn['total_pedido'].astype(int)
        df_asn['descripcion'] = ''
        
        # Filtrar columna 'cliente' con valores nulos
        df_asn = df_asn.dropna(subset=['cliente'])
        #print(df_asn)
        
        # Crear columna para la fecha de ejecución
        df_asn['fecha_ejecucion'] = hoy
        
        # Orden de columnas según mapeo
        columnas_deseadas = ['cliente','numero_de_documento','tipo_de_documento','total_pedido','fecha_creacion',
                             'estado_recepcion','fecha_eta','proveedor','sku','descripcion','cantidad',
                             'tipo_de_entrega','fecha_ejecucion']
        
        # Usamos reindex para reordenar/agregar las columnas deseadas.
        # Las columnas que no existan en el DataFrame original se llenarán con NaN.
        df_asn = df_asn.reindex(columns=columnas_deseadas)

        # Muestra las primeras 5 filas para verificar que se cargó correctamente
        print("Primeras 5 filas:\n", df_asn.head())

        # usuario = 'logistica'
        # contrasena = 'cargadatos'
        # nombre_bd = 'dwh'
        # direccion_servidor = '172.16.7.109'
        # puerto = '5432'
        # url_conexion = f'postgresql://{usuario}:{contrasena}@{direccion_servidor}:{puerto}/{nombre_bd}'
        # engine = create_engine(url_conexion)
        # nombre_tabla_append = 'logistica_recepciones'
        # schema_name = 'dev'

        # df_asn.to_sql(nombre_tabla_append, con=engine, schema=schema_name, if_exists='append', index=False, method='multi')

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {file_path}")
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está vacío")
    except Exception as e:
        print(f"Error: Ocurrió un error al leer el archivo CSV. Detalles: {e}")

# Llama a la función con la ruta absoluta
#procesar_csv_con_pandas(file_path)
