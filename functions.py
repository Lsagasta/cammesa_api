import requests

def conection(url):
    try:
        response= requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        return response, data
    
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexíon a la API: {e}")
        return None, None


