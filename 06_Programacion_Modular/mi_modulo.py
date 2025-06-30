string = "Hola Mundo"
lista = ["rojo", "verde", "amarillo"]

def my_function(arg):
    print("Imprimo desde mi modulo")
    print(arg)

def mi_suma(a, b):
    c = a + b
    print("mi suma es igual:", c)


class Coche:
    pass

print("__NAME__ de Mi modulo.py:",__name__)


# my_function("Estoy ejecutando mi funcion")

if __name__ == '__main__':
    mi_suma(3, 5)
    
