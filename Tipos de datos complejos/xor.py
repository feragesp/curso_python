def xor_manual(a, b):
    i = 0
    result_xor = 0
    while i < 8:
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
    
        xor_bits = (bit_a + bit_b) % 2
        result_xor |= (xor_bits << i) 
        
        i = i + 1
    
    return result_xor



input_a = input("A: ")
a = int(ord(input_a))
b = int(input("B: "))
result = xor_manual(a, b)
print(result)
print(chr(result))