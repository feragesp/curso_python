"""
ByteArray y Byte

- 1 byte = 8 bits
- Los objetos bytes son inmutables
- Dato: bytes
- Sintaxis b'<cadena de bytes>'
"""

cadena_bytes = b'\x02\x1f' # 543
print(type(cadena_bytes))
print(cadena_bytes)

print(bin(543))
print(type(bin(543)))
print(hex(543))
print(type(hex(543)))


num_bytes = b'\x02\x1f'
num_int = int.from_bytes(num_bytes, 'big')
print(num_int)

cadena_bytes_2 = bytes(3)
print(cadena_bytes_2)

texto = "No me mateis"
texto_bytes = b'No me mateis'
print(type(texto))
print(type(texto_bytes))

print(texto_bytes)
texto_bytes = b'\x41\x42\x43'

hex_to_dec = int("42", base=16)
print(hex_to_dec)
print(texto_bytes)

texto_bytes = b'\x20\x19\x61\x62\x39\x40'
print(texto_bytes)
hex_to_dec = int("19", base=16)
print(hex_to_dec)

texto_bytes[-1]
print(texto_bytes[-1:])