import json
from mapa import gerar_mapa
from geojson import gerar_geojson, salvar_geojson
import estatisticas
from cidades import carregar_cidades, mostrar_cidade

if __name__ == "__main__":

    cidades = carregar_cidades("cidades.json")

    geojson = gerar_geojson(cidades)

    salvar_geojson(geojson)

    gerar_mapa(cidades)

    print("=== Relatório das cidades ===")
    print(" ")
    qtd_cidades = estatisticas.contar_cidades(cidades)

    print("Quantidade de cidades:", qtd_cidades)
    nome_cidade, populacao = estatisticas.cidade_mais_populosa(cidades)
    populacao_formatada = estatisticas.formatar_populacao(populacao)

    print("Cidade mais populosa:")
    print(nome_cidade, "-", populacao_formatada, "habitantes")

    nome_cidade, menor_populacao = estatisticas.cidade_menos_populosa(cidades)
    populacao_formatada = estatisticas.formatar_populacao(menor_populacao)
    print("Cidade menos populosa:")
    print(nome_cidade, "-", populacao_formatada, "habitantes")

    total = estatisticas.populacao_total(cidades)
    populacao_formatada = estatisticas.formatar_populacao(total)
    print("População total:")
    print(populacao_formatada, "habitantes")

    print(" ")
    print("=== Cidades por população ===")
    cidades_ordenadas = estatisticas.cidade_por_populacao(cidades)

    for numero, cidade in enumerate(cidades_ordenadas, start=1):

        populacao = estatisticas.formatar_populacao(cidade["populacao"])

        print(numero, "-", cidade["nome"], "-", populacao, "habitantes")

    # for cidade in cidades:
        # mostrar_cidade(cidade)
