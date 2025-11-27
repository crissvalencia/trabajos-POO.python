class Botella :
   def __int__(self, marca, capacidad, tapa):
    self.marca= marca 
    self.capacidad = capacidad 
    self.tapa = tapa

   def llenar_botella(self,capacidad):
     print(f"la botella se esta llenando:{capacidad}")
     print(f"se va a usar la tapa: {self.tapa}")

   def vaciar_tapar(self, dato_canntidad):
     print(f"se uso la tapa :{self.tapa}")
     print(F"cantidad de tapas usadas:{dato_canntidad}")
     return dato_canntidad

   def imprimir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Tipo de tapa: {self.tapa}")