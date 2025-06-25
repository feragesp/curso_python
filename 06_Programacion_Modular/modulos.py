"""
Modulos
- Este escrito en Python
- Esta escrito en C y cargado dinamicamente
- Incorporado en el interpreter

Acceder al contenido de un Modulo: 'import'
Modulo Python = fichero.py
"""

import mi_modulo
import sys

# PYTHONPATH
# var_sys = sys.path.append("c:/Users/Matins/python/02_Operadores")
# import var_sys

# print(var_sys.num1)

print(sys.path)
var = mi_modulo.lista
print(var)


bmw = mi_modulo.Coche()
mi_modulo.my_function(bmw)

