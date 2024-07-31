from functions import conection, save_json


api_url = "https://api.cammesa.com/demanda-svc/generacion/ObtieneGeneracioEnergiaPorRegion?id_region=429"
    
response, data = conection(api_url)

print(response)
print("---------")
print(data)

save_json(data)


