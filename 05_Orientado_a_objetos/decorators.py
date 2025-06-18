"""
Decorators
=> Es un wrapper de una funcion, modifica el comportamiento de una funcion
    realizando una combinancion de todas las propiedades de la funcion
"""

def func():
    # print("HOLA CLASE")
    i = 10
    return i

var = func
print(var)
# var()
j = var() + 12
print(j)

print("-"*10)
var2 = func()
print(var2)

def func2():
    print("HOLA CLASE")

def func3(function):
    print(function)
    function()

func3(func2)


print("-"*30)

def mi_func():
    print("Hola Mundo!")

def mi_decorator(function):
    def wrapper():
        print("Ejecuto antes de la invocacion de la funcion")
        function()
        print("Ejecuto despues de la funcion invocada")
    return wrapper

mi_funcion_mod = mi_decorator(mi_func)
print(mi_funcion_mod)
mi_funcion_mod()