import json

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

def salvar_geojson(geojson: str):
    try:
            with open("cidades.geojson", "w", encoding="utf-8") as arquivo_geojson:
                json.dump(geojson, arquivo_geojson, indent=4, ensure_ascii=False)
    except IOError as erro:
            print(f"Ocorreu um erro de sistema/IO inesperado: {erro}")
    