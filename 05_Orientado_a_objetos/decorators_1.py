"""Decorators"""

def func():
    num = 2
    return num


var = func
print(var)

var2 = func()
print(var2)

var3 = var() + 5
print(var3)

print("-"*10)
print("Funciones Recursivas")

def func():
    print("Hola Mundo")

def func2(function):
    function()

func2(func)

# Decorators funciones que envuelven a otra funcion y cambia el comportamiento

print("-"*10)
print("Decorators")

def mi_funcion():
    print("Hola Mundo")
    return 10

memo = mi_funcion
print("Mem Funcion", memo)

def mi_decorator(function):
    memo_deco = mi_decorator
    print("Mem Deco", memo_deco)
    def wrapper():
        memo_wrapper = wrapper
        print("Mem Wrap",memo_wrapper)
        print("Antes de ejecutar funcion de parametro")
        j = function() + 20
        print("Despues de ejecutar funcion del parametro")
        return j
    return wrapper

print("Que vale mi deco",mi_decorator(mi_funcion))

mi_funcion_mod = mi_decorator(mi_funcion)
print("variable",mi_funcion_mod())

num_nuevo = mi_funcion_mod()
print(num_nuevo)

print("-"*10)
print("Decorators con condicionales")

def funcion():
    print("Hola Mundo")

def mi_decorator(func):
    def wrapper():
        if var4 < 5:
            func()
        else:
            print("Jajaja no lo vas ejecutar")
    return wrapper

funcion = mi_decorator(funcion)
print(funcion)
var4 = 20
funcion()

print("-"*10)
print("Syntactic Sugar")

def my_decorator(func):
    def wrapper():
        if n < 5:
            k = func() + n
        else: 
            print(f"ERROR: {n} es > 5")
            k = 0
        return k
    return wrapper

@my_decorator # function = my_decorator(function)
def my_function():
    print("init function")
    return 30

n = 70
# my_function()
print(my_function())
