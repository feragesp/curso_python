"""
Clases
=> Estructura principal de los lenguajes orientados a objetos
=> Medio para agrupar datos y funcionalidades
=> Dentro de las clases hay instancias y estas se denominan objetos
=> Cada intancia puede tener atributos para mantener su estado y métodos para modificar su estado
=> La primera letra del nombre de una clase va en Mayúsculas

class <Nombre_clase>:
    <sentencias>

<Nombre_clase>(<argumento>)
"""

#print(help(float))

class Coche:
    pass

coche1 = Coche()
print(coche1)

print(type(coche1))

print(id(coche1))

#print(__name__)
if __name__ == "__main__":
    pass

coche2 = Coche()
print(id(coche2))

print(coche1 is coche2)
print(coche1 == coche2)
