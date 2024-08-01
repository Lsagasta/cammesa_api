import requests
import sys
import json
from datetime import datetime



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
    fecha = datetime.today().strftime('%Y-%m-%d')
    with open(f"jsons/generacion-electrica-{fecha}.json", 'w') as archivo:
        json.dump(data, archivo, indent=4)




