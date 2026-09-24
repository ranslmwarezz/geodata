import json
import folium

def mostrar_cidade(cidade: dict):
    print(" ")
    print("Cidade:", cidade['nome'])
    print("Estado:", cidade['estado'])
    print("População:", cidade['populacao'])
    print("Latitude:", cidade['latitude'])
    print("Longitude:", cidade['longitude'])
    print(" ")

def contar_cidades(lista: list[dict]) -> int:
    tamanho = len(lista)
    return tamanho

def cidade_mais_populosa(lista: list[dict]) -> tuple[str, int]:
    maior_populacao = 0
    nome_cidade = ""

    for cidade in lista:
        if cidade["populacao"] > maior_populacao:
            maior_populacao = cidade["populacao"]
            nome_cidade = cidade["nome"]


    return nome_cidade, maior_populacao

def cidade_menos_populosa(lista: list[dict]) -> tuple[str, int]:
    menor_populacao = lista[0]["populacao"]
    nome_cidade = lista[0]["nome"]

    for cidade in lista:
        if cidade["populacao"] < menor_populacao:
            menor_populacao = cidade["populacao"]
            nome_cidade = cidade["nome"]

    return nome_cidade, menor_populacao

def populacao_total(lista: list[dict]) -> int:
    total = 0

    for cidade in lista:
        total += cidade["populacao"]


    return total

def gerar_geojson(lista: list[dict]) -> dict:
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for cidade in lista:
        feature_cidade = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [cidade["longitude"], cidade["latitude"]]
            },
            "properties": {
                "nome": cidade["nome"],
                "estado": cidade["estado"],
                "populacao": cidade["populacao"]
            }
        }
        geo_json["features"].append(feature_cidade)

    return geo_json

def calcular_centroide(lista: list[dict]) -> tuple[float, float]:
    total = contar_cidades(lista)
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

if __name__ == "__main__":

    try:
        with open("cidades.json", 'r', encoding='utf-8') as arquivo_json:
            cidades = json.load(arquivo_json)

    except FileNotFoundError:
        print("Arquivo não encontrado!")
        exit(1)
    except json.JSONDecodeError:
        print("cidades.json possui JSON inválido. Verifique o arquivo!") 
        exit(1)

    geojson = gerar_geojson(cidades)

    try:
        with open("cidades.geojson", "w", encoding="utf-8") as arquivo_geojson:
            json.dump(geojson, arquivo_geojson, indent=4, ensure_ascii=False)
    except IOError as erro:
        print(f"Ocorreu um erro de sistema/IO inesperado: {erro}")

    gerar_mapa(cidades)

    print("=== Relatório das cidades ===")
    qtd_cidades = contar_cidades(cidades)

    print("Quantidade de cidades:", qtd_cidades)
    nome_cidade, populacao = cidade_mais_populosa(cidades)

    print("Cidade mais populosa:")
    print(nome_cidade, "-", populacao, "habitantes")

    nome_cidade, menor_populacao = cidade_menos_populosa(cidades)
    print("Cidade menos populosa:")
    print(nome_cidade, "-", menor_populacao, "habitantes")

    total = populacao_total(cidades)
    print("População total:")
    print(total, "habitantes")
    for cidade in cidades:
        mostrar_cidade(cidade)
