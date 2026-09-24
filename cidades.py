import json

def mostrar_cidade(cidade: dict):
    print(" ")
    print("Cidade:", cidade['nome'])
    print("Estado:", cidade['estado'])
    print("População:", cidade['populacao'])
    print("Latitude:", cidade['latitude'])
    print("Longitude:", cidade['longitude'])
    print(" ")

def carregar_cidades(arq: str) -> list[dict]:
    try:
        with open(arq, "r", encoding='utf-8') as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
            print("Arquivo não encontrado!")
            exit(1)
    except json.JSONDecodeError:
            print("cidades.json possui JSON inválido. Verifique o arquivo!") 
            exit(1)