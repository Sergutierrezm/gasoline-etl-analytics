import requests
import pandas as pd

def extraer_gasolineras():

    """Conecta a la API del Ministerio y devuelve un DataFrame con toda España."""
    url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"

    try:
        print("Descargando datos en tiempo real del Ministerio...")
        respuesta = requests.get(url, timeout=15)
        respuesta.raise_for_status()

        # Extraemos la lista de estaciones desde el JSON
        datos_json = respuesta.json()
        lista_gasolineras = datos_json.get("ListaEESSPrecio", [])

        #Convertimos a DataFrame
        df = pd.DataFrame(lista_gasolineras)
        print(f"Extracción completada: {len(df)} registros obtenidos.")
        return df


    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión con la API: {e}")
    
        return None
    
    except Exception as e:
    
        print(f"Error al procesar la respuesta: {e}")
    
        return None
        