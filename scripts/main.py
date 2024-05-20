# #from logistica_recepciones import procesar_csv_con_pandas
# from logistica_recepcion_update import procesar_csv_2_con_pandas

# # Ruta absoluta para el archivo CSV
# #file_path = "C:/workspace/blue-attached/manual-load/consolidate/consolidated_data_recep.csv"
# file_path_2 = "C:/workspace/blue-attached/manual-load/consolidate/consolidated_data_recep_update.csv"

# # Llama a la función para procesar el archivo logistica_recepcion CSV
# #procesar_csv_con_pandas(file_path)

# # Llama a la función para procesar el archivo logistica_recepcion_update CSV
# procesar_csv_2_con_pandas(file_path_2)

# import pandas as pd

# # Crear un DataFrame de ejemplo
# data = {
#     'cliente': ['A', 'A', 'A', 'B'],
#     'numero_de_documento': [1, 1, 1, 2],
#     'sku': ['X', 'X', 'X', 'Y'],
#     'operacion': ['op1', 'op1', 'op1', 'op2'],
#     'descripcion': ['desc1', 'desc1', 'desc1', 'desc2'],
#     'usuario': ['user1', 'user1', 'user1', 'user2'],
#     'fecha_recepcion_finalizada': ['2024-05-10', '2024-05-10', '2024-05-10', '2024-05-14'],
#     'total_pedido': [10, 10, 30, 40],
#     'total_recepcionado': [5, 10, 15, 20]
# }

# df = pd.DataFrame(data)
# print(df)

# # Convertir la columna de fecha a tipo datetime
# df['fecha_recepcion_finalizada'] = pd.to_datetime(df['fecha_recepcion_finalizada'])

# # Definir una función personalizada para sumar los valores únicos de 'total_pedido' dentro de cada grupo
# def sumar_valores_unicos(series):
#     return series.drop_duplicates().sum()

# # Agrupar por las columnas especificadas y aplicar las operaciones deseadas
# result = df.groupby(['cliente', 'operacion', 'numero_de_documento', 'sku', 'descripcion', 'fecha_recepcion_finalizada']).agg({
#     'usuario': 'last',
#     'total_pedido': sumar_valores_unicos,  # Usar la función personalizada para sumar los valores únicos
#     'total_recepcionado': 'sum'
# }).reset_index()

# # Sumar los valores únicos de 'total_pedido'
# total_pedido_distintos = result['total_pedido'].sum()

# print("Resultado:")
# print(result)
# print("Suma de valores distintos de 'total_pedido':", total_pedido_distintos)

# import pandas as pd

