import requests
import sys
import json
from datetime import datetime, timedelta, timezone
import csv
from decouple import config
import psycopg2



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
        fieldnames = ["timestamp", "sumTotal", "hidraulico", "termico", "nuclear", "renovable", "importacion"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# Redshift Conection
def conection():
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








