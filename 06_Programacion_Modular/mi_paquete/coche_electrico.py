from .coche import Coche

class CocheElectrico(Coche):
    """Esta clase reperesenta coche electrico"""

    def __init__(self, marca, modelo, potencia, vel_max, con_medio, capacidad_bateria):
        """Inicializa los atributos de la clase padre"""
        super().__init__(marca, modelo, potencia, vel_max, con_medio)
        self._combustible = "KWh/100km"
        self._capacidad_bateria = capacidad_bateria
    
    def detalles_bateria(self):
        """Muestra detalles de la bateria del coche"""
        print(f"El tamaño de la bateria es {self._capacidad_bateria} KWh")

    def consumo_total(self):
        """Muestra el concumo total desde el Kilometro 0"""
        consumo_total = (self._km_actuales / 100) * self._con_medio
        print(f"El consumo total es de {consumo_total} KWh")

def funcion():
    print("HOLA")