# Conector API CAMMESA

Este repositorio permite conectarse a la API de CAMMESA (Compañía Administradora del Mercado Mayorista Eléctrico Sociedad Anónima) para obtener datos de la generación eléctrica total del país en intervalos de 5 minutos.

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
Instalación
Clona el repositorio:
sh
Copiar código
git clone https://github.com/tu_usuario/cammesa-api-connector.git
Navega al directorio del proyecto:
sh
Copiar código
cd cammesa-api-connector
Instala las dependencias:
sh
Copiar código
pip install -r requirements.txt
Uso
Ejemplo de código
Aquí hay un ejemplo de cómo utilizar este conector para obtener datos de la API de CAMMESA:

python
Copiar código
import requests

url = "URL_DE_LA_API_CAMMESA"
response = requests.get(url)
data = response.json()

print(data)
Asegúrate de reemplazar URL_DE_LA_API_CAMMESA con la URL real de la API.

Documentación
Para más detalles sobre el uso de esta API, consulta la documentación oficial de CAMMESA.

Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva característica').
Sube tus cambios a la rama (git push origin feature/nueva-caracteristica).
Abre un Pull Request.
Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

Contacto
Para cualquier duda o consulta, puedes contactarnos a través de tu_email@example.com.

go
Copiar código

Recuerda reemplazar `URL_DE_LA_API_CAMMESA` y `URL_DE_LA_DOCUMENTACION` con las URLs correspondien