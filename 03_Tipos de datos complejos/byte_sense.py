def bytes_transform(string, slicing):
    """
    Va a modificar un string en bytes y devolverá su valor en hexadecimal
    Input: STR
    OUTPUT: HEX
    """
    # String to Bytes
    byte_text = string.encode('utf-8')
    print(byte_text)

    # Extract bytes to evens bytes
    bytes_evens = byte_text[::2]
    print(bytes_evens)

    # Concat evens bytes + bytes original
    bytes_concat = byte_text + bytes_evens
    print(bytes_concat)

    bytes_finish = bytearray(bytes_concat)
    print(bytes_finish)

    # XOR
    # slicing = 5
    i = 0
    len_bytes = len(bytes_finish)
    while i < len_bytes:
        bytes_finish[i] ^= (i + slicing) % 256
        i = i + 1
    print(bytes_finish)

    # Convert to Hex
    result = bytes_finish.hex()
    return result



# ======== PRUEBA INTERACTIVA ======== #
text_input = input("Introduce un texto para transformar: ")
slicing = int(input("Introduce desplazamiento: "))
byte_sense = bytes_transform(text_input, slicing)
print("\nResultado transformado:", byte_sense)