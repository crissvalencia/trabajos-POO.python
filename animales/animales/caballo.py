from servivo import servivo

class Caballo(servivo):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 rapidez_max, textura_pelo, es_domestico):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.rapidez_max = rapidez_max
        self.textura_pelo = textura_pelo
        self.es_domestico = es_domestico
    
    def correr_rapido(self):
        print(f"{self.nombre} corre velozmente alcanzando {self.rapidez_max} km/h.")
    
    def comer_pasto(self):
        print(f"{self.nombre} se alimenta tranquilamente en la pradera.")