# # Crear DataFrame con los datos proporcionados
# data = {
#     'cliente': ['CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'CLOCKWISE', 'JCBT', 'CLOCKWISE', 'JCBT', 'JCBT'],
#     'operacion': ['PRUEBA CANDADO', 'PRUEBA CANDADO', 'PRUEBA CANDADO', 'PRUEBA CANDADO', 'PRUEBA CANDADO', '', '', '', '', '', '', '', 'PRUEBA CANDADO', 'PRUEBA CANDADO', 'PRUEBA CANDADO', '', 'PRUEBA CANDADO', '', ''],
#     'proveedor': ['', '', '', '', '', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', 'RECBATCH01', '', '', '', ''],
#     'numero_de_documento': [10004012, 10004012, 10004012, 10004012, 10004012, '', '', '', '', '', '', '', 10004012, 10004012, 10004012, 7427, 10004012, 7427, 7427],
#     'sku': ['PROD001', 'COR001', 'COR001', 'COR001', 'COR001', 'ITBATCH03', 'ITBATCH03', 'ITBATCH02', 'ITBATCH02', 'ITBATCH02', 'ITBATCH01', 'ITBATCH01', 'ITBATCH01', 'PROD001', 'PROD001', 'MP-46103', 'PROD001', 'MP-46084', 'MP-46104'],
#     'descripcion': ['Producto de Prueba N1 TESTTESTÃ‘', 'CORONA LATA 330 CC', 'CORONA LATA 330 CC', 'CORONA LATA 330 CC', 'CORONA LATA 330 CC', 'Item prueba 3 con batch_', 'Item prueba 3 con batch_', 'Item prueba con batch_code', 'Item prueba con batch_code', 'Item prueba con batch_code', 'Item prueba con batch', 'Item prueba con batch', 'Item prueba con batch', 'Producto de Prueba N1 TESTTESTÃ‘', 'Producto de Prueba N1 TESTTESTÃ‘', 'FIGURA DRAGON BALL Z BURNING FIGHTERS VOL2 A VEGETA BANPRESTO 18388', 'Producto de Prueba N1 TESTTESTÃ‘', 'FIGURA DRAGON BALL Z HISTORY BOX VOL2 BANPRESTO 17977', 'FIGURA DRAGON BALL Z GRANDISTA RESOLUTION OF SOLDIERSSON GOHAN #2 BANPRESTO 17976'],
#     'total_pedido': [20, 0, 0, 0, 0, 0, 0, 60, 20, 20, 40, 30, 10, 20, 20, 100, 20, 60, 5],
#     'total_recepcionado': [1, 5, 3, 3, 1, 6, 3, 14, 20, 6, 14, 7, 6, 1, 2, 5, 1, 90, 10],
#     'fecha_recepcion_comienzo': ['2023-11-07 14:17:34.079', '2023-11-22 17:54:54.101', '2024-03-11 14:40:00.800', '2024-03-11 14:10:44.019', '2023-12-01 11:29:45.692', '2023-12-12 07:28:57.445', '2023-12-12 07:31:31.760', '2023-12-12 07:31:31.749', '2023-12-12 07:28:57.433', '2023-12-27 11:03:16.903', '2023-12-12 07:31:31.754', '2023-12-12 07:28:57.439', '2023-12-27 11:01:25.881', '2023-12-28 06:11:12.288', '2024-01-29 14:01:21.116', '2024-03-20 12:46:26.134', '2023-11-22 15:14:38.468', '2024-03-20 13:38:50.077', '2024-03-20 12:45:41.763'],
#     'fecha_recepcion_finalizada': ['2023-11-07 14:17:34.079', '2023-11-22 17:54:54.101', '2024-03-11 14:40:00.800', '2024-03-11 14:10:44.019', '2023-12-01 11:29:45.692', '2023-12-12 07:28:57.445', '2023-12-12 07:31:31.760', '2023-12-12 07:31:31.749', '2023-12-12 07:28:57.433', '2023-12-27 11:03:16.903', '2023-12-12 07:31:31.754', '2023-12-12 07:28:57.439', '2023-12-27 11:01:25.881', '2023-12-28 06:11:12.288', '2024-01-29 14:01:21.116', '2024-03-20 12:46:26.134', '2023-11-22 15:14:38.468', '2024-03-20 13:38:50.077', '2024-03-20 12:45:41.763'],
#     'usuario': [100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001, 100000001],
#     'caja_lpn': ['', '', '', '', '', 6, 6, 6, 6, 1, 6, 6, 1, 1, 1, 1, '', '', ''],
#     'estado_de_recepcion': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
#     'fecha_ejecucion': ['2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000', '2024-05-15 18:41:43.000']
# }

# df = pd.DataFrame(data)

# # Convertir las columnas de fecha a tipo datetime
# df['fecha_recepcion_comienzo'] = pd.to_datetime(df['fecha_recepcion_comienzo'])
# df['fecha_recepcion_finalizada'] = pd.to_datetime(df['fecha_recepcion_finalizada'])
# df['fecha_ejecucion'] = pd.to_datetime(df['fecha_ejecucion'])

# print(df)


# # Definir una función personalizada para sumar los valores únicos de 'total_pedido' dentro de cada grupo
# def sumar_valores_unicos(series):
#     return series.drop_duplicates().sum()

# # Agrupar por las columnas especificadas y aplicar las operaciones deseadas
# df = df.groupby(['cliente', 'operacion', 'numero_de_documento', 'sku', 'descripcion']).agg({
#         'usuario': 'last',
#         'fecha_recepcion_finalizada': 'last',
#         'estado_de_recepcion': 'max',
#         'total_pedido': sumar_valores_unicos,  # Usar la función personalizada para sumar los valores únicos
#         'total_recepcionado': 'sum'
#     }).reset_index()


