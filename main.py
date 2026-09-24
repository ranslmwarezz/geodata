def mostrar_cidade(nome: str, estado: str, populacao: int, latitude: float, longitude: float):
    print("Cidade:", nome)
    print("Estado:", estado)
    print("População:", populacao)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print(" ")

if __name__ == "__main__":

    cidades = [{
        "nome":"Aracaju",
        "estado":"Sergipe",
        "populacao":602757,
        "latitude":-10.9472,
        "longitude": -37.0731
        },

        {"nome":"Recife",
        "estado":"Pernambuco",
        "populacao":1500000,
        "latitude":-8.0476,
        "longitude": -34.8770
        },

        {"nome":"Salvador",
        "estado":"Bahia",
        "populacao":2418005,
        "latitude":-12.9714,
        "longitude": -38.5014}
        ]

    print("=== Relatório das cidades ===")
    for cidade in cidades:
        mostrar_cidade(nome=cidade["nome"],
            estado=cidade["estado"],
            populacao=cidade["populacao"],
            latitude=cidade["latitude"],
            longitude=cidade["longitude"]
            )
