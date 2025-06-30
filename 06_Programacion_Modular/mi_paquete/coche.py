class Coche:
    """Esta es una clase que representa un coche"""

    def __init__(self, marca, modelo, potencia, vel_max, con_medio):
        """Iniciliza los atributos
        Argumentos posicionales:
        marca - str marca del coche
        modelo - str modelo del coche
        potencia - int potencia del coche en CV
        vel_max - int velocidad maxima del coche km/h
        con_medio - float consumo medio del coche en l/100km
        """
        self._marca = marca
        self._modelo = modelo
        self._potencia = potencia
        self._vel_max = vel_max
        self._con_medio = con_medio
        self._km_actuales = 0
        self._combustible = "l/100km"

    def especificaciones(self):
        """Muestra las especificaciones del coche"""
        print(f"Marca: {self._marca}\
              \nModelo: {self._modelo}\
              \nPotencia: {self._potencia} cv\
              \nVelocidad Máxima: {self._vel_max} km/h\
              \nConsumo Medio: {self._con_medio} {self._combustible}\
              \nKilometros Actuales: {self._km_actuales} km")
    
    @property
    def kilometros(self): # GETTER
        return self._km_actuales
    
    @kilometros.setter
    def kilometros(self, kilometros): # SETTER
        """Actualizar los kilometros"""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("ERROR: No se puede ir atrás en kilometraje")

    def consumo_total(self): # GETTER
        "Muestra el consumo real del coche desde el kilometro 0"
        consumo_total = (self._km_actuales / 100) * self._con_medio
        print(f"El consumo total del coche es de {consumo_total} litros")