# # Sumar los valores únicos de 'total_pedido'
# total_pedido_distintos = df['total_pedido'].sum()

# # # Sumar los valores únicos de 'total_pedido'
# # total_pedido_distintos = df['total_pedido'].sum()

# print("Resultado:")
# print(df)
# print("Suma de valores distintos de 'total_pedido':", total_pedido_distintos)

# import pandas as pd

# # Carga los datos en un DataFrame
# data = [
#     {"owner": "JCBT", "comment": "", "reception_nbr": "0000007427", "sku": "MP-46104", "description": "FIGURA DRAGON BALL Z GRANDISTA RESOLUTION OF SOLDIERSSON GOHAN #2 BANPRESTO 17976", "requested_qty": 5, "received_qty": 10, "created_at": "2024-03-20T12:45:41.763446", "details_out": 1, "rec_partial": "17299", "employee_rut": "100000001", "caja": "CAJA20031", "qty": 5, "container_created_at": "2024-03-20T12:45:41.716043", "document_nbr": "F20031"},
#     {"owner": "CLOCKWISE", "comment": "", "reception_nbr": "RECBATCH01", "sku": "ITBATCH03", "description": "Item prueba 3 con batch_", "requested_qty": 0, "received_qty": 3, "created_at": "2023-12-12T07:31:31.760855", "details_out": 6, "rec_partial": "17292", "employee_rut": "100000001", "caja": None, "qty": None, "container_created_at": None, "document_nbr": "F12345"},
#     # Aquí van todos los datos
# ]

# df = pd.DataFrame(data)
# print(df)

# # Agrupa los datos y calcula los valores requeridos
# grouped_data = df.groupby(['owner', 'reception_nbr', 'document_nbr', 'sku', 'description', 'caja', 'container_created_at']).agg(
#     usuario=('employee_rut', 'last'),
#     fecha_recepcion_finalizada=('created_at', 'last'),
#     estado_de_recepcion=('details_out', 'last'),
#     total_recepcionado=('received_qty', 'sum'),
#     qty=('qty', 'sum')
# ).reset_index()

# print(grouped_data)

# import pandas as pd

