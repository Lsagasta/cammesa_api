import requests
import sys
import json
from datetime import datetime, timedelta, timezone
import csv
from decouple import config
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd



# Obtener hora de ejecución para insertar en el nombre del archivo
utc_now = datetime.now(timezone.utc)
utc_minus_3 = utc_now - timedelta(hours=3)
fecha = utc_minus_3.strftime('%Y-%m-%d-%H-%M')


#Conectar a API
def conection(url):
    try:
        response= requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        return response, data
    
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión a la API: {e}")
        sys.exit(1)  

# Guardar archivo JSON
def save_json(data):
    with open(f"jsons/generacion-electrica-{fecha}.json", 'w') as archivo:
        json.dump(data, archivo, indent=4)

#Guardar archivo CSV
def save_csv(data):
    with open(f'csvs/generacion-electrica{fecha}.csv', 'w', newline='') as csvfile:
        fieldnames = ["fecha", "sumTotal", "hidraulico", "termico", "nuclear", "renovable", "importacion"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return(data)


# Probando conexion a redshift
def redshift_conection():
    try:
        conn = psycopg2.connect(
            host = config("host"),
            port = config("port"),
            database = config("database"),
            user = config("user"),
            password = config("password")
            )
        print("Conexion realizada")
        return conn
    
    except Exception as e:
        print("No se a podido conectar a la base de datos")
        print(e)


type_map = {
    'int64': 'INT',            # Para columnas con enteros grandes
    'float64': 'FLOAT',        # Para columnas con números de punto flotante
    'object': 'VARCHAR(255)',  # Para columnas con texto o strings, 255 es una longitud típica
    'bool': 'BOOLEAN',         # Para columnas con valores booleanos (True/False)
    'datetime64[ns]': 'TIMESTAMP',  # Para columnas con fechas y horas
    'timedelta[ns]': 'INTERVAL',    # Para columnas con diferencias de tiempo
    'int32': 'INT',            # Para enteros más pequeños
    'float32': 'FLOAT'         # Para números de punto flotante más pequeños
}




def cargar_en_bd(conn, table_name, dataframe):
    print("Iniciando la función cargar_en_bd...")
    
    # Verificar si el dataframe es un pandas.DataFrame
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("El argumento 'dataframe' debe ser un pandas.DataFrame")
    
    print("El argumento 'dataframe' es un DataFrame válido.")
    
    # Obtener tipos de datos y columnas del DataFrame
    dtypes = dataframe.dtypes
    cols = list(dtypes.index)
    tipos = list(dtypes.values)
    
    print(f"Columnas detectadas: {cols}")
    print(f"Tipos de datos detectados: {tipos}")

    # Mapeo de tipos de datos de pandas a SQL
    type_map = {
    'int64': 'INT',            # Para columnas con enteros grandes
    'float64': 'FLOAT',        # Para columnas con números de punto flotante
    'object': 'VARCHAR(255)',  # Para columnas con texto o strings, 255 es una longitud típica
    'bool': 'BOOLEAN',         # Para columnas con valores booleanos (True/False)
    'datetime64[ns]': 'TIMESTAMP',  # Para columnas con fechas y horas
    'timedelta[ns]': 'INTERVAL',    # Para columnas con diferencias de tiempo
    'int32': 'INT',            # Para enteros más pequeños
    'float32': 'FLOAT'         # Para números de punto flotante más pequeños
}
    sql_dtypes = [type_map[str(dtype)] for dtype in tipos]

    print(f"Tipos de datos SQL correspondientes: {sql_dtypes}")

    # Definir formato SQL VARIABLE TIPO_DATO
    column_defs = [f"{name} {data_type}" for name, data_type in zip(cols, sql_dtypes)]
    
    # Combine column definitions into the CREATE TABLE statement
    table_schema = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join(column_defs)}
    );
    """
    
    print(f"Esquema de la tabla generado:\n{table_schema}")

    # Crear la tabla
    cur = conn.cursor()
    cur.execute(table_schema)
    print(f"Tabla '{table_name}' creada o ya existe.")

    # Generar los valores a insertar
    values = [tuple(x) for x in dataframe.to_numpy()]
    
    # Imprimir la cantidad de registros a insertar
    num_records = len(values)
    print(f"Número de registros a insertar: {num_records}")
    
    # Mostrar el primer y el último registro
    if num_records > 0:
        print(f"Primer registro a insertar: {values[0]}")
        print(f"Último registro a insertar: {values[-1]}")
    else:
        print("No hay registros para insertar.")
    
    # Definir el INSERT
    insert_sql = f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES %s"
    print(f"Consulta SQL para inserción generada:\n{insert_sql}")

    # Execute the transaction to insert the data
    cur.execute("BEGIN")
    print("Transacción BEGIN iniciada.")
    
    execute_values(cur, insert_sql, values)
    print("Datos insertados en la tabla.")

    cur.execute("COMMIT")
    print("Transacción COMMIT completada.")
    
    print('Proceso terminado')








