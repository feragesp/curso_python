"""
NameSpace
=> Mapeo de los nombre de los objetos. Se crean en diferentes momentos
    y tienen diferente tiempos de vida
=> A los NameSpace se accede mediante scopes
=> Pyhton crea un NameSpace por defecto y nunca se borra
"""

# print(dir(__builtins__))

# NameSpace globals dura hasta que se cierra el interpreter
var_modulo = 10

# print(globals())

# NameSpce locals dura hasta que acaba la función

def fun():
    var_local = 5
    print(locals())

fun()
print(globals())

"""
Scope
=> Region de un programa desde donde se accede a un
    Namespace directamente
"""

# Scope Locales

def func():
    var_local_fun = 10
    print(var_local_fun)

func()

# Scope no local

def func1_padre():
    var_padre = 10
    print("NameSpace", locals())
    def func2_hijo():
        var_hijo = 5
        var_abuelo = var_padre + 4
        print("NameSpace", locals())
    func2_hijo()

func1_padre()
print ("-"*10)
# Scope global

var_global = 89
def func3():
    def func4():
        var_global = 90
        print(var_global)
        print(locals())
        print(globals())
    func4()

func3()
print(var_global)

# Global / Non Local
contador = 0
def actualizar_contador():
    global contador # Añade permisos de esctritura a global
    while contador < 10:
        print(contador)
        contador += 1

actualizar_contador()
print(contador)

def fun_contador():
    cont = 0
    def act_contador():
        nonlocal cont
        while cont < 10:
            print(cont)
            cont += 1
    act_contador()
    print(cont)

fun_contador()