# # Convertir tus datos en un DataFrame de pandas
# data = [
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46104",
#         "description": "FIGURA DRAGON BALL Z GRANDISTA RESOLUTION OF SOLDIERSSON GOHAN #2 BANPRESTO 17976",
#         "requested_qty": 5,
#         "received_qty": 10,
#         "created_at": "2024-03-20T12:45:41.763446",
#         "details_out": 1,
#         "rec_partial": "17299",
#         "employee_rut": "100000001",
#         "caja": "CAJA20031",
#         "qty": 5,
#         "container_created_at": "2024-03-20T12:45:41.716043",
#         "document_nbr": "F20031"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH03",
#         "description": "Item prueba 3 con batch_",
#         "requested_qty": 0,
#         "received_qty": 3,
#         "created_at": "2023-12-12T07:31:31.760855",
#         "details_out": 6,
#         "rec_partial": "17292",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH02",
#         "description": "Item prueba con batch_code",
#         "requested_qty": 20,
#         "received_qty": 6,
#         "created_at": "2023-12-27T11:03:16.903233",
#         "details_out": 1,
#         "rec_partial": "17293",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G66666"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH02",
#         "description": "Item prueba con batch_code",
#         "requested_qty": 20,
#         "received_qty": 14,
#         "created_at": "2023-12-12T07:31:31.749803",
#         "details_out": 6,
#         "rec_partial": "17292",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 7,
#         "created_at": "2023-12-12T07:28:57.439246",
#         "details_out": 6,
#         "rec_partial": "17291",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46084",
#         "description": "FIGURA DRAGON BALL Z HISTORY BOX VOL2 BANPRESTO 17977",
#         "requested_qty": 60,
#         "received_qty": 90,
#         "created_at": "2024-03-20T13:38:50.077370",
#         "details_out": 1,
#         "rec_partial": "17300",
#         "employee_rut": "100000001",
#         "caja": "CAJA20033",
#         "qty": 90,
#         "container_created_at": "2024-03-20T13:38:50.052890",
#         "document_nbr": "F20032"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 3,
#         "created_at": "2024-03-11T14:10:44.019004",
#         "details_out": 1,
#         "rec_partial": "17297",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G666"
#     },
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46104",
#         "description": "FIGURA DRAGON BALL Z GRANDISTA RESOLUTION OF SOLDIERSSON GOHAN #2 BANPRESTO 17976",
#         "requested_qty": 5,
#         "received_qty": 10,
#         "created_at": "2024-03-20T12:45:41.763446",
#         "details_out": 1,
#         "rec_partial": "17299",
#         "employee_rut": "100000001",
#         "caja": "CAJA20032",
#         "qty": 5,
#         "container_created_at": "2024-03-20T12:46:26.050054",
#         "document_nbr": "F20031"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH02",
#         "description": "Item prueba con batch_code",
#         "requested_qty": 20,
#         "received_qty": 7,
#         "created_at": "2023-12-12T07:28:57.433343",
#         "details_out": 6,
#         "rec_partial": "17291",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 1,
#         "created_at": "2023-12-28T06:11:12.288960",
#         "details_out": 1,
#         "rec_partial": "17294",
#         "employee_rut": "100000001",
#         "caja": "CJT01",
#         "qty": 1,
#         "container_created_at": "2023-12-28T06:11:12.204385",
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH03",
#         "description": "Item prueba 3 con batch_",
#         "requested_qty": 0,
#         "received_qty": 6,
#         "created_at": "2023-12-12T07:28:57.445463",
#         "details_out": 6,
#         "rec_partial": "17291",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "JUAN",
#         "comment": '',
#         "reception_nbr": "PRUEBA2222",
#         "sku": "8000035039",
#         "description": "Cafetera Espresso Full Auto",
#         "requested_qty": 10,
#         "received_qty": 8,
#         "created_at": "2023-08-22T11:20:52.421004",
#         "details_out": 1,
#         "rec_partial": "17283",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 2,
#         "created_at": "2024-03-11T14:40:00.777908",
#         "details_out": 1,
#         "rec_partial": "17298",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G888888"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 6,
#         "created_at": "2023-12-27T11:01:25.881631",
#         "details_out": 1,
#         "rec_partial": "17293",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G66666"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 1,
#         "created_at": "2023-11-07T14:17:34.079524",
#         "details_out": 1,
#         "rec_partial": "17285",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G123"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 10,
#         "created_at": "2023-11-22T15:14:38.468145",
#         "details_out": 1,
#         "rec_partial": "17287",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 14,
#         "created_at": "2023-12-12T07:31:31.754320",
#         "details_out": 6,
#         "rec_partial": "17292",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 1,
#         "created_at": "2024-01-29T14:01:21.116024",
#         "details_out": 1,
#         "rec_partial": "17295",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 3,
#         "created_at": "2024-03-11T14:40:00.800299",
#         "details_out": 1,
#         "rec_partial": "17298",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G888888"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 1,
#         "created_at": "2023-12-01T11:29:45.692341",
#         "details_out": 1,
#         "rec_partial": "17290",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "OS3"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 1,
#         "created_at": "2024-03-11T14:06:44.724662",
#         "details_out": 1,
#         "rec_partial": "17296",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G123"
#     },
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46103",
#         "description": "FIGURA DRAGON BALL Z BURNING FIGHTERS VOL2 A VEGETA BANPRESTO 18388",
#         "requested_qty": 100,
#         "received_qty": 5,
#         "created_at": "2024-03-20T12:46:26.134804",
#         "details_out": 1,
#         "rec_partial": "17299",
#         "employee_rut": "100000001",
#         "caja": "CAJA20032",
#         "qty": 5,
#         "container_created_at": "2024-03-20T12:46:26.050054",
#         "document_nbr": "F20031"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 2,
#         "created_at": "2024-03-11T14:10:43.990921",
#         "details_out": 1,
#         "rec_partial": "17297",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G666"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 5,
#         "created_at": "2023-11-22T17:54:54.101951",
#         "details_out": 1,
#         "rec_partial": "17288",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G55555"
#     }
# ]

# df = pd.DataFrame(data)

# # Asegurarse de que fechas sea de tipo datetime
# df['created_at'] = pd.to_datetime(df['created_at'])
# df['container_created_at'] = pd.to_datetime(df['container_created_at'])

