from functions import conection, save_json

# la región 1002 corresponde al total de las regiones.


api_url = "https://api.cammesa.com/demanda-svc/generacion/ObtieneGeneracioEnergiaPorRegion?id_region=1002"

    
response, data = conection(api_url)

print(response)
print("---------")
print(data)

save_json(data)



