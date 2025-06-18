"""
Método
=> Funciones dentro de una clase
=> La forma de invocar a una funcion es diferente 
    a cuando se define en el main
"""

var = "Hola"

print(globals())

class Coche:
    def velocidad_maxima(self, vel):
        """Retorna la v_max del coche"""
        print("Velocidad Maxima:", vel)


coche1 = Coche()

coche1.velocidad_maxima(30)


# --------
"""def fun_vel_max():
    print("Velocidad MAXIMA")

fun_vel_max()"""
# -------

class Coche:
    atributo_vel_max = 160

    def velocidad_maxima(self):
        """Retorna la v_max del coche"""
        print("Velocidad Maxima:", self.atributo_vel_max)

print("-"*30)
print("Renault")
renault = Coche()
renault.velocidad_maxima()
print(renault.atributo_vel_max)


print("-"*30)
print("BMW")
bmw = Coche()
bmw.velocidad_maxima()
print(bmw.atributo_vel_max)


print("-"*30)

class Coche:

    def __init__(self, vel_max, con_medio):
        self.vel_max_attr = vel_max
        self.con_medio_attr = con_medio

    def velocidad_maxima(self):
        """Retorna la v_max del coche"""
        print("Velocidad Maxima:", self.vel_max_attr)
    
    def consumo_medio(self):
        print("El consumo medio es:", self.con_medio_attr)

renault = Coche(160, 6)
renault.velocidad_maxima()
renault.consumo_medio()
print("-"*30)

bmw = Coche(220, 7)
bmw.velocidad_maxima()
bmw.consumo_medio()
bmw.con_medio_attr = 10
bmw.consumo_medio()

help(Coche)