# # Definir una función personalizada para sumar los valores únicos de 'total_pedido' dentro de cada grupo
# def sumar_valores_unicos(series):
#     return series.drop_duplicates().sum()

# def obtener_ultimo_valor(series):
#     return series.dropna().iloc[-1]

# # Agrupar por las columnas especificadas y aplicar las operaciones deseadas
# df_update = df.groupby([
#     'owner', 'reception_nbr', 'sku', 'description', 'rec_partial', 'employee_rut', 'caja', 'document_nbr']).agg({
#     'created_at': 'max',
#     'container_created_at': obtener_ultimo_valor,
#     'comment': 'last',
#     'requested_qty': sumar_valores_unicos,
#     'received_qty': 'sum',
#     'details_out': 'last'
# }).reset_index()

# # Sumar los valores únicos de 'total_pedido'
# total_pedido_distintos = df_update['requested_qty'].sum()

# # Mostrar el DataFrame actualizado y el total de 'total_pedido' sumado

# print(df_update)
# # Sumar la columna 'total_pedido'
# total_pedido_sumado = df_update['received_qty'].sum()

# # Imprimir la suma de la columna 'total_pedido'
# print("Total de 'total_pedido' sumado:", total_pedido_sumado)
# print(df_update['caja'])
# df_update.to_csv('df_update.csv', index=False)

# import pandas as pd

