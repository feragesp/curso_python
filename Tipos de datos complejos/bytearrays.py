"""
ByteArrays
Cadenas de bytes similar a bytes pero son MUTABLES
tipo de dato: bytearray()
"""

cadena_bytes = bytearray(b'\x20\x19\x61\x62\x39\x40')
print(cadena_bytes)
print(type(cadena_bytes))

# Acceso a los elementos
print(cadena_bytes[0])
print(cadena_bytes[0:4])

# Modificacion
cadena_bytes[0:1] = b'A'
print(cadena_bytes)
cadena_bytes[1] = 127
print(cadena_bytes)

# help(ord)
print(ord('X'))

# help(chr)
print(chr(97))

print((ord('X') == 88))

cadena_bytes[2] = ord('X')
print(cadena_bytes)

cad1 = bytearray(b'\x20\x55\x61')         
print("cad1", cad1)
cad2 = bytearray(b'\x62\x40\x39')
print("cad2", cad2)

cad3 = cad1 + cad2
print("cad1+cad2", cad3)

cad4 = bytearray(bytes(9))
print(cad4)

c = ord('a') # 'a'
print("c_init",c)
i = 0
while i < 9:
    cad4[i] = c
    c += 1
    print("c:",c)
    i += 1
    print("i:",i)
print(cad4)
    