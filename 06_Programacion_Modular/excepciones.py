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

    # colores_admitidos = ("rojo", "azul", "violeta")
    # color = "fff"
    # if color not in colores_admitidos:
    #     raise print(type(Exception(f"El color {color} no esta en colores permitidos")))


    # print("Codigo despues del try").


    """
    Excepcion AssertionError
    Permite verificar en un punto determinado que el programa este funcionando
    'assert'
    """
    # passwd = input("Introduce tu contraseña de mas de 8 caracteres: ")
    # print(passwd)
    # assert len(passwd) > 8 and passwd.isdigit(), "La contraseña es menor de 8"

    """
    Finally
    Sentencia que se usa para 'limpiar' una ejecucion en excepcion
    """

    try:
        print(variable3)
    except NameError:
        print("La variable no está definida")
        variable3 = "Hola Mundo"
        print(globals())
        
    del variable3
    print(globals())
    