# # Datos de ejemplo en forma de diccionario
# data = [
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46104",
#         "description": "FIGURA DRAGON BALL Z GRANDISTA RESOLUTION OF SOLDIERSSON GOHAN #2 BANPRESTO 17976",
#         "requested_qty": 5,
#         "received_qty": 10,
#         "created_at": "2024-03-20T12:45:41.763446",
#         "details_out": 1,
#         "rec_partial": "17299",
#         "employee_rut": "100000001",
#         "caja": "CAJA20031",
#         "qty": 5,
#         "container_created_at": "2024-03-20T12:45:41.716043",
#         "document_nbr": "F20031"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH03",
#         "description": "Item prueba 3 con batch_",
#         "requested_qty": 0,
#         "received_qty": 3,
#         "created_at": "2023-12-12T07:31:31.760855",
#         "details_out": 6,
#         "rec_partial": "17292",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH02",
#         "description": "Item prueba con batch_code",
#         "requested_qty": 20,
#         "received_qty": 6,
#         "created_at": "2023-12-27T11:03:16.903233",
#         "details_out": 1,
#         "rec_partial": "17293",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G66666"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH02",
#         "description": "Item prueba con batch_code",
#         "requested_qty": 20,
#         "received_qty": 14,
#         "created_at": "2023-12-12T07:31:31.749803",
#         "details_out": 6,
#         "rec_partial": "17292",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 7,
#         "created_at": "2023-12-12T07:28:57.439246",
#         "details_out": 6,
#         "rec_partial": "17291",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46084",
#         "description": "FIGURA DRAGON BALL Z HISTORY BOX VOL2 BANPRESTO 17977",
#         "requested_qty": 60,
#         "received_qty": 90,
#         "created_at": "2024-03-20T13:38:50.077370",
#         "details_out": 1,
#         "rec_partial": "17300",
#         "employee_rut": "100000001",
#         "caja": "CAJA20033",
#         "qty": 90,
#         "container_created_at": "2024-03-20T13:38:50.052890",
#         "document_nbr": "F20032"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 3,
#         "created_at": "2024-03-11T14:10:44.019004",
#         "details_out": 1,
#         "rec_partial": "17297",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G666"
#     },
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46104",
#         "description": "FIGURA DRAGON BALL Z GRANDISTA RESOLUTION OF SOLDIERSSON GOHAN #2 BANPRESTO 17976",
#         "requested_qty": 5,
#         "received_qty": 10,
#         "created_at": "2024-03-20T12:45:41.763446",
#         "details_out": 1,
#         "rec_partial": "17299",
#         "employee_rut": "100000001",
#         "caja": "CAJA20032",
#         "qty": 5,
#         "container_created_at": "2024-03-20T12:46:26.050054",
#         "document_nbr": "F20031"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH02",
#         "description": "Item prueba con batch_code",
#         "requested_qty": 20,
#         "received_qty": 7,
#         "created_at": "2023-12-12T07:28:57.433343",
#         "details_out": 6,
#         "rec_partial": "17291",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 1,
#         "created_at": "2023-12-28T06:11:12.288960",
#         "details_out": 1,
#         "rec_partial": "17294",
#         "employee_rut": "100000001",
#         "caja": "CJT01",
#         "qty": 1,
#         "container_created_at": "2023-12-28T06:11:12.204385",
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH03",
#         "description": "Item prueba 3 con batch_",
#         "requested_qty": 0,
#         "received_qty": 6,
#         "created_at": "2023-12-12T07:28:57.445463",
#         "details_out": 6,
#         "rec_partial": "17291",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "JUAN",
#         "comment": '',
#         "reception_nbr": "PRUEBA2222",
#         "sku": "8000035039",
#         "description": "Cafetera Espresso Full Auto",
#         "requested_qty": 10,
#         "received_qty": 8,
#         "created_at": "2023-08-22T11:20:52.421004",
#         "details_out": 1,
#         "rec_partial": "17283",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 2,
#         "created_at": "2024-03-11T14:40:00.777908",
#         "details_out": 1,
#         "rec_partial": "17298",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G888888"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 6,
#         "created_at": "2023-12-27T11:01:25.881631",
#         "details_out": 1,
#         "rec_partial": "17293",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G66666"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 1,
#         "created_at": "2023-11-07T14:17:34.079524",
#         "details_out": 1,
#         "rec_partial": "17285",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G123"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 10,
#         "created_at": "2023-11-22T15:14:38.468145",
#         "details_out": 1,
#         "rec_partial": "17287",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "",
#         "reception_nbr": "RECBATCH01",
#         "sku": "ITBATCH01",
#         "description": "Item prueba con batch",
#         "requested_qty": 10,
#         "received_qty": 14,
#         "created_at": "2023-12-12T07:31:31.754320",
#         "details_out": 6,
#         "rec_partial": "17292",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "F12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 1,
#         "created_at": "2024-01-29T14:01:21.116024",
#         "details_out": 1,
#         "rec_partial": "17295",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G12345"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 3,
#         "created_at": "2024-03-11T14:40:00.800299",
#         "details_out": 1,
#         "rec_partial": "17298",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G888888"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 1,
#         "created_at": "2023-12-01T11:29:45.692341",
#         "details_out": 1,
#         "rec_partial": "17290",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "OS3"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 1,
#         "created_at": "2024-03-11T14:06:44.724662",
#         "details_out": 1,
#         "rec_partial": "17296",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G123"
#     },
#     {
#         "owner": "JCBT",
#         "comment": "",
#         "reception_nbr": "0000007427",
#         "sku": "MP-46103",
#         "description": "FIGURA DRAGON BALL Z BURNING FIGHTERS VOL2 A VEGETA BANPRESTO 18388",
#         "requested_qty": 100,
#         "received_qty": 5,
#         "created_at": "2024-03-20T12:46:26.134804",
#         "details_out": 1,
#         "rec_partial": "17299",
#         "employee_rut": "100000001",
#         "caja": "CAJA20032",
#         "qty": 5,
#         "container_created_at": "2024-03-20T12:46:26.050054",
#         "document_nbr": "F20031"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "PROD001",
#         "description": "Producto de Prueba N1 TESTTESTÑ",
#         "requested_qty": 20,
#         "received_qty": 2,
#         "created_at": "2024-03-11T14:10:43.990921",
#         "details_out": 1,
#         "rec_partial": "17297",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G666"
#     },
#     {
#         "owner": "CLOCKWISE",
#         "comment": "PRUEBA CANDADO",
#         "reception_nbr": "10004012",
#         "sku": "COR001",
#         "description": "CORONA LATA 330 CC",
#         "requested_qty": 0,
#         "received_qty": 5,
#         "created_at": "2023-11-22T17:54:54.101951",
#         "details_out": 1,
#         "rec_partial": "17288",
#         "employee_rut": "100000001",
#         "caja": '',
#         "qty": '',
#         "container_created_at": '',
#         "document_nbr": "G55555"
#     }
# ]

