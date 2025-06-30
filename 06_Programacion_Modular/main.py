# import mi_paquete.coche
from mi_paquete import *
# from mi_paquete.coche_electrico import CocheElectrico


if __name__ == "__main__":
    print("-"*30)
    bmw = coche.Coche("BMW", "X5", 360, 280, 17.8) #Tractor Caro
    bmw.especificaciones()
    print("-"*30)
    tesla = CocheElectrico("Tesla", "S3", 280, 260, 7.5, 300)
    tesla.especificaciones()
    print(globals())
