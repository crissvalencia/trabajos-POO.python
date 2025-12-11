from caballo import Caballo
from cocodrilo import Cocodrilo
from pezdeaguastempladas import pezdeaguastempladas
from insecto import insecto
from pato import pato

def index():
    
    equino = Caballo("Trueno", 7, "montaña", "hierba", "mediano", "blanco", 55, "ondulado", False)
    equino.galopar()
    
    print("\n" + "-"*40 + "\n")
    
    
    reptil = Cocodrilo("Mordisco", 15, "pantano", "carnívoro", "enorme", "gris verdoso", 2500, False, 5.2)
    reptil.sumergirse()
    
    print("\n" + "-"*40 + "\n")
    
    
    pececito = pezdeaguastempladas("Nemo", 2, "coral", "algas", "diminuto", "naranja", 28, "ovalada", False)
    pececito.nadar()
    
    print("\n" + "-"*40 + "\n")
    
    
    insecto = insecto("Hércules", 1, "bosque tropical", "fruta podrida", "mediano", "café oscuro", 920, "rugoso", 4)
    insecto.excavar()
    
    print("\n" + "-"*40 + "\n")
    
    
    ave = pato("Cuac", 2, "laguna", "omnívoro", "pequeño", "gris", 0.65, False, "impermeable")
    ave.nadar()

if __name__ == "__main__":
    index()