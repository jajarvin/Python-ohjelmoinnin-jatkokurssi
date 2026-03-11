# Saman luokan oliot metodien parametrina
class Henkilo:
    def __init__(self, nimi: str, syntynyt: int):
        self.nimi = nimi
        self.syntynyt = syntynyt
        
    
# huomaa, että tyyppivihje pitää antaa hipsuissa jos parametri on saman luokan olio!
def vanhempi_kuin(self, toinen: "Henkilo"):
    return self.syntynyt < toinen.syntynyt

if __name__ == "__main__":
    jakke = Henkilo("Jakke", 1947)
    kake = Henkilo("Kake", 1952)
    print(vanhempi_kuin(jakke, kake))
