#   syntymapaiva = "1950.8.6"
def elonpaivat(syntymapaiva: str) -> str:
    
    from datetime import datetime
    spaiva = syntymapaiva.split(".")
    
    nyt = datetime.now()
    spaiva = datetime(int(spaiva[0]), int(spaiva[1]), int(spaiva[2]))
    ero =  nyt - spaiva
    print(ero.days)
    
syntymapaiva = "1950.8.6"
elonpaivat(syntymapaiva)
