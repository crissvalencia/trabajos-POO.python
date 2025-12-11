from servivo import servivo

class cocodrilo(servivo):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 potencia_mordida, es_acuatico, largo_total):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.potencia_mordida = potencia_mordida
        self.es_acuatico = es_acuatico
        self.largo_total = largo_total
    
    def acechar_presa(self):
        print(f"{self.nombre} permanece completamente inmóvil antes de su ataque.")
    
    def sumergirse(self):
        print(f"{self.nombre} desciende bajo el agua de forma silenciosa.")