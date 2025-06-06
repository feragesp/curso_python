"""
TUPLAS: Objetos identicos a Listas excepto por las siguientes propiedades

- Definicion: mi_tupla = (obj1, obj2, obj3, ..., objn)
- LAS TUPLAS SON INMUTABLES
- type(mi_tupla) => tuple
"""

mi_nombrecito = (1, 2, 3, 4, 5)
print(type(mi_nombrecito))
print(mi_nombrecito)

mi_nombrecito = (1, 2, 3, "string", 4, 5)
print(mi_nombrecito)
print(mi_nombrecito[0:4])

# mi_nombrecito[3] = "HOLA"
# Particularidades
tupla = (12,)
print(type(tupla))

# Packing & Unpacking
mi_tuplita = (1, 2, 3, 6, 7)
num1, num2, num3, num4, num5 = mi_tuplita
print(num4)

def func():
    return 5,6
print(func())

n1, n2 = func()
print(n2)

tupla = 1, 2, 3
print(type(tupla))
print(tupla)