"""
Sentencia if / elif / else

[if]
Estructura del if
if <expresión>:
    <sentecia_1>
    <sentencia_2>
    <sentencia_n>

<expresion> se evalua en un contexto booleano => True or False
<sentencias> solo se ejecutaran en el caso que la expresion sea "True"
"""

n_1 = 5
n_2 = 10

# Expresion

print(n_1 == n_2)

if (n_1 > n_2):
    print("Hola Mundo")
print("sigo el programa")

lista = ["azul", "verde", "rojo"]

if "azul" in lista:
    print("Sentencia 1")
    print("Sentencia 2")

tupla = (1, 2, 4, 6)

if 3 in tupla:
    print("3 en tupla")

"""
[else]
Else ejecuta la expresion en "False"

if <expresion>:
    <sentencias>
else:
    <sentencia_1>
    <sentencia_2>
    <sentencia_n>
"""

n_1 = 5
n_2 = 10

if n_1 == n_2:
    print("Esto es True")
else:
    print("Esto es False")

if ((n_1 * 3) == n_2) and (n_1 < n_2):
    print("Esto es True")
else:
    print("Esto es False")


"""
[elif]
Evalua diferentes expresiones para ejecucion del codigo "True"

if <expresion_1>:
    <sentencias>
elif <expresion_2>:
    <sentencias>
elif <expresion_3>:
    <sentencias>
elif <expresion_n>
    <sentencias>
else:
    <sentencias>
"""

nombres = ["Oakland", "Xavi", "Sergi", "Bryan"]

if "Carlos" in nombres:
    print("Hola Carlos")
elif "Bryan" in nombres:
    print("Hola Vlad")
elif "Alex" in nombres:
    print("Hola Alex")
elif "Sergi" in nombres:
    print("Hola Oakland")
else:
    print("El nombre no está en la lista")

if 4 > 2: print("Soy Mayor"); print("4 es muy guay")

if 4 < 2: print("4 Es menor")
else: print("4 no es menor")

"""
Operadores condicionales
<expresion> if <expresion_condicional> else <expresion_2>
"""

nombre = "Fernando"

edad = 30 if nombre == "Pedro" else 15
# Mi edad es 30 si soy Pedro sino tengo 15 años
print(edad)

edad = 0
if nombre == "Pedro":
    edad = 30
else:
    edad = 15


tiempo = "lluvia"

print("Vamos", "a la playa" if tiempo == "sol" else "a ver netflix")

if tiempo == "sol":
    print("Vamos a la playa")
else:
    print("Vamos a ver netflix")