# df = pd.DataFrame(data)

# # # Agrupar por la columna "owner" y sumarizar la columna "requested_qty"
# # resultados = df.groupby(['owner','comment','reception_nbr','sku','description','created_at','caja']).agg({'requested_qty': ['sum', 'count']})

# # # Renombrar las columnas para mayor claridad
# # resultados.columns = ['total_requested_qty', 'count']

# # Agrupar por las columnas especificadas y sumarizar 'requested_qty' y obtener la fecha máxima de 'created_at'
# df = df.groupby(['owner', 'comment', 'reception_nbr', 'sku', 'description', 'caja','document_nbr']).agg(
#     total_requested_qty=('requested_qty', 'sum'),
#     count=('requested_qty', 'count'),
#     container_created_at=('container_created_at','max'),
#     max_created_at=('created_at', 'max'),
#     employee_rut=('employee_rut', 'max'),
#     qty=('qty','sum')
# ).reset_index()

# # Imprimir los resultados
# print(df)
# df.to_csv('df_update.csv', index=False)

# import pandas as pd

# # Crear el DataFrame con datos de ejemplo
# data = {
#     'categoria': ['A', 'A', 'B', 'B', 'A', 'B'],
#     'subcategoria': ['X', 'Y', 'X', 'Y', 'X', 'X'],
#     'ventas': [100, 200, 150, 300, 250, 400]
# }

# df = pd.DataFrame(data)

# # Mostrar el DataFrame original
# print("DataFrame original:")
# print(df)

# # Agrupar por 'categoria' y 'subcategoria' y sumar la columna 'ventas'
# grouped_df = df.groupby(['categoria', 'subcategoria']).sum().reset_index()

# # Mostrar el DataFrame agrupado
# print("\nDataFrame agrupado y sumado:")
# print(grouped_df)

import pandas as pd

# Supongamos que este es tu DataFrame
df = pd.DataFrame({
    'cliente': ['A', '', 'C'],
    'numero_de_documento': [123, 456, None],
    'sku': [789, 101, 112],
    'caja_lpn': ['LPN1', 'LPN2', ''],
    'documento_referencia': ['REF1', None, 'REF3'],
    'operacion': ['OP1', 'OP2', ''],
    'descripcion': ['desc1', 'desc2', 'desc3'],
    'total_pedido': [10, 20, 30],
    'total_recepcionado': [5, 10, 15],
    'fecha_recepcion_finalizada': ['2023-05-01', '2023-05-02', '2023-05-03'],
    'usuario': ['user1', 'user2', 'user3'],
    'estado_de_recepcion': ['estado1', 'estado2', 'estado3'],
    'qty': [100, 200, 300],
    'container_created_at': ['2023-04-01', '2023-04-02', '2023-04-03']
})

# Definir las columnas clave
keys = ['cliente', 'numero_de_documento', 'sku', 'caja_lpn', 'documento_referencia', 'operacion']

# Definir los valores por defecto para las claves
default_values = {
    'cliente': 'Desconocido',
    'numero_de_documento': 'Sin Documento',
    'sku': 'Sin SKU',
    'caja_lpn': 'Sin LPN',
    'documento_referencia': 'Sin Referencia',
    'operacion': 'Sin Operacion'
}

# Reemplazar valores vacíos o nulos en las claves con los valores por defecto
df[keys] = df[keys].replace('', pd.NA).fillna(value=default_values)

# Definir la forma de agregar los datos
agg_funcs = {
    'descripcion': 'first',  # Mantener la primera descripción
    'total_pedido': 'sum',  # Sumar los totales pedidos
    'total_recepcionado': 'sum',  # Sumar los totales recepcionados
    'fecha_recepcion_finalizada': 'max',  # Tomar la fecha de recepción más tardía
    'usuario': 'first',  # Mantener el primer usuario
    'estado_de_recepcion': 'first',  # Mantener el primer estado de recepción
    'qty': 'sum',  # Sumar las cantidades
    'container_created_at': 'min'  # Tomar la fecha de creación más temprana
}

# Agrupar por las claves y aplicar las funciones de agregación
grouped_df = df.groupby(keys).agg(agg_funcs).reset_index()

print(grouped_df)

