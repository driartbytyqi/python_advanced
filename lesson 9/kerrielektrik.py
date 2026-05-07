from kerri import Kerri

class Kerrielektrik(Kerri):

    def __init__(self,emri,viti,modeli,bateria):
        super().__init__(emri,viti,modeli)
        self.bateria=bateria

    def rritjeShpejtsis(self):
        print("kerri elektrik eshte duke shpejtuar")

    def mbusheBateria(self):
        print("mbushe baterin")