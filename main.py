from functions import conection


api_url = "https://api.cammesa.com/demanda-svc/generacion/ObtieneGeneracioEnergiaPorRegion?id_region=429"
    
response, data = conection(api_url)

print(data)





