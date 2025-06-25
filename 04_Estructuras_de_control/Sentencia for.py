"""
Sentencia for

-- Bucles
Estructura que implementa sentencias que se repiten un número finito de veces

for <variable> in <iterable>:
    <sentencias>

<iterable> => colección de elementos (tupla, listas,...)
<variable> => recibe un elemento del objeto <iterable> en cada iteraccion
<sentencias> => sentencias que se ejecutan repetidamente
"""

colores = ["rojo", "azul", "verde"]

for yuju in colores:
    print(yuju)

print(yuju)


# Objetos Iterables

"""
Función iter()
=> Si un objeto es iterable
"""

print(iter("Cadena de texto"))
print(iter([1, 3, 5, "Hola"]))
print(iter({'key_1':"valor1", "key_2":3 }))
# print(iter(45))


#for guapo in "Esta es mi cadenita":
#    print(guapo)

# next() => Devuelve valor uno a uno de un iterador

lista = ["Azul", "Rojo", "Verde"]

lista_iter = iter(lista)
print(type(lista_iter))

print("Len de iter:", len(next(iter(lista))))
print("Lista sin inicializar", lista_iter)
print("Lista inicializada:", next(lista_iter))
print("Lista inicializada:", next(lista_iter))
print("Lista inicializada:", next(lista_iter))
# print("Lista inicializada:", next(lista_iter))

# NO HACER NUNCA
for i in ["azul", "verde", "rojo"]:
    print(i)
else:
    print("No hay mas colores")

# print(help(range))

print(range(5))
[0, 1, 2, 3, 4]
list_range = list(range(5))
print(list_range)

list_range = list(range(10, 50))
print(list_range)
list_range = list(range(10, 50))
print(list_range)

list_range = list(range(10, 50, 2))
print(list_range)

for num in range(11):
    print(num)

print("-" * 3)
lista_num = [0, 1, 2, 3, 4]
len_num = len(lista_num)

for num in lista_num:
    print(num),

print("-" * 3)
for num in range(len(lista_num)):
    print(num)

print("-" * 3)
for num in range(len_num, 0, -1):
    print(num)

alpha = []
for i in range(ord('a'), ord('z') + 1):
    # alpha += chr(i)
    alpha.append(chr(i))
print(alpha)
