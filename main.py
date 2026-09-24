import json

def mostrar_cidade(nome: str, estado: str, populacao: int, latitude: float, longitude: float):
    print("Cidade:", nome)
    print("Estado:", estado)
    print("População:", populacao)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print(" ")

if __name__ == "__main__":

    try:
    # r de read
        with open("cidades.json", 'r', encoding='utf-8') as arquivo_json:
            cidades = json.load(arquivo_json)

    except FileNotFoundError:
        print("Arquivo não encontrado!")
        exit(1)
    except json.JSONDecodeError:
        print("cidades.json possui JSON inválido. Verifique o arquivo!") 
        exit(1)

    print("=== Relatório das cidades ===")
    for cidade in cidades:
        mostrar_cidade(nome=cidade["nome"],
            estado=cidade["estado"],
            populacao=cidade["populacao"],
            latitude=cidade["latitude"],
            longitude=cidade["longitude"]
            )
