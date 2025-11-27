from modelo_botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, marca, capacidad, tapa, color_vidrio):
        # Llamamos al constructor del padre
        super().__init__(marca, capacidad, tapa)
        # Atributos propios de la botella de vidrio
        self.color_vidrio = color_vidrio
        self.grosor = ""
        self.retornable = ""

    def reutilizar_botella(self, es_retornable):
        self.retornable = es_retornable
        print(f"la botella se puede reutilizar: {es_retornable}")

    def imprimir_info_vidrio(self):
        print(f"el color del vidrio es: {self.color_vidrio}")
        print(f"el grosor es: {self.grosor}")
        print(f"es retornable: {self.retornable}")
        super().imprimir_info()
        print(f"la tapa padre es: {self.tapa}")