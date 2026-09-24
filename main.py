import json

def mostrar_cidade(nome: str, estado: str, populacao: int, latitude: float, longitude: float):
    print(" ")
    print("Cidade:", nome)
    print("Estado:", estado)
    print("População:", populacao)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
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
        mostrar_cidade(nome=cidade["nome"],
            estado=cidade["estado"],
            populacao=cidade["populacao"],
            latitude=cidade["latitude"],
            longitude=cidade["longitude"]
            )
