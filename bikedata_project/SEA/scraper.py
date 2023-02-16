import requests
from bs4 import BeautifulSoup
import json

# URL base y parámetros iniciales para la búsqueda
url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"
params = {
    "bbo_desde_fecha": "01/01/2022",
    "bbo_hasta_fecha": "16/02/2023",
    "pagina": "1"
}

# Lista para almacenar todos los datos
datos = []

# Loop para recorrer todas las páginas
while True:
    # Realizar la solicitud HTTP y analizar el contenido HTML
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar la tabla de resultados
    tabla_resultados = soup.find('table', {'class': 'tabla-resultados'})

    # Encontrar todas las filas de la tabla, excepto la primera (que contiene los encabezados de la columna)
    filas = tabla_resultados.find_all('tr')[1:]

    # Iterar sobre cada fila y extraer los datos
    for fila in filas:
        # Extraer cada celda de la fila
        celdas = fila.find_all('td')

        # Extraer los datos de cada celda y almacenarlos en un diccionario
        proyecto = {
            "id_proyecto": celdas[0].text.strip(),
            "nombre": celdas[1].text.strip(),
            "estado": celdas[2].text.strip(),
            "tipo": celdas[3].text.strip(),
            "etapa": celdas[4].text.strip(),
            "fecha_ingreso": celdas[5].text.strip(),
            "fecha_calificacion": celdas[6].text.strip(),
            "region": celdas[7].text.strip(),
            "comuna": celdas[8].text.strip(),
            "latitud": celdas[9].text.strip(),
            "longitud": celdas[10].text.strip()
        }
        datos.append(proyecto)

    # Encontrar el botón "Siguiente" para continuar a la siguiente página
    boton_siguiente = soup.find('a', {'class': 'siguiente'})

    # Si no hay un botón "Siguiente", significa que hemos llegado a la última página
    if not boton_siguiente:
        break

    # Actualizar los parámetros de la búsqueda para la siguiente página
    params["pagina"] = str(int(params["pagina"]) + 1)

# Almacenar la información en un archivo .json
with open("datos_proyectos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)