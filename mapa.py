import folium

def calcular_centroide(lista: list[dict]) -> tuple[float, float]:
    total = len(lista)
    soma_latitude = 0.0
    soma_longitude = 0.0

    for cidade in lista:
        soma_latitude += cidade["latitude"]
        soma_longitude += cidade["longitude"]

    latitude_media = soma_latitude / total
    longitude_media = soma_longitude / total

    return latitude_media, longitude_media

def gerar_mapa(lista: list[dict]):
    latitude, longitude = calcular_centroide(lista)
    mapa = folium.Map([latitude, longitude], zoom_start=6)
    for cidade in lista:
        infos = gerar_popup(cidade)
        folium.Marker(location=[cidade["latitude"], cidade["longitude"]], popup=infos).add_to(mapa)

    mapa.save("mapa.html")

def gerar_popup(cidade: dict) -> str:      
    return (f"<b>{cidade['nome']}</b><br>"
            f"Estado: {cidade['estado']}<br><br>"
            f"População: {cidade['populacao']}<br><br>"
            f"Latitude: {cidade['latitude']}<br><br>"
            f"Longitude: {cidade['longitude']}")