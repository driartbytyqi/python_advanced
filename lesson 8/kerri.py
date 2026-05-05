class Kerri:

    def __init__(self,emri,viti,modeli,kilometrat,prejardhje):
        self.emri=emri
        self.viti = viti
        self.modeli = modeli
        self.kilometrat=kilometrat
        self.prejardhje = prejardhje



    def rriteShpejtisin(self):
        print("shpejtsia e kerrit eshte duke u rritur")

    def ndalu(self):
       print(" stoooop")

    def info(self):
        print(f"{self.emri}, eshte nje vetur e fuqishme dhe eshte prodhuar ne vitin: {self.viti}, dhe eshte prodhuuar ne:{self.prejardhje}")