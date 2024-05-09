from logistica_recepciones import procesar_csv_con_pandas
#from logistica_recepcion_update import procesar_csv_2_con_pandas

# Ruta absoluta para el archivo CSV
file_path = "C:/workspace/blue-attached/consolidate/archivo_normalizado.csv"

# Llama a la función para procesar el archivo logistica_recepcion CSV
procesar_csv_con_pandas(file_path)

# Llama a la función para procesar el archivo logistica_recepcion_update CSV
#procesar_csv_2_con_pandas(file_path)