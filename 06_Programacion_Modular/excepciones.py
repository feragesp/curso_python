# Excepciones.py

"""
try:
    <sentencias>
except <excepcion>:
    <sentencias si excepcion>
"""


if __name__ == "__main__":
    print("Codigo previo al try")
    
    # try:
    #     var = 10 + input("Introduce Numero: ")
    # except:
    #     print("Input es un str no un int")
    #     print("Error NameError")
    # except TypeError:
    # except ZeroDivisionError:
    #     print("Input es un str no un int")

    colores_admitidos = ("rojo", "azul", "violeta")
    color = "fff"
    if color not in colores_admitidos:
        raise print(type(Exception(f"El color {color} no esta en colores permitidos")))


    print("Codigo despues del try")

    