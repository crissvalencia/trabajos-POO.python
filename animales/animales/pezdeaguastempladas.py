from servivo import servivo
class Pezdeaguastempladas (servivo):
    def __init__(self, nombre, años, habitat, adaptaciones, alimentacion, tamaño, coloracion,
                 tipo_reproduccion, tipo_aleta, de_aguastempladas):
        super().__init__(nombre, años, habitat, alimentacion, tamaño, coloracion, adaptaciones)
        self.tipo-reproduccion = tipo_reproduccion
        self.tipo_aleta = tipo_aleta
        self.de_aguastempladas = de_aguastempladas

    def buscaralimento(self):
        print(f"{self.nombre} nada entre las aguas temppladas suavemente.")

    def reproducirse(self):
        print(f"{self.nombre} libera huevos en el agua y su pareja los fertiliza para formar nuevas crías.")

    def ponerhuevos(self):
        print(f"{self.nombre} pone huevos en un lugar seguro dentro de su hábitat de aguas templadas.")