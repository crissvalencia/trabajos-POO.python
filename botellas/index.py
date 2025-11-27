from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio


print("=" * 50)
print("PROBANDO CLASE PADRE - Botella")
print("=" * 50)
objBotella = Botella("Coca-Cola", "1.5L", "Rosca")
objBotella.imprimir_info()
objBotella.llenar_botella("1.5L")


print("\n" + "=" * 50)
print("PROBANDO CLASE HIJA - Botella Plástico")
print("=" * 50)
objBotella_plastica = Botella_plastico("Pepsi", "500ml", "Presión", "Redondo")
dato_out = objBotella_plastica.imprimir_info()
print(f"\nRetorno del método: {dato_out}")


objBotella_plastica.reciclar_botella("PET reciclado")

print("\n" + "=" * 50)
print("PROBANDO CLASE HIJA - Botella Vidrio")
print("=" * 50)
objBotella_vidrio = Botella_vidrio("Corona", "355ml", "Corona", "Transparente", 3.5)
dato_vidrio = objBotella_vidrio.imprimir_info()
print(f"\nRetorno del método: {dato_vidrio}")


objBotella_vidrio.cambiar_retornable(True)


print("\n" + "=" * 50)
print("PROBANDO HERENCIA - Método del padre")
print("=" * 50)
objBotella_plastica.vaciar_tapar(5)
objBotella_vidrio.llenar_botella("355ml")