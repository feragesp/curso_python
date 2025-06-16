"""
BYTES
Son inmutables
Tipo de dato es "bytes"
Sitanxis b'<cadena de bytes>'
"""

cadena_bytes = b'\x02\x1f' # (decimal) => 543
print(type(cadena_bytes))
print(cadena_bytes)

int_to_bin = bin(543)
print(int_to_bin)
print(type(int_to_bin))

int_to_hex = hex(543)
print(int_to_hex)
print(type(int_to_hex))

cadena_bytes = b'\x02\x1f' # (decimal) => 543
hex_to_int = int.from_bytes(cadena_bytes, "big")
print(hex_to_int)

cadena_bytes_2 = bytes(3)
print(cadena_bytes_2)

# Transformar datos en bytes

texto = "Hola Mundo"
print(type(texto))

texto_bytes = b'Hola Mundo'
print(type(texto_bytes))
print(texto_bytes)

# Representacion de bytes en ASCII

cadena_bytes_3 = b'\x41\x42\x43' # A B C en ASCII
hex_to_int = int("41", base=16)
print(hex_to_int)
print(cadena_bytes_3)

cadena_bytes_4 = b'\x20\x19\x61\x62\x39\x40'
print(cadena_bytes_4)
hex_to_int = int("40", base=16)
print(hex_to_int)

# Acceso a los elementos de las cadenas de bytes 
cadena_bytes = b'\x20\x19\x61\x62\x39\x40'
print(cadena_bytes[-1])
int_to_hex = hex(cadena_bytes[-1])
print(int_to_hex)

slicing = cadena_bytes[-1:]
print(slicing)
stride = cadena_bytes[0::2]
print(stride)

# SON INMUTABLES
# cadena_bytes[0] = b'4' # DARA ERROR

# Operaciones

cadena_bytes1 = b'\x20\x19\x61'
cadena_bytes2 = b'\x62\x39\x40'

cad3 = cadena_bytes1 + cadena_bytes2
print(cad3)

cad3 = cadena_bytes1
print(cad3)

print(cadena_bytes1 != cadena_bytes2)
print(cadena_bytes1 is cadena_bytes1)

