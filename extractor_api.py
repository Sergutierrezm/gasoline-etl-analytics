import requests
import pandas as pd

def extraer_gasolineras():

    """Conecta a la API del Ministerio y devuelve un DataFrame con toda España."""
    url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"

    try:
        print("Descargando datos en tiempo real del Ministerio...")
        respuesta = requests.get(url, timeout=15)
        respuesta.raise_for_status()





    except:
        