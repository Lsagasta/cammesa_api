#importo las funciones necesarias desde mi archivo de funciones
from functions import conection, save_json, save_csv

#defino la URL de la API que quiero consultar
api_url = "https://api.cammesa.com/demanda-svc/generacion/ObtieneGeneracioEnergiaPorRegion?id_region=1002"

# ejecuto la conexión y guardo las respuestas obtenidas. 
response, data = conection(api_url)


#consulto si el status_code de la respuesta de la API es correcta
#En caso afirmativo, ejecuto 2 funciones. La primera guarda un json con los datos crudos. La segunda genera un archivo csv en un formato mas amigable para realizar la subida de datos a Reshift
# En caso negativo, se muestra el tipo de error.
if response.status_code == 200:
    save_json(data)
    save_csv(data)
    print("los archivos han sido generados correctamente")    
else: print(response)

