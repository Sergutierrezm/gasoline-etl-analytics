import pandas as pd

def limpiar_y_filtrar_mostoles(df):
    """
    Recibe el DataFrame crudo de toda España, filtra por Móstoles, 
    limpia los tipos de datos y lo devuelve listo para guardar.
    """
    if df is None or df.empty:
        print("Error: El DataFrame de entrada está vacío o es None.")
        return None

    try:
        # 2. Filtrado exacto por municipio. 
        # IMPORTANTE: El MITECO devuelve el texto en mayúsculas y con tildes.
        df_local = df[df['Municipio'] == 'MÓSTOLES'].copy()

        if df_local.empty:
            print("Aviso: No se encontraron gasolineras en Móstoles.")
            return None

        # 3. Selección de columnas relevantes. 
        columnas_utiles = [
            'Rótulo',                 # Nombre de la gasolinera (Repsol, Plenoil, etc.)
            'Dirección',              # Calle de ubicación
            'Precio Gasolina 95 E5',  # Precio de la gasolina 95
            'Precio Gasoleo A'        # Precio del diésel normal
        ]

        df_local = df_local[columnas_utiles]

        # 4. Limpieza de tipos de datos (Casting)
        # Bucle para aplicar la misma limpieza a gasolina y diésel

        for columna in ['Precio Gasolina 95 E5', 'Precio Gasoleo A']:
            df_local[columna] = df_local[columna].str.replace(',','.')

        # Paso B: Convertir la columna de texto (Object) a número decimal (Float)
            # errors='coerce' fuerza a que si una gasolinera no tiene precio (viene vacío), 
            # ponga un NaN (nulo) en lugar de que el programa se rompa.
        
        df_local = df_local.sort_values(by='Precio Gasolina 95 E5')
        print(f"Transformación completada: {len(df_local)} gasolineras procesadas en Móstoles.")
        return df_local
    except KeyError as e:
        print(f"Error: La columna {e} no existe en los datos del Ministerio. ¿Han cambiado la API?")
        return None
    except Exception as e:
        print(f"Error inesperado en la transformación: {e}")
        return None
