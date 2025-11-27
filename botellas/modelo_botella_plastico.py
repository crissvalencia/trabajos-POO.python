from modelo_botella import Botella

class Botella_plastico(Botella):
    def __init__(self):
        super().__init__()
        self.diseño = ""
        self.tinte = ""
        self.material = ""


    def reciclar_botella(self, material):
        self.material = material
        print(f"la botellase va a reciclar: {material}")

    def imprimir_info_plastico(self):
        print(f"el diseño es: {self.diseño}")
        print(f"el material es: {self.material}")
        print(f"print el color es: {self.tinte}")
        super().imprimir_info()
        print(f"la tapa padre es: {self.tapa}")
