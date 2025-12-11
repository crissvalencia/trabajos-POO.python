class SerVivo:
    def __init__(self, apodo, años, ambiente, tipo_alimento, altura, tono):
        self.apodo = apodo
        self.años = años
        self.ambiente = ambiente
        self.tipo_alimento = tipo_alimento
        self.altura = altura
        self.tono = tono

    def desplazarse(self):
        print(f"{self.apodo} está desplazándose por su entorno.")

    def emitir_sonido(self):
        print(f"{self.apodo} está haciendo sonidos propios de su especie.")

    def comer(self):
        print(f"{self.apodo} está consumiendo su alimento.")

    def relajarse(self):
        print(f"{self.apodo} se encuentra descansando tranquilamente.")
