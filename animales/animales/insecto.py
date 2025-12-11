from servivo import SerVivo


class Insecto(SerVivo):
    def __init__(self, apodo, años, ambiente, tipo_alimento, altura, tono,
                 exoesqueleto_color=None, antenas=2, patas=6, tiene_alas=False, metamorfosis='completa'):
        super().__init__(apodo, años, ambiente, tipo_alimento, altura, tono)

        # Atributos específicos de insectos
        self.exoesqueleto_color = exoesqueleto_color if exoesqueleto_color is not None else tono
        self.antenas = antenas
        self.patas = patas
        self.tiene_alas = tiene_alas
        self.metamorfosis = metamorfosis

    def volar(self):
        if self.tiene_alas:
            print(f"{self.apodo} vuela usando sus alas.")
        else:
            print(f"{self.apodo} no puede volar; no tiene alas.")

    def desplazarse(self):
        movimiento = "volando" if self.tiene_alas else "caminando/trepando"
        print(f"{self.apodo} se está desplazando {movimiento} con {self.patas} patas.")

    def describir(self):
        print(f"{self.apodo}: {self.años} años, ambiente {self.ambiente}, color {self.exoesqueleto_color}, antenas {self.antenas}.")


if __name__ == '__main__':
    
    abeja = Insecto(apodo='Abejita', años=1, ambiente='jardín', tipo_alimento='nectar', altura=0.5, tono='amarillo', exoesqueleto_color='amarillo-negro', antenas=2, patas=6, tiene_alas=True, metamorfosis='completa')
    abeja.describir()
    abeja.desplazarse()
    abeja.volar()
