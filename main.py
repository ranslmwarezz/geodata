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
    qtd_cidades = estatisticas.contar_cidades(cidades)

    print("Quantidade de cidades:", qtd_cidades)
    nome_cidade, populacao = estatisticas.cidade_mais_populosa(cidades)

    print("Cidade mais populosa:")
    print(nome_cidade, "-", populacao, "habitantes")

    nome_cidade, menor_populacao = estatisticas.cidade_menos_populosa(cidades)
    print("Cidade menos populosa:")
    print(nome_cidade, "-", menor_populacao, "habitantes")

    total = estatisticas.populacao_total(cidades)
    print("População total:")
    print(total, "habitantes")
    for cidade in cidades:
        mostrar_cidade(cidade)
