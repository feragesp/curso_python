"""
break
Se utiliza de manera inmediata un estructura de control de flujo for / while
"""
print("Break")
colores = ["rojo", "verde", "azul"]

for color in colores:
    print(color)
    break

n = 5
while n > 0:
    print(n)
    n -= 1
    break

for color in colores:
    print(color)
    break
else:
    print("Printa Else")
print ("-" * 10)
"""
continue
No termina la ejecución completa sino que que termina
la ejecución de la iteración actual
"""
print("Continue")
colores = ["rojo", "verde", "azul"]

for color in colores:
    if (color == "verde"):
        continue
    print(color)

for color in colores:
    if (color == "verde"):
        break
    print(color)

"""
pass
Define el esqueleto de las estructuras
"""
print("-"*10)
print("pass")

def fun():
    pass

colores = ["rojo", "verde", "azul"]

for color in colores:
    # Nose que se va a realizar
    pass