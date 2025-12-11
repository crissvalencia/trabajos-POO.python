from  servivo import servivo

class pato (servivo):
  
    def __init__(self, nombre, edad, color_plumas, habitat, reproduccion, acuatico, volar):
        super().__init__(nombre, edad, color_plumas, habitat, reproduccion, acuatico, volar)

        self.acuatico = "acuatico"
        self.reproduccion = "reproduccion"
        self.habitat = "habitat"

        def nadar (self):
            print(f"{self.nombre} esta nadando en el agua ")

        def volar (self):
            print(f"{self.nombre} vuela alto en el cielo en epocas  migratorias ")

        def plumaje (self):
            print(f"{self.nombre} tiene distintos plumas de diferrentes colores ")
