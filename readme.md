# Conector API CAMMESA

Este repositorio permite conectarse a la API de CAMMESA (Compañía Administradora del Mercado Mayorista Eléctrico Sociedad Anónima) para obtener datos de la generación eléctrica total del país en intervalos de 5 minutos.

La API es pública, por lo que no es necesario utilizar credenciales.

## Descripción

CAMMESA es una compañía argentina encargada de operar el mercado eléctrico mayorista de Argentina. La API proporciona datos detallados sobre la generación eléctrica, desglosada de la siguiente forma:

```json
{
    "fecha": "2024-07-31T00:00:00.000-0300",
    "sumTotal": 19723.6,
    "hidraulico": 3777.6,
    "termico": 9913.2,
    "nuclear": 1669.3,
    "renovable": 2275.3,
    "importacion": 2088.2
}
```

## Documentación
Para más detalles sobre el uso de esta API, consultar la documentación oficial de CAMMESA:
https://microfe.cammesa.com/static-content/CammesaWeb/download-manager-files/Api/Documentacion%20API%20Web.pdf


