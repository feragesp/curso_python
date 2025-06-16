"""
While
Estructura implementar sentencias un numero infinito de veces

while <expresion>:
    <sentencias>
<expresion> = "True" para ejecutar while
"""

n = 10

while n >= 0:
    print(n)
    n -= 1
print("-" * 4)
print("n final:", n)

n = 1
while n > 0:
    print(n)