'''
 Tiedoston JSON_jj.json sisältö:
 [
    {
        "nimi": "Pekka Pythonisti",
        "ika": 27,
        "harrastukset": [
            "koodaus",
            "kutominen"
        ]
    },
    {
        "nimi": "Jaana Javanainen",
        "ika": 24,
        "harrastukset": [
            "koodaus",
            "kalliokiipeily",
            "lukeminen"
        ]
    }
]


'''


def tulosta_henkilot(tiedosto: str):
    import json

    with open(tiedosto) as tiedosto:
        
        data = tiedosto.read()
        print(data)             # merkkijono
        print(type(data))
        
        opiskelijat = json.loads(data)
        print(opiskelijat)       # lista
        print(type(opiskelijat))
        
    for opiskelija in opiskelijat:
        print(f"{opiskelija['nimi']} {opiskelija['ika'] } vuotta ({(', ').join(opiskelija['harrastukset'])})")
        
    
tulosta_henkilot("JSON_jj.json")
