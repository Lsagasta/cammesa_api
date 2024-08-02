import requests
import sys
import json
from datetime import datetime
import csv

fecha = datetime.today().strftime('%Y-%m-%d')


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




