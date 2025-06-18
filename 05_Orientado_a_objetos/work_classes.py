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
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.vel_max = vel_max
        self.con_medio = con_medio
        self.km_actuales = 0

    def especificaciones(self):
        """Muestra las especificaciones del coche"""
        # print("Potencia {}".format(self.potencia)) # Formatea todo a string
        # print(f"Potencia {self.potencia}")
        """print("Marca: ",self.marca,
              "\nModelo: ",self.modelo,
              "\nPotencia: {} cv".format(self.potencia),
              "\nVelocidad Máxima: {} km/h".format(self.vel_max),
              "\nConsumo Medio: {} l/100km".format(self.con_medio))"""
        
        print(f"Marca: {self.marca}\
              \nModelo: {self.modelo}\
              \nPotencia: {self.potencia} cv\
              \nVelocidad Máxima: {self.vel_max} km/h\
              \nConsumo Medio: {self.con_medio} l/100km\
              \nKilometros Actuales: {self.km_actuales} km")

mercedes = Coche("Mercedes", "C200", 200, 240, 7.5)
mercedes.especificaciones()
# help(Coche)
print("-"*30)

mercedes.km_actuales = 100
