"""
Método
=> Funciones dentro de una clase
=> La forma de invocar a una funcion es diferente 
    a cuando se define en el main
"""

class Coche:
    def velocidad_maxima(self):
        """Retorna la v_max del coche"""
        print("Velocidad Maxima: ")

coche1 = Coche()

coche1.velocidad_maxima()



def fun_vel_max():
    print("Velocidad MAXIMA")

fun_vel_max()