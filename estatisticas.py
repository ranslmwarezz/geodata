def contar_cidades(lista: list[dict]) -> int:
    tamanho = len(lista)
    return tamanho

def cidade_mais_populosa(lista: list[dict]) -> tuple[str, int]:

    if not lista:
         return "", 0

    maior_populacao = lista[0]["populacao"]
    nome_cidade = lista[0]["nome"]

    for cidade in lista:
        if cidade["populacao"] > maior_populacao:
            maior_populacao = cidade["populacao"]
            nome_cidade = cidade["nome"]


    return nome_cidade, maior_populacao

def cidade_menos_populosa(lista: list[dict]) -> tuple[str, int]:
    if not lista:
        return "", 0

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

def cidade_por_populacao(lista: list[dict]) -> list[dict]:

    return sorted(lista, key=lambda cidade: cidade['populacao'], reverse=True)

def formatar_populacao(numero: int) -> str:
    return f"{numero:,}".replace(",", ".")