print("Hola, app de clima!")
import requests
import sys 
API_KEY= "Ec3b82db8914514857122becb4faddc4"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

# --- 3. Pedir Datos al Usuario ---
ciudad = input("Ingrese el nombre de la ciudad (o 'salir' para terminar): ")

# Salir si el usuario quiere
if ciudad.lower() == 'salir':
    sys.exit()

# --- 4. Armar el "Pedido" (Request) ---

# Este diccionario 'params' es el "pedido" que le hacemos al mozo.
# requests se encargará de armar la URL por nosotros (ej: ...?q=Funes&appid=...)
params = {
    'q': ciudad,         # 'q' es el parámetro para "query" (la ciudad)
    'appid': API_KEY,  # 'appid' es el parámetro para la API Key
    'units': 'metric', # 'units=metric' es para que nos dé la temperatura en Celsius
    'lang': 'es'       # 'lang=es' para que las descripciones vengan en español
}

# --- 5. "Llamar al Mozo" (Hacer la llamada a la API) ---
try:
    # "Llamamos al mozo" (requests.get) con la URL de la "cocina" (BASE_URL)
    # y nuestro "pedido" (params)
    response = requests.get(BASE_URL, params=params)
    
    # Esta línea es un seguro: si la respuesta fue un error (ej: 404, 401),
    # el programa saltará al "except" de abajo.
    response.raise_for_status()

    # --- 6. Procesar la Respuesta (Si todo salió bien) ---
    
    # Convertimos la respuesta (que es texto JSON) en un diccionario de Python
    data = response.json()

    # --- 7. Extraer y Mostrar los Datos ---
    
    # (Si querés ver TODO lo que te devolvió la API, descomentá la línea de abajo)
    # print(data) 
    
    # Navegamos el diccionario para encontrar los datos que queremos
    nombre_ciudad = data['name']
    temp_actual = data['main']['temp']
    sensacion_termica = data['main']['feels_like']
    descripcion_clima = data['weather'][0]['description']

    print(f"\n--- Clima en {nombre_ciudad} ---")
    print(f"Descripción: {descripcion_clima.capitalize()}")
    print(f"Temperatura: {temp_actual}°C")
    print(f"Sensación Térmica: {sensacion_termica}°C")


# --- 8. Manejo de Errores ---
except requests.exceptions.HTTPError as err:
    # Esta sección se ejecuta si 'raise_for_status()' falla
    if response.status_code == 401:
        print("Error: API Key incorrecta. Revisa tu variable API_KEY.")
    elif response.status_code == 404:
        print(f"Error: No se pudo encontrar la ciudad '{ciudad}'.")
    else:
        print(f"Error HTTP: {err}")
except requests.exceptions.RequestException as err:
    # Esto atrapa errores de conexión (ej: no tenés internet)
    print(f"Error de conexión: {err}")


