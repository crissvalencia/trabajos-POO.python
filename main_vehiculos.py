from autodeportivo import AutoDeportivo
from furgoneta import Furgoneta
from camion import Camion

def main():
    # Crear un auto deportivo
    deportivo = AutoDeportivo("BMW Z4", "Negro", "3.0L Turbo", 2, 2, "Gasolina", 
                               250, 4.5, True, "Automática")
    deportivo.arranque()
    deportivo.modo_sport()
    deportivo.aceleracion_maxima()
    deportivo.bajar_techo()
    
    print("\n" + "-"*50 + "\n")
    
    # Crear una furgoneta
    furgon = Furgoneta("Ford Transit", "Blanco", "2.0L Diesel", 4, 3, "Diesel",
                       1200, 5.34, 2.05, 2.52)
    furgon.arranque()
    furgon.cargar_mercancia()
    furgon.abrir_puertas_traseras()
    furgon.modo_trabajo()
    
    print("\n" + "-"*50 + "\n")
    
    # Crear un camión
    camion_carga = Camion("Freightliner M2", "Blanco", "6.7L Diesel", 2, 3, "Diesel",
                          12, 2, False, "Materiales de construcción")
    camion_carga.arranque()
    camion_carga.transportar_carga_pesada()
    camion_carga.levantar_plataforma()
    camion_carga.sistema_direccion()

if __name__ == "__main__":
    main()